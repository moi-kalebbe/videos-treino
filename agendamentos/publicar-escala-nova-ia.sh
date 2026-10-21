#!/bin/bash
# Publica "A escala nova e a IA" (v2) uma única vez, em 20/10/2026 às 19h (aprovado pelo dono em 20/10/2026), com capa e legenda.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/escala-nova-ia.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-20" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/escala-nova-ia-v2.mp4 roteiros/escala-nova-ia-legenda.txt --capa producao/escala-nova-ia/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-escala-nova-ia" 2>/dev/null
fi
