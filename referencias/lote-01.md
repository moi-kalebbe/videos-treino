# Lote 01 — referências das Notas Rápidas (18/10/2026)

Material bruto (vídeo, frames, áudio, transcrição) fica em `referencias/_brutos/<nº>/` — fora do git.
Folhas de contato: 1 quadro por segundo, 12 s por folha (`folha_01.jpg` = 0–11 s, `folha_02.jpg` = 12–23 s…).

## Resumo: o que vira skill

| # | Autor | Assunto | Vira skill? |
|---|---|---|---|
| 01 | @guivilas.ia | **OpenMontage** — "produtora" de agentes (pesquisa → roteiro → locução → imagens → B-roll → montagem) | Sim — pipeline completo |
| 02 | @carloshenrique_ia | 5 ferramentas: **HyperFrames** (HeyGen), **onetake**, **Collage B-roll**, **Claude Animation Base**, **Lemo-Opuscar** | Sim — 5 estilos/motores |
| 03 | @olucaoferraz | **17 efeitos de vídeo** que o Claude cria (catálogo) | Sim — biblioteca de efeitos |
| 04 | @billyia_ | **Xtool** — Claude Code cria app iOS | Não é vídeo (guardar como referência de formato) |
| 05 | @yurikimoro | **Google Flow** `/brand-takeover` — comercial de produto com IA | Sim — comercial de produto |
| 06 | @oandrenuneu | "editor-profissional.zip" — Claude edita vídeo bruto (corta pausas, melhor tomada, zoom, SFX, trilha) | Sim — **edição de talking head** (o mais importante) |
| 07 | @eduardocavalcanti | **LongCat-Video-Avatar** (Meituan) — foto + áudio = avatar falando | Sim — avatar/clone (exige GPU) |
| 08 | @radaropensource | **OpenFilm** — `npx skills add openfilm/openfilm`, vídeo em HTML + editor no navegador | Sim — motor HTML + editor visual |

---

## 01 — OpenMontage (@guivilas.ia) · 46 s · 1080×1920

**Conteúdo:** projeto open source (diz "60 mil+ estrelas") que simula uma equipe de produção com agentes: pesquisador, roteirista, locutor, editor. Formatos: explicativo animado, anúncio de produto, documentário, trailer.

**Edição (frames):**
- Layout em **duas metades**: em cima, card animado ilustrativo (fundo bege, ilustração flat de "um criador" com laptop, card "GitHub · Produtora de vídeo" ganhando itens Roteiro/Imagens/Som/Edição/CLAUDE); embaixo, o rosto do apresentador em card com cantos arredondados.
- **Kicker + título** fixo por bloco (ex.: `UM CRIADOR · GITHUB` / "Ele liberou o projeto.", `OPEN SOURCE` / "OpenMontage.").
- **Legenda palavra a palavra** em pílula preta, com a palavra ativa destacada em **amarelo-limão**.
- Logo "OpenMontage" entrando letra a letra + claquete + selo "★ 60 mil+".
- CTA: "comenta VÍDEO".

## 02 — 5 ferramentas (@carloshenrique_ia) · 62 s · 1080×1920

**Conteúdo:** HyperFrames (cenas em HTML → vídeo), onetake (plano contínuo, uma cena vira a próxima sem corte), Collage B-roll (recortes de papel que se montam peça por peça, animação com Gemini), Claude Animation Base (desenho estilo pintura à mão, mascote do Claude Code), Lemo-Opuscar (43 estilos de filme feitos por código, sem modelo de vídeo).

**Edição (frames):**
- **Sem rosto** — 100% motion graphics, fundo escuro com vinheta vermelho-acastanhada.
- Título com mistura tipográfica: sans branca + **palavra em serifa itálica vermelha** ("Vídeos com o *Claude* em 5 estilos.", "Cenas em HTML que viram *vídeo.*").
- **Paginador 1-2-3-4-5** com o item atual em vermelho.
- Legenda karaokê embaixo: palavra falada branca, futura cinza, nome-chave em vermelho.
- Demonstração "código → resultado": bloco `index.html` + seta + celular com "Olá!".

## 03 — 17 efeitos (@olucaoferraz) · 26 s · 1080×1920

**Conteúdo:** catálogo de efeitos. Lista exata: órbita, parede de posts, dentro do app, saindo da tela, zoom digital, mockup de celular, checklist, mural de manchete, corte no zoom, gráfico subindo, revelação, chroma key, recorte de papel, rabisco vivo, vertigem, capa de revista, letra de vidro.

**Edição (frames):**
- Apresentador segurando um "celular" na mão; dentro dele roda **cada efeito** com contador `01/17`…`17/17`.
- Título fixo "**17** efeitos de vídeo que o Claude cria" (número amarelo) + lista em duas colunas com o item atual em amarelo.
- Depois da lista: legenda centralizada branca, bold, 1 frase curta por vez.
- CTA: "comenta **EFEITOS**" + card do perfil dentro do celular.
- **Esse vídeo é o índice da futura biblioteca de efeitos** — cada um dos 17 vira uma receita.

## 04 — Xtool (@billyia_) · 78 s · 1080×1920

**Conteúdo:** Claude Code + Xtool para criar e instalar app iOS. Fora do tema vídeo.

**Edição (frames):** formato "**green screen sobre print**" — print de tweet/GitHub de fundo, apresentador recortado no canto inferior direito, título em caixa amarela com texto preto. Útil como template "reação a notícia".

## 05 — Google Flow (@yurikimoro) · 18 s · 1440×2560 · sem fala (só música)

**Conteúdo:** comercial de perfume gerado no Google Flow com o comando `/brand-takeover`.

**Edição (frames):** gancho com rosto + texto condensado em caixa alta ("VÍDEO COMERCIAL FEITO COM IA GRATUITO (EM 10 SEGUNDOS)") → gravação de tela do celular digitando o comando → resultado: planos cinematográficos (água azul em macro, frasco em close, textura). Estrutura **gancho → processo → resultado**.

## 06 — Editor profissional no Claude (@oandrenuneu) · 40 s · 1080×1920 · 11 mil curtidas

**Conteúdo:** "cola esse arquivo" (editor-profissional.zip) no Claude → ele "aprende a editar". Manda o vídeo bruto → ele ouve cada palavra, **corta as pausas, fica com a melhor tomada, põe legenda, zoom, efeito sonoro e trilha**. Pedir ajuste em linguagem natural.

**Edição (frames):**
- Gancho: placa de texto branca "Seu editor de vídeo agora mora no Claude 🎬" que **pega fogo** e é consumida.
- Muda para **mockup animado da interface do Claude** (fundo creme, sunburst do Claude ao fundo): anexar zip, digitação "Pronto! Aprendi…", carimbo verde "PRONTO PRA EDITAR", anexar `bruto.mov`.
- Legenda de 2 linhas: linha 1 sans bold, linha 2 serifa itálica.
- CTA de anúncio ("Toca em Saiba Mais").
- **É exatamente o objetivo deste repo** — virar o "editor-profissional" do Claude/Codex.

## 07 — LongCat avatar (@eduardocavalcanti) · 39 s · 1080×1920

**Conteúdo:** LongCat-Video-Avatar (Meituan), open source: foto + áudio → vídeo falando com lip-sync. Comparado ao HeyGen. Requer GPU boa.

**Edição (frames):** título vermelho com texto branco/amarelo ("SUA FOTO VIRA VÍDEO FALANDO DE GRAÇA"); apresentador sobreposto a gravações de tela do Hugging Face Space; legenda **1–2 palavras por vez**, caixa alta condensada, branca/amarela; pausas com fundo azul-marinho.

## 08 — OpenFilm (@radaropensource) · 29 s · 1080×1920

**Conteúdo:** OpenFilm — instala como skill (`npx skills add openfilm/openfilm`), pede o vídeo no chat, monta com HTML/animações web, abre editor visual no navegador (textos, cortes, trilha). Requer Node 22.2+ e ffmpeg. Provedores opcionais (ElevenLabs, OpenAI, Google, fal).

**Edição (frames):** sem rosto. Título condensado caixa alta com palavra em caixa amarela; scroll de print do README do GitHub; legenda karaokê amarela com contorno; fechamento com card "OPENFILM ★755 TypeScript — O QUE DÁ PRA FAZER" e itens entrando um a um.

---

## Padrões que se repetem (base do guia de estilo)

1. **Formato:** 9:16, 1080×1920, 18–78 s (maioria 26–46 s).
2. **Gancho em 1–3 s:** frase de impacto em texto grande logo no primeiro quadro.
3. **Legenda sempre ligada**, sincronizada por palavra; destaque de cor na palavra ativa ou na palavra-chave (amarelo ou vermelho).
4. **Título/kicker fixo por bloco**, mudando a cada assunto.
5. **Prova visual:** print do GitHub, interface animada ou demo antes/depois.
6. **Contador/paginador** quando é lista (1/5, 01/17).
7. **CTA de palavra-chave** no final ("comenta VÍDEO / EFEITOS / FILME / app").
8. Dois tipos de base: **talking head + overlay** (01, 03, 04, 06, 07) e **motion graphics sem rosto** (02, 08).

## Ferramentas a investigar (próximo passo)

OpenMontage · HyperFrames (HeyGen) · onetake · Collage B-roll · Claude Animation Base · Lemo-Opuscar · OpenFilm · LongCat-Video-Avatar · Google Flow. Conferir repo, licença, requisitos e se roda local no Mac.
