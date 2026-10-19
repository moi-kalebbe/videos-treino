#!/bin/bash
# Publica o Caso Real da Movida uma única vez, em 21/10/2026 (aprovado pelo dono em 18/10/2026), com capa e legenda.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/caso-movida.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-21" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/caso-movida.mp4 roteiros/caso-movida-legenda.txt --capa producao/caso-movida/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-caso-movida" 2>/dev/null
fi
