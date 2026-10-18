"""Gera a narração no ElevenLabs com tempo por palavra.

Uso:
    python3 scripts/narracao.py <falas.txt> <pasta-assets> [--voz VOICE_ID]

<falas.txt>: uma fala por linha, uma linha por cena (na ordem das cenas).
    Para siglas ou nomes que a voz pronuncia mal, use {legenda|fala}:
    "uma pesquisa da {PwC|pê dáblio cê}" -> a voz fala "pê dáblio cê", a legenda mostra "PwC".
Saída em <pasta-assets>:
    audio/narracao.mp3
    legenda.js  -> window.LEGENDA (palavras com início/fim) e window.CENAS (início de cada fala)
"""

import argparse
import base64
import json
import re
import os
import pathlib
import subprocess
import sys
import tempfile
import urllib.request

API = "https://api.elevenlabs.io/v1/text-to-speech/{voz}/with-timestamps"
VOZ_PADRAO = "xNGAXaCH8MaasNuo7Hr7"  # Beto - Deep, Warm Narrator (pt-BR)
MODELO = "eleven_multilingual_v2"
# Pausa real (silêncio) entre falas. Não usar <break>: o modelo às vezes inventa fala dentro dela.
PAUSA_ENTRE_CENAS = 0.5


def carregar_chave() -> str:
    raiz = pathlib.Path(__file__).resolve().parent.parent
    env = raiz / ".env"
    if env.exists():
        for linha in env.read_text().splitlines():
            if linha.startswith("ELEVENLABS_API_KEY="):
                return linha.split("=", 1)[1].strip()
    chave = os.environ.get("ELEVENLABS_API_KEY", "")
    if not chave:
        sys.exit("ELEVENLABS_API_KEY não encontrada no .env")
    return chave


def sintetizar(texto: str, voz: str, chave: str, antes: str = "", depois: str = "") -> dict:
    corpo = json.dumps({
        "text": texto,
        "model_id": MODELO,
        # contexto vizinho mantém a entonação contínua entre falas geradas separadamente
        "previous_text": antes,
        "next_text": depois,
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.85, "style": 0.25, "use_speaker_boost": True},
    }).encode()
    req = urllib.request.Request(
        API.format(voz=voz), data=corpo, method="POST",
        headers={"xi-api-key": chave, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.load(resp)


def palavras_com_tempo(alinhamento: dict) -> list[dict]:
    """Junta o alinhamento por caractere em palavras, ignorando as tags de pausa."""
    chars = alinhamento["characters"]
    inicios = alinhamento["character_start_times_seconds"]
    fins = alinhamento["character_end_times_seconds"]
    palavras, atual, ini, dentro_tag = [], "", None, False
    for c, s, e in zip(chars, inicios, fins):
        if c == "<":
            dentro_tag = True
        if dentro_tag:
            dentro_tag = c != ">"
            continue
        if c.isspace():
            if atual:
                palavras.append({"w": atual, "s": round(ini, 3), "e": round(fim, 3)})
            atual, ini = "", None
            continue
        if ini is None:
            ini = s
        atual += c
        fim = e
    if atual:
        palavras.append({"w": atual, "s": round(ini, 3), "e": round(fim, 3)})
    return palavras


TROCA = re.compile(r"\{([^|{}]+)\|([^{}]+)\}")


def texto_falado(fala: str) -> str:
    return TROCA.sub(lambda m: m.group(2), fala)


def tokens_da_legenda(fala: str) -> list[tuple[str, int]]:
    """Palavras da legenda e quantas palavras faladas cada uma cobre."""
    tokens, pos = [], 0
    for m in TROCA.finditer(fala):
        tokens += [(w, 1) for w in fala[pos:m.start()].split()]
        exibida, falada = m.group(1).split(), m.group(2).split()
        # pontuação colada depois da troca (ex.: "{PwC|pê dáblio cê},") fica na última palavra exibida
        tokens += [(w, 0) for w in exibida[:-1]] + [(exibida[-1], len(falada))]
        pos = m.end()
    resto = fala[pos:]
    if resto and not resto[0].isspace() and tokens:
        primeira, *demais = resto.split()
        tokens[-1] = (tokens[-1][0] + primeira, tokens[-1][1])
        resto = " ".join(demais)
    tokens += [(w, 1) for w in resto.split()]
    return tokens


def legenda_com_trocas(falas: list[str], faladas: list[dict]) -> list[dict]:
    legenda, i = [], 0
    for fala in falas:
        for palavra, n in tokens_da_legenda(fala):
            if n == 0:
                legenda.append({"w": palavra, "s": faladas[i]["s"], "e": faladas[i]["s"]})
                continue
            legenda.append({"w": palavra, "s": faladas[i]["s"], "e": faladas[i + n - 1]["e"]})
            i += n
    return legenda


def inicio_das_falas(falas: list[str], palavras: list[dict]) -> list[float]:
    inicios, i = [], 0
    for fala in falas:
        inicios.append(palavras[i]["s"])
        i += len(texto_falado(fala).split())
    return inicios


def duracao(arquivo: pathlib.Path) -> float:
    saida = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(arquivo)],
        capture_output=True, text=True, check=True,
    )
    return float(saida.stdout.strip())


def juntar_com_silencio(partes: list[pathlib.Path], destino: pathlib.Path) -> None:
    """Concatena as falas com PAUSA_ENTRE_CENAS de silêncio entre elas."""
    entradas, filtros = [], []
    for i, parte in enumerate(partes):
        entradas += ["-i", str(parte)]
        filtros.append(f"[{i}:a]aresample=44100,apad=pad_dur={PAUSA_ENTRE_CENAS if i + 1 < len(partes) else 0}[a{i}]")
    filtros.append("".join(f"[a{i}]" for i in range(len(partes))) + f"concat=n={len(partes)}:v=0:a=1[out]")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", *entradas, "-filter_complex", ";".join(filtros), "-map", "[out]", "-b:a", "192k", str(destino)],
        check=True,
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("falas")
    p.add_argument("assets")
    p.add_argument("--voz", default=VOZ_PADRAO)
    args = p.parse_args()

    falas = [l.strip() for l in pathlib.Path(args.falas).read_text().splitlines() if l.strip()]
    faladas_txt = [texto_falado(f) for f in falas]
    chave = carregar_chave()
    assets = pathlib.Path(args.assets)
    (assets / "audio").mkdir(parents=True, exist_ok=True)

    faladas, partes, deslocamento = [], [], 0.0
    with tempfile.TemporaryDirectory() as tmp:
        for i, texto in enumerate(faladas_txt):
            antes = faladas_txt[i - 1] if i > 0 else ""
            depois = faladas_txt[i + 1] if i + 1 < len(faladas_txt) else ""
            resposta = sintetizar(texto, args.voz, chave, antes, depois)
            parte = pathlib.Path(tmp) / f"fala-{i:02d}.mp3"
            parte.write_bytes(base64.b64decode(resposta["audio_base64"]))
            partes.append(parte)
            for w in palavras_com_tempo(resposta["alignment"]):
                faladas.append({"w": w["w"], "s": round(w["s"] + deslocamento, 3), "e": round(w["e"] + deslocamento, 3)})
            deslocamento += duracao(parte) + PAUSA_ENTRE_CENAS
        juntar_com_silencio(partes, assets / "audio" / "narracao.mp3")

    esperadas = sum(len(texto_falado(f).split()) for f in falas)
    if len(faladas) != esperadas:
        sys.exit(f"Alinhamento com {len(faladas)} palavras, esperado {esperadas}. Confira o texto.")

    cenas = inicio_das_falas(falas, faladas)
    palavras = legenda_com_trocas(falas, faladas)
    js = "window.LEGENDA = " + json.dumps(palavras, ensure_ascii=False) + ";\n"
    js += "window.CENAS = " + json.dumps(cenas) + ";\n"
    js += f"window.FIM_NARRACAO = {palavras[-1]['e']};\n"
    (assets / "legenda.js").write_text(js)

    print("cenas:", cenas)
    print("fim da narração:", palavras[-1]["e"], "s")


if __name__ == "__main__":
    main()
