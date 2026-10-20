#!/bin/bash
# Publica A Conta 01 (O sábado, escala 6x1) uma única vez, em 22/10/2026 (aprovado pelo dono em 19/10/2026), com capa e legenda.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/a-conta-01.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-22" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/a-conta-01.mp4 roteiros/a-conta-01-legenda.txt --capa producao/o-sabado/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-a-conta-01" 2>/dev/null
fi
