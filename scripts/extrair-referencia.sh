#!/usr/bin/env bash
# Baixa um vídeo de referência e gera: frames (1/s), folhas de contato (12 s cada), áudio e transcrição.
# Uso: scripts/extrair-referencia.sh <nome> <url>
set -euo pipefail
nome="$1"; url="$2"
modelo="${WHISPER_MODEL:-$HOME/.cache/whisper-models/ggml-large-v3-turbo-q5_0.bin}"
destino="referencias/_brutos/$nome"
mkdir -p "$destino/frames"

yt-dlp -q --no-warnings --write-info-json -o "$destino/video.%(ext)s" "$url"
ffmpeg -v error -y -i "$destino/video.mp4" -vf "fps=1,scale=360:-2" "$destino/frames/f_%03d.jpg"
ffmpeg -v error -y -i "$destino/video.mp4" -vf "fps=1,scale=240:-2,tile=6x2:padding=4:color=white" "$destino/folha_%02d.jpg"
ffmpeg -v error -y -i "$destino/video.mp4" -ar 16000 -ac 1 "$destino/audio.wav"
whisper-cli -m "$modelo" -l pt -f "$destino/audio.wav" -osrt -otxt -of "$destino/transcricao" -np >/dev/null 2>&1

echo "Pronto: $destino (folhas de contato = 1 quadro/s, 12 s por folha)"
