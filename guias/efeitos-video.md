# Catálogo de efeitos de vídeo (17 efeitos)

Origem: Reel "17 video effects claude can create" (Notas, 18/10/2026). Mapeado para o **HyperFrames 0.8.171**
pesquisando o catálogo (`npx hyperframes catalog --json`, 447 blocos/componentes) e os comandos do CLI.

**Regra:** em todo vídeo novo, de qualquer estilo, escolher no roteiro **2 a 4 efeitos** desta lista que
servem à história (não enfeite). Anotar no roteiro, numa linha `Efeitos:`, quais entram e em qual cena.
Um efeito só entra se reforça a fala daquele momento (fala = tela).

## Como usar uma peça do catálogo
```bash
npx hyperframes catalog <palavra>          # procurar
npx hyperframes add <nome> --no-clipboard  # instala em compositions/ e imprime o snippet de include
```
Blocos são sub-composições (entram por include); componentes são primitivas para colar no `index.html`.
Antes de usar pela primeira vez, ler o arquivo instalado e adaptar às cores e fontes do estilo.
Status "não testado" = peça existe no catálogo, ainda não rodou num vídeo nosso. Ao testar, atualizar aqui.

## Os 17

| # | Efeito | O que é | Como fazer no HyperFrames | Custo | Status |
|---|---|---|---|---|---|
| 01 | **Orbit** | Câmera gira em volta de um objeto, card ou texto em 3D | Blocos `orbit-card`, `three-orbiting-cards`, `carousel-orbit-1..5`; comp `locked-nucleus-orbit`. Na mão: `perspective` no pai + `rotationY` no GSAP | 0 | não testado |
| 02 | **Couch wall** | (nome não padrão, a confirmar vendo o Reel) provável parede/mosaico de telas ou vídeos | `mk-placeholder-grid` (grade N-up), `gallery-tunnel` (corredor de painéis), `carousel-vision-*` | 0 | interpretar ao ver a referência |
| 03 | **UI world** | A câmera entra numa interface (site, app) como se fosse um cenário | `parallax-device-dive` (câmera atravessa a tela do celular), `ui-3d-reveal`, `ui-focus-zoom`, `scroll-camera-story`. `npx hyperframes capture <url>` transforma um site real em componentes editáveis | 0 | não testado |
| 04 | **Frame break** | Algo sai de dentro da moldura e passa por cima da borda | `npx hyperframes remove-background clip.mp4 -o sujeito.webm` (local, sem crédito) → vídeo original dentro do card com `overflow:hidden` + sujeito recortado por cima, fora do card. Apoio: `freeze-frame-dressing` | 0 | não testado |
| 05 | **Digital zoom** | Punch-in rápido num detalhe do quadro | comp `yt-camera-move` (zoom/slide/tilt), `push-in`, `cursor-zoom-follow` (zoom de gravação de tela), `ui-focus-zoom`. Na mão: `scale` + `transformOrigin` no ponto | 0 | parcial (Ken Burns já usado) |
| 06 | **Phone mockup** | A tela aparece dentro de um celular | comp `device-frame-stage`, `browser-device-stage`, `multi-device-splay`; blocos `vfx-iphone-device` (iPhone 3D real), `ios26-liquid-glass`, `app-showcase` | 0 | não testado |
| 07 | **Checklist** | Itens marcados um a um | `mk-specs-list`, `marker-checklist-card`, `success-check`, `grid-card-assemble` | 0 | não testado |
| 08 | **Headline wall** | Parede de manchetes empilhadas | `mk-clone-wall-transition` (parede de palavras), grade de abas de portal como no Plantão; `stagger-cascade`/`stagger-lattice` para a entrada | 0 | **testado** no Plantão 01 (abertura): grade de `.pcard` 3 colunas, `rotationX:30 rotationZ:-9 transformPerspective:1500`, desliza em y; fade escuro no topo para não cobrir a logo |
| 09 | **Zoom-through cut** | Zoom que atravessa um elemento e cai na cena seguinte | comp `zoom-through-transition`, `parallax-zoom`; bloco `cinematic-zoom` (shader) | 0 | **testado** no Plantão 01: `scale 1→7` em `power3.in` (0,55 s) num wrapper com `transform-origin` no card-alvo + flash branco de 0,12 s no corte; mirar o origin pelo snapshot |
| 10 | **Chart grow** | Gráfico que cresce animado | `chart-story` (barras com valores exatos), `data-chart`, `mk-line-graph`, `decline-chart`, `animated-bar-chart`, `bar-chart-race`, `count-up` | 0 | parcial (contadores no Plantão 01) |
| 11 | **Pull-back reveal** | Começa num detalhe e afasta até o contexto inteiro | comp `pull-back-reveal` (detalhe → manchete + cards), `parallax-unzoom` | 0 | não testado |
| 12 | **Green screen** | Pessoa recortada sobre outro fundo | `npx hyperframes remove-background avatar.mp4 -o avatar.webm` (WebM com alfa, local). Serve para tirar o avatar do card e pôr ele direto sobre a cena | 0 | **testado** no Plantão 01: `remove-background --quality best` (206 quadros em 41 s, CoreML); `<video>` webm fora do `#palco`, `object-fit: contain` + máscara de degradê embaixo; brilho vermelho atrás |
| 13 | **Paper cut** | Visual de papel recortado, camadas e sombras | `paper-collage-reveal`, `torn-paper-rip`, `freeze-frame-dressing` (papel, fita, flash) | 0 | não testado |
| 14 | **Doodle boil** | Rabisco à mão que treme quadro a quadro | família `hw-*`: `hw-boil`, `hw-callout-circle`, `hw-arrow`, `hw-underline`, `hw-frame`, `hw-title`, `marker-highlight`, `vox-annotate` | 0 | **testado** no Plantão 01 ("não existia"): path SVG de elipse irregular gerado em JS, desenha com `strokeDashoffset`, troca entre 3 variações a cada 0,125 s. Esconder com `opacity:0` até desenhar (a ponta redonda aparece como um ponto solto) |
| 15 | **Vertigo** | Dolly zoom (Hitchcock): fundo estica, sujeito parado | bloco `camera-dolly-zoom`. Com foto 2D: recortar o sujeito (`remove-background` em PNG) e escalar fundo e sujeito em sentidos opostos | 0 | não testado |
| 16 | **Cover story** | A cena vira capa de revista, com título atrás do sujeito | `remove-background` no frame/imagem + título gigante entre o fundo e o sujeito (camadas), chamadas em volta; apoio `caption-parallax-layers`, `mk-emphasis-type` | 0 | não testado |
| 17 | **Glass type** | Texto ou card de vidro fosco sobre o vídeo | CSS `backdrop-filter: blur()` + borda clara; blocos `liquid-glass-widgets`, `liquid-glass-notification`, `glass-hero` (vidro 3D refratando o título), `glass-shard-title` | 0 | não testado |

Todos são de custo zero em créditos (rodam no HyperFrames local). Atenção: blocos `webgpu`/`webgl`/`three-js`
pesam no render; testar com `snapshot` antes de render longo.

## Efeitos extras vistos nas referências (lote 04)

| Efeito | Visto em | Como fazer |
|---|---|---|
| **HUD de cantos** | ref 13 | micro texto mono nos 4 cantos (data, REC, posição, itens n/N); comps `telemetry-hud`, `camcorder-hud` |
| **Blur-in por palavra** | ref 13 | comps `blur-in`, `focus-blur-resolve`, `soft-blur-in` |
| **Glow em número** | ref 13 | `text-shadow` em camadas da cor neon + `count-up`; estrelinhas com `stagger` |
| **Progresso como objeto** | ref 12 | o contador `n/N` vira um objeto (tomadas ligando, post-its marcados); SVG próprio, `tl.set` por item |
| **Odômetro** | ref 12 | comps `number-wheel`, `slot-machine-roll` |
| **Metáfora física por item** | ref 12 | um objeto ilustrado por item da lista (piscina, cancela, impressora); `paper-collage-reveal` / `hw-frame` para o tom de desenho |
| **Gráfico de tokens/vetor** | ref 11 | frase quebrada em caixinhas com números + tabela acendendo célula a célula; `stagger-lattice`, `tl.set` por célula |

## Efeitos extras vistos nas referências (lote 05 e Hard Copy)

| Efeito | Visto em | Como fazer |
|---|---|---|
| **Tela preta seca com 1 palavra** | Hard Copy | cena só com fundo `#000` e texto condensado; corte sem transição + golpe grave |
| **Texto palavra a palavra com palavra vermelha** | Hard Copy | cada palavra entra no seu tempo (`window.LEGENDA`), sans condensada pesada, palavra-chave `#e5162e` |
| **Número dourado de metal** | Hard Copy | gradiente dourado + `text-shadow` + `count-up`; comp `gloss-sweep` |
| **Personagem-símbolo de rosto escondido** | Hard Copy | 1 personagem gerado com a mesma descrição em todas as cenas (cabeça = objeto) |
| **Mão desenhando no papel** | Hard Copy (tipo B) | metade de cima com desenho em traço (`hw-*`, `whiteboard-ink`), metade de baixo com a cena |
| **Contagem regressiva no canto** | ref 15 | selo "Tutorial em 00:15" com `tl.set` por segundo; segura a retenção |
| **Objeto de cena que traduz o gancho** | ref 16, ref 17 | prop real ou gerado ilustrando literalmente a frase (remédio para "não durmo", alicate como ponteiro) |
| **Antes/depois lado a lado** | ref 19 | dois cards verticais (Before pequeno, After grande) rodando juntos; `before-after-wipe`, `comparison-split` |
| **Título em duas camadas** | ref 14 | palavra pequena em serifa itálica + palavra gigante condensada embaixo |

## Onde cada efeito rende mais

**Caso Real** (case de empresa com dado):
- Gancho: **cover story** com a imagem do case (empresa vira "capa") ou **vertigo** na imagem principal.
- Dado: **chart grow** (`chart-story`) e **pull-back reveal** (número sozinho → contexto).
- Método/passos: **checklist** e **doodle boil** circulando o ponto-chave.
- Avatar: **green screen** (tirar do card) ou **frame break** (sair da moldura) no gancho e no CTA.

**Plantão IA** (notícias da semana):
- Abertura: **headline wall** com as 6 manchetes + **zoom-through cut** entrando na 1ª notícia.
- Notícia com site/produto: **UI world** ou **phone mockup** com a página real (`capture`).
- Notícia com número: **chart grow** / contador; notícia de mapa: rota já usada.
- Notícia inusitada: **doodle boil** (seta e círculo rabiscado), **paper cut** para o tom de humor.
- Transição entre notícias: **zoom-through cut** ou **digital zoom** no carimbo.
- Avatar da abertura: **green screen** sobre a vinheta em vez do card.

## Checklist por vídeo
- [ ] Roteiro tem a linha `Efeitos:` com 2 a 4 escolhas e a cena de cada uma.
- [ ] Cada efeito casa com a fala do momento.
- [ ] Peça instalada com `add`, cores e fontes do estilo aplicadas, `check` sem erro.
- [ ] Atualizar o **Status** desta tabela depois do primeiro uso real.
