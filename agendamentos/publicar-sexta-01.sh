#!/bin/bash
# Publica o IA por Setor 01 (Financeiro) uma única vez, em 30/10/2026 (remarcado de 23/10 em 19/10/2026) (aprovado pelo dono em 19/10/2026), com capa e legenda.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/sexta-01.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-30" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/sexta-01-conciliacao.mp4 roteiros/sexta-01-conciliacao-legenda.txt --capa producao/sexta-01-conciliacao/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-sexta-01" 2>/dev/null
fi
