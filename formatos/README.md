# Formatos sem rosto (motion)

Formatos tirados das referências ([lote 01](../referencias/lote-01.md), [lote 02](../referencias/lote-02.md), [lote 03](../referencias/lote-03.md)), adaptados para **não aparecer**: só motion graphics, telas simuladas, texto na tela e narração (TTS pt-BR) ou só música.

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
