#!/bin/bash
# Publica o IA por Setor 02 (Comercial) uma única vez, em 30/10/2026 (pedido pelo dono em 19/10/2026), com capa e legenda.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/sexta-02.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-30" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/sexta-02-comercial.mp4 roteiros/sexta-02-comercial-legenda.txt --capa producao/sexta-02-comercial/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-sexta-02" 2>/dev/null
fi
