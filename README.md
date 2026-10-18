# videos-treino

Base de treino para o **Claude Code** e o **Codex** criarem e editarem vídeos (Reels/Shorts 9:16).

- `referencias/` — análise dos vídeos de referência (frames + transcrição). Os arquivos brutos ficam em `referencias/_brutos/` e não vão para o git.
- `scripts/extrair-referencia.sh <nome> <url>` — baixa um vídeo e gera frames, folhas de contato, áudio e transcrição.

Requisitos: `yt-dlp`, `ffmpeg`, `whisper-cli` (whisper.cpp) com o modelo `ggml-large-v3-turbo-q5_0.bin` em `~/.cache/whisper-models/`.
