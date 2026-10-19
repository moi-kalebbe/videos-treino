# Bancos de mídia e geração grátis

**Regra:** antes de gastar crédito com imagem ou vídeo gerado, ver se algo daqui resolve a cena.
Ordem: banco grátis (filmagem real) → motion no HyperFrames → modelo aberto local → IA paga só em 1 ou 2 planos-chave.
Anotar a fonte e a licença de cada arquivo usado no roteiro (seção Fontes).

| Recurso | O que tem | Chave | Licença | Bom para |
|---|---|---|---|---|
| **Pexels** | vídeos (até 4K vertical) e fotos | `PEXELS_API_KEY` ✅ | uso comercial livre, sem crédito obrigatório | B-roll de escritório, cidade, tecnologia, pessoas trabalhando |
| **Pixabay** | vídeos, fotos, músicas e efeitos sonoros | `PIXABAY_API_KEY` ✅ | uso comercial livre | B-roll, trilha e SFX extras |
| **Coverr** | vídeos de B-roll | criar se precisar | uso comercial livre | escritório, notebook, reunião |
| **Unsplash** | fotos (sem vídeo) | criar se precisar | uso comercial livre | foto de abertura, capa |
| **Freesound** | efeitos sonoros | `FREESOUND_API_KEY` (vazia) | **varia por som**: usar só CC0 ou CC-BY (e creditar) | SFX que a biblioteca não tem |
| **NASA** (images.nasa.gov) | imagens e vídeos de espaço e Terra | não precisa | domínio público (sem usar o logo da NASA como endosso) | satélite, Terra à noite, "volta ao mundo", cabos/rotas |
| **Wikimedia Commons** | logos de empresas, fotos de pessoas públicas e lugares | não precisa | **conferir arquivo por arquivo** (muitos logos são marca registrada: usar só para identificar a empresa do caso) | logo da empresa no Caso Real, foto de fachada |
| **Hugging Face** | modelos abertos rodando nos servidores deles (Spaces) | conta `kalebbe` conectada | depende do modelo | gerar vídeo/imagem com modelo aberto quando o Mac não der conta (cota diária grátis) |
| **LTX-Video local** | modelo aberto de vídeo (Lightricks), roda no Mac | não precisa | aberta (conferir licença da versão) | B-roll e cenas de exagero de ~4 s sem crédito, ~1 min por clipe (ver abaixo) |

## Como buscar

```bash
# Pexels (vídeo vertical)
curl -s -H "Authorization: $PEXELS_API_KEY" "https://api.pexels.com/videos/search?query=data%20center&orientation=portrait&per_page=10"
# Pixabay (vídeo)
curl -s "https://pixabay.com/api/videos/?key=$PIXABAY_API_KEY&q=server+room&per_page=10"
# NASA (sem chave)
curl -s "https://images-api.nasa.gov/search?q=earth%20night&media_type=video"
```
Baixar o arquivo para `producao/<slug>/assets/broll/` (fora do git, como todo vídeo) e guardar a URL da página de origem no roteiro.

```bash
# Wikimedia Commons: foto histórica (filtrar "Public domain") e baixar redimensionada
curl -s -G "https://commons.wikimedia.org/w/api.php" --data-urlencode "action=query" --data-urlencode "format=json" \
  --data-urlencode "generator=search" --data-urlencode "gsrnamespace=6" --data-urlencode "gsrsearch=Titanic 1912" \
  --data-urlencode "prop=imageinfo" --data-urlencode "iiprop=url|size|extmetadata" --data-urlencode "iiextmetadatafilter=LicenseShortName"
curl -sL -o foto.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/<Arquivo.jpg>?width=2000"
# NASA Black Marble (Terra à noite, equiretangular: x=(lon+180)/360*W, y=(90-lat)/180*H)
curl -sL -o terra.jpg "https://eoimages.gsfc.nasa.gov/images/imagerecords/144000/144898/BlackMarble_2016_3km.jpg"
```

**Música e efeitos da Pixabay** não têm API. Abrir `pixabay.com/music/search/<termo>/` (ou `/sound-effects/search/`) no navegador embutido e, no JS da página, buscar cada faixa com `fetch` e pegar o link `cdn.pixabay.com/download/audio/...mp3`; depois baixar com `curl -e https://pixabay.com/`.

**Imagem gerada grátis (Hugging Face):** o conector do Claude não deixa invocar Spaces. Usar `gradio_client` no venv `~/.cache/ltx-teste` (`flux.py <saida> "<prompt>"`, Space `mcp-tools/FLUX.1-Krea-dev`, 768x1344). Sem token HF a cota é de ~3 imagens por dia; com token, bem mais. Ficou com cara de cinema (vigia no mastro, chave antiga, armário) na A Virada 01.

## LTX-Video local (teste em 18/10/2026)
Ambiente em `~/.cache/ltx-teste/` (fora do repo): `.venv` com PyTorch (MPS) + diffusers, script `gerar.py`.
Modelo `ltxv-2b-0.9.8-distilled` (8 passos) + T5 em bf16 carregado à parte, para caber nos 16 GB.
Resultado do teste (19/10/2026): **funciona**. Prompt de exagero ("funcionário soterrado por avalanche de planilhas") saiu convincente: 97 quadros 512x768 (~4 s a 24 fps) em **~67 s de geração** + ~45 s para codificar o prompt, sem crédito nenhum. Limites: resolução baixa (ampliar para 1080 perde nitidez; usar com grão/vinheta), 4 s por clipe, rosto e texto podem deformar, física de "explosão" às vezes vira mancha branca. Bom para cenas de exagero estilo Abrahub em cortes de 1–2 s.
Correção necessária no `gerar.py`: trocar o scheduler para `FlowMatchEulerDiscreteScheduler.from_config(..., use_dynamic_shifting=False)` (senão dá erro de `mu`).
Uso: `cd ~/.cache/ltx-teste && source .venv/bin/activate && python gerar.py texto "<prompt em inglês>" && python gerar.py video saida.mp4`.

## Atenção: vídeo HDR do Pexels (aprendido em 19/10/2026)
Alguns vídeos do Pexels são HDR de iPhone (`color_transfer=arib-std-b67`, `bt2020`). Basta **um** clipe assim para o HyperFrames renderizar o vídeo inteiro em HDR 16 bits: fica 10× mais lento (50 min sem terminar) e sai com perfil de cor errado para o Instagram. Antes de renderizar:
```bash
for f in producao/<slug>/assets/video/*.mp4; do ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer -of csv=p=0 "$f" | grep -qE "b67|2084" && echo "HDR: $f"; done
```
Para cada HDR: `ffmpeg -i in.mp4 -vf "setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709,eq=contrast=1.12:saturation=1.1:gamma=0.95" -color_primaries bt709 -color_trc bt709 -colorspace bt709 -c:v libx264 -crf 20 -pix_fmt yuv420p out.mp4`. Render normal de ~2 min de vídeo: 5 min. Renderizar um vídeo por vez.
