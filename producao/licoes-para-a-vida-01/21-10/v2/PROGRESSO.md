# Lição 21/10 · v4 (5 exemplos + desfecho) · em andamento

Nota do dono na v3: 6/10. Pediu 5 exemplos reais do dia a dia e desfecho mais elaborado; depois que aprovar, agendar para 21/10 às 6h (Story, ≤ 60 s).

Feito:
- Vozes novas (n3 câmera enxuta, f2, m2, n4 com 5 exemplos, n5 desfecho) em assets/audio; versões v3 guardadas com sufixo -v3.
- config.json v4 escrito (timeline até 59,86 s; config-v3.json é a versão anterior).
- 2 imagens novas pedidas no fluxo ElevenLabs KEQrMvsCYOr3yiX9uORg: n0KC3eFS2LQMfCBpt8AC → assets/img/g-relatorio.png, ZMfm33zcSefc4ReRFSSX → assets/img/h-quarto.png (baixar pelo link content.png e redimensionar para 1080x1935).

Falta:
1. Baixar as 2 imagens.
2. `python3 scripts/licoes_story.py producao/licoes-para-a-vida-01/21-10/v2/config.json producao/licoes-para-a-vida-01/21-10/v2`, check, snapshots.
3. Render + `scripts/mixar_audio.py`, versão celular, conferir duração ≤ 60 s, mandar ao dono.
4. Após OK: agendar Story para 21/10 06:00 (LaunchAgent + `scripts/publicar-instagram.py <mp4> --story --publicar`), calendário e Google Agenda.
5. Dono tem mais uma ideia de vídeo: avisar quando terminar.
