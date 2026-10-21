#!/bin/bash
# Publica o Story "Lições para a Vida · 21/10 · Conte o fato, não dê um rótulo" (v4) uma única vez,
# em 21/10/2026 por volta das 6h (aprovado pelo dono em 20/10/2026).
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/licao-21-10.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-21" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py producao/licoes-para-a-vida-01/21-10/saida/licao-21-10-v4.mp4 --story --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-licao-21-10" 2>/dev/null
fi
