"""Recalcula o data-start dos efeitos sonoros a partir dos tempos da narração.

Uso:
    python3 scripts/sincronizar-audio.py <pasta-do-projeto> [--fim-extra 2.5]

Cada <audio> ou <video> com `data-sinc` é reposicionado:
    data-sinc="palavra:ia:2:-0.1"  -> 2ª ocorrência da palavra "ia" menos 0,1 s
    data-sinc="cena:3:-0.2"        -> início da 4ª cena (índice 3) menos 0,2 s
Também ajusta a duração do <audio id="narracao"> e a duração total (root, palco, legenda, trilha)
para o fim da narração + `--fim-extra` segundos.
"""

import argparse
import json
import pathlib
import re
import subprocess

LIMPAR = re.compile(r"[.,?!:;]")


def carregar_tempos(assets: pathlib.Path) -> tuple[list[dict], list[float]]:
    js = (assets / "legenda.js").read_text()
    palavras = json.loads(re.search(r"window\.LEGENDA = (.*?);\n", js).group(1))
    cenas = json.loads(re.search(r"window\.CENAS = (.*?);\n", js).group(1))
    return palavras, cenas


def tempo(regra: str, palavras: list[dict], cenas: list[float]) -> float:
    tipo, *args = regra.split(":")
    if tipo == "cena":
        indice, ajuste = int(args[0]), float(args[1])
        return cenas[indice] + ajuste
    alvo, n, ajuste = args[0], int(args[1]), float(args[2])
    vistos = [p for p in palavras if LIMPAR.sub("", p["w"].lower()) == alvo]
    if len(vistos) < n:
        raise SystemExit(f"Palavra '{alvo}' ocorre {len(vistos)}x, regra pede a {n}ª ({regra})")
    return vistos[n - 1]["s"] + ajuste


def duracao(arquivo: pathlib.Path) -> float:
    saida = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(arquivo)],
        capture_output=True, text=True, check=True,
    )
    return float(saida.stdout.strip())


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("projeto")
    p.add_argument("--fim-extra", type=float, default=2.5)
    args = p.parse_args()

    projeto = pathlib.Path(args.projeto)
    html_path = projeto / "index.html"
    html = html_path.read_text()
    palavras, cenas = carregar_tempos(projeto / "assets")

    def reposicionar(m: re.Match) -> str:
        tag = m.group(0)
        regra = re.search(r'data-sinc="([^"]+)"', tag).group(1)
        inicio = max(0.0, round(tempo(regra, palavras, cenas), 2))
        return re.sub(r'data-start="[^"]*"', f'data-start="{inicio}"', tag)

    html = re.sub(r"<(?:audio|video)[^>]*data-sinc=\"[^\"]+\"[^>]*>", reposicionar, html)

    narracao = duracao(projeto / "assets" / "audio" / "narracao.mp3")
    total = round(narracao + args.fim_extra, 1)
    html = re.sub(r'(<audio id="narracao"[^>]*data-duration=")[^"]*"', rf'\g<1>{round(narracao, 2)}"', html)
    for alvo in ('id="root"', 'id="palco"', 'id="legenda"', 'id="trilha"'):
        html = re.sub(rf'({alvo}[^>]*data-duration=")[^"]*"', rf'\g<1>{total}"', html)
    html = re.sub(r"const DURACAO = [\d.]+;", f"const DURACAO = {total};", html)

    html_path.write_text(html)
    print(f"narração {narracao:.2f} s · vídeo {total} s · efeitos reposicionados")


if __name__ == "__main__":
    main()
