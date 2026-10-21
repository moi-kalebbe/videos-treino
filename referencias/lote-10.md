# Lote 10 · Virais da semana para modelar (14 a 21/10/2026)

Pedido do dono (21/10): modelar o que já viralizou na semana, como fizemos com o comercial do chinelo.

**Método:** abri a aba Reels de 11 perfis no Chrome do dono e comparei as views de cada Reel com a mediana do próprio perfil ("vezes a mediana"). A data vem do código do post. O material bruto está em `referencias/_brutos/w19…w24` (fora do git).

## Ranking da semana

| # | Reel | Views | Vezes a mediana | Curt. / coment. | Duração | Formato |
|---|---|---|---|---|---|---|
| W20 | @yurikimoro · comercial com ChatGPT + Google Flow ([link](https://www.instagram.com/reel/Des05_vxOUx/)), 20/10 | 150 mil | **5,1×** | 4,0 mil / 2.480 | 27 s | rosto no gancho → tela do celular → comercial pronto (o mesmo do PéDireito) |
| W19 | @leilahormozi · bastidor do casal ([link](https://www.instagram.com/reel/Det_2Vjkfkt/)), 20/10 | 824 mil | 5,0× | 20,7 mil / 370 | — | compilação de humor do casal. **Não serve** (depende de duas pessoas e da fama) |
| W21 | @yurikimoro · "comercial em 10 segundos", Flow `/brand-takeover` ([link](https://www.instagram.com/reel/DemMAubRFdG/)), 17/10 | 139 mil | 4,7× | 3,3 mil / 3.749 | 19 s | o mesmo formato, mais curto, com a promessa de tempo no título |
| W24 | @olucaoferraz · 17 nichos ocultos ([link](https://www.instagram.com/reel/Deu9uFkDiZp/)), 20/10 | 9,9 mil | 3,0× | 292 / **678** | 38 s | **listicle relâmpago**: rosto embaixo, a capa de cada item pulando em cima com o contador 01/17, as capas anteriores se empilhando |
| W22 | @guivilas.ia · vídeo 4K com o Claude + MCP Morphix ([link](https://www.instagram.com/reel/DerNT5GlARb/)), 19/10 | 7,3 mil | ~3× | 229 / 45 | — | resultado primeiro, depois o passo a passo na tela |
| W23 | @odanilogato · IA invadindo TV Box ([link](https://www.instagram.com/reel/DektarZAbt-/)), 16/10 | 102 mil | 2,9× | 4,9 mil / 266 | 146 s | **notícia com imagem gerada em cima e rosto embaixo**, print do estudo com o trecho grifado, legenda de 2 palavras |

**Sem outlier nesta semana:** @danmartell (2,1×), @codiesanchez (1,3×), @aliabdaal (2,0×), @realrileybrown, @thaismartan e @cauhi.

## As 3 opções para modelar
1. **Listicle relâmpago (W24, Lucão).**
   - O dono grava em selfie no suporte, falando rápido uma lista: "17 tarefas da sua empresa que a IA já faz hoje".
   - Em cima, o card de cada tarefa entra com o contador e os cards anteriores vão se empilhando.
   - Feito para salvar e compartilhar. Duração de 30–40 s.
2. **Notícia com imagem em cima e rosto embaixo (W23, Danilo).**
   - Imagem gerada da cena da notícia, print da fonte com o trecho grifado e o dono explicando embaixo.
   - Encurtar para 40 s. Serve para o Plantão IA e para notícias com impacto em empresa.
3. **Comercial com IA, segunda parte (W20/W21, Yuri).**
   - O formato do chinelo segue rendendo para ele (dois virais na semana).
   - Variação "em 10 segundos" com o Google Flow `/brand-takeover`. Vale esperar o resultado do Olha Isso 02 (24/10).

## W25 · @guilhermepozzatto · "Engenharia reversa de vídeo?" ([link](https://www.instagram.com/reel/DeuxuEgRico/)), 20/10
Enviado pelo dono "para aprender mais uma coisa". É **publi** (#publi), 96 s, 85 curtidas e 15 comentários na coleta.

**A ferramenta: [Hypit](https://github.com/hypit-ai/hypit)** (open source, ~22 mil estrelas no GitHub).
- É uma skill para agentes como o Claude Code (`npx skills add hypit-ai/hypit -g`, Node ≥ 22).
- Analisa um vídeo de referência e devolve a estrutura num **projeto editável**.
- O tempo das legendas e do B-roll fica **preso às palavras do roteiro**, e não ao segundo. Trocar o texto refaz o tempo sozinho.
- O núcleo é grátis. Os modelos de imagem, vídeo e voz são pagos à parte.
- Segundo o próprio autor, a análise é o ponto alto; a edição "no escuro" sai genérica.
- **Para nós:** é a mesma coisa que fazemos à mão com `extrair-referencia.sh`, as folhas de contato e o HyperFrames. Vale testar o Hypit num viral para comparar com a nossa análise antes de adotar.

**Técnicas do próprio vídeo:**
- **A ficha da engenharia reversa na tela**, com uma linha por item:
  - gancho (personagem conhecido + frase absurda);
  - ritmo (o B-roll troca a cada 1,5 s);
  - ordem (quem fez → o que fez → motivo);
  - legenda (uma palavra por vez);
  - B-roll (a imagem da palavra dita);
  - efeitos (3 transições de glitch).
  
  **Vamos adotar essa ficha como padrão para analisar os virais** (ver `guias/ficha-engenharia-reversa.md`).
- **Edição:** selfie com microfone de lapela na mão e parede lisa; a tela da ferramenta entra na metade de cima. A legenda vem em caixa, com a palavra-chave destacada em verde. Cards "✕ copia o vídeo / ✓ entende como foi montado".
- O gancho faz uma comparação com algo que já viralizou: "já fizeram engenharia reversa de jogo, mas e de vídeo?".

## Fora da curva: views (ou curtidas) ÷ seguidores (21/10)
Pedido do dono: achar os vídeos que **quebram o padrão**, com muito mais alcance do que o tamanho da conta.

**Método:**
- Busca por assunto no Instagram ("empresário", "gestão de empresa", "dono de negócio", "IA na empresa", "pequena empresa"), só com posts de 28/09 em diante. Foram 34 posts.
- As curtidas e os comentários vêm do yt-dlp; os seguidores, do perfil.
- A busca não mostra as views, então **curtidas ÷ seguidores** serve como medida aproximada.
- Nos perfis grandes, vale a comparação com a mediana do perfil.

| # | Reel | Seguidores | Curtidas | **Curt. ÷ seg.** | Duração | O que é | Serve? |
|---|---|---|---|---|---|---|---|
| X1 | @douglasmove_ ([link](https://www.instagram.com/p/Deh43JYBrHJ/)) | 13,2 mil | 120 mil | **9,1×** | 23 s | música motivacional "quem trabalha sábado e domingo ganha dinheiro" | não (meme de música) |
| X2 | @kadugrowth ([link](https://www.instagram.com/p/DePNM9nCQF-/)) | 3,4 mil | 30 mil | **8,7×** | 28 s | **POV em animação 3D low-poly: o dev conversando com o Claude** às 2h47 ("você tá dormindo?" → "/loop 30m" → "de manhã tem um PR te esperando") | **sim** |
| X3 | @nanda__yoshida ([link](https://www.instagram.com/p/DeksWkzpCJH/)) | 11,9 mil | 64 mil | **5,4×** | 166 s | **minifilme feito com IA**: lavador de carro e entregador pedindo avaliação no Google; o cartão de avaliação resolve (parte 2 de uma série) | sim, encurtado |
| X4 | @tonyareda ([link](https://www.instagram.com/p/DesFqaxvlX5/)) | 17,9 mil | 55 mil | **3,0×** | 124 s | **POV no escritório real conversando com o assistente de IA "Alfred"** (voz de mordomo). Texto: "A IA vai te substituir / Já me substituiu, chefe, e ainda colocou 200 funcionários pra trabalhar pra mim" | **sim** |
| X5 | @caiocarneiro / comovcfezissopodcast ([link](https://www.instagram.com/reel/DeuxqmWJv2g/)) | 2,9 mi | 227 mil (3,3 mi views) | 1,1 (views) · **51× a mediana** | 27 s | corte de podcast sobre política e SUS | não (política) |

**Contas grandes, sem quebra de padrão:** @omardeideais (0,58), @eusouramses (0,9), @albertoneofc (0,25), @izabela.anholett, @matheusfonseca.ia, @daniellimae, @gabrielbollico, @dennisnaka e @nathanlopes.ia, todas abaixo de 0,4.

## W26 · @charlieautomates · "My entire content team runs on Claude Code (10 tools)" ([link](https://www.instagram.com/reel/DeSW9GFBQvF/)), 09/10
Enviado pelo dono para modelar com MCPs de empresa.

### Ficha (`guias/ficha-engenharia-reversa.md`)
| Item | Anotação |
|---|---|
| **Números** | 111 mil views · 53,7 mil seguidores · **2,1 views ÷ seguidores** · **7,6× a mediana** (14,6 mil) · 469 curtidas · **785 comentários** |
| **Gancho** | O título fixo no alto o vídeo todo: "My Entire Content Team / Runs On **Claude Code** / (10 Tools)". Embaixo, ele de costas, digitando num setup escuro com luz roxa e verde. Sem fala, só música. |
| **Ritmo** | Um card por ferramenta a cada ~1,5 s; são 10 cards em 18 s. |
| **Ordem** | Na ordem do trabalho: achar o que funciona (Apify, vidIQ) → ranquear (skill) → baixar e entender (yt-dlp, Whisper, ffmpeg) → produzir (Remotion, Higgsfield) → medir (Analytics) → entregar (Skool). |
| **Card** | Janela de terminal (`~/content-team $ run apify-mcp`, contador [01/10]): logo + nome, um número grande em verde (01…10), uma linha "> Claude faz X" e o print do site da ferramenta. |
| **Legenda** | não tem; o card é o texto. |
| **Efeitos** | o card entra por cima do anterior, com fade rápido; música eletrônica. |
| **Fecho** | card "Comment 'CLAUDE' for the links, prompts and playbook". |
| **Duração** | 18 s |

### Nossa versão: "Minha empresa inteira roda no Claude (10 ferramentas)"
- Só ferramentas **que o dono já tem conectadas** ao Claude, e que portanto são prova real: Gmail, Google Agenda, Google Drive, Google Sheets, ClickUp, Meta Ads, as métricas do Instagram (o MCP próprio), Supabase, Canva e ElevenLabs.
- Cada card diz o que a ferramenta faz **pela empresa**, por exemplo:
  - "lê a caixa e separa o que é cliente";
  - "marca a reunião sem troca de mensagem";
  - "fecha a planilha do financeiro".
- O fundo é o dono de costas no PC, gravado com o suporte do celular.
- O fecho segue `guias/fechamento-e-cta.md`: "manda pro sócio que ainda faz isso na mão" e "salva".
