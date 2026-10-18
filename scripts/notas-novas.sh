#!/usr/bin/env bash
# Lista os links de vídeo (Instagram, TikTok, YouTube) e de perfis do Instagram das notas do app Notas
# que ainda não foram processados. Lê os anexos e também os links escritos no texto da nota.
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
    set corpo to plaintext of n
    set AppleScript's text item delimiters to {return, linefeed}
    set partes to text items of corpo
    set AppleScript's text item delimiters to " "
    set corpo to partes as string
    set AppleScript's text item delimiters to ""
    set saida to saida & corpo & tab & (name of n) & tab & (creation date of n as string) & linefeed
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
python3 -c '
import re, sys
links = re.compile(r"https?://(?:www\.)?(?:instagram\.com/(?:reel|p)/[\w-]+|instagram\.com/(?!moiseskalebbe)[\w.]+/?|tiktok\.com/\S+|youtube\.com/watch\S+|youtu\.be/\S+)")
for linha in sys.stdin:
    partes = linha.rstrip("\n").split("\t")
    texto, resto = partes[0], partes[1:]
    for url in links.findall(texto):
        if "instagram" in url or "tiktok" in url:
            url = url.split("?")[0].rstrip("/") + "/"
        print("\t".join([url] + resto))
' \
  | awk -F'\t' '!visto[$1]++' \
  | while IFS=$'\t' read -r url nome data; do
      grep -qxF "$url" "$processados" || printf '%s\t%s\t%s\n' "$url" "$nome" "$data"
    done
