# Plantão IA 01: onde parei (18/10/2026, ~16:05)

Roteiro aprovado: `roteiros/plantao-ia-01.md`. Custo aprovado pelo dono: ~7.800 créditos.

## Feito
- [x] Projeto criado (`producao/plantao-ia-01/`, fontes + logo copiadas do estilo Caso Real).
- [x] `falas.txt` (8 falas) e narração na voz clonada `aORS9tvW5qcMM0bnzsRU`: `assets/audio/narracao.mp3` (82,7 s), `assets/legenda.js`.
  Cenas: `[0.0, 6.537, 16.186, 28.203, 39.709, 52.423, 63.883, 78.779]`. Conferida localmente por trechos: ok.
- [x] Sons de telejornal em `assets/audio/`: vinheta, suspense, ding, trombone, teletipo, glitch, alerta, carimbo + `trilha.mp3` (88 s).
- [x] 4 cenas em `assets/img/`: `escuta.png` (notícia 2), `pedreiro.png` (3), `estudio.png` (5), `servidores.png` (6).
- [x] Avatar da abertura: fala `avatar/fala-avatar.mp3` (6,85 s com +0,7 s de respiro) + base `avatar/base-rosto-8s.mp4` subidas no fluxo ElevenLabs
  "Plantão IA 01 · avatar abertura" (flow `uPwMTkyW9rwtrTisbVYo`). **Sync 2 Pro rodando**: sessão `AMsyF2pedv6G5N239utf` (3.458 créditos).

- [x] Avatar baixado: `assets/avatar/clip-abertura.mp4` (6,87 s) + `rosto-capa.png`.
- [x] `index.html` telejornal montado; check ok; snapshots revisados (corrigido: mapa do pedreiro usava o 1º "ela", carimbo cobria o rosto, vazio na notícia do Google, páginas sobre o "722").
- [x] Capa `capa/capa-9x16.jpg` (zona segura 4:5 conferida em `capa/previa-recortes.jpg`) + `roteiros/plantao-ia-01-legenda.txt`.

## Falta
1. Render → -14 LUFS → `saida/plantao-ia-01.mp4`; conferência local por trechos; nota pela rubrica.
2. Entregar vídeo + capa + legenda para aprovação. Publicar só com o ok do dono (`publicar-instagram.py --capa`).
3. Depois de aprovado: salvar como estilo `estilos/plantao-ia/` (guia + modelo).
