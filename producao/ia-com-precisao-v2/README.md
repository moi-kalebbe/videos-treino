# Qahtani / IA · V2

Revisão solicitada após V1 receber 2/10. Histórico e fontes em `roteiros/ia-com-precisao-v2.md`.

## Reprodução local

- Não rodar o TTS novamente: áudios Beto e Moisés já gerados em `dub/` e `voz/`.
- `python3 preparar.py --audio-only`: reconstrói áudio e timeline preservando vídeos corrigidos.
- `rastrear-v2.py` foi executado no ambiente temporário `/tmp/qahtani-cv` com OpenCV 4; `faces-v2.json` registra posições, sem reconhecimento de identidade.
- `python3 enquadrar.py`: reconstrói enquadramento a partir da mídia combinada em `referencias/_brutos/qahtani-poder-palavras/trecho-v2-fontes.mp4`. As duas faixas de imagem mantêm a mesma sequência temporal; fontes/timestamps registrados no roteiro.
- `python3 montar-motion.py`: escreve composição editável.
- `npx --yes hyperframes@0.8.171 check`
- `npx --yes hyperframes@0.8.171 render -q high -w 2 -o ../../saida/ia-com-precisao-v2-bruto.mp4`
- `reparar-plano.py` (OpenCV) prepara a passagem de 65–72,5 s com cabeça inteira; `python3 sons.py` gera cliques/papel locais.
- `python3 finalizar.py`: aplica o plano recuperado e o cabeçalho, faz o mix, exporta Full HD, cópia leve e evidências.

A dublagem tem tempo por frase, sem geração labial. A segunda parte da palestra usa a fonte completa, menos nítida que a edição oficial. O conteúdo de saúde na abertura é o argumento fictício do discurso e é identificado como tal.

Sem publicação ou agendamento. Não sobrescreve a V1.
