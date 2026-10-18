# Ferramentas citadas no lote 01 — investigação (18/10/2026)

Máquina-alvo: **MacBook Apple M5, 16 GB RAM**, Node 22.23, Python 3.15 (usar `uv` com Python 3.11/3.12 — várias libs ainda não suportam 3.15), Chrome instalado, ffmpeg instalado.

| Ferramenta | Repo | ★ | Licença | O que é | Requisitos | Roda no Mac? | Custo |
|---|---|---|---|---|---|---|---|
| **HyperFrames** | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 66,5 mil | Apache-2.0 | HTML/CSS + animações → MP4 determinístico. 21 skills (router `/hyperframes`, `/talking-head-recut`, `/general-video`, registry de blocos/transições) | Node 22+, ffmpeg, Chrome headless | ✅ sim | grátis |
| **OpenFilm** | [openfilm/openfilm](https://github.com/openfilm/openfilm) | 938 | MIT | `film.html` com trilhas; cada cena é uma página com `frame(t)`. **Studio** (editor no navegador: textos, cortes, legendas, export p/ Premiere/Resolve/FCP). Comando `openfilm look` gera folha de contato | Node 22.2+, ffmpeg, Chrome; tem app desktop pra macOS | ✅ sim | grátis; voz/música/imagem via chaves próprias (ElevenLabs, OpenAI, fal…) |
| **OpenMontage** | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 69,4 mil | **AGPL-3.0** | Sistema completo de produção com agentes: 12 pipelines, 100+ ferramentas, pesquisa → roteiro → narração → imagens/stock → legendas por palavra → render (Remotion/HyperFrames). Painel "Backlot" e aprovação de storyboard | Python 3.10+, Node 18+, ffmpeg; Piper TTS local | ✅ sim | grátis com stock (Pexels/Pixabay) + Piper; geração por IA paga (ex.: curta de 60 s ≈ US$1,33) |
| **Lemo-Opuscar** | [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 3 mil | MIT (código) · CC BY 4.0 (demos) | Skill de curtas **sem modelo de vídeo**: 51 estilos de filme, cada um com prompt de estilo + filme-demo feito 100% em código | Node 20+, ffmpeg, Python 3.11+ (ou uv) | ✅ sim | grátis |
| **Claude Animation Base** | [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | 1,3 mil | MIT | Kit p5.js + p5.brush p/ animação estilo pintura à mão com o mascote Clawd (31 emoções). `ANIMATION_GUIDE.md` = regras; renderiza folhas de contato pra se auto-revisar | Node, Chrome, ffmpeg | ✅ sim (aquarela é lenta sem GPU dedicada — segundos por frame) | grátis |
| **Collage B-roll** | [pyang5166/gbro-collage-broll](https://github.com/pyang5166/gbro-collage-broll) | 1,4 mil | MIT | B-roll de 5 s em colagem de papel com retícula, montado peça por peça. Fluxo de 3 portões de aprovação (metáfora → still → vídeo) | `GEMINI_API_KEY` (Gemini Omni Flash), Python 3.10+, `google-genai`, ffmpeg. **Still depende do `image_gen` do Codex** | ⚠️ sim, mas o Gate 2 é feito pro Codex | pago por uso (Gemini) |
| **onetake** | [feitangyuan/onetake](https://github.com/feitangyuan/onetake) | 2,6 mil | **PolyForm Noncommercial** | Skill de motion "plano contínuo": cada beat nasce do anterior, sem corte | python3 + playwright/chromium, numpy, scipy, Pillow, matplotlib, ffmpeg, node; narração com faster-whisper + Kokoro TTS | ✅ sim | grátis **só p/ uso não comercial** — comercial exige onetake Pro |
| **LongCat-Video-Avatar** | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) · [MeiGen-AI/LongCat-Video-Avatar](https://github.com/MeiGen-AI/LongCat-Video-Avatar) · pesos no [HF](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar) | 9,2 mil | MIT (código) | Foto + áudio → vídeo falando com lip-sync (avatar/clone) | GPU **NVIDIA/CUDA** grande; nó ComfyUI: [rookiestar28/ComfyUI-LongCat-Avatar](https://github.com/rookiestar28/ComfyUI-LongCat-Avatar) | ❌ não (CPU/MPS sem suporte; só um branch `macOS-MLX` experimental). Alternativa: rodar em GPU na nuvem ou no HF Space | grátis, mas exige GPU |

## Conclusões

**Base recomendada (tudo roda no Mac, licença comercial ok):**
1. **HyperFrames** — motor principal de motion graphics em HTML. Maior ecossistema, já tem `/talking-head-recut` (overlays em vídeo de rosto), que é o formato da maioria das referências (01, 03, 06, 07).
2. **OpenFilm** — o editor visual (Studio) é o diferencial: o agente monta e você ajusta à mão. Bom para o fluxo "Claude edita → eu reviso".
3. **Lemo-Opuscar** + **Claude Animation Base** — bibliotecas de estilo (51 estilos de filme + animação pintada). Servem de referência de prompts/estilo mesmo se não forem o motor.

**Usar com cuidado:**
- **OpenMontage** — muito completo, mas **AGPL-3.0**: se modificarmos e oferecermos como serviço, o código precisa ser aberto. Para uso interno gerando vídeos, ok.
- **onetake** — **proibido uso comercial** na versão grátis. Só para estudo, ou comprar o Pro.
- **Collage B-roll** — custa API do Gemini por vídeo e foi feito pro Codex.

**Não roda aqui:** **LongCat** (CUDA). Se quiser avatar, precisa de GPU alugada (RunPod/Modal) ou do Space do Hugging Face.

**Lacuna:** nenhuma dessas faz exatamente o que o vídeo 06 promete (pegar vídeo bruto → cortar pausas/erros → melhor tomada → legenda → zoom → SFX → trilha). Esse "editor profissional" de talking head é o que este repo precisa construir — provavelmente whisper (cortes por palavra) + ffmpeg + HyperFrames para os overlays. As skills que você já tem (`video-use`, `reels-multicam`) podem ser o ponto de partida.

## Para testar (lote 05)
- **Drama Claw** (ref 14): história escrita → personagens, storyboard, locução, edição e vídeo. Versão comunitária grátis, roda em servidor próprio (Docker). Ver se gera cenas com personagem consistente para o F14.
- **Higgsfield + Seedance 2.5** (ref 15): vídeo com o rosto da pessoa a partir de uma selfie. Pago. O ElevenLabs também tem Seedance 2.5 (~14 mil créditos por clipe, orçado em 18/10).

