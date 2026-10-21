# Variações do avatar: fundo e cor de camisa

Uma gravação do dono vira várias bases de avatar: fundo novo, cor de camisa nova ou as duas coisas. Roda local no Mac (MPS), **sem crédito**. A voz é o clone 1 (`aORS9tvW5qcMM0bnzsRU`). A fala nova entra depois, com a sincronia labial (Sync 2 Pro, ver `producao/base-avatar/README.md`).

Referência visual: @oandrenuneu em `referencias/lote-03.md` (o cenário e a roupa mudam a cada assunto, com uma linha de luz varrendo na transição).

## Ferramentas
- Recorte da pessoa: [RobustVideoMatting](https://github.com/PeterL1n/RobustVideoMatting) (resnet50, tem memória entre quadros, então a borda não treme).
- Máscara da camisa: SegFormer `mattmdjaga/segformer_b2_clothes` (classe Upper-clothes).
- Ambiente: `~/.cache/avatar-tools/.venv` e modelos em `~/.cache/avatar-tools/modelos/` (fora do repo).
- Script: `scripts/avatar_variacoes.py`.

## Passo a passo
1. Cortar o trecho e reduzir para 1080×1920 (o iPhone grava em 4K girado; o ffmpeg já desvira):
   `ffmpeg -ss 40 -t 4 -i IMG_0619.MOV -vf scale=1080:1920 -map 0:v:0 -map 0:a:0 -c:v libx264 -crf 14 -c:a aac trecho.mp4`
2. Gerar a variação:
   `~/.cache/avatar-tools/.venv/bin/python -I scripts/avatar_variacoes.py trecho.mp4 saida.mp4 --fundo fundo.jpg --camisa "#1f2a44"`
   - `--fundo` aceita imagem, vídeo (roda em loop) ou cor `#RRGGBB`.
   - `--camisa` aceita cor `#RRGGBB`.
3. Velocidade medida no M5: ~10 s de processamento por segundo de vídeo com as duas trocas.

## O que funciona (teste de 20/10/2026)
- **Camisa clara virando qualquer cor** (azul-marinho, preta, branca): fica natural e mantém dobras e sombras. A camisa social azul-clara do vídeo IMG_0619 é a melhor base.
- **Polo preta**: troca de fundo perfeita, e escurecer para outra cor escura (azul-marinho) também fica natural. Clarear tecido preto (branco, bege) não fica bom: não há detalhe de dobra para preservar. O dono aprovou usar a polo (20/10).
- **Fundo**: escolher fundo **sem pessoas** e com luz parecida com a do rosto. Desfocado parece mais real.
- **Troca de roupa inteira** (camisa → terno ou jaleco) não é coberta: precisa de edição por IA paga (Kling O3 Edit). Medir custo num trecho curto antes.
- O reflexo da camisa entre as mãos continua com a cor original. Para fechar isso, ajustar a máscara.

## Enquadramento
- **Usar do umbigo para cima** (pedido do dono, 20/10): corta os fiapos da polo e aproxima o rosto. A gravação é 4K (2160 px de largura), então dá para dar zoom de até ~2× sem perder qualidade em 1080×1920.
- Cortar o trecho já com zoom antes de rodar as variações: `-vf "crop=iw/1.6:ih/1.6:(iw-ow)/2:ih*0.05,scale=1080:1920"` (ajustar o `y` para o umbigo ficar na borda de baixo).

## Gravações-base (fora do git, em `producao/base-avatar/brutos/`)
| Arquivo | Roupa | Trecho só com o dono | Observação |
|---|---|---|---|
| IMG_0619.MOV | camisa social azul-clara | 0–64 s | 4K 30 fps SDR; aponta para a direita e para a esquerda, joia, sério, rindo |
| IMG_0621.MOV | polo preta | 0–69 s | mesmos gestos + "impacto", "olha isso", "veja essa notícia" |

Depois desses trechos há conversa com a filha do dono. **Não usar** esse trecho no avatar nem na voz.
