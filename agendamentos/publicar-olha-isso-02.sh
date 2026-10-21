#!/bin/bash
# Publica o Olha Isso 02 (comercial PéDireito, modelo Yuri Kimoro) uma única vez, em 24/10/2026 (aprovado pelo dono em 20/10/2026), com capa e legenda.
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
FEITO="$HOME/.local/share/videos-treino/olha-isso-02.publicado"
[ "$(date +%Y-%m-%d)" = "2026-10-24" ] || exit 0
[ -f "$FEITO" ] && exit 0
cd "/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino" || exit 1
caffeinate -i -s -t 1800 &
if python3 scripts/publicar-instagram.py saida/olha-isso-02.mp4 roteiros/olha-isso-02-legenda.txt --capa producao/olha-isso-02/capa/capa-9x16.jpg --publicar; then
  touch "$FEITO"
  launchctl bootout "gui/$(id -u)/com.moiseskalebbe.publicar-olha-isso-02" 2>/dev/null
fi
