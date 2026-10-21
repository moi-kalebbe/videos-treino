"""Gera index.html: título fixo + 10 cards de ferramenta (estilo terminal) + card final."""
import re
from pathlib import Path

CARDS = [
    ("gmail", "Gmail", "EA4335", "lê a caixa e separa o que é cliente"),
    ("googlecalendar", "Google Agenda", "4285F4", "marca a reunião sem troca de mensagem"),
    ("googledrive", "Google Drive", "1FA463", "acha qualquer contrato em segundos"),
    ("googlesheets", "Google Sheets", "34A853", "fecha a planilha do financeiro"),
    ("clickup", "ClickUp", "7B68EE", "distribui as tarefas da equipe"),
    ("meta", "Meta Ads", "0081FB", "mostra qual anúncio dá venda"),
    ("instagram", "Instagram", "E4405F", "manda o relatório das redes toda segunda"),
    ("supabase", "Supabase", "3FCF8E", "puxa os números do sistema"),
    ("canva", "Canva", "00C4CC", "faz a arte do post"),
    ("elevenlabs", "ElevenLabs", "111111", "grava a narração dos vídeos"),
]
INICIO, PASSO, FINAL = 1.4, 1.5, 3.4
DURACAO = round(INICIO + PASSO * len(CARDS) + FINAL, 2)


def icone(nome: str, cor: str) -> str:
    svg = Path(f"assets/logos/{nome}.svg").read_text()
    caminho = re.search(r'<path d="([^"]+)"', svg).group(1)
    return f'<svg viewBox="0 0 24 24" width="64" height="64"><path fill="#{cor}" d="{caminho}"/></svg>'


def card(i: int, nome: str, rotulo: str, cor: str, linha: str) -> str:
    n = f"{i + 1:02d}"
    return f'''
      <div class="card" id="c{i}">
        <div class="barra"><span class="d r"></span><span class="d y"></span><span class="d g"></span>
          <span class="cmd">~/minha-empresa $ claude --mcp {nome}</span><span class="cont">[{n}/10]</span></div>
        <div class="topo"><div class="logo">{icone(nome, cor)}</div><div class="nome">{rotulo}</div><div class="num">{n}</div></div>
        <div class="linha">&gt; o Claude {linha}</div>
        <div class="print"><img src="assets/sites/{nome}.png" alt=""/></div>
      </div>'''


def timeline() -> str:
    linhas = []
    for i in range(len(CARDS)):
        t = round(INICIO + PASSO * i, 2)
        linhas.append(f'tl.fromTo("#c{i}", {{opacity:0, y:60, scale:0.96}}, {{opacity:1, y:0, scale:1, duration:0.28, ease:"power3.out", immediateRender:false}}, {t});')
        linhas.append(f'tl.fromTo("#c{i} .num", {{scale:1.6}}, {{scale:1, duration:0.35, ease:"back.out(2)", immediateRender:false}}, {t + 0.05});')
        if i:
            linhas.append(f'tl.to("#c{i - 1}", {{opacity:0, y:-30, duration:0.22}}, {t});')
    fim = round(INICIO + PASSO * len(CARDS), 2)
    linhas.append(f'tl.to("#c{len(CARDS) - 1}", {{opacity:0, y:-30, duration:0.22}}, {fim});')
    linhas.append(f'tl.fromTo("#final", {{opacity:0, y:60}}, {{opacity:1, y:0, duration:0.35, ease:"power3.out", immediateRender:false}}, {fim});')
    linhas.append(f'tl.fromTo("#final .socio", {{scale:0.6}}, {{scale:1, duration:0.4, ease:"back.out(2.5)", immediateRender:false}}, {fim + 0.25});')
    return "\n      ".join(linhas)


def sons() -> str:
    tags = [f'<audio id="tri" src="assets/sons/trilha.mp3" data-start="0" data-duration="{DURACAO}" data-volume="0.55"></audio>',
            '<audio id="wh" src="assets/sons/whoosh.mp3" data-start="1.25" data-duration="0.8" data-volume="0.45"></audio>']
    for i in range(len(CARDS)):
        tags.append(f'<audio id="k{i}" src="assets/sons/s_clique.mp3" data-start="{round(INICIO + PASSO * i, 2)}" data-duration="0.4" data-volume="0.55"></audio>')
    fim = round(INICIO + PASSO * len(CARDS), 2)
    tags.append(f'<audio id="dg" src="assets/sons/ding.mp3" data-start="{fim + 0.25}" data-duration="1.0" data-volume="0.35"></audio>')
    return "\n      ".join(tags)


HTML = f'''<!doctype html>
<html lang="pt-BR" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Minha empresa roda no Claude</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ width:1080px; height:1920px; overflow:hidden; background:#000; }}
      #root {{ position:relative; width:100%; height:100%; overflow:hidden; background:#0b0612; }}
      #fundo {{ position:absolute; inset:0; width:1080px; height:1920px; object-fit:cover; filter:saturate(1.1) brightness(0.9); }}
      #tinta {{ position:absolute; inset:0; background:linear-gradient(180deg, rgba(40,10,70,0.55) 0%, rgba(10,4,20,0.15) 40%, rgba(5,2,10,0.6) 100%); }}
      #titulo {{ position:absolute; left:0; width:1080px; top:200px; text-align:center; font-family:Inter, sans-serif; }}
      #titulo .l {{ display:inline-block; background:rgba(8,8,12,0.88); color:#fff; font-weight:900; font-size:64px; line-height:1; padding:12px 26px; border-radius:14px; margin:6px 0; border:2px solid rgba(255,255,255,0.12); }}
      #titulo .claude {{ color:#E8835F; }}
      #titulo .sub {{ display:inline-block; margin-top:10px; font:800 40px "JetBrains Mono", monospace; color:#39FF88; background:rgba(8,8,12,0.88); padding:8px 20px; border-radius:10px; border:2px solid rgba(57,255,136,0.35); }}
      .card {{ position:absolute; left:70px; top:600px; width:940px; background:rgba(14,14,20,0.94); border:2px solid rgba(255,255,255,0.14); border-radius:26px; overflow:hidden; opacity:0; box-shadow:0 30px 80px rgba(0,0,0,0.6), 0 0 60px rgba(150,80,255,0.25); }}
      .barra {{ height:62px; display:flex; align-items:center; padding:0 22px; gap:10px; background:rgba(255,255,255,0.05); border-bottom:1px solid rgba(255,255,255,0.08); font:600 24px "JetBrains Mono", monospace; color:#9aa0b0; }}
      .d {{ width:16px; height:16px; border-radius:8px; }} .r {{ background:#ff5f57; }} .y {{ background:#febc2e; }} .g {{ background:#28c840; }}
      .cmd {{ margin-left:14px; flex:1; white-space:nowrap; overflow:hidden; }}
      .cont {{ color:#39FF88; }}
      .topo {{ display:flex; align-items:center; padding:30px 34px 6px; gap:24px; }}
      .logo {{ width:100px; height:100px; border-radius:24px; background:#fff; display:flex; align-items:center; justify-content:center; }}
      .nome {{ flex:1; font:800 58px Inter, sans-serif; color:#fff; }}
      .num {{ font:800 104px "JetBrains Mono", monospace; color:#39FF88; text-shadow:0 0 30px rgba(57,255,136,0.55); }}
      .linha {{ padding:4px 36px 26px; font:600 38px/1.25 "JetBrains Mono", monospace; color:#e9e9f2; }}
      .print {{ margin:0 30px 30px; border-radius:16px; overflow:hidden; border:1px solid rgba(255,255,255,0.12); height:500px; }}
      .print img {{ width:100%; display:block; }}
      #final {{ position:absolute; left:70px; top:640px; width:940px; padding:56px 50px 60px; background:rgba(14,14,20,0.95); border:2px solid rgba(57,255,136,0.45); border-radius:26px; text-align:center; opacity:0; box-shadow:0 0 70px rgba(57,255,136,0.25); }}
      #final .cmd2 {{ font:600 26px "JetBrains Mono", monospace; color:#9aa0b0; margin-bottom:30px; }}
      #final .t1 {{ font:800 68px/1.15 Inter, sans-serif; color:#fff; }}
      #final .socio {{ display:inline-block; color:#0b0612; background:#39FF88; padding:0 18px; border-radius:12px; }}
      #final .t2 {{ margin-top:34px; font:700 44px Inter, sans-serif; color:#cfd2dc; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DURACAO}" data-width="1080" data-height="1920">
      <video id="fundo" src="assets/fundo.mp4" muted playsinline data-start="0" data-duration="{DURACAO}"></video>
      <div id="tinta"></div>
      <div id="titulo">
        <div class="l">Minha empresa inteira</div><br/>
        <div class="l">roda no <span class="claude">Claude</span></div><br/>
        <div class="sub">(10 ferramentas)</div>
      </div>
      {"".join(card(i, *c) for i, c in enumerate(CARDS))}
      <div id="final">
        <div class="cmd2">~/minha-empresa $ compartilhar</div>
        <div class="t1">Manda pro <span class="socio">sócio</span><br/>que ainda faz<br/>isso na mão 👇</div>
        <div class="t2">📌 Salva pra montar a sua</div>
      </div>
      {sons()}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      tl.fromTo("#titulo", {{opacity:0, y:-40}}, {{opacity:1, y:0, duration:0.4, ease:"power3.out", immediateRender:false}}, 0.05);
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
