# Rubrica de qualidade (nota 1–10)

Meta: **≥ 9**. A nota mede **impacto** ("isso para o scroll e convence um dono de empresa?"), não só se está tecnicamente limpo.

> Calibragem: o case Chewy v1 recebeu 7,9 na rubrica antiga e **3/10 do dono**. A versão abaixo foi refeita a partir do que ele apontou. Ver a v1 como exemplo de 3.

## 1. Travas (teto da nota)

Antes de pontuar, conferir. Cada trava que falha limita a nota final:

| Trava | Se falhar, nota máxima |
|---|---|
| **Presença humana**: avatar/apresentador falando em pelo menos parte do vídeo (enquanto o formato pedir) | 5 |
| **Imagem real do assunto**: se a fala cita algo concreto (pet, loja, produto, empresa), isso aparece na tela; empresa do case com logotipo | 6 |
| **Marca d'água** com a logo do dono em todo o vídeo | 7 |
| **Fala = tela**: todo item mostrado é falado, e vice-versa (nada de 4 tópicos na tela com 3 na fala) | 7 |
| **Dado com fonte** na tela; previsão dita como previsão | 4 |

Nota final = **menor** valor entre a soma ponderada e o teto das travas que falharam.

## 2. Pontuação ponderada

| Critério | Peso | 10 de 10 é… | Exemplo de nota baixa |
|---|---|---|---|
| **Gancho (0–3 s)** | 2,5 | Imagem inicial que para o scroll (rosto, objeto real, contraste forte) **e** frase que cria tensão em até 3 s falados | Número em fundo vazio; frase de 7 s |
| **Presença e imagem** | 2,0 | Avatar com boa sincronia labial; B-roll/imagens reais que ilustram cada afirmação; logotipos certos | Só texto e formas abstratas |
| **Ritmo e retenção** | 1,5 | Algo muda a cada 1–2 s; corte no tempo da fala; 30–60 s | Tela parada por 3 s ou mais |
| **Uma ideia, clara** | 1,0 | Dá para resumir em uma frase; cada cena serve a ela | Vários assuntos |
| **Acabamento visual** | 1,0 | Nada sobreposto sem querer, nada cortado, hierarquia clara, marca consistente | Selo em cima de outro elemento |
| **Verdade e fontes** | 1,0 | Fonte primária na tela; nenhum exagero | Número sem fonte |
| **Legenda e áudio** | 0,5 | Legenda sincronizada e sem erro; pronúncia correta de nomes; ~ -14 LUFS | "PwC" falado como "Pedwac" |
| **Público e CTA** | 0,5 | Um CEO mandaria pro sócio; fecho "manda pro <pessoa específica>" (+ "salva" se ensina), conforme `guias/fechamento-e-cta.md` | Tutorial de ferramenta |

**Soma ponderada = Σ (nota 0–10 × peso) ÷ 10.**

## 3. Como avaliar
1. `hyperframes check` sem erros.
2. Folha de contato do **MP4 renderizado** (1 quadro/s) e o **1º quadro em tamanho cheio** (é a capa no feed).
3. Transcrição do áudio final: conferir pronúncia de nomes e se cada item da tela foi falado.
4. Ser duro: na dúvida entre duas notas, dar a menor. Registrar a avaliação no roteiro do vídeo.
