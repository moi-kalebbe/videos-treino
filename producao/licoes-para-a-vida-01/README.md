# Lições para a Vida · Piloto 01

Story de teste técnico: **Os dois caminhos — o poder da escolha**.

**Ainda não é um vídeo da série diária pronto para publicar.** O personagem desenhado é genérico e não representa o Moisés. A narração também é provisória. Este teste demonstra somente o formato vertical, a composição e o movimento. Seguir `../../guias/serie-licoes-para-a-vida.md` para continuar.

- Formato: 1080 × 1920, 24 fps, cerca de 26 segundos.
- Ideia: uma mensagem desagradável abre dois caminhos, impulso ou pausa.
- Inspiração: *Os 7 Hábitos das Pessoas Altamente Eficazes*, Stephen R. Covey. O texto do vídeo é uma adaptação original, não uma citação literal.
- Narração atual: voz provisória pt-BR. Substituir pela voz clonada aprovada antes da publicação.
- Avatar real: ainda não há imagem confirmada pelo dono neste checkout. Não reutilizar as antigas opções de `producao/apresentador/`; eram um rosto incorreto e foram excluídas.

Para renderizar, com Pillow e FFmpeg instalados:

```powershell
python render_story.py --audio assets/audio/narracao-provisoria.mp3 --output piloto.mp4
```

O arquivo MP4 e os áudios de narração são ignorados pelo Git.
