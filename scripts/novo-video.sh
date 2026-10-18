#!/usr/bin/env bash
# Começa um vídeo novo a partir de um estilo salvo.
# Uso: scripts/novo-video.sh <estilo> <slug>      ex.: scripts/novo-video.sh caso-real case-klarna
# Sem argumentos: lista os estilos disponíveis.
set -euo pipefail
cd "$(dirname "$0")/.."

if [ $# -lt 2 ]; then
  echo "Estilos disponíveis:"
  for d in estilos/*/; do
    nome=$(basename "$d")
    resumo=$(sed -n '3p' "$d/README.md" 2>/dev/null | cut -c1-110)
    echo "  - $nome: $resumo"
  done
  echo; echo "Uso: scripts/novo-video.sh <estilo> <slug>"
  exit 0
fi

estilo="$1"; slug="$2"
origem="estilos/$estilo/modelo"
destino="producao/$slug"
[ -d "$origem" ] || { echo "Estilo '$estilo' não existe (veja estilos/)"; exit 1; }
[ -e "$destino" ] && { echo "$destino já existe"; exit 1; }

cp -R "$origem" "$destino"
mkdir -p "$destino/assets/img" "$destino/assets/avatar"
sed -i '' "s/\"name\": \"[^\"]*\"/\"name\": \"$slug\"/" "$destino/package.json" 2>/dev/null || true
echo "Pronto: $destino (a partir do estilo $estilo)"
echo "Guia do estilo: estilos/$estilo/README.md"
