"""Painel offline, sem CDN, scripts externos ou dados de seguidores."""
from html import escape
from core import LOCAL, now
from analise import listar_posts, comparar_series, conta


def generate(desde):
    posts=listar_posts(desde)
    profile=conta(desde)
    latest=profile['snapshots'][-1] if profile['snapshots'] else {}
    def fmt(value,percentage=False):
        return '—' if value is None else f'{value*100:.1f}%' if percentage else f'{value:g}'
    charts=[]
    for field,label,percent in [('reach','Alcance',False),('retencao','Retenção média',True),('shares_alcance','Compartilhamentos / alcance',True),('saves_alcance','Salvamentos / alcance',True),('cta_comments','Comentários com CTA',False)]:
        max_value=max((p.get(field) or 0 for p in posts),default=0) or 1
        bars=[]
        for p in posts:
            value=p.get(field)
            title=escape(p.get('slug') or p['id'])
            bars.append(f'<div class="bar"><div><span>{title}</span><b>{fmt(value,percent)}</b></div><div class="track"><i style="width:{(value or 0)/max_value*100:.2f}%"></i></div></div>')
        charts.append(f'<section><h2>{label}</h2>'+''.join(bars)+'</section>')
    rows=[]
    for p in posts:
        link=escape(p['permalink'],quote=True) if p['permalink'].startswith('https://www.instagram.com/') else '#'
        rows.append(f'<tr><td><a href="{link}" target="_blank" rel="noopener">{escape(p.get("slug") or p["id"])}</a><small>{escape(p["serie"])}</small></td><td>{fmt(p["reach"])}</td><td>{fmt(p["retencao"],True)}</td><td>{fmt(p["cta_comments"])}</td><td>{p["idade_horas"]:.1f} h</td><td>{escape(p["collected_at"][:16])}</td></tr>')
    missing=sum(len(p['missing']) for p in posts)+len(profile['missing'])
    html='''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Instagram · Processos & IA</title><style>
    *{box-sizing:border-box}body{margin:0;background:#f4f3ee;color:#192a2b;font:16px system-ui,sans-serif}main{max-width:1180px;margin:auto;padding:48px 28px}header{border-top:5px solid #177565;padding-top:20px}header p{color:#46605a}h1{font-size:clamp(32px,5vw,58px);letter-spacing:-2px;margin:16px 0}h2{font-size:18px;margin:0 0 24px}.eyebrow{text-transform:uppercase;letter-spacing:2px;font-size:12px}.intro{max-width:750px;line-height:1.7}.kpis{display:flex;gap:45px;flex-wrap:wrap;border-block:1px solid #cad3cc;padding:25px 0;margin:30px 0}.kpis strong{font-size:32px;display:block}.kpis span,small{font-size:12px;color:#526862}small{display:block;margin-top:6px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}section{background:#fff;padding:26px;border:1px solid #e2e5df;border-radius:8px}.bar{margin:22px 0}.bar>div:first-child{display:flex;justify-content:space-between;gap:15px;font-size:13px}.track{height:10px;background:#e8efea;margin-top:9px;border-radius:5px;overflow:hidden}.track i{height:100%;background:#177565;display:block}.table{overflow:auto;margin-top:24px}table{width:100%;border-collapse:collapse;white-space:nowrap}th,td{text-align:left;padding:16px 12px;border-bottom:1px solid #e2e5df;font-size:13px}a{color:#146457}aside{background:#e6ede3;padding:24px;line-height:1.7;margin:24px 0;border-left:4px solid #177565}footer{font-size:12px;color:#526862;line-height:1.8;margin-top:24px}@media(max-width:700px){main{padding:25px 16px}.grid{grid-template-columns:1fr}.kpis{gap:24px}section{padding:18px}}
    </style><main><header><span class="eyebrow">Processos & IA / Instagram</span><h1>O que os números dizem.</h1><p class="intro">Acompanhe o alcance, a atenção e os pedidos de diagnóstico dos seus Reels. Dados oficiais; nenhuma estimativa preenche campos ausentes.</p></header>'''
    html+=f'<div class="kpis"><div><strong>{len(posts)}</strong><span>Reels desde {escape(desde)}</span></div><div><strong>{fmt(latest.get("followers_count"))}</strong><span>Seguidores observados</span></div><div><strong>{missing}</strong><span>Campos indisponíveis</span></div></div>'
    html+='<aside><b>Ainda é cedo para escolher uma série vencedora.</b><br>Compare posts com a mesma idade e reúna pelo menos cinco por série. Alcance e interações são acumulados; retenção é a fração média assistida, não a taxa de conclusão.</aside>'
    html+='<div class="grid">'+''.join(charts)+'</div><section class="table"><h2>Cada Reel, com contexto</h2><table><thead><tr><th>Reel</th><th>Alcance</th><th>Retenção</th><th>CTA</th><th>Idade na coleta</th><th>Coletado em</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></section>'
    html+=f'<footer>Gerado em {now():%d/%m/%Y %H:%M} · America/Sao_Paulo. “—” significa indisponível. CTA: comentários de primeiro nível acessíveis pela API; não inclui respostas.<br>Retenção usa duração do MP4 local; sem duração verificada, permanece ausente. Este painel é local e funciona sem internet.</footer></main></html>'
    path=LOCAL/'painel.html';path.write_text(html);return path
