# Instruções para agentes (Claude Code e Codex)

Este repo treina agentes para criar e editar vídeos curtos verticais sobre **implementação de IA em empresas**.

## Por onde começar
1. `repertorio/README.md` — pautas, pilares e a primeira leva.
2. `formatos/README.md` — formatos sem rosto (F1–F8) e o motor de cada um.
3. `roteiros/_modelo.md` — modelo de roteiro; um arquivo por vídeo: `roteiros/NN-slug.md`.
4. `referencias/lote-01.md` e `referencias/ferramentas.md` — o que as referências fazem e quais ferramentas usar.

## Referências novas (fluxo recorrente)
O dono sobe vídeos de referência nas **Notas Rápidas** do Mac. Quando pedir para "atualizar" ou "ver as notas":
1. `scripts/notas-novas.sh` lista os links ainda não processados.
2. Para cada um: `scripts/extrair-referencia.sh <nº> <url>`, anotar o link em `referencias/processados.txt` e em `referencias/_brutos/urls.txt`.
3. Analisar folhas de contato + transcrição e registrar num `referencias/lote-NN.md`: conteúdo, edição (frames) e **o que agrega** (formato novo, pauta nova, técnica).
4. Levar o que agrega para `formatos/` e `repertorio/`.

## Regras
- Por enquanto **nenhum vídeo mostra rosto**: só motion, telas simuladas, texto e narração.
- Voz: **ElevenLabs** (`ELEVENLABS_API_KEY` no `.env`, que nunca vai pro git).
- **Transcrição sempre com whisper local** (`whisper-cli`), nunca com o ElevenLabs. Créditos do ElevenLabs só para o que entra no vídeo final; usar `estimate_only` antes de gerações caras.
- Número ou notícia na tela só com fonte listada no roteiro, ou marcado como exemplo.
- Para estudar um vídeo novo: `scripts/extrair-referencia.sh <nome> <url>` e analisar as `folha_*.jpg` (1 quadro/s, 12 s por folha) + `transcricao.srt`.
- Nunca commitar vídeo, áudio ou frames de terceiros (ficam em `referencias/_brutos/`, que está no `.gitignore`). O repo é público.
