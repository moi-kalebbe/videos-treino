# Instruções para agentes (Claude Code e Codex)

Este repo treina agentes para criar e editar vídeos curtos verticais sobre **implementação de IA em empresas**.

## Quando o dono pedir um vídeo novo
1. **Perguntar primeiro: "Que estilo de vídeo você quer?"** e listar os estilos de `estilos/README.md` (ou "um formato novo").
2. Se ele escolher um estilo salvo: ler `estilos/<estilo>/README.md`, mandar a ele o **briefing** daquele estilo (o que preciso dele + custo típico) e rodar `scripts/novo-video.sh <estilo> <slug>`.
3. Seguir o passo a passo e o checklist do guia; nota ≥ 9 pela rubrica antes de entregar.
   **Efeitos:** antes de produzir, escolher 2 a 4 efeitos de `guias/efeitos-video.md` que reforçam a história e anotar no roteiro (linha `Efeitos:`), dizendo ao dono quais entram.
   **Capa responsiva é obrigatória em todo vídeo** e vai junto na publicação (o Instagram não deixa trocar depois).
4. Quando um formato novo for aprovado pelo dono, salvar como estilo novo em `estilos/` (guia + modelo).

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
- **Voz e áudio:** seguir `guias/voz-e-audio.md` em todo vídeo ("IA" escrito normal, fala por fala sem `<break>`, +0,7 s no fim do avatar, conferência local por trechos).
- **Mídia grátis primeiro:** antes de gerar imagem ou vídeo pago, ver `guias/bancos-de-midia.md` (Pexels, Pixabay, NASA, Wikimedia, Hugging Face, LTX local).
- **Efeitos:** catálogo dos 17 efeitos e como fazer cada um no HyperFrames em `guias/efeitos-video.md` (vale para todos os estilos).
- **Roteiro:** seguir `guias/linguagem-natural.md` (fala de conversa, sem impacto genérico, humor quando couber).
- Por enquanto **nenhum vídeo mostra rosto**: só motion, telas simuladas, texto e narração.
- Voz: **ElevenLabs** (`ELEVENLABS_API_KEY` no `.env`, que nunca vai pro git).
- **Transcrição sempre com whisper local** (`whisper-cli`), nunca com o ElevenLabs. Créditos do ElevenLabs só para o que entra no vídeo final; usar `estimate_only` antes de gerações caras.
- Número ou notícia na tela só com fonte listada no roteiro, ou marcado como exemplo.
- Para estudar um vídeo novo: `scripts/extrair-referencia.sh <nome> <url>` e analisar as `folha_*.jpg` (1 quadro/s, 12 s por folha) + `transcricao.srt`.
- Nunca commitar vídeo, áudio ou frames de terceiros (ficam em `referencias/_brutos/`, que está no `.gitignore`). O repo é público.
