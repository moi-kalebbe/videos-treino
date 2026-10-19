#!/bin/bash
# Publica a A Virada 04 uma única vez, em 09/11/2026 (aprovada pelo dono em 19/10/2026).
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/a-virada-04.publicado"
[ "$(date +%Y-%m-%d)" = "2026-11-09" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/a-virada-04.mp4 roteiros/a-virada-04-legenda.txt --capa producao/a-virada-04/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-a-virada-04" 2>/dev/null
fi
