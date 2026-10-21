# Estilo "Cena Impossível"

> **Desde 21/10/2026, o CTA `DIAGNÓSTICO` deste guia não vale mais para vídeos novos.** O fechamento segue `guias/fechamento-e-cta.md` (manda pro <pessoa específica> + salva quando ensina, 25–40 s).

Vídeo curto que para o dedo no **primeiro quadro** com uma cena impossível, mas que todo empresário entende, e leva para a aplicação de IA dentro da empresa. Base: o método do [@abrahubstudio](../../referencias/abrahub.md) (§6–7), adaptado para quem vende **IA aplicada**, não curso de vídeo. Criado com o dono em 19/10/2026; ainda sem vídeo aprovado (o primeiro é o teste).

**Para quem:** dono, CEO, diretor rolando o feed. **Objetivo:** alcance + compartilhamento ("manda pro sócio"), levando ao CTA `DIAGNÓSTICO`.

## 1. A diferença em relação ao Abrahub (ler antes de todo roteiro)
Ele vende **a habilidade de fazer o vídeo**: qualquer tema em alta serve, porque o próprio vídeo é a vitrine do curso. Nós vendemos **IA dentro da empresa**: o vídeo não é a vitrine, é a **ponte**. Por isso, toda cena impossível precisa:
1. ser **uma dor da empresa levada ao pé da letra** (não um absurdo qualquer);
2. levar a uma **virada concreta**: o que a IA faz com aquela dor (uma cena real, não promessa).
Se o assunto em alta não vira uma dor de empresa em uma frase, não serve.

## 2. O método em 3 engrenagens (versão nossa)
1. **Estranheza com significado** (para o dedo em < 2 s): contraste (calma × caos, luxo × decadência), contradição (dois significados opostos na mesma cena) e simbolismo (a cena aponta para uma emoção que o gestor já sente: sufoco, desperdício, medo de ficar para trás).
2. **Estética travada**: um bloco de estilo (§5) igual em todas as cenas do vídeo. Muda de vídeo para vídeo, nunca dentro do mesmo vídeo.
3. **Carona**: um assunto em alta (§3) ou uma **expressão que todo empresário fala**, levada ao pé da letra (§4).

## 3. Como pegar carona em assunto em alta sem sair do nicho
Regra: o assunto em alta é a **roupa**; a dor da empresa é o **corpo**; a IA é a **saída**.
`assunto em alta → a emoção/situação dele → a mesma situação dentro da empresa → cena impossível → virada com IA`

| Assunto em alta (exemplo) | Situação que ele carrega | Dentro da empresa | Cena impossível | Virada com IA |
|---|---|---|---|---|
| Futebol / VAR | lance revisto, erro que ninguém viu | erro de lançamento que só aparece no fechamento | um juiz com VAR no meio do financeiro revendo cada nota fiscal | IA conferindo 100% dos lançamentos, não por amostra |
| Reality show / paredão | alguém é eliminado | processo manual "no paredão" | a planilha sentada no paredão, a equipe votando | qual processo eliminar primeiro com IA |
| Black Friday | fila infinita | WhatsApp com 3 mil mensagens | atendente soterrado por balões de mensagem que caem do teto | agente respondendo de madrugada |
| Imposto de Renda / fim de ano | pilhas de papel, prazo | fechamento contábil | contador num escritório que vira montanha de papel | conciliação automática (ver sexta 01) |
| Apagão / sistema fora do ar | tudo para | empresa que depende de uma pessoa só | a empresa inteira congelada quando a "Dona Maria" sai de férias | processo documentado e agente que sabe o que ela sabe |
| Notícia de IA da semana (Plantão) | "a IA fez X" | o que isso muda na sua operação | a notícia acontecendo dentro de um escritório comum | uma aplicação concreta para empresa |
| Eleição / política | promessa × entrega | fornecedor de IA prometendo milagre | **sem políticos reais**: um palanque de campanha dentro da sala de reunião prometendo "IA resolve tudo" | diagnóstico antes da promessa |

**Nunca:** pessoa pública real (político, influenciador, atleta) gerada por IA, nem lado político. Usamos a **situação**, não a pessoa.

## 4. Banco de expressões de empresa para levar ao pé da letra
É a técnica que ele mais usa ("mamar nas tetas" = vaca com "IMPOSTO" sendo ordenhada). As nossas:
- **apagar incêndio** → gestor tranquilo tomando café com o escritório em chamas (testado ✔)
- **afogado em planilha** → CEO afundando num mar de planilhas na sala de reunião
- **empresa dinossauro** → um T-rex de terno numa reunião de diretoria decidindo "no papel"
- **elefante branco** → um elefante branco gigante no meio do escritório: o sistema caro que ninguém usa
- **sangrando dinheiro** → cédulas escorrendo de uma torneira aberta na copa e ninguém fecha
- **bola de neve** → a pilha de pedidos atrasados rolando pelo corredor e crescendo
- **trabalho de formiguinha** → a equipe virando formigas carregando papel enquanto um robô passa ao lado
- **cobertor curto** → diretor puxando um cobertor minúsculo entre comercial e financeiro
- **tiro no pé** → (cuidado com arma: preferir "dar com a cara na porta")
- **tudo na cabeça do dono** → o dono com o escritório inteiro equilibrado na cabeça

## 5. Estética travada (modelo)
Escrever o bloco uma vez por vídeo e repetir em **todo** prompt (em inglês):
```json
{"style": "photorealistic cinematic film still, shot on ARRI Alexa, 35mm lens, natural window light mixed with warm practical lights, Brazilian corporate office, <paleta do vídeo> color grade, subtle film grain, shallow depth of field, no text, no logos",
 "framing": "vertical 9:16, <enquadramento>",
 "mood": "<o contraste da cena em 5 palavras>"}
```
Para cada vídeo, trocar **paleta, tipografia da tela e entrada do texto** em relação aos últimos (ver [video-sem-molde-fixo] na memória e o [catálogo de efeitos](../../guias/efeitos-video.md)).

## 6. Como gerar as cenas (grátis primeiro)
Ordem testada em 19/10/2026:
1. **Quadro real + impossível injetado (melhor resultado):** pegar um quadro de um vídeo real do Pexels (pessoa, escritório) e animar com o **LTX-Video no Mac em modo imagem → vídeo**, pedindo o elemento impossível ("o quadro branco pega fogo e ele continua desenhando"). Fica com cara de filmagem real. ~1,5 min por cena de 4 s, sem crédito. Exemplo: `saida/testes/ltx-teste-i2v.mp4`.
2. **Texto → vídeo no LTX:** serve para cenas abertas (avalanche de papel, fogo ao fundo), mas o rosto e as mãos ficam "plásticos". Exemplo: `saida/testes/ltx-teste-incendio.mp4`.
3. **Imagem de alta qualidade (FLUX no Hugging Face) → LTX imagem → vídeo (melhor para cena que não existe em banco):** testado em 19/10/2026 com `HF_TOKEN` no `.env`: a imagem sai em ~30 s com cara de cinema e o Mac anima em ~1,5 min (`saida/testes/flux-ceo-incendio.png` → `saida/testes/flux-ltx-ceo-incendio.mp4`). É o caminho padrão do quadro 0.
4. Pago (ElevenLabs, ~800 créditos a imagem): só no quadro 0, se nenhum dos acima resolver.

```bash
cd ~/.cache/ltx-teste && source .venv/bin/activate
python gerar.py texto "<prompt em inglês, descrevendo a ação em ordem, + bloco de estilo>"
IMAGEM=quadro.png LARG=576 ALT=1024 python gerar.py video cena.mp4   # sem IMAGEM = texto → vídeo
```
Cópia do script em `estilos/cena-impossivel/gerar-ltx.py`. Prompt do LTX: frases em ordem do que acontece ("A senior executive... Suddenly... he keeps..."), câmera no fim.

## 7. Estrutura (30–45 s)
| Tempo | Bloco | O que é |
|---|---|---|
| 0–2 s | **Quadro impossível** | a cena mais forte, já em movimento, sem logo, sem texto grande; no máximo 3 palavras na tela |
| 2–20 s | **Bits compilados** | 6–10 cenas de 1–2 s, a mesma estética, escalando o absurdo; cada uma é uma dor da empresa ao pé da letra |
| 20–28 s | **A virada** | corte seco para o real: "Parece exagero. Na sua empresa, é segunda-feira." |
| 28–40 s | **A saída com IA** | uma cena concreta e real do que a IA faz com aquela dor (tela, número, antes × depois), com fonte ou marcada como exemplo |
| final | **CTA** | comenta `DIAGNÓSTICO` |

**Som:** trilha forte de banco grátis (Pixabay) puxando o ritmo dos cortes + efeitos nos impactos. **Fala:** pouca ou nenhuma até a virada; o texto na tela conta. Se tiver voz, na voz do dono, em blocos fluidos ([voz-fluida] na memória).
**Tela:** formato de cinema (tarjas pretas) só quando combinar; legenda pequena e **uma** palavra gigante no clímax. Selo discreto "cenas criadas com IA" na legenda do post.

## 8. O que eu preciso do dono (briefing)
| Item | Obrigatório? |
|---|---|
| Tema/dor (ou "escolhe você" com base no assunto da semana) | não |
| Aprovar o roteiro (as cenas e a virada) | sim |
| Token do Hugging Face (grátis) para imagens de alta qualidade | recomendado |

**Custo:** cenas no Mac = 0 crédito. Voz (se tiver) ~300–600 créditos. Imagem paga só se precisar (~800 cada).

## 9. Checklist
- [ ] O quadro 0 para o dedo sem precisar de som
- [ ] Toda cena é uma dor de empresa ao pé da letra (não absurdo solto)
- [ ] Nenhuma pessoa pública real, nenhum lado político
- [ ] Estética igual em todas as cenas; diferente dos últimos vídeos
- [ ] A virada tem uma aplicação concreta de IA
- [ ] Vídeos sem HDR antes do render ([bancos de mídia](../../guias/bancos-de-midia.md)); capa responsiva
