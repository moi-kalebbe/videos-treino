"""Gera index.html: título fixo + 10 cards de ferramenta (estilo terminal) + card final."""
import re
from pathlib import Path

CARDS = [
    ("github", "GitHub", "181717", "guarda o código e abre o PR sozinho"),
    ("nextdotjs", "Next.js", "000000", "monta os sites e sistemas"),
    ("supabase", "Supabase", "3ECF8E", "cria o banco e o login dos clientes"),
    ("vercel", "Vercel", "000000", "põe o site no ar a cada commit"),
    ("docker", "Docker", "2496ED", "sobe os sistemas na VPS"),
    ("redis", "Redis", "DC382D", "dispara as mensagens em fila"),
    ("googlechrome", "Claude in Chrome", "D97757", "testa o site clicando como cliente"),
    ("googlegemini", "Veo 3.1", "4285F4", "gera as cenas de vídeo com IA"),
    ("elevenlabs", "ElevenLabs", "000000", "narra os vídeos com a minha voz"),
    ("hyperframes", "HyperFrames", "111111", "edita os vídeos escrevendo código"),
]
INICIO, PASSO, FINAL = 2.6, 1.35, 2.03
DURACAO = round(INICIO + PASSO * len(CARDS) + FINAL, 2)


CURTO = {"github":"github","nextdotjs":"next","supabase":"supabase","vercel":"vercel","docker":"docker","redis":"redis","googlechrome":"chrome","googlegemini":"veo","elevenlabs":"elevenlabs","hyperframes":"hf"}
DOMINIO = {"github":"github.com","nextdotjs":"nextjs.org","supabase":"supabase.com","vercel":"vercel.com","docker":"docker.com","redis":"redis.io","googlechrome":"claude.com/chrome","googlegemini":"deepmind.google/models/veo","elevenlabs":"elevenlabs.io","hyperframes":"hyperframes.dev"}
ESCUROS = {"github", "docker", "googlechrome", "redis", "googlegemini"}


def icone(nome: str, cor: str) -> str:
    if nome == "hyperframes":
        return '<span style="font:800 50px Outfit,sans-serif;color:#fff;letter-spacing:-2px">HF</span>'
    if nome == "googlechrome":
        nome = "claude"
    svg = Path(f"assets/logos/{nome}.svg").read_text()
    caminho = re.search(r'<path d="([^"]+)"', svg).group(1)
    return f'<svg viewBox="0 0 24 24" width="74" height="74"><path fill="#fff" d="{caminho}"/></svg>'


def card(i: int, nome: str, rotulo: str, cor: str, linha: str) -> str:
    n = f"{i + 1:02d}"
    return f'''
      <div class="card" id="c{i}">
        <div class="barra"><span class="d p"></span><span class="d y"></span><span class="d g"></span>
          <span class="cmd">~/minha-empresa $ run {CURTO[nome]}</span><span class="cont">[{n}/10]</span></div>
        <div class="topo"><div class="logo" style="background:#{cor}">{icone(nome, cor)}</div><div class="nome">{rotulo}</div><div class="num">{n}</div></div>
        <div class="linha"><span class="seta">&gt;</span> Claude {linha}</div>
        <div class="nav"><div class="url"><span class="pt"></span>{DOMINIO[nome]}</div><div class="print"><img class="{'' if nome in ESCUROS else 'inv'}" src="assets/sites/{nome}.png" alt=""/></div></div>
      </div>'''


def timeline() -> str:
    linhas = []
    for i in range(len(CARDS)):
        t = round(INICIO + PASSO * i, 2)
        linhas.append(f'tl.fromTo("#c{i}", {{opacity:0, scale:0.94, filter:"blur(8px)"}}, {{opacity:1, scale:1, filter:"blur(0px)", duration:0.3, ease:"power2.out", immediateRender:false}}, {t});')
        linhas.append(f'tl.set("#p{i}", {{backgroundColor:"#4ADE80", opacity:1}}, {t});')
        if i:
            linhas.append(f'tl.to("#c{i - 1}", {{opacity:0, duration:0.25}}, {t});')
            linhas.append(f'tl.set("#p{i - 1}", {{backgroundColor:"#A855F7"}}, {t});')
    fim = round(INICIO + PASSO * len(CARDS), 2)
    linhas.append(f'tl.to("#c{len(CARDS) - 1}", {{opacity:0, duration:0.25}}, {fim});')
    linhas.append(f'tl.set("#p{len(CARDS) - 1}", {{backgroundColor:"#A855F7"}}, {fim});')
    linhas.append(f'tl.fromTo("#final", {{opacity:0, scale:0.94, filter:"blur(8px)"}}, {{opacity:1, scale:1, filter:"blur(0px)", duration:0.3, ease:"power2.out", immediateRender:false}}, {fim});')
    linhas.append(f'tl.fromTo("#final .socio", {{scale:0.6}}, {{scale:1, duration:0.4, ease:"back.out(2.5)", immediateRender:false}}, {fim + 0.25});')
    return "\n      ".join(linhas)


def sons() -> str:
    return f'<audio id="mus" src="assets/sons/musica-original.m4a" data-start="0" data-duration="{DURACAO}" data-volume="1.0"></audio>'


HTML = f'''<!doctype html>
<html lang="pt-BR" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Minha empresa roda no Claude</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ width:1080px; height:1920px; overflow:hidden; background:#000; }}
      #root {{ position:relative; width:100%; height:100%; overflow:hidden; background:#0b0612; }}
      #fundo {{ position:absolute; inset:0; width:1080px; height:1920px; object-fit:cover; }}
      #tinta {{ position:absolute; inset:0; background:radial-gradient(ellipse at 90% 40%, rgba(40,230,130,0.28), transparent 50%), radial-gradient(ellipse at 10% 15%, rgba(160,60,255,0.35), transparent 55%), linear-gradient(180deg, rgba(60,10,110,0.25) 0%, rgba(0,0,0,0) 45%, rgba(30,4,60,0.45) 100%); mix-blend-mode:normal; }}
      #titulo {{ position:absolute; left:0; width:1080px; top:180px; text-align:center; font-family:Outfit, sans-serif; }}
      .bx {{ display:inline-block; position:relative; color:#fff; font-weight:800; font-size:70px; line-height:1; letter-spacing:-1px; padding:14px 30px 18px; border-radius:20px; margin:6px 0;
        background:linear-gradient(rgba(16,10,26,0.86), rgba(16,10,26,0.86)) padding-box, linear-gradient(90deg, #A855F7, #4ADE80) border-box; border:3px solid transparent; }}
      .verde {{ color:#4ADE80; }}
      .sub {{ display:inline-block; margin-top:8px; font:700 50px "JetBrains Mono", monospace; color:#4ADE80; padding:8px 30px 10px; border-radius:20px;
        background:linear-gradient(rgba(16,10,26,0.86), rgba(16,10,26,0.86)) padding-box, linear-gradient(90deg, #A855F7, #4ADE80) border-box; border:3px solid transparent; }}
      #prog {{ position:absolute; top:548px; left:0; width:1080px; display:flex; justify-content:center; gap:10px; }}
      #prog i {{ width:46px; height:8px; border-radius:4px; background:rgba(255,255,255,0.22); }}
      .card, #final {{ position:absolute; left:90px; top:592px; width:900px; border-radius:30px; overflow:hidden; opacity:0;
        background:linear-gradient(rgba(28,18,44,0.78), rgba(18,12,30,0.82)) padding-box, linear-gradient(160deg, #A855F7, #4ADE80) border-box; border:3px solid transparent;
        backdrop-filter:blur(14px); -webkit-backdrop-filter:blur(14px); box-shadow:0 0 50px rgba(168,85,247,0.35), 0 30px 80px rgba(0,0,0,0.5); }}
      .barra {{ height:72px; display:flex; align-items:center; padding:0 28px; gap:12px; border-bottom:1px solid rgba(255,255,255,0.10); font:500 30px "JetBrains Mono", monospace; color:#b9b4c8; }}
      .d {{ width:18px; height:18px; border-radius:9px; }} .p {{ background:#A855F7; }} .y {{ background:#F59E0B; }} .g {{ background:#4ADE80; }}
      .cmd {{ margin-left:16px; flex:1; white-space:nowrap; overflow:hidden; }}
      .cont {{ color:#4ADE80; font-weight:700; }}
      .topo {{ display:flex; align-items:center; padding:24px 30px 10px; gap:28px; }}
      .logo {{ width:118px; height:118px; border-radius:26px; display:flex; align-items:center; justify-content:center; box-shadow:0 6px 20px rgba(0,0,0,0.4); flex:none; }}
      .nome {{ flex:1; font:800 66px Outfit, sans-serif; color:#fff; letter-spacing:-1px; white-space:nowrap; }}
      .num {{ font:800 112px "JetBrains Mono", monospace; background:linear-gradient(180deg, #A855F7, #4ADE80); -webkit-background-clip:text; background-clip:text; color:transparent; }}
      .linha {{ padding:6px 32px 26px; font:600 39px/1.25 Outfit, sans-serif; color:#fff; }}
      .seta {{ color:#4ADE80; font-weight:800; margin-right:8px; }}
      .nav {{ margin:0 30px 30px; border-radius:16px; overflow:hidden; border:1px solid rgba(255,255,255,0.12); background:#07060b; }}
      .url {{ height:54px; display:flex; align-items:center; gap:14px; padding:0 20px; font:500 28px "JetBrains Mono", monospace; color:#c9c5d6; border-bottom:1px solid rgba(255,255,255,0.08); }}
      .pt {{ width:12px; height:12px; border-radius:6px; background:#4ADE80; }}
      .print {{ height:470px; overflow:hidden; }}
      .print img {{ width:100%; display:block; }}
      .print img.inv {{ filter:invert(0.93) hue-rotate(180deg) brightness(1.05) contrast(0.95); }}
      #final {{ padding:0 0 60px; text-align:center; }}
      #final .barra {{ text-align:left; }}
      #final .t0 {{ margin-top:50px; font:700 44px Outfit, sans-serif; color:#4ADE80; }}
      #final .t1 {{ margin-top:18px; font:800 76px/1.12 Outfit, sans-serif; color:#fff; letter-spacing:-1px; }}
      #final .socio {{ display:inline-block; color:#120a1e; background:#4ADE80; padding:0 18px 6px; border-radius:14px; }}
      #final .t2 {{ margin-top:40px; font:700 48px Outfit, sans-serif; color:#d9d4e8; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DURACAO}" data-width="1080" data-height="1920">
      <video id="fundo" src="assets/fundo.mp4" muted playsinline data-start="0" data-duration="{DURACAO}"></video>
      <div id="tinta"></div>
      <div id="titulo">
        <div class="bx">Minha empresa inteira</div><br/>
        <div class="bx">roda no <span class="verde">Claude Code</span></div><br/>
        <div class="sub">(10 ferramentas)</div>
      </div>
      <div id="prog">{"".join(f'<i id="p{i}"></i>' for i in range(len(CARDS)))}</div>
      {"".join(card(i, *c) for i, c in enumerate(CARDS))}
      <div id="final">
        <div class="barra"><span class="d p"></span><span class="d y"></span><span class="d g"></span><span class="cmd">~/minha-empresa $ compartilhar</span><span class="cont">[fim]</span></div>
        <div class="t0">Gostou?</div>
        <div class="t1">Manda pro <span class="socio">sócio</span><br/>que ainda faz<br/>isso na mão 👇</div>
        <div class="t2">📌 Salva pra montar a sua</div>
      </div>
      {sons()}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      
      {timeline()}
      tl.set({{}}, {{}}, {DURACAO});
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

Path("index.html").write_text(HTML)
print("duração", DURACAO)
