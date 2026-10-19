# Estilo "Dossiê"

Documentário de investigação curto, no jeito de *Mayday! Desastres Aéreos* (Nat Geo) e Investigação Discovery: **casos reais contados pelos relatórios oficiais**, um padrão entre eles, e a virada para a empresa ("a sua empresa está voando sem checklist"). Aprovado pelo dono em 19/10/2026 (edição 01: `producao/dossie-01/`, roteiro `roteiros/dossie-01-o-detalhe.md`, no ar sex 23/10/2026). Ideia original: Fernanda Jurgensen.

**Para quem:** dono, CEO, gestor. **Objetivo:** alcance pela carona num assunto em alta + autoridade (documento oficial na tela) → CTA `DIAGNÓSTICO`.
**Quando usar:** quando um assunto real está em alta (documentário, aniversário de tragédia, notícia) e dá para ligar os casos a **um padrão de processo** que também existe nas empresas (conferência, alerta ignorado, cansaço, dono do processo).

## 1. O que preciso do dono (briefing)
| Item | Obrigatório? |
|---|---|
| Tema/casos (ou "escolhe você") | não |
| Aprovar roteiro + data | sim |
| Escolher o narrador (amostras de 10 s) na primeira vez de cada série | sim |

## 2. Custo
Narração ~2.000 créditos (narrador de biblioteca + a voz do dono na virada). Imagens do Pexels, relatórios oficiais (públicos) e trilha da Pixabay são grátis. Cenas geradas (FLUX + LTX no Mac) também, quando o Hugging Face está no ar.

## 3. Estrutura (~90–120 s)
| Bloco | O que é | Ed. 01 |
|---|---|---|
| **Abertura fria** | data, hora e lugar digitados na tela + uma contagem ("faltavam 4,6 km"), já dentro do caso mais conhecido | Marília Mendonça, 05 NOV 2021 |
| **Caso 1** | o que o relatório diz, com a **página real grifada** + um gráfico (mapa, régua) + carimbo "FATOR CONTRIBUINTE" | perna do vento alongada, cabo sem sinalização |
| **Respiro** | tela preta, silêncio: "UM DETALHE." → "**5** VIDAS" → título "DOSSIÊ · O DETALHE" | |
| **Casos 2 e 3** | ficha "CASO 2/3 · data · lugar", um número que conta a falha (barra, relógio), documento grifado, "**N** VIDAS" | Chapecoense (4h22 = 4h22), Mamonas (16h30 × 11h) |
| **O padrão** | um dado com fonte ("70–80%, FAA") + "um detalhe que ninguém conferiu, um alerta que ninguém ouviu, um cansaço que ninguém viu" + o que a área aprendeu (acidente → relatório → regra → checklist) | |
| **A virada (voz do dono)** | troca de voz = troca de capítulo; perguntas sobre a empresa em cartões; "voando sem checklist" | |
| **A saída** | painel de IA com 3 alertas concretos, **dados fictícios marcados** e "revisão humana" | preço abaixo da tabela, cliente sem resposta, pedido parado |
| **CTA** | comenta `DIAGNÓSTICO` + "Em memória de todas as vítimas" quando houver vítimas | |

## 4. Linguagem (o que é deste estilo)
- **Paleta fria:** fundo `#070b10`, aço, branco `#e9eef3`, ciano `#5fd3e6` para dados, **marca-texto amarelo** `#ffd23f` só nos trechos dos documentos, **vermelho** `#e0312b` só em carimbo e número de vítimas. Nada do dourado/Anton da A Virada nem do lima da sexta.
- **Tipografia:** JetBrains Mono para tempo, lugar, fichas e fontes; Inter 800 para números grandes; legenda de **frase inteira**, discreta (não karaokê).
- **Documento como prova:** página real do relatório (PyMuPDF: `search_for` + `add_highlight_annot`), entrando como papel levemente torto, e a câmera desce até o trecho grifado. PDF escaneado: grifar com `drawbox` no ffmpeg.
- **Som:** drone grave → **silêncio seco** no lugar de qualquer impacto (nunca som de batida) → trilha de investigação → piano no "o que aprendemos" → pulso na virada. Chiado de rádio, bipe de radar, papel, carimbo, relógio.
- **Voz:** narrador de documentário da biblioteca ElevenLabs (ed. 01: **Dimmy**, `chFi7TdzwurwZVzGKeLH`, escolhido pelo dono) nos casos; **a voz do dono só na virada**. Gerar **em blocos** com `scripts/narracao_blocos.py` (soa fluido; frase por frase soa "lendo").
- **Imagem:** banco real (Pexels) com selo "IMAGENS ILUSTRATIVAS"; reconstituição gerada só sem rosto e sem marca de companhia.

## 5. Regras de respeito e de fato (inegociáveis)
- **Só o que o relatório oficial diz**, com a mesma força: "o relatório apontou como fator que contribuiu", nunca "o piloto errou". Lembrar na legenda que o CENIPA não aponta culpados.
- **Nada** de imagem das vítimas, do acidente, de destroços, de velório ou de família. Nada de som de impacto. Nada de humor.
- **Sem trecho de telejornal** (direito da emissora, risco de strike) e **sem foto de pessoa real** (direito de imagem). Pode: documento público, manchete curta com fonte, áudio oficial curto com crédito.
- **Carona sem copiar:** a capa evoca o assunto em alta (cor, luz, tipografia), sem logo, pôster ou foto.
- Checar cada número com a fonte primária antes de gravar (ed. 01: um agente leu os 3 relatórios inteiros; achou que "fadiga" era fato oficial e que só 1 dos 4 fatores do caso Marília era "contribuiu").

## 6. Passo a passo
```bash
scripts/novo-video.sh dossie dossie-NN-<tema>
# 1. pesquisa: relatórios oficiais (PDF), datas, números, o que é "contribuiu" × "indeterminado"
# 2. falas.txt em blocos (#voz=, #pausa=, linha em branco fecha o bloco) → amostras de voz se for narrador novo
python3 scripts/narracao_blocos.py producao/<slug>/falas.txt producao/<slug>/assets
# 3. páginas grifadas → assets/img/; Pexels → assets/broll/ (conferir HDR!); trilha Pixabay em atos
# 4. adaptar index.html (CENAS, em("palavra", n), docs com a fração do trecho na página)
python3 scripts/sincronizar-audio.py producao/<slug> --fim-extra 2.7
cd producao/<slug> && npx --yes hyperframes@0.8.171 check && npx --yes hyperframes@0.8.171 snapshot --at ... && npx --yes hyperframes@0.8.171 render -q high -o ../../saida/<slug>-bruto.mp4
# 5. loudnorm -14 LUFS, whisper local por trechos, cópia -crf 26
```

## 7. Capa
Fundo escuro que evoca o assunto em alta (ed. 01: luzes douradas de palco desfocadas da série da Marília), nome do caso principal no topo, título "O detalhe que a *investigação* encontrou" (serifa itálica ciano na palavra-chave), carimbo vermelho, "+ outros casos" em mono, e um quadro frio do vídeo embaixo. Conferir recortes 4:5 e 3:4.

## 8. Checklist
- [ ] Cada afirmação bate com o relatório (e com a força certa)
- [ ] Nenhuma imagem de vítima, acidente, velório; nenhum som de impacto
- [ ] Páginas reais grifadas na tela, com nome e página do relatório
- [ ] Respiro em tela preta com o número de vidas
- [ ] A virada liga o padrão a uma dor concreta da empresa, na voz do dono
- [ ] Painel de IA com dados fictícios marcados e revisão humana
- [ ] Sem HDR antes do render; -14 LUFS; whisper ok; capa conferida
