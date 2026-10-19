#!/bin/bash
# Publica a A Virada 01 (contêiner já preparado) uma única vez, em 19/10/2026 às 12h.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/a-virada-01.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-19" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
if python3 scripts/publicar-instagram.py --conteiner 18029145437915035; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-a-virada-01" 2>/dev/null
fi
