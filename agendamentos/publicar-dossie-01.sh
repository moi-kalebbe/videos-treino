#!/bin/bash
# Publica o Dossiê 01 (O Detalhe) uma única vez, em 23/10/2026 (pedido pelo dono em 19/10/2026), com capa e legenda.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/dossie-01.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-23" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/dossie-01.mp4 roteiros/dossie-01-legenda.txt --capa producao/dossie-01/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-dossie-01" 2>/dev/null
fi
