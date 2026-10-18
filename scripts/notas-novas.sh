#!/usr/bin/env bash
# Lista os links de vídeo (Instagram, TikTok, YouTube) das notas do app Notas que ainda não foram processados.
# Uso: scripts/notas-novas.sh [quantas-notas-recentes]   (padrão: 12; as notas vêm da mais recente para a mais antiga)
# Processados ficam em referencias/processados.txt (um link por linha, sem parâmetros de rastreio).
set -euo pipefail
cd "$(dirname "$0")/.."
limite="${1:-12}"
processados="referencias/processados.txt"
touch "$processados"

osascript <<EOF |
tell application "Notes"
  set saida to ""
  set ns to notes
  set total to count of ns
  if total > $limite then set total to $limite
  repeat with i from 1 to total
    set n to item i of ns
    repeat with a in attachments of n
      try
        set u to URL of a
        if u is not missing value then set saida to saida & (u as string) & tab & (name of n) & tab & (creation date of n as string) & linefeed
      end try
    end repeat
  end repeat
  return saida
end tell
EOF
grep -E 'instagram\.com/(reel|p)/|tiktok\.com/|youtube\.com/|youtu\.be/' \
  | sed -E '/instagram|tiktok/ s/\?[^[:space:]]*//' \
  | awk -F'\t' '!visto[$1]++' \
  | while IFS=$'\t' read -r url nome data; do
      grep -qxF "$url" "$processados" || printf '%s\t%s\t%s\n' "$url" "$nome" "$data"
    done
