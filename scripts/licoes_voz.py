"""Gera a voz de um Story da série Lições para a Vida, com o tempo de cada palavra.

Uso:
    python3 scripts/licoes_voz.py <texto.txt> <pasta-assets> [--nome voz] [--antes "texto anterior"]

Saída: <assets>/audio/<nome>.mp3 e <assets>/<nome>.json (palavras com início e fim em segundos).
Voz oficial do dono (clone 1) com eleven_multilingual_v2; o modelo flash soou pior (20/10/2026).
"""

import argparse
import base64
import json
import pathlib
import urllib.request

VOZ = "aORS9tvW5qcMM0bnzsRU"
MODELO = "eleven_multilingual_v2"
AJUSTES = {"stability": 0.45, "similarity_boost": 0.85, "style": 0.25, "use_speaker_boost": True}
RAIZ = pathlib.Path(__file__).resolve().parent.parent


def chave() -> str:
    for linha in (RAIZ / ".env").read_text().splitlines():
        if linha.startswith("ELEVENLABS_API_KEY="):
            return linha.split("=", 1)[1].strip().strip('"')
    raise SystemExit("ELEVENLABS_API_KEY ausente no .env")


def palavras(alinhamento: dict) -> list[dict]:
    saida, atual, inicio, fim = [], "", 0.0, 0.0
    letras = zip(alinhamento["characters"], alinhamento["character_start_times_seconds"],
                 alinhamento["character_end_times_seconds"])
    for letra, s, e in letras:
        if letra.isspace():
            if atual:
                saida.append({"w": atual, "s": round(inicio, 3), "e": round(fim, 3)})
                atual = ""
            continue
        if not atual:
            inicio = s
        atual += letra
        fim = e
    if atual:
        saida.append({"w": atual, "s": round(inicio, 3), "e": round(fim, 3)})
    return saida


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("texto", type=pathlib.Path)
    p.add_argument("assets", type=pathlib.Path)
    p.add_argument("--nome", default="voz")
    p.add_argument("--antes", default="")
    p.add_argument("--voz", default=VOZ, help="outra voz (personagens da cena)")
    p.add_argument("--estilo", type=float, default=None, help="style 0–1 (mais emoção nas falas de personagem)")
    args = p.parse_args()

    ajustes = dict(AJUSTES, **({"style": args.estilo, "stability": 0.35} if args.estilo is not None else {}))
    corpo = {"text": args.texto.read_text().strip(), "model_id": MODELO, "voice_settings": ajustes}
    if args.antes:
        corpo["previous_text"] = args.antes
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{args.voz}/with-timestamps?output_format=mp3_44100_192",
        data=json.dumps(corpo).encode(), headers={"xi-api-key": chave(), "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as resp:
        dados = json.load(resp)

    (args.assets / "audio").mkdir(parents=True, exist_ok=True)
    (args.assets / "audio" / f"{args.nome}.mp3").write_bytes(base64.b64decode(dados["audio_base64"]))
    lista = palavras(dados["alignment"])
    (args.assets / f"{args.nome}.json").write_text(json.dumps(lista, ensure_ascii=False))
    print(f"{args.nome}: {len(corpo['text'])} caracteres, {lista[-1]['e']:.2f} s")


if __name__ == "__main__":
    main()
