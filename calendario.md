# Calendário de publicações

Fonte única do que está publicado, agendado e planejado no Instagram. **Atualizar sempre que publicar ou agendar.**

## Grade semanal
| Dia | Série | Estilo | Horário | Papel no funil |
|---|---|---|---|---|
| Domingo | Plantão IA | [estilos/plantao-ia](estilos/plantao-ia/README.md) | 18h00 | atrair: notícias de IA da semana |
| Segunda | A Virada | F14 Manifesto cinematográfico ([formatos](formatos/README.md)) | 12h00 | emocionar: história com virada → diagnóstico |
| Quarta | Caso Real | [estilos/caso-real](estilos/caso-real/README.md) | 12h00 (a confirmar) | provar: empresa que aplicou IA e saiu em notícia de portal, com fonte |
| Sexta | IA por Setor | [estilos/ia-por-setor](estilos/ia-por-setor/README.md) | 12h00 | utilidade: algo que o executivo aplica no mesmo dia; CTA = seguir (toda sexta uma dica nova) |

## Agenda
| Data | Hora | Vídeo | Situação | Como foi/será publicado |
|---|---|---|---|---|
| dom 18/10/2026 | 18h00 | Plantão IA 01 ([roteiro](roteiros/plantao-ia-01.md)) | ✅ publicado: https://www.instagram.com/reel/DepeteHAEtd/ | contêiner preparado antes + job no horário |
| seg 19/10/2026 | 12h00 | A Virada 01 · A Chave ([roteiro](roteiros/a-virada-01.md)) | ⏳ agendado | contêiner `18029145437915035` (preparado 18/10 ~19h, vale até 19/10 ~19h) + launchd no Mac: `com.moiseskalebbe.publicar-a-virada-01` roda às 12h00 o `~/.local/share/videos-treino/publicar-a-virada-01.sh`. Mac ligado e com a tampa aberta. |
| qua 21/10/2026 | ~12h00 | Caso Real · Movida ([roteiro](roteiros/caso-movida.md)) | ⏳ agendado | launchd no Mac: `com.moiseskalebbe.publicar-caso-movida` roda às 11h45 o `~/.local/share/videos-treino/publicar-caso-movida.sh` (vídeo `saida/caso-movida.mp4` + capa `producao/caso-movida/capa/capa-9x16.jpg` + legenda `roteiros/caso-movida-legenda.txt`). Log em `~/.local/share/videos-treino/caso-movida.log`. Mac ligado e com a tampa aberta. |
| sex 23/10/2026 | ~12h00 | IA por Setor 01 · Financeiro (conciliação) ([roteiro](roteiros/sexta-01-conciliacao.md)) | ⏳ agendado | launchd no Mac: `com.moiseskalebbe.publicar-sexta-01` roda às 11h45 o `~/.local/share/videos-treino/publicar-sexta-01.sh` (vídeo + capa + legenda). Log em `~/.local/share/videos-treino/sexta-01.log`. Mac ligado e com a tampa aberta. |
| dom 25/10/2026 | 18h00 | Plantão IA 02 (a produzir) | 📝 a fazer | — |
| seg 26/10/2026 | ~12h00 | A Virada 02 · Seu Antônio ([roteiro](roteiros/a-virada-02.md)) | ⏳ agendado | launchd no Mac: `~/Library/LaunchAgents/com.moiseskalebbe.publicar-a-virada-02.plist` roda às 11h45 o `~/.local/share/videos-treino/publicar-a-virada-02.sh` (sobe com capa e legenda e publica). Log em `~/.local/share/videos-treino/a-virada-02.log`. Mac ligado e com a tampa aberta. |
| sex 30/10/2026 | ~12h00 | IA por Setor 02 · Comercial (propostas paradas no CRM) ([roteiro](roteiros/sexta-02-comercial.md)) | ⏳ agendado | launchd no Mac: `com.moiseskalebbe.publicar-sexta-02` roda às 11h45 o `~/.local/share/videos-treino/publicar-sexta-02.sh` (vídeo + capa + legenda). Log em `~/.local/share/videos-treino/sexta-02.log`. Mac ligado e com a tampa aberta. |
| seg 02/11/2026 | ~12h00 | A Virada 03 · O Planador (Gimli Glider) ([roteiro](roteiros/a-virada-03.md)) | ⏳ agendado | launchd no Mac: `com.moiseskalebbe.publicar-a-virada-03` roda às 11h45 o `~/.local/share/videos-treino/publicar-a-virada-03.sh` (vídeo + capa + legenda). Log em `~/.local/share/videos-treino/a-virada-03.log`. Mac ligado e com a tampa aberta. |
| seg 09/11/2026 | ~12h00 | A Virada 04 · Dez Anos (Kodak) ([roteiro](roteiros/a-virada-04.md)) | ⏳ agendado | launchd no Mac: `com.moiseskalebbe.publicar-a-virada-04` roda às 11h45 o `~/.local/share/videos-treino/publicar-a-virada-04.sh` (vídeo + capa + legenda). Log em `~/.local/share/videos-treino/a-virada-04.log`. Mac ligado e com a tampa aberta. |

## Como agendar
- **Até 24 h antes:** preparar o contêiner (`scripts/publicar-instagram.py <mp4> <legenda> --capa <jpg>`) e, no horário, publicar com `--conteiner <ID>` por um job com `caffeinate`.
- **Mais de 24 h antes:** o contêiner expira, então usar um LaunchAgent de uma vez só (como o da A Virada 02): ele roda `--publicar` no dia e se desliga.
- **Google Agenda do dono** (kalebbe.moises@gmail.com): todo agendamento vira um evento "📲 Reel · <série> · <tema>" no horário em que o Mac roda (lembrete 30 min antes, para ligar o Mac); vídeo ainda não produzido entra como "⚠️ Reel · ... (A PRODUZIR)", com lembrete 2 dias antes. Ao reagendar ou cancelar, atualizar o evento também. Eventos de 19/10 a 09/11 criados em 19/10/2026.
- Conferir depois: `launchctl print gui/$(id -u)/<label>` e o log; ao publicar, trocar a linha da agenda para ✅ com o link.
