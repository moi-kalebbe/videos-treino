"""Monta o áudio final a partir das tags <audio> do index.html e junta no vídeo renderizado.

O render do HyperFrames nem sempre mistura bem muitos sons; aqui cada <audio> entra
no tempo (data-start), com a duração (data-duration) e o volume (data-volume) que estão no HTML.

Uso:
    python3 scripts/mixar_audio.py producao/<slug>/index.html <video-bruto.mp4> <saida.mp4>
"""

import argparse
import pathlib
import re
import subprocess

FADE = 0.05  # evita estalo no corte de cada som
LOUDNORM = "loudnorm=I=-14:TP=-1.5:LRA=11"


def ler_audios(html: pathlib.Path) -> list[dict]:
    audios = []
    for tag in re.findall(r"<audio\b[^>]*>", html.read_text()):
        atributos = dict(re.findall(r'([\w-]+)="([^"]*)"', tag))
        audios.append({
            "src": html.parent / atributos["src"],
            "inicio": float(atributos.get("data-start", 0)),
            "duracao": float(atributos["data-duration"]),
            "volume": float(atributos.get("data-volume", 1)),
        })
    return audios


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("html", type=pathlib.Path)
    p.add_argument("video", type=pathlib.Path)
    p.add_argument("saida", type=pathlib.Path)
    args = p.parse_args()

    audios = ler_audios(args.html)
    entradas, filtros = [], []
    for i, a in enumerate(audios):
        entradas += ["-i", str(a["src"])]
        atraso = int(a["inicio"] * 1000)
        fim_fade = max(a["duracao"] - FADE, 0)
        filtros.append(
            f"[{i + 1}:a]atrim=0:{a['duracao']},asetpts=N/SR/TB,aresample=48000,"
            f"afade=t=out:st={fim_fade}:d={FADE},volume={a['volume']},adelay={atraso}|{atraso}[a{i}]"
        )
    mistura = "".join(f"[a{i}]" for i in range(len(audios)))
    filtros.append(f"{mistura}amix=inputs={len(audios)}:normalize=0,{LOUDNORM}[mix]")
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-i", str(args.video), *entradas,
        "-filter_complex", ";".join(filtros), "-map", "0:v", "-map", "[mix]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", str(args.saida),
    ], check=True)
    print(f"pronto: {args.saida} ({len(audios)} sons)")


if __name__ == "__main__":
    main()
