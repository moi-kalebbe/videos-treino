import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from core import API, APIError, connect, count_cta, scalar, collect
from analise import listar_posts, comparar_series, top_e_bottom, metricas_post, ratio

class Tests(unittest.TestCase):
    def test_pagination_trusted_host_cursor(self):
        api=object.__new__(API)
        with patch.object(api,'get',side_effect=[{'data':[1],'paging':{'next':'https://evil.test/?access_token=secret','cursors':{'after':'a'}}},{'data':[2]}]) as get:
            self.assertEqual(list(api.pages('123/media')), [1,2])
            self.assertEqual(get.call_args.args,('123/media',))
            self.assertEqual(get.call_args.kwargs,{'after':'a'})

    def test_broken_pagination_is_not_complete(self):
        api=object.__new__(API)
        with patch.object(api,'get',return_value={'data':[],'paging':{'next':'x'}}):
            with self.assertRaises(APIError): list(api.pages('123/media'))

    def test_cta_accents_words_and_duplicates(self):
        api=object.__new__(API)
        with patch.object(api,'pages',return_value=iter([{'text':'DIAGNÓSTICO! diagnostico'},{'text':'diagnosticos'},{'text':'Quero diagnóstico'}])):
            self.assertEqual(count_cta(api,'1',['DIAGNÓSTICO']),2)
        self.assertIsNone(count_cta(api,'1',[]))

    def test_missing_zero_and_ratios(self):
        self.assertEqual(scalar({'data':[{'values':[{'value':0}]}]}),0)
        self.assertIsNone(scalar({'data':[]}))
        self.assertIsNone(ratio(2,0))
        self.assertIsNone(ratio(None,10))
        self.assertEqual(ratio(0,10),0)

    def fixture(self, db):
        with connect(db) as c:
            for run,reach in [(1,10),(2,20)]:
                c.execute('INSERT INTO runs VALUES (?,?,?,?)',(run,f'2026-10-{18+run}T20:00:00-03:00','ok','[]'))
                for pid in ['a','b','c']:
                    c.execute('INSERT OR IGNORE INTO posts VALUES (?,?,?,?)',(pid,'2026-10-19T12:00:00-03:00',f'https://www.instagram.com/reel/{pid}/',json.dumps({'serie':'Teste','estilo':'x','duracao_s':20})))
                    c.execute('INSERT INTO snapshots VALUES (?,?,?,?)',(run,pid,json.dumps({'reach':reach if pid!='c' else None,'ig_reels_avg_watch_time':10000,'shares':0,'saved':0,'cta_comments':0}), '{}'))

    def test_latest_snapshot_median_null_and_retention(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=Path(tmp)/'test.db';self.fixture(db)
            rows=listar_posts('2026-10-19',db=db)
            self.assertEqual(len(rows),3)
            self.assertEqual(rows[0]['retencao'],0.5)
            self.assertEqual(rows[0]['reach'],20)
            result=comparar_series('2026-10-19',db=db)['series'][0]
            self.assertEqual(result['reach'],{'mediana':20,'n':2})
            self.assertEqual(len(metricas_post('https://www.instagram.com/reel/a/?x=1',db=db)['evolucao']),2)
            self.assertEqual(listar_posts('2026-10-20',db=db),[])

    def test_ranking_ties_not_fabricated(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=Path(tmp)/'test.db';self.fixture(db)
            result=top_e_bottom('2026-10-19',db=db)
            self.assertEqual(result['top'],[])
            self.assertEqual(result['bottom'],[])

    def test_collection_history_privacy_and_partial_comments(self):
        class Fake:
            user='owner'
            fail=False
            def pages(self,path,**params):
                if path.endswith('/media'):
                    yield {'id':'123','timestamp':'2026-10-19T15:00:00+0000','permalink':'https://www.instagram.com/reel/test/','media_product_type':'REELS','caption':'Comenta DIAGNÓSTICO'}
                else:
                    yield {'text':'Diagnóstico SEGREDO-DO-SEGUIDOR'}
                    if self.fail: raise APIError(403,200)
            def get(self,path,**params):
                if path=='owner': return {'followers_count':10}
                return {'data':[{'values':[{'value':0}]}]}
        with tempfile.TemporaryDirectory() as tmp:
            db=Path(tmp)/'test.db';api=Fake()
            with patch('core.calendar_metadata',return_value={}):
                collect('2026-10-19',db=db,api=api)
                api.fail=True
                collect('2026-10-19',db=db,api=api)
            history=metricas_post('123',db=db)['evolucao']
            self.assertEqual(len(history),2)
            self.assertEqual(history[0]['cta_comments'],1)
            self.assertIsNone(history[1]['cta_comments'])
            self.assertEqual(history[1]['reach'],0)
            self.assertNotIn(b'SEGREDO-DO-SEGUIDOR',db.read_bytes())

    def test_bad_date_rejected(self):
        with self.assertRaises(ValueError): listar_posts('not-a-date')

    def test_error_no_raw_secrets(self):
        self.assertNotIn('access_token', str(APIError(403,200)))

if __name__=='__main__': unittest.main()
