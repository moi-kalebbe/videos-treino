import argparse
import json
from datetime import timedelta
from core import collect, now, APIError
from analise import report


def main():
    parser = argparse.ArgumentParser(description='Coleta somente leitura de Reels e insights oficiais.')
    parser.add_argument('--desde', default=(now().date()-timedelta(days=30)).isoformat())
    parser.add_argument('--somente-relatorio', action='store_true')
    args = parser.parse_args()
    try:
        if not args.somente_relatorio:
            print(json.dumps(collect(args.desde),ensure_ascii=False))
        print('Relatório:', report(args.desde))
        from painel import generate
        print('Painel:', generate(args.desde))
    except (APIError,ValueError) as exc:
        parser.exit(1,str(exc)+'\n')

if __name__=='__main__': main()
