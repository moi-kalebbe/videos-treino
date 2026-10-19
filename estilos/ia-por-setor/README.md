# Estilo "IA por Setor" (sexta, 12h)

Toda sexta, **uma dica que o executivo aplica no mesmo dia** num setor da empresa (financeiro, comercial, RH, contabilidade, diretoria, jurídico, compras, marketing). Aprovado pelo dono em 19/10/2026 (episódio 01: `producao/sexta-01-conciliacao/`, agendado para 23/10).

**Para quem:** CFO, CEO, controller, diretor. Use a língua do cargo (fechamento, razão, DRE, DSO, aging, turnover, SLA, CAC, LGPD) e mostre ganho em tempo, dinheiro ou risco.
**CTA:** seguir. "Segue o perfil. Toda sexta, uma dica nova pra aplicar na sua empresa." Sem lead magnet e sem palavra no comentário: o dono decidiu assim.
**Teste da pauta:** dá para o diretor fazer **hoje**, com o que já tem (Claude, Claude no Excel, Claude Cowork + plugin)? Se precisa de desenvolvedor, não é para a sexta.

## 1. O que preciso do dono (briefing)
| Item | Obrigatório? |
|---|---|
| Setor e tarefa (ou "escolhe você", seguindo o rodízio) | não |
| Aprovar roteiro + vídeo + capa + legenda | sim |

## 2. Custo
Só a narração na voz clonada: ~900 créditos. Fundos (Pexels), trilha (Pixabay) e a demonstração (rodada aqui, com dados fictícios) são grátis.

## 3. Estrutura (~60 s, 10 falas)
| # | Bloco | Exemplo (ep. 01) |
|---|---|---|
| 1 | **Hook: o resultado pronto no quadro 0** + o número | "142 lançamentos. 4 não bateram. E o Claude achou os 4 em minutos." |
| 2 | **O que é, na língua do cargo**, e o que custa não fazer | "Conciliar é bater extrato com razão. O que não bate trava o fechamento." |
| 3–5 | **Passo 1, 2, 3** (tag "PASSO N" grande) | exporta numa pasta → abre o Claude Cowork e cola **este pedido** → ele cruza linha a linha |
| 6–7 | **O resultado detalhado** (falou, mostrou: cada item citado aparece) | as 4 divergências + a capa da conciliação com selo |
| 8 | **O pulo do gato (nível avançado)** | "transforma esse pedido num plugin: sai igual todo mês" |
| 9 | **O cuidado** (tela escura, frase em serifa lima) | "A IA concilia. Quem assina é você." |
| 10 | **CTA seguir** + "Próxima sexta: <setor>" | botão Seguir → Seguindo ✓ |

## 4. Regras
- **A demonstração é real.** Montar e rodar o processo aqui com dados fictícios (pasta `producao/<slug>/dados/`), e mostrar o resultado de verdade, marcado como exemplo.
- **O pedido mostrado na tela é o mesmo que vai na legenda**, inteiro, para copiar e colar. É o que faz salvar o post.
- **Fundo sempre com vídeo de escritório rodando** (Pexels claro, sem texto legível em inglês ou fora de contexto). Os cards de papel ficam por cima.
- **Identidade "manual de bolso":** papel `#f6f4ef`, tinta `#0e1424`, lima `#d7ff3a`, verde `#0f7a37`, vermelho `#e5484d`. Inter 800 + Instrument Serif itálico + JetBrains Mono para números e arquivos. Legenda em pílula clara, palavra falada em lima. Selo fixo "IA POR SETOR · NN SETOR" no canto.
- **Honestidade:** nunca prometer tempo exato que não medimos ("em minutos", não "em 10 minutos"). Avisar na legenda sobre a política de dados antes de subir arquivo real.
- **Rodízio:** Financeiro (01) → Comercial → RH → Contabilidade → Diretoria → Jurídico → Compras → Marketing.

## 5. Passo a passo
```bash
scripts/novo-video.sh ia-por-setor sexta-NN-<tarefa>
# 1. montar dados fictícios e rodar o processo (dados/ + resultado)
# 2. falas.txt (10 linhas) e roteiros/sexta-NN-<tarefa>.md + -legenda.txt (com o pedido inteiro)
python3 scripts/narracao.py producao/<slug>/falas.txt producao/<slug>/assets --voz aORS9tvW5qcMM0bnzsRU
# 3. fundos Pexels → assets/clipes/bg-*.mp4 (1080x1920, um por cena); trilha Pixabay → assets/audio/trilha.mp3
# 4. adaptar index.html (cenas, textos, em("palavra", n)) e capa/index.html
python3 scripts/sincronizar-audio.py producao/<slug> --fim-extra 2.5
cd producao/<slug> && npx --yes hyperframes@0.8.171 check && npx --yes hyperframes@0.8.171 snapshot --at ... && npx --yes hyperframes@0.8.171 render -q high -o ../../saida/<slug>-bruto.mp4
# 5. loudnorm -14 LUFS, whisper local por trechos, cópia -crf 26 para o celular
```

## 6. Capa
Fundo com o quadro do vídeo e card de papel: selo da série, título com a palavra-chave em serifa lima ("Conciliação bancária em *minutos* com o Claude"), uma linha de resultado, dois chips (bateu / não bateu) e os 3 passos em tags lima. Conferir os recortes 4:5 e 3:4 (`previa-recortes.jpg`).

## 7. Checklist
- [ ] Dá para aplicar hoje, sem desenvolvedor
- [ ] Resultado real no quadro 0
- [ ] Pedido na tela = pedido na legenda
- [ ] Cada item falado aparece
- [ ] Nenhum fundo parado; nenhum texto estranho no B-roll
- [ ] whisper local ok, -14 LUFS, capa conferida
- [ ] "Próxima sexta: <setor>" no CTA e na legenda
