"""Consultas reproduzíveis e relatório sem confundir lifetime com ganho no período."""
import json
from statistics import median
from datetime import datetime, timedelta
from core import DB, ROOT, TZ, connect, now, valid_date


def ratio(a,b):
    return a/b if a is not None and b is not None and b>0 else None


def derive(row):
    row = dict(row)
    meta = json.loads(row.pop('metadata'))
    metrics = json.loads(row.pop('metrics'))
    missing = json.loads(row.pop('missing'))
    watch_s = metrics.get('ig_reels_avg_watch_time')
    watch_s = watch_s/1000 if watch_s is not None else None
    return {**row, **meta, **metrics, 'missing':missing, 'tempo_medio_s':watch_s,
            'retencao':ratio(watch_s,meta.get('duracao_s')),
            'shares_alcance':ratio(metrics.get('shares'),metrics.get('reach')),
            'saves_alcance':ratio(metrics.get('saved'),metrics.get('reach')),
            'cta_alcance':ratio(metrics.get('cta_comments'),metrics.get('reach')),
            'idade_horas':(datetime.fromisoformat(row['collected_at'])-datetime.fromisoformat(row['published_at'])).total_seconds()/3600}


def listar_posts(desde, serie=None, db=DB):
    desde = valid_date(desde)
    with connect(db) as conn:
        rows = conn.execute('''SELECT p.*,s.metrics,s.missing,r.collected_at FROM posts p
          JOIN snapshots s ON s.post_id=p.id JOIN runs r ON r.id=s.run_id
          WHERE s.run_id=(SELECT MAX(s2.run_id) FROM snapshots s2 WHERE s2.post_id=p.id)
          AND substr(p.published_at,1,10)>=? ORDER BY p.published_at DESC''',(desde,)).fetchall()
    return [p for r in rows if (p:=derive(r)) and (serie is None or p['serie']==serie)]


def metricas_post(id_ou_link, db=DB):
    from core import shortcode
    with connect(db) as conn:
        rows = conn.execute('''SELECT p.*,s.metrics,s.missing,r.collected_at FROM posts p
          JOIN snapshots s ON p.id=s.post_id JOIN runs r ON r.id=s.run_id ORDER BY r.id''').fetchall()
    history = [derive(r) for r in rows if r['id']==id_ou_link or (shortcode(id_ou_link) and shortcode(r['permalink'])==shortcode(id_ou_link))]
    return {'post':history[-1] if history else None, 'evolucao':history,
            'nota':'Snapshots acumulados lifetime. Diferenças entre snapshots não equivalem a métricas diárias únicas.'}


def comparar_series(desde, db=DB):
    posts = listar_posts(desde,db=db)
    groups = {}
    for p in posts:
        groups.setdefault((p['serie'],p.get('estilo')),[]).append(p)
    fields = ('reach','retencao','shares_alcance','saves_alcance','cta_comments','cta_alcance')
    def aggregate(items):
        return {field:{'mediana':median(values) if (values:=[p[field] for p in items if p.get(field) is not None]) else None,'n':len(values)} for field in fields}
    return {'series':[{'serie':s,'estilo':style,'posts':len(items),'evidencia':'indício; amostra menor que 5' if len(items)<5 else 'comparação descritiva; não causal',**aggregate(items)} for (s,style),items in groups.items()],
            'perfil':aggregate(posts), 'nota':'Posts publicados desde a data; métricas acumuladas até cada coleta. Idades diferentes afetam comparação.'}


def top_e_bottom(desde, n=3, db=DB):
    if not 1<=n<=20:
        raise ValueError('n deve estar entre 1 e 20')
    posts = listar_posts(desde,db=db)
    # A single explicit criterion, never mix reach and conversion in one ranking.
    eligible = [p for p in posts if p.get('cta_alcance') is not None]
    metric = 'cta_alcance'
    if len(eligible)<2 or len({p[metric] for p in eligible})<2:
        metric = 'shares_alcance'
        eligible = [p for p in posts if p.get(metric) is not None]
    if len(eligible)<2 or len({p[metric] for p in eligible})<2:
        metric = 'reach'
        eligible = [p for p in posts if p.get(metric) is not None]
    eligible.sort(key=lambda p:(-p[metric],p['id']))
    if len(eligible)<2 or len({p[metric] for p in eligible})<2:
        return {'criterio':metric,'top':[],'bottom':[],'nota':'Sem diferença observável suficiente para ranking. Ausente não é zero.'}
    size = min(n,len(eligible)//2)
    return {'criterio':metric,'top':eligible[:size],'bottom':list(reversed(eligible[-size:])),
            'nota':'Ordem descritiva; empate não implica diferença. Top e bottom não se sobrepõem; posts com métrica ausente ficam de fora.'}


def conta(desde, db=DB):
    desde = valid_date(desde)
    with connect(db) as conn:
        rows = conn.execute('SELECT a.payload,r.collected_at FROM account a JOIN runs r ON a.run_id=r.id ORDER BY r.id').fetchall()
    daily, snapshots, latest = {}, [], None
    for r in rows:
        payload = json.loads(r['payload']); latest = payload
        if r['collected_at'][:10]>=desde:
            snapshots.append({'coletado_em':r['collected_at'],**payload['profile']})
        for d in payload['daily']:
            if d['date']>=desde:
                daily[(d['date'],d['metric'])] = d
    return {'snapshots':snapshots,'daily':list(daily.values()),'missing':latest['missing'] if latest else {},
            'nota':'followers_count é total observado; follower_count é a métrica da API e não é substituído pelo total. Sem atribuição de seguidores a posts.'}


def report(desde, db=DB, output=None):
    desde = valid_date(desde)
    posts = listar_posts(desde,db=db)
    comparison = comparar_series(desde,db=db)
    rank = top_e_bottom(desde,db=db)
    def fmt(v,percent=False):
        return 'indisponível' if v is None else f'{v*100:.1f}%' if percent else f'{v:g}'
    lines = [f'# Instagram · {now().date().isoformat()}', '',f'Posts publicados desde {desde}; {len(posts)} Reels. Fonte: API oficial, snapshots locais.',
        '', 'Métricas acumuladas até a coleta, não ganhos da semana. Retenção = tempo médio (ms ÷ 1.000) ÷ duração do MP4 local. Não equivale a taxa de conclusão. CTA conta comentários acessíveis de primeiro nível, não pessoas nem vendas.',
        '', '| Série | Alcance mediano | Retenção | Shares/alcance | Saves/alcance | CTA mediano | Posts |', '|---|---:|---:|---:|---:|---:|---:|']
    for s in comparison['series']:
        lines.append('| '+s['serie']+' | '+' | '.join(fmt(s[f]['mediana'],f in ('retencao','shares_alcance','saves_alcance')) for f in ('reach','retencao','shares_alcance','saves_alcance','cta_comments'))+f" | {s['posts']} |")
    lines += ['', 'Amostras menores que cinco posts por série são indícios. Compare também a idade dos posts. Campos ausentes não entram na mediana.']
    for title,key in [('Mais altos','top'),('Mais baixos','bottom')]:
        lines += ['',f'## {title} · critério: {rank["criterio"]}']
        for p in rank[key]:
            lines += [f'- [{p.get("slug") or p["id"]}]({p["permalink"]}): alcance {fmt(p["reach"])}; retenção {fmt(p["retencao"],True)}; compartilhamentos {fmt(p["shares"])}; CTA {fmt(p["cta_comments"])}; idade {p["idade_horas"]:.1f} h. Coleta {p["collected_at"]}.']
        if not rank[key]: lines.append('Sem dados suficientes para distinguir posições.')
    lines += ['', '## O que repetir', 'Manter a coleta e comparar vídeos na mesma idade (por exemplo, 24 h e 72 h). A amostra atual ainda não prova que um gancho ou série causa melhor resultado.', '', '## O que parar', 'Não eliminar uma série por um único post nem confundir curtidas com pedidos de diagnóstico. Não tratar dado ausente como zero.', '', '## Próximo vídeo']
    upcoming=[]
    for line in (ROOT/'calendario.md').read_text().splitlines():
        match=__import__('re').search(r'(\d{2})/(\d{2})/(\d{4})',line)
        if match and ('agendado' in line or 'a fazer' in line):
            d=datetime.strptime(match.group(),'%d/%m/%Y').date()
            if d>=now().date(): upcoming.append((d,line.split('|')[3].strip()))
    if upcoming:
        d,title=sorted(upcoming)[0]
        lines.append(f'Preservar o próximo teste do calendário: {title}, {d:%d/%m/%Y}. Não há evidência suficiente para substituir a pauta; medir retenção e CTA após publicação.')
    else: lines.append('Consultar calendario.md; sem próxima publicação identificada automaticamente.')
    lines += ['', '## Limites e dados ausentes']
    for p in posts:
        if p['missing']: lines.append(f'- {p.get("slug") or p["id"]}: '+ '; '.join(f'{k}: {v}' for k,v in p['missing'].items()))
        if not p.get('duracao_s'): lines.append(f'- {p.get("slug") or p["id"]}: duração final não verificada; retenção indisponível.')
    account = conta(desde,db=db)
    lines += [f'- Conta · {k}: {v}' for k,v in account['missing'].items()]
    lines += ['- Pesquisa de nicho via Apify não executada: requer token próprio e autorização de custo. As referências editoriais do repositório não comprovam desempenho do nicho.', '', '## Referências', '- calendario.md; roteiros correspondentes; referencias/instagram-analise.md.', '- ferramentas/instagram-mcp/README.md: metodologia, instalação e limites.', '']
    output = output or ROOT/'analises/instagram'/f'{now().date().isoformat()}.md'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text('\n'.join(lines))
    return output
