# Estilo "Plantão IA"

> **Desde 21/10/2026, o CTA `DIAGNÓSTICO` deste guia não vale mais para vídeos novos.** O fechamento segue `guias/fechamento-e-cta.md` (manda pro <pessoa específica> + salva quando ensina, 25–40 s).

Telejornal semanal de ~85 s com **as 6 notícias de IA da semana**, publicado **todo domingo às 18h**. Aprovado pelo dono em 18/10/2026 (edição 01: `saida/plantao-ia-01.mp4`, projeto `producao/plantao-ia-01/`, roteiro `roteiros/plantao-ia-01.md`).

**Para quem:** público amplo interessado em IA (alcance), com a última notícia puxando para empresa.
**Objetivo:** virar hábito de domingo e levar ao CTA `DIAGNÓSTICO` pela notícia que importa para empresa.
**Tom:** telejornal um pouco sensacionalista, humor leve nas inusitadas, seriedade no alerta. Linguagem de conversa ([guia](../../guias/linguagem-natural.md)).

---

## 1. O que eu preciso de você (briefing)

| Item | Obrigatório? | Exemplo |
|---|---|---|
| Aprovar as 6 notícias + selos + tom | sim | eu pesquiso a semana e mando a pauta |
| Aprovar o roteiro | sim | 8 falas (abertura, 6 notícias, fechamento) |
| Palavra-chave do CTA | não (padrão `DIAGNÓSTICO`) | |
| Aprovar o custo | sim | estimativa antes de gerar |
| Ok para publicar | sim | eu preparo o Reel e agendo para domingo 18h |

## 2. Custo típico por edição (créditos ElevenLabs)

| Item | Créditos |
|---|---|
| Narração na voz clonada (~1.100 caracteres, 8 falas) | ~1.200 |
| 4 cenas geradas (Nano Banana 2, 9:16) | ~1.600 |
| Avatar da abertura ~7 s (Sync 2 Pro) | ~3.500 |
| Vinheta, stings e trilha | 0 (biblioteca em `modelo/assets/audio/`, feita na edição 01 por ~2.000) |
| Motion, efeitos, recorte do avatar, render (HyperFrames local) | 0 |
| **Total** | **~6.300** |

## 3. Estrutura (8 falas, uma por linha em `falas.txt`)

| # | Tempo | Fala | Visual |
|---|---|---|---|
| 0 | 0–6,5 s | **Abertura**: "Plantão IA. Seis notícias de IA da semana. E a última pode estar acontecendo na sua empresa." | **headline wall** 3D com as 6 manchetes, **avatar recortado (green screen)** na frente com brilho vermelho, vinheta; **zoom-through** no card da notícia 1 |
| 1–6 | ~10–14 s cada | **Notícia** (fato concreto → detalhe → fecho com humor, opinião ou impacto real) | selo (🚀 LANÇAMENTO, 💣 BOMBA, 🤦 INUSITADO, 🧠 CIÊNCIA, ⚠️ ALERTA, 🏢 NA SUA EMPRESA) + **tarja inferior** (local + manchete) + contador `n/6`; cena gerada com Ken Burns **ou** visual próprio (mapa com rota, chuva de páginas, número gigante); **aba de portal** com a manchete real e marca-texto lima; carimbo vermelho no clímax |
| 6 | | A última é sempre **a que importa pra empresa** | medidor de impacto subindo até ALTO |
| 7 | ~4 s | **Fechamento**: "Se você quer descobrir, comenta DIAGNÓSTICO. Domingo que vem tem mais." | grade com as 6 manchetes (a 6ª em destaque), "Quer descobrir? Comenta", campo digitando a palavra, selo PLANTÃO IA + "Todo domingo, *18h*" |

Fixos o vídeo todo: barra superior (selo PLANTÃO IA, "EDIÇÃO NN · DD/MM", contador, logo branca), **ticker** "ÚLTIMAS" no rodapé, barra de progresso vermelha, legenda por palavra (pílula, palavra falada em branco).

## 4. Identidade visual

- Fundo `#070b18` com radial azul e linhas de TV; **vermelho telejornal `#e5162e`**, lima `#d7ff3a` para marca-texto e rabisco.
- Inter 800 + Instrument Serif itálico + JetBrains Mono (URL e contador). Fontes em `modelo/assets/fonts/`.
- Mídia num card 1000×1030 (y 190–1220); tarja em y 1250; legenda em y 1590; ticker em y 1850.
- Logo branca 140 px no canto superior direito. Nunca texto "MOISÉS KALEBBE". Sem selo "avatar IA".
- Não imitar marca de TV real (a cena de estúdio da notícia do Bill Gates é genérica, sem logo da CNN).

## 5. Roteiro: regras

- Notícias da **semana** (seg–dom), cada uma com 2+ fontes listadas no roteiro. Acusação dita como acusação.
- Ordem: começa forte (lançamento grande), alterna sério e engraçado, **termina na que mexe com empresa**.
- "O que muda pra empresa" **só na notícia que de fato mexe**; as outras terminam na história, no humor ou numa opinião curta.
- Manchete da aba de portal = título real (em inglês, se for o caso); tarja e fala em português.
- Número só aparece quando é falado. Uma fala por linha, sem `<break>`, "IA" escrito normal ([voz e áudio](../../guias/voz-e-audio.md)).

## 6. Áudio

- Voz clone `aORS9tvW5qcMM0bnzsRU` o vídeo todo, via `scripts/narracao.py`.
- Efeitos com `data-sinc` (ex.: `cena:2:0` para o suspense, `palavra:preso:1:0.1` para o carimbo, `palavra:não:1:0.15` para o trombone) + `scripts/sincronizar-audio.py`.
- Por notícia: `ding` na entrada, `teletipo` na aba de portal; `suspense` na BOMBA, `trombone` no clímax da INUSITADO, `glitch` no ALERTA, `alerta` + `carimbo` na NA SUA EMPRESA. Trilha 0,14. Final a -14 LUFS.
- **Cuidado na conferência:** em trechos de 10 s o whisper às vezes erra na borda (escreveu "era Iá"). Antes de refazer uma fala, transcrever **só aquele trecho** isolado.

## 7. Avatar (só na abertura)

1. Recortar a fala 0 da narração + 0,7 s de silêncio → `avatar/fala-avatar.mp3`; base de rosto de 8 s.
2. Sync 2 Pro no ElevenLabs Flows (upload pelo Chrome, `estimate_only` antes) → `assets/avatar/clip-abertura.mp4`.
3. **Green screen local:** `npx hyperframes remove-background assets/avatar/clip-abertura.mp4 -o assets/avatar/abertura-recorte.webm --quality best` (~40 s, sem crédito).
4. `<video>` do recorte **fora** do `#palco`, `object-fit: contain`, máscara de degradê embaixo.
5. Quadro com boa expressão → `capa/assets/avatar/rosto-capa.png`.

## 8. Imagens

- 4 cenas geradas (Nano Banana 2, 9:16) para as notícias que não têm visual próprio. Sem texto e sem logo.
- Notícias com número, mapa ou volume ganham visual em motion (contador, rota SVG, chuva de páginas) em vez de imagem.

## 9. Efeitos (ver [catálogo](../../guias/efeitos-video.md))

Fixos do estilo: **headline wall**, **zoom-through cut**, **green screen** (abertura), **doodle boil** (clímax da inusitada).
A cada edição, escolher mais 1 ou 2 conforme as notícias (ex.: **phone mockup**/**UI world** para lançamento de app, **chart grow** para número, **paper cut** para humor).

## 10. Checklist antes de entregar
- [ ] Pauta e roteiro aprovados; fontes no roteiro
- [ ] Efeitos da edição anotados no roteiro
- [ ] `npx hyperframes check` sem erros; snapshots de cada notícia revisados (cuidado com `em("palavra", n)`: contar a ocorrência na narração **inteira**; na edição 01 o 1º "ela" era da notícia do Google)
- [ ] Nada cobre rosto ou assunto da imagem (carimbos abaixo do rosto)
- [ ] Transcrição local por trechos; -14 LUFS
- [ ] Nota pela [rubrica](../../guias/rubrica-qualidade.md) ≥ 9
- [ ] Capa (4:5 conferido) + legenda com as 6 manchetes e as fontes
- [ ] Para aprovação: vídeo + capa + legenda juntos. Vídeo > 30 MB: mandar cópia `-crf 26` para o celular

## 11. Passo a passo

```bash
scripts/novo-video.sh plantao-ia plantao-ia-NN
# 1. pesquisa da semana → pauta (6 notícias, selos, tom) → aprovação
# 2. roteiros/plantao-ia-NN.md + producao/plantao-ia-NN/falas.txt (8 linhas) → aprovação + custo
python3 scripts/narracao.py producao/plantao-ia-NN/falas.txt producao/plantao-ia-NN/assets --voz aORS9tvW5qcMM0bnzsRU
# 3. cenas → assets/img/ ; avatar + recorte (seção 7)
# 4. trocar no index.html: manchetes da parede, tarjas, portais (site + URL + manchete + trecho marcado), números, grade final, ticker, "EDIÇÃO NN · DD/MM"
python3 scripts/sincronizar-audio.py producao/plantao-ia-NN
cd producao/plantao-ia-NN && npx hyperframes check && npx hyperframes render -q high -o ../../saida/plantao-ia-NN-bruto.mp4
ffmpeg -i saida/plantao-ia-NN-bruto.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k saida/plantao-ia-NN.mp4
```

## 12. Capa e publicação

- Capa: `modelo/capa/index.html`. Selo PLANTÃO IA + "EDIÇÃO NN · DATA" em cima; foto da **notícia mais curiosa** com o rosto livre; tarja branca com a manchete curta e o fim em serifa itálica vermelha ("Viajou 2 mil km pela namorada. *Ela era IA.*"); card do rosto do dono + "+ 5 notícias de IA *da semana*". Tudo entre y=285 e y=1635.
- Publicar: preparar o contêiner antes (`publicar-instagram.py <mp4> <legenda> --capa <jpg>`, guarda 24 h) e, no horário, só `--conteiner <ID>`. Para domingo 18h, deixar um job esperando o horário com `caffeinate` (o Mac não pode dormir).

## Histórico

| Edição | Nota | Lição |
|---|---|---|
| 01 v1 | 8,5 (minha) | Vazio na notícia sem imagem; mapa sumiu por ocorrência errada de palavra; carimbo cobrindo rosto; fechamento vazio |
| 01 v2 | aprovada ("fantástico") | Abertura com parede de manchetes + zoom-through + avatar recortado; rabisco no clímax; fechamento cheio |
