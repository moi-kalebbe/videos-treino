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
| **LTX-Video local** | modelo aberto de vídeo (Lightricks), roda no Mac | não precisa | aberta (conferir licença da versão) | B-roll de fundo de 3 a 5 s sem crédito. **Em teste** (ver abaixo) |

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
Resultado do teste: _a preencher_.
