# Calendário de publicações

Fonte única do que está publicado, agendado e planejado no Instagram. **Atualizar sempre que publicar ou agendar.**

## Grade semanal
| Dia | Série | Estilo | Horário | Papel no funil |
|---|---|---|---|---|
| Domingo | Plantão IA | [estilos/plantao-ia](estilos/plantao-ia/README.md) | 18h00 | atrair: notícias de IA da semana |
| Segunda | A Virada | F14 Manifesto cinematográfico ([formatos](formatos/README.md)) | 12h00 | emocionar: história com virada → diagnóstico |
| Quarta | Caso Real | [estilos/caso-real](estilos/caso-real/README.md) | 12h00 (a confirmar) | provar: empresa que aplicou IA e saiu em notícia de portal, com fonte |
| Sexta | Aplica na sua empresa | a criar | a definir | utilidade: um processo pronto para aplicar (proposta, começar depois que a quarta estiver redonda) |

## Agenda
| Data | Hora | Vídeo | Situação | Como foi/será publicado |
|---|---|---|---|---|
| dom 18/10/2026 | 18h00 | Plantão IA 01 ([roteiro](roteiros/plantao-ia-01.md)) | ✅ publicado: https://www.instagram.com/reel/DepeteHAEtd/ | contêiner preparado antes + job no horário |
| seg 19/10/2026 | 12h00 | A Virada 01 · A Chave ([roteiro](roteiros/a-virada-01.md)) | ⏳ agendado | contêiner `18029145437915035` (preparado 18/10 ~19h, vale 24 h) + job em segundo plano na sessão do Claude Code. **Depende do app aberto e do Mac acordado.** |
| qua 21/10/2026 | 12h00 | Caso Real (a produzir) | 📝 a fazer | — |
| dom 25/10/2026 | 18h00 | Plantão IA 02 (a produzir) | 📝 a fazer | — |
| seg 26/10/2026 | ~12h00 | A Virada 02 · Seu Antônio ([roteiro](roteiros/a-virada-02.md)) | ⏳ agendado | launchd no Mac: `~/Library/LaunchAgents/com.moiseskalebbe.publicar-a-virada-02.plist` roda às 11h45 o `~/.local/share/videos-treino/publicar-a-virada-02.sh` (sobe com capa e legenda e publica). Log em `~/.local/share/videos-treino/a-virada-02.log`. Mac ligado e com a tampa aberta. |

## Como agendar
- **Até 24 h antes:** preparar o contêiner (`scripts/publicar-instagram.py <mp4> <legenda> --capa <jpg>`) e, no horário, publicar com `--conteiner <ID>` por um job com `caffeinate`.
- **Mais de 24 h antes:** o contêiner expira, então usar um LaunchAgent de uma vez só (como o da A Virada 02): ele roda `--publicar` no dia e se desliga.
- Conferir depois: `launchctl print gui/$(id -u)/<label>` e o log; ao publicar, trocar a linha da agenda para ✅ com o link.
