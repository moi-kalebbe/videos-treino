# Instagram, TikTok e YouTube Shorts (desde 21/10/2026)

Decisão do dono: **o mesmo vídeo vai para as 3 redes** e comparamos qual rende mais. Um formato que funcione bem nas 3 sai melhor do que três versões diferentes.

## O que muda no vídeo
- **Área segura.**
  - Cada rede cobre uma parte da tela com seus botões: a lateral direita no TikTok e no Instagram, e a faixa de baixo com o nome e a legenda nas três.
  - No quadro de 1080×1920, **texto e rosto ficam entre y 220 e y 1480, e entre x 90 e x 900.**
  - A legenda queimada fica perto de y 1250–1450, nunca encostada embaixo.
- **Nada de marca de outra rede no vídeo.** Sem logo do Instagram, sem "@" de outra plataforma e sem marca d'água: as redes entregam menos quando veem marca da concorrente. Renderizamos nós mesmos, então o arquivo já sai limpo.
- **Música.**
  - Música comercial pode ser silenciada no TikTok e no YouTube (Content ID).
  - Usar trilha livre (biblioteca própria, Pixabay ou gerada).
  - Se o vídeo depende de uma música da moda, colocar a música pelo app de cada rede, e não no arquivo.
- **Duração:** de 25 a 40 s serve para as 3 (o Shorts aceita até 3 min, mas a regra de `guias/fechamento-e-cta.md` vale igual).
- **Fecho:** "manda pro…" serve nas 3. "Salva" funciona no Instagram e no TikTok; no YouTube, o equivalente é "deixa o like pra achar depois".

## O que muda na publicação
| Rede | Legenda | Hashtags | Como publicar hoje |
|---|---|---|---|
| Instagram | a de sempre | 3–5 | `scripts/publicar-instagram.py` (automático) |
| TikTok | mais curta, a primeira linha é a frase do gancho | 3–5 | manual pelo app até termos acesso à API de postagem do TikTok (precisa de app aprovado) ou a um agendador (Publora) |
| YouTube Shorts | título com até 100 caracteres (é o que aparece na busca) + descrição | `#shorts` + 2–3 | manual pelo YouTube Studio; dá para automatizar pela YouTube Data API (OAuth do canal) |

## Como comparar
- Postar o mesmo vídeo nas 3 redes no mesmo dia, com até 1 h de diferença.
- Depois de 7 dias, anotar em `calendario.md`: views, tempo médio assistido, compartilhamentos e seguidores ganhos em cada rede.
- Depois de ~2 semanas, decidir onde investir mais e se algum formato pede corte diferente por rede.
