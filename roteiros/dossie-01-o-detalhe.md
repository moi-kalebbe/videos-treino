# Dossiê · 01 · O Detalhe (Marília Mendonça, Chapecoense, Mamonas)

| Campo | Valor |
|---|---|
| Formato | **Dossiê** (novo): documentário de investigação no estilo *Mayday! Desastres Aéreos* (Nat Geo) / Investigação Discovery, curto |
| Ideia | Fernanda Jurgensen (19/10/2026), reescrita com os relatórios oficiais |
| Carona | série "Marília Mendonça: Sentimento Louco" (Prime Video, 16/10/2026), que **não investiga o acidente** |
| Duração | ~85 s |
| Público | dono/gestor: "quanto da sua operação depende de alguém lembrar?" |
| CTA | comenta `DIAGNÓSTICO` |
| Status | roteiro aprovado · produzido (~121 s) · agendado no Mac para sex 23/10/2026 11h45 → no ar ~12h00, com capa e legenda |

## Como ficou (produção)
- Narrador Dimmy (biblioteca ElevenLabs, `chFi7TdzwurwZVzGKeLH`) nos casos; a voz do dono só a partir de "Agora pensa na sua empresa". Narração gerada **em blocos** (`scripts/narracao_blocos.py`), +5% de velocidade.
- Páginas reais dos relatórios com marca-texto (`producao/dossie-01/assets/img/`), mapa esquemático da aproximação, régua de distância, barras de combustível e de jornada, carimbos, cadeia "acidente → relatório → regra → checklist", painel de conferência da IA com dados fictícios.
- Imagens: banco Pexels (avião entre os fios, torres de energia, cabines, olho no escuro, checklist), marcadas "IMAGENS ILUSTRATIVAS". As reconstituições no FLUX/LTX não foram usadas (Hugging Face fora do ar na hora).
- Trilha (Pixabay): Dark Drone → silêncio → Investigation → Sad Documentary piano → Investigation.

## Linguagem (o que muda em relação aos outros vídeos)
- **Paleta fria de investigação:** aço, azul-petróleo e branco; vermelho só no carimbo "FATOR CONTRIBUINTE". Nada do dourado e preto da A Virada nem do lima da sexta.
- **Tipografia:** legendas de tempo e lugar em caixa alta, sem serifa, **digitadas na tela** ("05 NOV 2021 · 15H15 · PIEDADE DE CARATINGA, MG"); fichas de caso "CASO 1/3"; texto da fala em branco discreto embaixo, sem karaokê.
- **Documento como prova:** recortes reais dos relatórios oficiais (CENIPA, Aerocivil), com o trecho grifado em amarelo-marca-texto e o carimbo vermelho caindo.
- **Gráficos de investigação:** mapa escuro com a rota e o ponto do acidente; régua "faltavam 4,6 km"; barra de combustível "rota 4h22 = autonomia 4h22"; relógio de jornada "16h30 · limite: 11h".
- **Reconstituição sem rosto e sem destroços:** cabine à noite, aproximação com neblina, ponteiro de combustível, linha de transmissão no fim da tarde (FLUX + LTX no Mac, sem marca de companhia); **nenhuma imagem das vítimas, do acidente, de velório ou de família**.
- **Som:** zumbido grave contínuo, chiado de rádio, bipe de radar, coração; **silêncio seco** no lugar de qualquer impacto (nunca som de batida).
- **Voz:** narrador de documentário, grave e pausado, até a virada; **a sua voz** entra só em "Agora pensa na sua empresa" (troca de voz = troca de capítulo).

## Narração
**Abertura fria (narrador)**
1. Cinco de novembro de 2021. Faltavam quatro quilômetros para a pista.
2. O avião que levava Marília Mendonça estava em ordem. A investigação descartou falha mecânica.
3. Na aproximação, a curva foi mais longa do que o previsto, e o relatório apontou essa avaliação como fator que contribuiu.
4. No caminho, havia um cabo de energia sem sinalização. Pela regra, ele nem precisava estar sinalizado.
5. Um detalhe. Cinco vidas.
[tela: DOSSIÊ · O DETALHE]
6. E ela não foi a única.

**Caso 2 (narrador)**
7. Novembro de 2016. O voo da Chapecoense foi planejado com combustível para exatamente o tempo da viagem. Quatro horas e vinte e dois minutos. Nenhum minuto de reserva.
8. Quem recebeu o plano de voo avisou que a conta não fechava. O voo saiu assim mesmo.
9. Setenta e uma vidas.

**Caso 3 (narrador)**
10. Março de 1996. Os pilotos que levavam os Mamonas Assassinas estavam trabalhando havia dezesseis horas e meia. Cinco e meia além do limite da lei.
11. O relatório fala em fadiga, em coordenação falha e em falta de supervisão da empresa.
12. Nove vidas.

**O padrão (narrador)**
13. Segundo a FAA, de setenta a oitenta por cento dos acidentes aéreos envolvem erro humano.
14. Quase nunca é o avião. É um detalhe que ninguém conferiu. Um alerta que ninguém ouviu. Um cansaço que ninguém viu.
15. A aviação aprendeu com cada um deles. Todo acidente vira relatório, todo relatório vira regra, e toda regra vira checklist. Por isso hoje ela é o jeito mais seguro de viajar.

**A virada (sua voz)**
16. Agora pensa na sua empresa. Quem confere o preço antes do pedido sair? Quem percebe que o cliente está sem resposta há três dias? Quem vê que a equipe está no limite?
17. Se a resposta é "alguém lembra", a sua empresa está voando sem checklist.
18. A IA pode ser essa camada de conferência: cruza os dados, aponta o valor que não bate e avisa do pedido parado, antes de virar prejuízo. Com processo definido e gente revisando.
19. Comenta diagnóstico que eu te mostro por onde começar.

[cartela final pequena: "Em memória de todas as vítimas."]

## Planos (rascunho)
| Fala | Visual |
|---|---|
| 1 | preto → legenda digitada "05 NOV 2021 · 15H15 · PIEDADE DE CARATINGA, MG" + régua "FALTAM 4,6 KM" sobre aproximação noturna com neblina (gerada) |
| 2 | recorte do relatório CENIPA "não houve falha mecânica" grifado |
| 3 | mapa escuro: perna do vento prevista (1 NM) × real (+1,5 NM) desenhando; carimbo FATOR CONTRIBUINTE: julgamento de pilotagem |
| 4 | linha de transmissão ao entardecer (gerada/banco) + recorte "não se enquadrava... passível de ser sinalizado" |
| 5 | silêncio seco · tela preta "UM DETALHE." → "5 VIDAS" |
| 6–9 | ficha CASO 2/3 · 28 NOV 2016 · MEDELLÍN; barra "ROTA 4H22 = AUTONOMIA 4H22", ponteiro de combustível descendo; recorte do relatório da Aerocivil; "71 VIDAS" |
| 10–12 | ficha CASO 3/3 · 02 MAR 1996 · SERRA DA CANTAREIRA, SP; relógio de jornada 16H30 × limite; recorte "comportamento típico de fadiga física"; "9 VIDAS" |
| 13 | "70–80%" grande · fonte FAA (2000) |
| 14 | três quadros: checklist em branco, rádio chiando, olhos cansados |
| 15 | piloto passando o dedo num checklist real (banco) · cartela "RELATÓRIO → REGRA → CHECKLIST" |
| 16–17 | corte para escritório: WhatsApp, planilha, pedido parado (banco) |
| 18 | tela simulada de IA conferindo pedidos e cobranças (dados fictícios, marcado como exemplo) |
| 19 | CTA + "Em memória de todas as vítimas." |

## Capa
Evoca a série sem copiar: fundo escuro com **luzes de palco douradas desfocadas** (letreiro de lâmpadas), título lateral em dourado + tarja fria de dossiê. Texto: "**MARÍLIA MENDONÇA**" pequeno em cima, "**O detalhe que a investigação encontrou**" grande, e "+ 2 casos" no canto. Sem foto dela, sem coroa, sem logo do Prime Video.

## Fontes
- Marília: relatório final A-121/CENIPA/2021 (15/05/2023), [PDF via Poder360](https://static.poder360.com.br/2023/05/relatorio-cenipa-marilia-mendonca.pdf): 18:15 UTC (15h15 de Brasília), 2 pilotos + 3 passageiros, cabo para-raios de linha de 69 kV a 2,5 NM (≈4,6 km) da cabeceira, linha fora da Zona de Proteção e sem exigência de sinalização, perna do vento alongada mais de 1,5 NM além do previsto, "julgamento de pilotagem — contribuiu" (os demais fatores "indeterminado"), sem falha mecânica. O CENIPA não atribui culpa.
- Chapecoense: relatório final da Aerocivil (27/04/2018), [PDF arquivado](https://web.archive.org/web/20220906113104/http://www.aerocivil.gov.co/autoridad-de-la-aviacion-civil/investigacion/listado%20de%20accidentes%202016/Final%20Report%20-%20ACCIDENT%20CP2933%20-%20English%20Version.pdf): tempo de rota = autonomia = 4h22, o escritório ARO/AIS apontou a inconsistência e foi ignorado, 77 a bordo, 71 mortos.
- Mamonas: relatório final do CENIPA PT-LSD (28/05/1996), [PDF arquivado](https://web.archive.org/web/2024id_/https://sistema.cenipa.fab.mil.br/cenipa/paginas/relatorios/rf/pt/PT-LSD_02-03-1996.pdf): jornada de 16h30, mais de 5h30 acima do limite da Lei 7.183/84, "comportamento típico de fadiga física", coordenação de cabine e supervisão deficientes, 9 mortos.
- "70 a 80%": FAA, DOT/FAA/AM-00/7 (Shappell e Wiegmann, 2000), [ERAU](https://commons.erau.edu/publication/737/).
- Série: "Marília Mendonça: Sentimento Louco", Prime Video, 16/10/2026, dir. Susanna Lira ([CNN Brasil](https://www.cnnbrasil.com.br/pop/streaming/serie-documental-sobre-marilia-mendonca-estreia-nesta-sexta-onde-assistir/)); não reconstitui nem investiga o acidente ([O Tempo](https://www.otempo.com.br/opiniao/diego-almeida/2026/10/17/sentimento-louco-mostra-a-queda-do-aviao-confira-o-que-a-serie-de-marilia-mendonca-conta)).
