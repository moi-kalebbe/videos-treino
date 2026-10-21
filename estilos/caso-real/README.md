# Estilo "Caso Real"

> **Desde 21/10/2026, o CTA `DIAGNÓSTICO` deste guia não vale mais para vídeos novos.** O fechamento segue `guias/fechamento-e-cta.md` (manda pro <pessoa específica> + salva quando ensina, 25–40 s).

Reel de 45–55 s que conta **um caso real de empresa que usou IA**, com **dado comprovado**, e termina numa lição de método. Aprovado pelo dono em 18/10/2026 (case Chewy v7: `saida/case-chewy-v7.mp4`, projeto `producao/case-chewy/`).

**Para quem:** dono, CEO, financeiro ou gestor que implanta tecnologia (quem **contrata**, não quem constrói).
**Objetivo:** ele comentar a palavra-chave e chamar para o diagnóstico.
**Teste da pauta:** "um CEO mandaria isso pro sócio?"

---

## 1. O que eu preciso de você (briefing)

| Item | Obrigatório? | Exemplo |
|---|---|---|
| O caso ou o tema | sim (ou "pesquisa um pra mim") | "empresa que cortou custo de atendimento com IA" |
| Palavra-chave do CTA | não (padrão `DIAGNÓSTICO`) | `DIAGNÓSTICO`, `MÉTODO` |
| Avatar | não (padrão: sim, em 3 momentos) | "sem avatar dessa vez" |
| Aprovar o gancho | sim | eu mando 3 opções, você escolhe 1 |
| Aprovar o custo | sim | eu mando a estimativa antes de gerar |

O resto (pesquisa, roteiro, voz, imagens, avatar, motion, legenda, render) é comigo.

## 2. Custo típico por vídeo (créditos ElevenLabs, plano Creator ≈ 121 mil/mês ≈ US$ 22)

| Item | Créditos |
|---|---|
| Narração na voz clonada (~770 caracteres) | ~800 |
| 4 imagens (Nano Banana 2, 9:16) | ~1.600 |
| Avatar 15 s (Sync 2 Pro) | ~7.700 |
| Trilha e efeitos | 0 (biblioteca em `modelo/assets/audio/`) |
| Motion, legenda, render (HyperFrames local) | 0 |
| **Total** | **~10.000 (≈ US$ 1,90)** → ~10 vídeos/mês no plano |

Sem avatar: ~2.400 créditos.

## 3. Estrutura (7 cenas, uma fala por cena)

| # | Tempo | Fala (papel) | Visual |
|---|---|---|---|
| 1 | 0–7 s | **Gancho**: número grande + contradição ("…vai economizar 50 milhões… E o segredo não foi a IA.") | **Tela dividida**: foto real do assunto + kicker `CASO REAL · PAÍS` + número gigante lima em cima; **avatar** num card 700×560 embaixo; frase do gancho numa faixa escura entre os dois; risco vermelho na palavra negada |
| 2 | 7–16 s | **Contexto com dado**: "Isso é raro. Uma pesquisa da {fonte}…" | "Isso é raro." em serifa itálica lima; grade de 100 pontos que fica vermelha no %; selo do % contando; fonte na tela |
| 3 | 16–21 s | **Quem é a empresa** ("…é a exceção.") | foto real (do setor da empresa) em card + **logo oficial** + "é a exceção." |
| 4 | 21–31 s | **O que ela fez** (3 áreas, cada uma com 1 número ou verbo) | 3 cards em cascata (mini-imagem + rótulo + frase); número só aparece quando é falado; fonte na tela |
| 5 | 31–41 s | **O segredo / a base** | título + barra de tempo; encaixes tracejados vazios que se preenchem com os blocos falados; bloco "IA" lima cai por último |
| 6 | 41–45 s | **Frase-tese** (curta, memorável) | **avatar** num card no alto + frase grande com fim em serifa itálica lima; peças girando cada vez mais rápido atrás |
| 7 | 45–50 s | **CTA**: "Quer saber se a sua empresa está pronta? Comenta {PALAVRA}." | **avatar** em card redondo; campo de comentário digitando a palavra; notificação de direct; palavra em caixa lima |

## 4. Identidade visual

- Fundo `#0b1020` com radial azul e grade sutil; acento **lima `#d7ff3a`**; vermelho `#ff5a5f` para o negativo.
- Tipografia: **Inter 800** (títulos, legenda) + **Instrument Serif itálico** (palavra de ênfase). Fontes locais em `modelo/assets/fonts/`.
- Kicker em caixa alta 28 px, espaçado, lima.
- **Legenda**: até 3 palavras por bloco, pílula escura, palavra falada em lima; posição y = 1540.
- **Logo do dono** (versão branca) no canto superior direito, 150 px, o vídeo todo. **Nunca** texto "MOISÉS KALEBBE".
- Barra de progresso lima no topo.
- Avatar em card com borda lima 5 px; **sem selo "avatar gerado com IA"** (o dono não quer).
- **Fonte na tela** (22 px, cinza) em toda cena com dado.

## 5. Roteiro: regras

- Voz da marca MK (skill `copy-avancada` + `voice-mk.md`): **sem travessão**, frases curtas, dono como herói, IA é "o como".
- Gancho: número concreto + contradição, legível no quadro 0. Escrever 3 opções e pedir aprovação.
- **Tudo que aparece na tela é falado** e vice-versa (a v1 levou nota 3 também por mostrar 4 blocos e falar 3).
- Projeção é dita como projeção ("prevê", "(previsão)" na tela).
- Siglas que a voz pronuncia mal: `{PwC|pê dáblio cê}` em `falas.txt` (a legenda mostra "PwC", a voz fala "pê dáblio cê").
- "IA": escrever normal ("IA"); com as configurações da voz abaixo fica natural.
- Uma fala por linha em `falas.txt`, uma linha por cena (7 linhas). Exemplo: `modelo/falas-exemplo.txt`.
- Fonte primária obrigatória (teleconferência de resultados, relatório oficial, pesquisa séria). Blog de fornecedor não serve.

## 6. Áudio

- Voz: **clone do Moisés** `aORS9tvW5qcMM0bnzsRU`, `eleven_multilingual_v2`, settings `0.45 / 0.85 / 0.25 / speaker_boost` (já são o padrão de `scripts/narracao.py`).
- Gerar com `python3 scripts/narracao.py <falas.txt> <assets> --voz aORS9tvW5qcMM0bnzsRU`, que gera **fala por fala** com silêncio real entre elas. **Nunca** usar `<break>`: o modelo inventa palavras dentro da pausa.
- Efeitos amarrados às palavras com `data-sinc` e recalculados com `python3 scripts/sincronizar-audio.py <projeto>` sempre que a narração mudar.
- Trilha a 0,16 de volume; mix final normalizado para **-14 LUFS** (`ffmpeg … loudnorm=I=-14:TP=-1.5:LRA=11`).
- Conferir sempre com **whisper local** (nunca Scribe do ElevenLabs). Transcrever em trechos de ~10 s, porque em arquivo longo o Whisper pula frases.

## 7. Avatar (3 momentos: gancho, frase-tese, CTA)

1. Recortar da narração os trechos das cenas 1, 6 e 7 e juntar num único áudio (`avatar/fala-avatar.mp3`), com **+0,7 s de silêncio no fim do último trecho** (sem isso a última palavra parece cortada).
2. Base: `producao/base-avatar/01/video.mp4`, trecho limpo 15–42 s, recorte `crop=1064:1064:8:856`, com duração ≥ áudio.
3. Fluxo no ElevenLabs Flows: 2 referências (vídeo e áudio) + nó **Sync 2 Pro**. O seletor do conector falha; subir os arquivos pelo **Chrome (Browser 1, macOS)** com `file_upload`. O dono aceita a política de upload ele mesmo.
4. Pedir `estimate_only`, passar o custo ao dono, rodar só o nó de sincronia (rodar junto com um nó de fala gera a fala duas vezes).
5. Recortar o resultado em `assets/avatar/clip1-3.mp4` e posicionar com `data-sinc="cena:N:0"`. Os `<video>` ficam **fora** do `#palco` (não pode haver ancestral com `data-start`).

## 8. Imagens

- 3–4 fotos reais geradas (Nano Banana 2, `aspect_ratio 9:16`, ~406 créditos cada), sem texto e sem logo, paleta azul-marinho com luz quente.
- **Nunca repetir** a mesma foto em duas cenas.
- Logo da empresa do caso: Wikimedia Commons (conferir licença).
- Foto do gancho com espaço vazio em cima para o título; o avatar **não cobre** o assunto da foto.

## 9. Checklist antes de entregar
- [ ] 2 a 4 efeitos de [`guias/efeitos-video.md`](../../guias/efeitos-video.md) escolhidos e anotados no roteiro (sugestões para este estilo estão lá).
- [ ] `npx hyperframes check` sem erros
- [ ] Folha de contato do MP4 (1 quadro/s) + 1º quadro em tamanho cheio
- [ ] Nada sobreposto sem querer; número não aparece antes de ser falado
- [ ] Transcrição local por trechos: pronúncia certa, sem falas fantasmas
- [ ] -14 LUFS
- [ ] Nota pela [rubrica](../../guias/rubrica-qualidade.md) registrada no roteiro; ≥ 9
- [ ] **Capa pronta** (seção 12) e conferida nos recortes 3:4 e 4:5: o Instagram **não deixa trocar a capa depois** de publicado
- [ ] Para aprovação do dono: vídeo + capa (com prévia dos recortes) + legenda, juntos

## 10. Passo a passo

```bash
scripts/novo-video.sh caso-real <slug>          # copia o modelo para producao/<slug>
# 1. pesquisa + 3 ganchos → aprovação
# 2. escrever producao/<slug>/falas.txt (7 linhas) e roteiros/<slug>.md
python3 scripts/narracao.py producao/<slug>/falas.txt producao/<slug>/assets --voz aORS9tvW5qcMM0bnzsRU
# 3. imagens (Nano Banana 2) → producao/<slug>/assets/img/
# 4. avatar (seção 7) → producao/<slug>/assets/avatar/
# 5. ajustar textos/cenas no index.html
python3 scripts/sincronizar-audio.py producao/<slug>
cd producao/<slug> && npx hyperframes check && npx hyperframes render -q high -o ../../saida/<slug>.mp4
```

## Histórico de notas do dono (o que ensinou)

| Versão | Nota | Lição |
|---|---|---|
| v1 | 3 | Sem rosto, sem imagem real, sem logo, gancho fraco, tela ≠ fala |
| v6 | 7 | Avatar cobrindo o assunto; selo "avatar IA"; marca em texto |
| v7 | aprovada | Tela dividida no gancho, logo real, sem selo |

## 11. Publicar no Instagram

```bash
python3 scripts/publicar-instagram.py saida/<slug>.mp4 roteiros/<slug>-legenda.txt --capa producao/<slug>/capa/capa-9x16.jpg   # prepara, não publica
python3 scripts/publicar-instagram.py --conteiner <ID>                                              # publica (só com o ok do dono)
```
O MP4 sai do Mac por um túnel temporário do Cloudflare (nome aleatório, fecha sozinho). Legenda na voz MK, com as fontes e "previsão" quando for o caso, CTA com a palavra-chave e 5 hashtags.

## 12. Capa (responsiva: Reels, grade e feed)

O Instagram mostra a mesma capa em 3 recortes. A capa é 1080×1920, mas **tudo que importa fica entre y=285 e y=1635** (recorte 4:5 do feed); a grade do perfil (3:4) corta y=240–1680; no Reels os botões cobrem o canto inferior direito.

Modelo: `modelo/capa/index.html` (é copiado junto pelo `novo-video.sh`). Layout aprovado: kicker + número gigante lima + "por ano, com IA" em cima; foto do assunto no meio **com o rosto/assunto livre**; faixa com a frase do gancho (palavra negada riscada em vermelho) logo abaixo; card do rosto do dono (quadro do avatar com expressão forte) + chamada "O que essa empresa fez *diferente*"; logo branca no canto direito.

```bash
# colocar a foto em capa/assets/img/ e o quadro do rosto em capa/assets/avatar/rosto-capa.png
ffmpeg -ss 5.3 -i avatar/sync-<slug>.mp4 -frames:v 1 capa/assets/avatar/rosto-capa.png
cd producao/<slug>/capa && npx hyperframes snapshot --at 0.5 --no-end -o /tmp/capa && cp /tmp/capa/frame-*.png capa-9x16.png
ffmpeg -i capa-9x16.png -q:v 2 capa-9x16.jpg
# conferir os recortes: crop=1080:1440:0:240 (grade) e crop=1080:1350:0:285 (feed)
python3 scripts/publicar-instagram.py saida/<slug>.mp4 roteiros/<slug>-legenda.txt --capa producao/<slug>/capa/capa-9x16.jpg
```
A capa só pode ser enviada **na hora de publicar**: depois, nem a API nem o app deixam trocar (aprendido no case Chewy, publicado sem capa). Por isso o script recusa publicar sem `--capa`.
