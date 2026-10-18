# Formatos sem rosto (motion)

Formatos tirados das referências ([lote 01](../referencias/lote-01.md), [lote 02](../referencias/lote-02.md), [lote 03](../referencias/lote-03.md), [lote 04](../referencias/lote-04.md), [lote 05](../referencias/lote-05.md), [Hard Copy](../referencias/hard-copy.md)), adaptados para **não aparecer**: só motion graphics, telas simuladas, texto na tela e narração (TTS pt-BR) ou só música.

**Avatar (regra de custo):** o apresentador aparece só em 3 momentos: **gancho** (~4 s), **um respiro no meio** (~3 s) e **CTA** (~5 s), uns 12 s no total (~7 mil créditos com HeyGen Avatar IV). O resto é motion, imagens e dados.

Padrão de todos: 9:16 · 1080×1920 · legenda sempre ligada (palavra ativa em destaque) · gancho escrito na tela no 1º segundo · CTA de palavra-chave no final.

| Código | Formato | Inspirado em | Duração | Motor sugerido |
|---|---|---|---|---|
| **F1** | Lista paginada | ref 02 (5 ferramentas) | 40–60 s | HyperFrames |
| **F2** | Catálogo relâmpago | ref 03 (17 efeitos) | 20–30 s | HyperFrames |
| **F3** | Interface simulada | ref 06 (Claude editor) | 30–45 s | HyperFrames / OpenFilm |
| **F4** | Radar com print | ref 08 (OpenFilm), ref 04 | 25–35 s | OpenFilm |
| **F5** | Explicador ilustrado | ref 01 (OpenMontage) | 40–60 s | HyperFrames |
| **F6** | Gancho → processo → resultado | ref 05 (Google Flow) | 15–25 s | HyperFrames (só música) |
| **F7** | Mini-história animada | ref 02 (Claude Animation Base, Lemo-Opuscar) | 15–30 s | Claude Animation Base / Lemo-Opuscar |
| **F8** | Fluxo que se monta | ref 01 (card que vai ganhando itens) | 30–45 s | HyperFrames |
| **F9** | Vitrine de exemplos | ref 09 (703 vídeos) | 30–50 s | HyperFrames |
| **F10** | Explicação que se monta (com avatar) | ref 10 (André Nunes) | 45–90 s | HyperFrames + avatar |
| **F11** | Viagem por dentro | ref 11 (Moisés, "2 segundos") | 45–75 s | HyperFrames + avatar |
| **F12** | Mascote com metáforas | ref 12 (Jeferson, 4 plugins) | 45–60 s | HyperFrames + personagem 2D |
| **F13** | Terminal neon | ref 13 (Maurício, repo nº 1) | 30–40 s | HyperFrames (só voz) |
| **F14** | Manifesto cinematográfico | perfil Hard Copy (virais de 5,1 e 1,2 mi) | 50–65 s | HyperFrames + cenas geradas/banco grátis |
| **F15** | Pedido → resultado | ref 15 (Cauhi, selfie + receita) | 30–45 s | HyperFrames + resultado real |

---

## F1 — Lista paginada
Fundo escuro com vinheta colorida. Título fixo em sans branca com **uma palavra em serifa itálica colorida**. Paginador `1 2 3 4 5` com o item atual aceso. Cada item: nome + 1 visual (print, ícone ou mini-animação) + 1 frase.
**Estrutura:** gancho (o título) → item 1…N (8–10 s cada) → CTA.
**Serve para:** "5 processos que…", "4 erros de…", "3 ferramentas…".

## F2 — Catálogo relâmpago
Mockup de celular ou card no centro com a demo de cada item; lista de todos os itens nas laterais com o atual destacado; contador `01/12`. Ritmo de 1–2 s por item, sem narração longa.
**Estrutura:** título com número grande → itens em sequência rápida → 1 frase de fechamento → CTA.
**Serve para:** "12 tarefas que um agente de IA faz na sua empresa".

## F3 — Interface simulada
Mockup animado de uma interface real (WhatsApp, chat de IA, CRM, planilha, painel). Mostra a coisa acontecendo: mensagem chegando, IA respondendo, carimbo "RESOLVIDO". Legenda de 2 linhas (sans bold + serifa itálica).
**Estrutura:** gancho em placa de texto (pode ter efeito, ex.: pegar fogo) → passo a passo na interface → resultado carimbado → CTA.
**Serve para:** demonstrar casos de uso sem cliente real.

## F4 — Radar com print
Título condensado em caixa alta com palavra em caixa amarela. Scroll por print (notícia, GitHub, post oficial) com legenda karaokê. Fecha com card-resumo "O QUE DÁ PRA FAZER" com 2–3 itens entrando.
**Estrutura:** gancho → print + explicação → "o que isso muda pra sua empresa" → CTA.
**Serve para:** novidades de IA traduzidas pro empresário. **Sempre com a fonte da notícia na tela.**

## F5 — Explicador ilustrado
Fundo claro (bege/creme), ilustração flat, kicker em caixa alta pequena + título curto que muda a cada bloco. Um card central que vai **ganhando elementos** conforme a narração.
**Estrutura:** gancho → contexto → conceito montado peça por peça → exemplo → CTA.
**Serve para:** explicar conceitos (agente, RAG, automação) de forma simples.

## F6 — Gancho → processo → resultado
Sem narração; só música e texto. Gancho em texto condensado grande → gravação de tela/simulação do processo → resultado final em planos bonitos.
**Estrutura:** 3 s de gancho → 7–12 s de processo → 5–8 s de resultado.
**Serve para:** "antes e depois" de um processo.

## F7 — Mini-história animada
Personagem animado (estilo pintura à mão ou um dos 51 estilos de filme do Lemo-Opuscar) vivendo a dor do empresário e a virada. Pouco ou nenhum texto.
**Estrutura:** situação → conflito → virada (a IA entra) → final.
**Serve para:** conteúdo emocional e de alcance, com o problema sendo o protagonista.

## F8 — Fluxo que se monta
Diagrama no estilo n8n: nós entram um a um e se conectam, um "pulso" percorre o fluxo e cada nó acende quando executa. Contador de tempo ou de economia aparece no fim.
**Estrutura:** gancho (o problema) → gatilho → passos → resultado com número → CTA.
**Serve para:** mostrar automação real de forma visual. **É o formato mais "nosso"**, porque mostra o que a gente implementa.

## F9 — Vitrine de exemplos
Carrossel 3D: um card vertical no centro em destaque, os vizinhos inclinados e desfocados atrás. Contador `1/7` + nome do exemplo no topo. Cada card é uma mini-peça rodando (ex.: cardápio, promoção, anúncio). Pode abrir com uma faixa de miniaturas rolando e fechar com uma grade por categoria.
**Estrutura:** gancho com número ("7 vídeos que…") → exemplos em sequência (4–6 s cada) → prova "código → resultado" (preço/marca exatos) → CTA.
**Serve para:** mostrar o que a IA produz *para o negócio do cliente*.

## F10 — Explicação que se monta (com avatar)
Apresentador (avatar) num card na metade de baixo; a metade de cima é um infográfico que **ilustra literalmente cada frase** no momento em que ela é dita. Cada assunto troca a paleta e, se possível, a roupa do apresentador. Números sempre contando; rótulos ligados aos objetos por linhas finas; selo "ilustrativo" quando o dado é exemplo.
**Estrutura:** gancho com o rosto → "antes" (custo/tempo se somando) → "hoje" → 2–4 demonstrações por área → recapitulação em grade → frase-tese → CTA encenado.
**Para o nosso nicho:** "se eu fosse o seu financeiro / comercial / atendimento / RH": cada área com o processo manual de antes e o fluxo com IA depois.
**Custo:** ver [lote 03](../referencias/lote-03.md#custo-estimado-de-um-vídeo-nesse-formato-60-s).

## F11 — Viagem por dentro
Um processo invisível contado como **viagem física**, um plano por frase: o dado sai do computador, passa pelo roteador, pelo cabo no fundo do mar, chega no data center e volta. Avatar fixo na metade de baixo, viagem na metade de cima. No meio da viagem, **1 ou 2 gráficos que explicam de verdade** (tokens, vetor, fila de processamento). O B-roll só ambienta.
**Estrutura:** gancho com o gesto cotidiano ("você aperta Enter") → a viagem em 6–8 paradas → o momento técnico explicado → volta → frase de fecho com contraste de escala ("duas voltas ao mundo em dois segundos").
**Para o nosso nicho:** "o que acontece com a planilha do seu financeiro quando ela vai pro ChatGPT" (com a parada do risco no meio), "o caminho de um pedido do WhatsApp até o ERP com um agente".
**Efeitos:** zoom-through entre paradas, UI world no computador inicial, chart grow no gráfico técnico, pull-back reveal no fecho.

## F12 — Mascote com metáforas
Personagem 2D fixo (mascote da marca) de meio corpo atrás de um balcão. Cada item da lista ganha **cenário de cor própria** e **uma metáfora física** que vira o visual do item (tomada que liga, piscina proibida, impressora que encurta o papel). O **indicador de progresso também é um objeto** (régua de tomadas 1/4) fixo no canto. Etiqueta de seção no canto superior esquerdo.
**Estrutura:** gancho em negativa ("não comece X antes de…") → 3–5 itens (o que faz + 1 detalhe concreto com número) → CTA de palavra.
**Para o nosso nicho:** "4 coisas pra arrumar antes de colocar IA na empresa", com a metáfora de cada uma (gaveta bagunçada = dados, cancela = permissão).
**Custo:** criar o mascote uma vez (imagem de referência + poses), depois reaproveitar. Gestos com poucos quadros (estilo recorte) resolvem em motion.
**Efeitos:** doodle boil, paper cut, checklist, chart grow (contadores mecânicos).

## F13 — Terminal neon
**Sem rosto, só texto, ícones e números.** Fundo preto com brilho neon (verde, ou o lima da marca) vindo de cima; **HUD em micro texto** nos 4 cantos (data, REC, posição, itens n/N); palavras entram com **blur → nítido**; números gigantes com glow; card real da fonte (GitHub, portal); ícones de linha em cards com borda neon; carimbo para responder a objeção.
**Estrutura (30–40 s):** "o nº 1 / o mais X" → o que faz → exemplo concreto → prova social (número) → objeção respondida → CTA "COMENTA PALAVRA" com campo de comentário.
**Para o nosso nicho:** ferramenta ou agente da semana, número de um relatório, "o que a lei nova muda". Bom formato de meio de semana entre um Caso Real e um Plantão.
**Custo:** só a narração (~400 créditos).
**Efeitos:** glass type, chart grow, digital zoom. Extras: `telemetry-hud`/`camcorder-hud`, `blur-in`, `focus-blur-resolve`, `count-up`, `rgb-glitch-text`.

## F14 — Manifesto cinematográfico
Voz em off grave e lenta (sua voz clonada), **sem rosto**. Uma imagem de cinema por frase, escura e quente, com corte seco a cada 1–3 s; **tela preta com 1 palavra vermelha** como respiro; texto central palavra a palavra em sans condensada pesada, branca, com a palavra-chave em vermelho. **Personagem-símbolo de rosto escondido**, sempre o mesmo (o do Hard Copy é um executivo com câmera de segurança no lugar da cabeça). Número de prova em dourado gigante. **Trilha de cinema alta e contínua** (−5 a −8 dB da voz, sem silêncio) e golpes graves nos cortes.
**Estrutura (50–65 s):** frase de filme em 2ª pessoa ("Você só precisa de um dia ruim") → repetição → analogia absurda **antes** do fato → inimigo comum → contraste de percepção → prova curta → anti-promessa ("não te promete nada, entrega o que você precisa") → CTA.
**Para o nosso nicho:** "Imagina contratar o melhor vendedor do país e dar a ele uma planilha de 2009" (IA em cima de bagunça); "Toda empresa vai ter IA. Poucas vão ter resultado"; manifesto da consultoria Processos & IA.
**Efeitos:** vertigo e pull-back reveal nas cenas, glass type no número, digital zoom; extras: tela preta seca, texto palavra a palavra, grão de filme (`grain-overlay`), vinheta (`vignette`), `camera-shake` leve.
**Custo:** só a voz + 6–8 cenas geradas (~3 mil créditos), ou ~400 créditos com banco grátis + motion. Personagem-símbolo: criar uma vez.
**Proibido:** trechos de filme, desenho ou vídeo de terceiros (os virais do Hard Copy usam; nós não).

## F15 — Pedido → resultado
O pedido em linguagem simples é digitado numa caixa de chat de IA ("faz um vídeo meu cozinhando essa picanha") com a fórmula fixa no topo ("1 selfie + 1 receita = *cinema*"), e então o **resultado real** aparece em tela cheia com contagem regressiva no canto e selo "gerado por IA".
**Para o nosso nicho:** "1 planilha + 1 pergunta = relatório pro sócio"; "1 áudio do cliente + 1 pedido = proposta pronta"; "1 print do WhatsApp = pedido lançado no ERP". O resultado tem que ser real (feito por nós) e com dado fictício marcado como exemplo.
**Efeitos:** UI world / phone mockup no pedido, zoom-through para o resultado, chart grow se o resultado for número.

## Cardápio de 39 tipos (ref 20)
Lista de tipos de Reels para combinar com os nossos estilos quando faltar ideia: fofoca · estudo fictício · use isso para isso · quadro branco · A + B + C · tela verde · talking head · mind map · tier list · tela na tela · musical · explicando para criança · reunião · caixinha de perguntas · erro comum · lista · cinemático · selfie no espelho · podcast · stories nativo · depoimento · POV · vlog · passo a passo · mitos e verdades · exercícios · resposta a comentário · bastidores do dia · giro de notícia · péssimo, bom e excelente · antes e depois · tablet na mão · UGC · carro · clone · vídeo escrito · narrado · cronômetro.
Já cobertos: giro de notícia (Plantão IA), cinemático (F14), lista (F1), antes e depois (Caso Real), clone (avatar), narrado/vídeo escrito (F13). Bons próximos para o nosso público: **tier list** de ferramentas de IA para empresa, **péssimo/bom/excelente** jeito de implantar IA, **erro comum**, **reunião** encenada, **caixinha de perguntas** (como o tipo D do Hard Copy).

