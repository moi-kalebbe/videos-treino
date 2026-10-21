"""Gera a narração por BLOCOS (várias falas numa só geração), para soar fluido, e sem perder o tempo de cada fala.

Uso:
    python3 scripts/narracao_blocos.py <falas.txt> <pasta-assets>

Formato do falas.txt:
    #voz=<voice_id>        troca a voz a partir do próximo bloco (vale até a próxima troca)
    #pausa=1.2             silêncio extra (s) antes do próximo bloco
    linha em branco        fecha o bloco
    uma fala por linha     cada linha vira uma "cena" (window.CENAS), como no narracao.py
    {legenda|fala}         troca de pronúncia, como no narracao.py

Por que blocos: gerar frase por frase com 0,5 s entre todas deixou a voz com cara de "lendo" (dono, 19/10/2026).
Saída: audio/narracao.mp3 e legenda.js (LEGENDA, CENAS, FIM_NARRACAO).
"""

import argparse
import base64
import json
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import urllib.request  # noqa: E402

from narracao import (  # noqa: E402
    API, MODELO, carregar_chave, duracao, legenda_com_trocas, palavras_com_tempo, texto_falado,
)

PAUSA_ENTRE_BLOCOS = 0.35
VOZ_DONO = {"stability": 0.38, "similarity_boost": 0.85, "style": 0.3, "use_speaker_boost": True}
AJUSTES = {  # voz clonada do dono: um pouco mais solta; narradores de biblioteca: estável
    "AscQZHgbWOkNYqBmOf0o": VOZ_DONO,  # clone 2, gravação própria de 20/10/2026 (oficial)
    "aORS9tvW5qcMM0bnzsRU": VOZ_DONO,  # clone 1, do Reel (vídeos antigos)
}
PADRAO = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.15, "use_speaker_boost": True}


def sintetizar(texto: str, voz: str, chave: str, antes: str, depois: str) -> dict:
    corpo = json.dumps({
        "text": texto, "model_id": MODELO, "previous_text": antes, "next_text": depois,
        "voice_settings": AJUSTES.get(voz, PADRAO),
    }).encode()
    req = urllib.request.Request(API.format(voz=voz), data=corpo, method="POST",
                                 headers={"xi-api-key": chave, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as resp:
        return json.load(resp)


def ler_blocos(caminho: pathlib.Path) -> list[dict]:
    blocos, atual, voz, pausa = [], [], None, 0.0
    for linha in caminho.read_text().splitlines() + [""]:
        linha = linha.strip()
        if linha.startswith("#voz="):
            voz = linha.split("=", 1)[1].strip()
        elif linha.startswith("#pausa="):
            pausa = float(linha.split("=", 1)[1])
        elif linha:
            atual.append(linha)
        elif atual:
            if not voz:
                sys.exit("Defina #voz= antes do primeiro bloco.")
            blocos.append({"voz": voz, "falas": atual, "pausa": pausa})
            atual, pausa = [], 0.0
    return blocos


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("falas")
    p.add_argument("assets")
    args = p.parse_args()

    blocos = ler_blocos(pathlib.Path(args.falas))
    chave = carregar_chave()
    assets = pathlib.Path(args.assets)
    (assets / "audio").mkdir(parents=True, exist_ok=True)

    todas_falas, faladas, cenas, partes, t = [], [], [], [], 0.0
    with tempfile.TemporaryDirectory() as tmp:
        for i, b in enumerate(blocos):
            texto = " ".join(texto_falado(f) for f in b["falas"])
            antes = " ".join(texto_falado(f) for f in blocos[i - 1]["falas"]) if i else ""
            depois = " ".join(texto_falado(f) for f in blocos[i + 1]["falas"]) if i + 1 < len(blocos) else ""
            r = sintetizar(texto, b["voz"], chave, antes, depois)
            parte = pathlib.Path(tmp) / f"bloco-{i:02d}.mp3"
            parte.write_bytes(base64.b64decode(r["audio_base64"]))
            t += b["pausa"] if i else 0.0
            ws = [{"w": w["w"], "s": round(w["s"] + t, 3), "e": round(w["e"] + t, 3)} for w in palavras_com_tempo(r["alignment"])]
            k = 0
            for f in b["falas"]:
                cenas.append(ws[k]["s"] if k < len(ws) else t)
                k += len(texto_falado(f).split())
            faladas += ws
            todas_falas += b["falas"]
            partes.append((parte, b["pausa"] if i else 0.0))
            t += duracao(parte) + PAUSA_ENTRE_BLOCOS

        entradas, filtros = [], []
        for i, (parte, pausa) in enumerate(partes):
            entradas += ["-i", str(parte)]
            atraso = f"adelay={int(pausa * 1000)}|{int(pausa * 1000)}," if pausa else ""
            filtros.append(f"[{i}:a]aresample=44100,{atraso}apad=pad_dur={PAUSA_ENTRE_BLOCOS if i + 1 < len(partes) else 0}[a{i}]")
        filtros.append("".join(f"[a{i}]" for i in range(len(partes))) + f"concat=n={len(partes)}:v=0:a=1[out]")
        subprocess.run(["ffmpeg", "-v", "error", "-y", *entradas, "-filter_complex", ";".join(filtros),
                        "-map", "[out]", "-b:a", "192k", str(assets / "audio" / "narracao.mp3")], check=True)

    esperadas = sum(len(texto_falado(f).split()) for f in todas_falas)
    if len(faladas) != esperadas:
        sys.exit(f"Alinhamento com {len(faladas)} palavras, esperado {esperadas}. Confira o texto.")
    palavras = legenda_com_trocas(todas_falas, faladas)
    js = "window.LEGENDA = " + json.dumps(palavras, ensure_ascii=False) + ";\n"
    js += "window.CENAS = " + json.dumps([round(c, 3) for c in cenas]) + ";\n"
    js += f"window.FIM_NARRACAO = {palavras[-1]['e']};\n"
    (assets / "legenda.js").write_text(js)
    print("cenas:", [round(c, 2) for c in cenas])
    print("fim da narração:", palavras[-1]["e"], "s")


if __name__ == "__main__":
    main()
