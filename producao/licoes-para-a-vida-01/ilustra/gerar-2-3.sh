#!/usr/bin/env bash
# Cenas das lições 2 (Carnegie) e 3 (A Meta) · grátis no Hugging Face
cd "$(dirname "$0")"; mkdir -p l2 l3
PY=~/.cache/ltx-teste/.venv/bin/python
ESTILO="flat vector cartoon illustration, soft cel shading, smooth dark outlines, warm cream, teal and navy palette, cozy explainer-video style, vertical composition, no text, no letters, no logos"
K() { $PY -I ~/.cache/ltx-teste/kontext.py "$1" "$2" "$3" ${4:-7}; }
F() { $PY -I ~/.cache/ltx-teste/flux.py "$1" "$2"; }
MO="the same cartoon man, same face, beard, hair, ear plugs and navy polo, keep the exact same cartoon style"
# ---- lição 2
K entrada-pensando.png l2/a-titulo.png "Turn this into a full vertical illustrated scene: $MO, standing in a cozy warm living room in the morning, hand on chin thinking, then a gentle smile. Leave empty space at the top. No text."
F l2/c-caixas.png "Two friends carrying cardboard moving boxes up the stairs of an apartment building, a young man with short curly red hair and round glasses in a green hoodie and a woman with straight black hair in a white t-shirt, the man casually saying thanks while already looking at his phone, the woman slightly unnoticed. $ESTILO"
K entrada-falando.png l2/d-apreciar.png "Turn this into a full vertical illustrated scene: $MO, in a bright calm room, one hand on his chest, warm sincere smile, a big glowing heart shaped speech bubble floating next to him. No text."
K l2/c-caixas.png l2/e-obrigado.png "Same two friends, same clothes and same cartoon style, now standing in the apartment next to the stacked boxes, the young man with red hair looking at the woman and thanking her sincerely with a hand on his heart, she is smiling touched. Vertical composition. No text."
K l2/c-caixas.png l2/f-mensagem.png "Same young man with short curly red hair, round glasses and green hoodie, same cartoon style, sitting on a sofa writing a thoughtful message on his phone with a small smile, a few moving boxes in the background, warm evening light. Vertical composition. No text."
# ---- lição 3
K entrada-apontando.png l3/a-titulo.png "Turn this into a full vertical illustrated scene: $MO, standing in a small cozy shop stockroom with shelves of cardboard boxes, pointing up with his index finger and smiling. Leave empty space at the top. No text."
F l3/c-loja.png "Back room of a small online shop: a young woman with a ponytail quickly packing many cardboard boxes on the left, and on the right a single older man with grey hair and glasses at a small desk slowly checking shipping labels, a tall pile of boxes waiting in front of his desk. $ESTILO"
F l3/d-trilha.png "A line of scouts hiking single file on a narrow forest trail, a chubby boy in the middle walking slowly with a huge heavy backpack, the kids behind him bunched up and waiting, the kids in front far ahead, sunny day. $ESTILO"
K entrada-falando.png l3/e-gargalo.png "Turn this into a full vertical illustrated scene: $MO, in a bright room, gesturing towards a giant glass bottle lying on its side with a narrow neck, many small cardboard boxes jammed at the narrow neck of the bottle. No text."
K l3/c-loja.png l3/f-etapas.png "Same young woman with a ponytail, same cartoon style, now in the same stockroom drawing three simple boxes connected by arrows on a whiteboard with a marker, sticky notes around, thoughtful expression. Vertical composition. No text."
K l3/c-loja.png l3/g-fluxo.png "Same small online shop back room, same two people and same cartoon style, now the older man with glasses at the desk is smiling and checking labels quickly with a neat checklist, the pile of boxes in front of him is small, boxes flowing out the door. Vertical composition. No text."
echo FIM
