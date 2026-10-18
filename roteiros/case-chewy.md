# [CASE] Chewy: 50 milhões por ano com IA, e o segredo não foi a IA

| Campo | Valor |
|---|---|
| Pilar | Case com dados |
| Formato | motion sem rosto (dados + case) |
| Duração alvo | 45 s |
| Voz | ElevenLabs · Beto (`xNGAXaCH8MaasNuo7Hr7`) |
| CTA | comenta `DIAGNÓSTICO` |
| Status | v7 (`saida/case-chewy-v7.mp4`) · falas atuais em `producao/case-chewy/falas.txt` |

**Estratégia:** consciente do problema e desconfiado (já ouviu muito hype de IA) · desejo: ter retorno de verdade e não jogar dinheiro fora · grande ideia: **IA em cima de bagunça só deixa a bagunça mais rápida. Quem ganha arrumou a base antes.**

## Ganchos considerados (3 s)

| Gancho | Tipo | Nota |
|---|---|---|
| **"Essa empresa prevê economizar 50 milhões de dólares por ano com IA. E o segredo não foi a IA."** | número grande + contradição | **escolhido**: número concreto, lacuna de curiosidade, verdadeiro |
| "56% dos CEOs não tiveram retorno nenhum com IA." | estatística chocante | forte, mas é negativo e não tem protagonista |
| "Você está investindo em IA do jeito errado." | acusação | genérico, sem prova no 1º segundo |

## Falas (uma por cena)

1. Essa empresa prevê economizar cinquenta milhões de dólares por ano com IA. E o segredo não foi a IA.
2. Uma pesquisa da PwC com mais de quatro mil CEOs mostrou que cinquenta e seis por cento não tiveram retorno nenhum com IA. Nem mais receita, nem menos custo.
3. A Chewy, gigante americana de produtos para pets, está do outro lado.
4. O assistente de atendimento já resolve sozinho trinta por cento dos chats. Na farmácia, a IA lê as receitas. Nas clínicas, uma assistente de voz confirma as consultas.
5. Mas antes de qualquer agente, eles passaram vários trimestres arrumando a base. Dados limpos, processos organizados. Só depois veio a IA.
6. IA em cima de bagunça só deixa a bagunça mais rápida.
7. Quer saber se a sua empresa está pronta? Comenta DIAGNÓSTICO.

## Cenas

| # | Visual | Texto na tela |
|---|---|---|
| 1 | Contador sobe de 0 a US$ 50 mi; "/ano" encaixa; a frase "o segredo não foi a IA" entra com "não foi" riscando "a IA" | CASO REAL · EUA / **US$ 50 mi** por ano |
| 2 | Grade de 100 pontos (CEOs); 56 apagam em cinza; contador 56% | **56%** dos CEOs: retorno zero com IA · fonte PwC 2026 |
| 3 | Os 44 pontos restantes viram um único ponto lima, que vira o card "Chewy" | Chewy · e-commerce de pets · EUA |
| 4 | Três cards entram em cascata; o de atendimento tem barra enchendo até 30% | Atendimento 30% · Farmácia · Clínicas |
| 5 | Blocos empilham: Dados → Processos → Infraestrutura; bloco "IA" cai por cima | Antes da IA: vários trimestres arrumando a base |
| 6 | Peças bagunçadas giram cada vez mais rápido (motion blur); corta seco para a frase | IA em cima de bagunça só deixa a bagunça *mais rápida.* |
| 7 | CTA | Comenta **DIAGNÓSTICO** |

## Fontes
- Chewy, teleconferência do 2º tri do ano fiscal 2027, via [CIO Dive, 11/09/2026](https://www.ciodive.com/news/chewy-projects-50m-annual-cost-savings-ai/830210/): US$ 50 mi/ano é **previsão** a partir do ano fiscal 2027; ~30% dos chats de autoatendimento resolvidos pelo assistente Cai; IA na farmácia (extração de dados) e assistente de voz Callie nas clínicas; vários trimestres investindo em infraestrutura e qualidade de dados.
- PwC, 29th Global CEO Survey (jan/2026), 4.454 CEOs: 56% sem aumento de receita nem redução de custo com IA ([Tech.co](https://tech.co/news/ceos-havent-see-ai-revenue-cost-benefits)).

## Avaliações ([rubrica](../guias/rubrica-qualidade.md))

### v1 · 18/10/2026 · nota **7,9**

| Critério | Peso | Nota | Por quê |
|---|---|---|---|
| Gancho | 2,0 | 7 | Frase forte, mas o 1º quadro mostra "US$ 10 mi" no meio da contagem; a narração do gancho leva 6,9 s |
| Uma ideia | 1,5 | 9 | "IA em cima de bagunça só deixa a bagunça mais rápida" amarra tudo |
| Verdade e fontes | 1,5 | 9 | Fonte na tela nas cenas de dado; previsão marcada como previsão |
| Ritmo | 1,5 | 7 | Trechos parados (grade 7–10 s; card Chewy 17–22 s); 53 s, poderia ter ~45 |
| Acabamento | 1,5 | 7 | Selo "Receita ↑ não" sobre a grade; descrição da Chewy quebra mal; muito vazio na cena 1 |
| Legenda | 1,0 | 8 | Sincronizada e legível; blocos de 3 palavras às vezes cortam a ideia |
| Áudio | 0,5 | 7 | Voz fala "PwC" como "Pedwac"; loudness -14,9 LUFS ok |
| Público e CTA | 0,5 | 9 | Fala com o dono; CTA de diagnóstico |

**Corrigir na v2:** número já em 50 no 1º quadro; gancho falado mais curto; "PwC" escrito foneticamente na fala ("pê dablio cê") mantendo "PwC" na legenda; chips abaixo da grade; animação contínua nos trechos parados; cortar ~6 s.

### Nota do dono para a v1: **3/10**
Sem avatar; sem imagem de pet nem logo da Chewy; gancho fraco; sem a logo dele; 4 blocos na tela e 3 falados.

### v2 → v5 · 18/10/2026 · sem avatar (decisão do dono) · nota **8,8**

O que mudou: gancho novo ("Uma loja online de ração vai economizar 50 milhões...") com foto real e número legível no 1º quadro; 4 imagens geradas (cachorro, armazém, farmácia, clínica) + logo oficial da Chewy (domínio público, Wikimedia); "PwC" falado certo via `{PwC|pê dáblio cê}`; narração gerada **fala por fala** com silêncio real (a versão com `<break>` inventava palavras nas pausas); efeitos amarrados às palavras com `data-sinc` + `scripts/sincronizar-audio.py`; pilha com 3 blocos = 3 itens falados; CTA encenado (campo de comentário digitando + notificação de direct); marca d'água provisória "MOISÉS KALEBBE".

| Critério | Peso | Nota | Por quê |
|---|---|---|---|
| Gancho | 2,5 | 9 | Foto real + "US$ 50 mi" legível no quadro 0; a frase falada do gancho ainda leva ~6 s |
| Presença e imagem | 2,0 | 8 | 4 fotos + logo; sem avatar (fica para a versão com o rosto do dono) |
| Ritmo | 1,5 | 8,5 | Quase sempre algo mudando; início da cena da base ainda é calmo |
| Uma ideia | 1,0 | 9 | "IA em cima de bagunça só deixa a bagunça mais rápida" |
| Acabamento | 1,0 | 9 | Sem sobreposição; check limpo |
| Verdade e fontes | 1,0 | 9 | Fontes na tela; previsão marcada; "loja online de ração" simplifica "e-commerce de produtos para pet" |
| Legenda e áudio | 0,5 | 9,5 | Pronúncia certa; -14,0 LUFS; sem falas fantasmas |
| Público e CTA | 0,5 | 9,5 | Fala com o dono; CTA de diagnóstico encenado |

**Trava pendente:** a marca d'água é provisória (texto). Com a logo real, a trava sai. Para passar de 9: avatar no gancho/meio/CTA (vídeos do dono) e gancho falado mais curto.

Custo da v2→v5 no ElevenLabs: ~1.600 créditos de imagens (4 × 406) + ~1.500 de narração (2 gerações) ≈ 3.100 créditos.

### v6 · 18/10/2026 · com avatar do dono · nota **9,0**

O que mudou: narração inteira na **voz clonada do Moisés** (`aORS9tvW5qcMM0bnzsRU`, settings 0.45/0.85/0.25); avatar (Sync 2 Pro sobre o Reel dele) em 3 momentos: gancho (0–7,5 s, card central sobre a foto), frase-tese (41,8–45,9 s, card no alto) e CTA (45,9–49,6 s, card redondo); selo "avatar gerado com IA" em cada card; ~0,7 s de silêncio no fim do último trecho.

| Critério | Peso | Nota | Por quê |
|---|---|---|---|
| Gancho | 2,5 | 9 | Rosto + foto real + "US$ 50 mi" no quadro 0 |
| Presença e imagem | 2,0 | 9 | Avatar nos 3 momentos; 4 fotos + logo |
| Ritmo | 1,5 | 8,5 | Começo da cena da base ainda é calmo |
| Uma ideia | 1,0 | 9 | Tese falada pelo próprio rosto |
| Acabamento | 1,0 | 9 | Check limpo, sem sobreposição |
| Verdade e fontes | 1,0 | 9 | Fontes na tela; selo de avatar IA |
| Legenda e áudio | 0,5 | 9 | Voz dele em tudo; -14,2 LUFS |
| Público e CTA | 0,5 | 9,5 | CTA encenado + rosto |

**Trava pendente:** marca d'água ainda provisória (texto). Custo da v6: ~800 (narração) + 7.702 (sincronia 15,3 s) ≈ 8.500 créditos.

### Nota do dono para a v6: **7/10**
Avatar no 1º quadro na frente da cara do cachorro; não quer o selo "avatar gerado com IA"; trocar "MOISÉS KALEBBE" pela logo (enviou versões branca e preta).

### v7 · 18/10/2026
- Selo "avatar gerado com IA" removido dos 3 cards.
- Logo oficial (versão branca, `assets/marca/logo-branca.png`, ponto solto do arquivo original removido) no canto superior direito, o vídeo todo.
- Gancho em **tela dividida**: foto do cachorro + número em cima, avatar num card 700×560 embaixo (cabeça inteira); "(previsão)" junto do "por ano, com IA".
- Sem custo novo de ElevenLabs (só re-render local).
