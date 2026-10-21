#!/usr/bin/env bash
# Cenas do Story 1 (grátis: FLUX Krea e FLUX Kontext no Hugging Face)
cd "$(dirname "$0")"
PY=~/.cache/ltx-teste/.venv/bin/python
ESTILO="flat vector cartoon illustration, soft cel shading, smooth dark outlines, warm cream, teal and navy palette, cozy explainer-video style, vertical composition, no text, no letters"
K() { $PY -I ~/.cache/ltx-teste/kontext.py "$1" "$2" "$3" ${4:-7}; }
K entrada-apontando.png a-titulo.png "Turn this into a full vertical illustrated scene: the same cartoon man, same face, beard, hair, ear plugs and navy polo, standing in a cozy warm living room at golden hour, pointing up with his index finger and smiling, as if presenting an idea. Keep the exact same cartoon style. Leave empty space at the top. No text."
$PY -I ~/.cache/ltx-teste/flux.py c-celular.png "A tired young woman with curly dark hair in a mustard sweater lying on a sofa at night scrolling her smartphone, a laptop glowing on the coffee table, dim blue screen light on her face, messy living room, she looks exhausted. $ESTILO"
K entrada-falando.png d-cuidar.png "Turn this into a full vertical illustrated scene: the same cartoon man, same face, beard, hair, ear plugs and navy polo, in a calm bright room, one hand on his chest, warm smile, next to a big glowing green battery icon that is recharging with small sparkles. Keep the exact same cartoon style. No text."
K c-celular.png e-louca.png "Same woman, same curly dark hair and mustard sweater, same cartoon style, now standing in a tidy kitchen in the afternoon calmly putting clean plates away in a cupboard, relaxed expression, warm sunlight. Vertical composition. No text."
K c-celular.png f-musica.png "Same woman, same curly dark hair and mustard sweater, same cartoon style, now relaxing in an armchair by a sunny window wearing big headphones, eyes closed, peaceful smile, a plant beside her, no phone. Vertical composition. No text."
K c-celular.png g-passeio.png "Same woman, same curly dark hair and mustard sweater, same cartoon style, now taking a short relaxed walk in a green park at sunset, smiling, trees and soft light. Vertical composition. No text."
K entrada-joia.png h-fim.png "Turn this into a full vertical illustrated scene: the same cartoon man, same face, beard, hair, ear plugs and navy polo, giving two thumbs up with a big smile in a cozy warm living room at golden hour. Keep the exact same cartoon style. Leave empty space at the top. No text."
echo FIM
