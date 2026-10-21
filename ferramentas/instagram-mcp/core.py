"""Instagram oficial → snapshots privados. Nenhuma operação de escrita na rede."""
from __future__ import annotations
import json
import os
import re
import sqlite3
import subprocess
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, date, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parents[2]
LOCAL = Path(__file__).resolve().parent
DB = LOCAL / 'dados/instagram.db'
TZ = ZoneInfo('America/Sao_Paulo')
METRICS = ('reach','views','likes','comments','shares','saved','total_interactions',
           'ig_reels_avg_watch_time','ig_reels_video_view_total_time')
SERIES = {'Plantão IA':'plantao-ia','A Virada':'manifesto-cinematografico',
          'Caso Real':'caso-real','IA por Setor':'ia-por-setor','Dossiê':'dossie'}


def now():
    return datetime.now(TZ)


def valid_date(value):
    return date.fromisoformat(value).isoformat()


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.casefold()) if not unicodedata.combining(c))


def shortcode(url):
    match = re.search(r'/(?:reel|reels|p)/([A-Za-z0-9_-]+)', url or '')
    return match.group(1) if match else None


class APIError(RuntimeError):
    def __init__(self, status, code=None):
        self.status, self.code = status, code
        hint = 'Verifique token e instagram_business_manage_insights / instagram_business_manage_comments.' if code in (10,190,200) or status in (401,403) else 'Métrica indisponível, parâmetros incompatíveis ou falha temporária.'
        super().__init__(f'API HTTP {status}, código {code}: {hint}')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class API:
    def __init__(self):
        env = {**dotenv_values(ROOT / '.env', interpolate=False), **os.environ}
        self.token = env.get('INSTAGRAM_ACCESS_TOKEN')
        self.user = env.get('INSTAGRAM_USER_ID')
        version = env.get('INSTAGRAM_API_VERSION', 'v23.0')
        if not re.fullmatch(r'v\d+\.\d+', version):
            raise ValueError('INSTAGRAM_API_VERSION inválida')
        if not self.token or not self.user:
            raise ValueError('Configure INSTAGRAM_USER_ID e INSTAGRAM_ACCESS_TOKEN no .env local.')
        self.base = f'https://graph.instagram.com/{version}'
        self.opener = urllib.request.build_opener(NoRedirect)

    def get(self, path, **params):
        if not re.fullmatch(r'[A-Za-z0-9_/]+', path):
            raise ValueError('Caminho de API inválido')
        url = f'{self.base}/{path}?{urllib.parse.urlencode(params)}'
        req = urllib.request.Request(url, headers={'Authorization':f'Bearer {self.token}'})
        for attempt in range(3):
            try:
                with self.opener.open(req, timeout=30) as response:
                    return json.load(response)
            except urllib.error.HTTPError as exc:
                try:
                    code = json.load(exc).get('error', {}).get('code')
                except (ValueError, AttributeError):
                    code = None
                if (exc.code == 429 or exc.code >= 500) and attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                raise APIError(exc.code, code) from None
            except (urllib.error.URLError, TimeoutError, OSError, ValueError):
                if attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                raise APIError(0) from None

    def pages(self, path, **params):
        # Never follow API-supplied next URLs with credentials. Reuse trusted host + cursor.
        seen = set()
        for _ in range(1000):
            response = self.get(path, **params)
            yield from response.get('data', [])
            paging = response.get('paging', {})
            if not paging.get('next'):
                return
            cursor = paging.get('cursors', {}).get('after')
            if not cursor or cursor in seen:
                raise APIError(0, 'pagination_incomplete')
            seen.add(cursor)
            params['after'] = cursor
        raise APIError(0, 'pagination_limit')


def connect(path=DB):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    conn = sqlite3.connect(path, timeout=30)
    path.chmod(0o600)
    conn.row_factory = sqlite3.Row
    conn.executescript('''
      CREATE TABLE IF NOT EXISTS runs (id INTEGER PRIMARY KEY, collected_at TEXT NOT NULL, status TEXT NOT NULL, diagnostics TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS posts (id TEXT PRIMARY KEY, published_at TEXT, permalink TEXT, metadata TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS snapshots (run_id INTEGER, post_id TEXT, metrics TEXT NOT NULL, missing TEXT NOT NULL, PRIMARY KEY(run_id,post_id));
      CREATE TABLE IF NOT EXISTS account (run_id INTEGER PRIMARY KEY, payload TEXT NOT NULL);
    ''')
    return conn


def calendar_metadata(root=ROOT):
    result = {}
    for line in (root / 'calendario.md').read_text().splitlines():
        link = re.search(r'https://www\.instagram\.com/(?:reel|p)/[\w-]+/', line)
        script = re.search(r'\((roteiros/[^)]+\.md)\)', line)
        if not link or not script or '✅' not in line:
            continue
        series = next((s for s in SERIES if s in line), 'Sem classificação')
        script_path = root / script.group(1)
        content = script_path.read_text() if script_path.exists() else ''
        duration = re.search(r'\| Duração[^|]*\|\s*~?([\d.,]+)\s*s', content)
        target = float(duration.group(1).replace(',','.')) if duration else None
        slug = script_path.stem
        actual = None
        render = root / 'saida' / f'{slug}.mp4'
        if render.exists():
            try:
                actual = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(render)], timeout=10, stderr=subprocess.DEVNULL))
            except (OSError, ValueError, subprocess.SubprocessError):
                pass
        speech = root / 'producao' / slug / 'falas.txt'
        hook = None
        if speech.exists():
            hook = next((x.strip() for x in speech.read_text().splitlines() if x.strip() and not x.startswith('#')), None)
        cta_line = next((x for x in content.splitlines() if re.match(r'\| CTA\s*\|',x)), '')
        keywords = re.findall(r'`([^`]+)`', cta_line) if 'definir' not in cta_line else []
        result[shortcode(link.group())] = dict(serie=series, estilo=SERIES.get(series), roteiro=script.group(1),
            slug=slug, gancho=hook, duracao_s=actual, duracao_alvo_s=target,
            duracao_fonte='ffprobe: '+str(render.relative_to(root)) if actual else None, cta_palavras=keywords)
    return result


def scalar(response):
    data = response.get('data', [])
    if not data:
        return None
    row = data[0]
    value = row.get('total_value', {}).get('value')
    if value is None:
        values = row.get('values', [])
        value = values[-1].get('value') if values else None
    return value if isinstance(value, (int,float)) and not isinstance(value,bool) and value >= 0 else None


def count_cta(api, media_id, words):
    if not words:
        return None
    patterns = [re.compile(r'\b'+re.escape(normalize(w))+r'\b') for w in words]
    total = 0
    for comment in api.pages(f'{media_id}/comments', fields='text', limit=100):
        total += any(p.search(normalize(comment.get('text',''))) for p in patterns)
    return total


def collect(desde=None, db=DB, api=None):
    desde = valid_date(desde or (now().date()-timedelta(days=30)).isoformat())
    api = api or API()
    collected = now().isoformat()
    metadata = calendar_metadata()
    posts, diagnostics = [], []
    # Fetch list first: pagination failure never masquerades as a successful partial collection.
    for post in api.pages(f'{api.user}/media', fields='id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count', limit=100):
        published = datetime.fromisoformat(post['timestamp']).astimezone(TZ).isoformat()
        if published[:10] < desde:
            continue
        if post.get('media_product_type') != 'REELS':
            continue
        meta = dict(metadata.get(shortcode(post.get('permalink')), {'serie':'Sem classificação','cta_palavras':[]}))
        # Caption is inspected transiently to resolve CTA; never persist comments or follower identities.
        caption = post.get('caption', '')
        words = re.findall(r'(?i)coment[ae]\s+["“\x27`]?([\wÀ-ÿ]+)', caption)
        if words:
            meta['cta_palavras'] = list(dict.fromkeys(w.upper() for w in words if len(w)>2))
        metrics, missing = {}, {}
        for metric in METRICS:
            try:
                value = scalar(api.get(f"{post['id']}/insights", metric=metric))
                if metric == 'views' and value is None:
                    value = scalar(api.get(f"{post['id']}/insights", metric='plays'))
                metrics[metric] = value
                if value is None:
                    missing[metric] = 'Resposta sem valor'
            except APIError as exc:
                metrics[metric] = None
                missing[metric] = str(exc)
                if metric == 'views' and exc.status == 400 and exc.code == 100:
                    try:
                        metrics[metric] = scalar(api.get(f"{post['id']}/insights", metric='plays'))
                        if metrics[metric] is not None:
                            missing.pop(metric)
                            meta['views_fonte'] = 'plays'
                    except APIError:
                        pass
        try:
            metrics['cta_comments'] = count_cta(api, post['id'], meta.get('cta_palavras',[]))
            if metrics['cta_comments'] is None:
                missing['cta_comments'] = 'Palavra CTA não identificada; não presumida'
        except APIError as exc:
            metrics['cta_comments'] = None
            missing['cta_comments'] = str(exc)
        meta['cta_escopo'] = 'Comentários de primeiro nível acessíveis pela API; não inclui respostas'
        posts.append((post['id'],published,post.get('permalink'),meta,metrics,missing))
    account = {'profile':{}, 'daily':[], 'missing':{}}
    try:
        account['profile'] = api.get(api.user, fields='id,username,followers_count,media_count')
    except APIError as exc:
        account['missing']['profile'] = str(exc)
    # One complete day per interval; never label a week total as a daily value.
    end = now().date()
    start = max(date.fromisoformat(desde), end-timedelta(days=7))
    for metric in ('reach','follower_count','profile_views','accounts_engaged','website_clicks'):
        for offset in range((end-start).days):
            day = start+timedelta(days=offset)
            params = dict(metric=metric, period='day', since=int(datetime.combine(day,datetime.min.time(),TZ).timestamp()), until=int(datetime.combine(day+timedelta(days=1),datetime.min.time(),TZ).timestamp()))
            if metric in ('reach','accounts_engaged','profile_views','website_clicks'):
                params['metric_type'] = 'total_value'
            try:
                value = scalar(api.get(f'{api.user}/insights', **params))
                account['daily'].append({'date':day.isoformat(),'metric':metric,'value':value})
                if value is None:
                    account['missing'][metric] = 'Resposta sem valor (pode haver atraso ou limiar de seguidores)'
            except APIError as exc:
                account['missing'][metric] = str(exc)
                break
    if any(p[-1] for p in posts) or account['missing']:
        diagnostics.append('Coleta parcial: consulte missing em cada post e na conta.')
    with connect(db) as conn:
        cur = conn.execute('INSERT INTO runs(collected_at,status,diagnostics) VALUES (?,?,?)', (collected,'partial' if diagnostics else 'ok',json.dumps(diagnostics)))
        run_id = cur.lastrowid
        for pid,published,link,meta,metrics,missing in posts:
            conn.execute('INSERT INTO posts VALUES (?,?,?,?) ON CONFLICT(id) DO UPDATE SET published_at=excluded.published_at,permalink=excluded.permalink,metadata=excluded.metadata', (pid,published,link,json.dumps(meta,ensure_ascii=False)))
            conn.execute('INSERT INTO snapshots VALUES (?,?,?,?)',(run_id,pid,json.dumps(metrics),json.dumps(missing,ensure_ascii=False)))
        conn.execute('INSERT INTO account VALUES (?,?)',(run_id,json.dumps(account,ensure_ascii=False)))
    return {'run_id':run_id,'coletado_em':collected,'posts':len(posts),'status':'partial' if diagnostics else 'ok','diagnostics':diagnostics,'conta_ausentes':account['missing']}
