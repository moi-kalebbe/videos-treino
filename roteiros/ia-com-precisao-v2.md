# Qahtani → decisões com IA · revisão 2

Solicitação do dono: preservar o trecho inteiro em que o palestrante constrói e conclui o raciocínio; deixá-lo visível; desenvolver motion com função narrativa. V1 recebeu 2/10. Não usar a nota interna como substituto do julgamento do dono.

## Direção
O tema pede que a demonstração seja assistida antes da explicação. O trecho vai da pergunta sobre cigarro à conclusão sobre mudar crenças e construir ou destruir com palavras. Preservar todos os argumentos, admissão, relato dos amigos e conclusão. A fala sobre tabaco é uma demonstração com argumentos inventados, identificada na imagem; não é informação de saúde. O relato dos amigos é apresentado como fala dele, não como acontecimento verificado independentemente.

A ponte usa uma venda ilustrativa. A resposta é aprovada, a folha sai de cima e revela custo antigo e frete omitido. A margem desaparece. A segunda sequência constrói o percurso: dados conferidos → ferramenta de cálculo → responsável. Não há código nem promessa de infalibilidade.

Diferente de V1/Hard Copy: palestra como plano principal, legendas em Inter por frase, paleta papel/verde escuro, documentos e ações que se transformam. Sem repetição de headline em Anton por cena.

Efeitos: UI world (pedido e decisão dentro da interface); pull-back/revelação (aprovação sai e mostra dados omitidos); chart grow invertido (margem se esvazia). Primitivas do catálogo lidas; implementação adaptada na timeline GSAP do HyperFrames, sem alegar uso de Framer Motion/React.

## Voz e custo
Beto para tradução do palestrante, Moisés para comentário. Sem clonagem do palestrante ou geração labial. Estimativa local registrada antes do TTS: 935 caracteres Beto + 612 Moisés = 1.547. Consumo real não consultado. Reutilizar áudios nas revisões de imagem.

## Fontes e mídia
- Palestra e contexto: fontes já listadas em ia-com-precisao.md.
- Upload inicial: https://www.youtube.com/watch?v=Iqq1roF4C8s . Alguns planos já vêm com enquadramento cortado; não chamar de gravação original oficial.
- Cópias comparadas: https://www.youtube.com/watch?v=I27y4mM9p-8 (640×260, limpa, qualidade limitada); https://www.youtube.com/watch?v=Z-RbbT55Vi0 (720p, legendas inglesas gravadas).
- Motion sobre vídeo de celular Pexels da biblioteca Movida; fonte registrada naquele roteiro.

## Ciclos de revisão
1. Roteiro: restabelecido argumento completo, sem interrupções da narração do dono.
2. Primeiro conjunto de snapshots: detectados pan que cortava o rosto, enquadramento problemático na própria fonte e sobreposição do título com o primeiro nó. Corrigidos layout e movimento; comparando fontes para corrigir enquadramento.
3. Validação técnica após correção: check sem erros/avisos e 26/26 verificações de contraste. Não equivale a aprovação editorial.
4. Render e inspeção final: pendentes.

Status: trabalho em revisão; publicação e agendamento não solicitados.

### Fonte oficial recuperada no ciclo 3
https://www.youtube.com/watch?v=qasE4ecA57Y — Toastmasters International, highlights em 1920×1080. O começo até a admissão foi preservado nessa edição; a parte dos amigos e a conclusão foram cortadas. Montagem utiliza os primeiros 48 s do recorte a partir de 20,650 s da fonte oficial, depois 39,6 s a partir de 90,100 s da cópia completa. A correlação do áudio confirma o deslocamento entre as cópias em amostras a cada 4 s (0,62–0,91). As falas não foram omitidas: troca-se a fonte de imagem da mesma gravação. A segunda fonte tem definição inferior; nenhuma melhora artificial foi prometida.

### Ciclo 4: validação da composição revisada
- Corrigido o pan lateral para manter o rosto dentro do quadro. Posições medidas localmente, sem identificação biométrica.
- Reduzida a folha do pedido depois de o zoom invadir a área de legenda. Snapshots novos em 98/100/105 s confirmam separação.
- Folhas da palestra a 1 quadro/s inspecionadas: imagem oficial mais nítida até 48 s; cópia completa depois. Alguns planos abertos da fonte completa conservam corte superior original; não há reconstrução artificial do rosto.
- 274 palavras: correspondência exata entre textos de dublagem/narração e palavras da timeline. Trecho da palestra 87,6 s; duração prevista 126,19 s.
- Voz conferida por Whisper local em 13 trechos de aproximadamente 10 s; finais de frases e CTA presentes. As transcrições na fronteira dos cortes podem repetir ou omitir partículas; comparar com alinhamento antes de atribuir erro ao TTS.
- Capa refeita com quadro da fonte oficial; textos dentro dos recortes 4:5 e 3:4.

### Ciclo 5: recuperação do plano aberto de 65–72,5 s
O corte superior remanescente foi corrigido com a mesma passagem da cópia 720p (Z-RbbT55Vi0), mantendo a cabeça inteira e focando o busto. A janela acima das legendas gravadas permite usar a imagem sem texto inglês concorrente. O deslocamento desta cópia é 11,44475 s para o início do trecho de referência; o plano usado começa em 76,44475 s. A aplicação acontece no acabamento FFmpeg (`finalizar.py`), preservando as legendas e o áudio da composição. Não há mudança do argumento nem reconstrução facial. Pequenos sons locais de clique e papel acompanham aprovação/revelação; nenhum crédito pago adicional.

## Entrega da revisão
- Full HD: `saida/ia-com-precisao-v2.mp4`, 1080×1920, H.264/AAC, 126,3 s.
- Cópia leve: `saida/ia-com-precisao-v2-celular.mp4`, 720×1280.
- Capa: `producao/ia-com-precisao-v2/capa/capa-9x16.jpg`; legenda: `roteiros/ia-com-precisao-v2-legenda.txt`.
- Mix medido: −14,04 LUFS integrados; −1,78 dBTP. Áudio preservado bit a bit na última correção visual (hash SHA256 idêntico).
- Transcrição do MP4 em 13 trechos concluída; dúvidas nas fronteiras resolvidas com três trechos sobrepostos (ponte, conclusão, amigos). Falas corretas, sem cortes no fechamento.
- Folhas do MP4 a 1 quadro/s, capa e primeiro quadro inspecionados. No acabamento, uma faixa residual da fonte anterior apareceu sobre o plano recuperado: corrigida e inspecionada novamente em 69 s.
- Evidências em `saida/qahtani-v2-validacao/`.

Avaliação: os dois problemas apontados pelo dono foram tratados estruturalmente, além de enquadramento, legibilidade, som e fontes. A meta continua 10/10; esta revisão não recebe um carimbo de aprovação automática. A nota de impacto cabe ao dono. Limitações reais: definição variável das fontes históricas e dublagem sem sincronização labial. Não publicada nem agendada.
