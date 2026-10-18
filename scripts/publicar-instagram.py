"""Publica um Reel no Instagram (@moiseskalebbe) pela API oficial.

O MP4 fica no Mac: um servidor local serve só esse arquivo (nome aleatório) por um túnel
temporário do Cloudflare (https://….trycloudflare.com). O Instagram baixa o vídeo e tudo é desligado.

Uso:
    python3 scripts/publicar-instagram.py <video.mp4> <legenda.txt> --capa capa.jpg [--publicar]
    python3 scripts/publicar-instagram.py --conteiner <ID>     # publica um Reel já preparado (até 24 h)

A capa é obrigatória: o Instagram não deixa trocar a capa depois que o Reel está no ar.
(--capa-ms só serve com --sem-capa-consciente, para testes.)

Sem --publicar: prepara o Reel no Instagram (contêiner não publicado, expira em 24 h) e para.
Com --publicar: prepara e publica. Só usar depois do "pode publicar" do dono.

Credenciais no .env: INSTAGRAM_USER_ID, INSTAGRAM_ACCESS_TOKEN.
"""

import argparse
import http.server
import json
import pathlib
import re
import secrets
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://graph.instagram.com/v23.0"
RAIZ = pathlib.Path(__file__).resolve().parent.parent


def carregar_env() -> dict:
    env = {}
    for linha in (RAIZ / ".env").read_text().splitlines():
        if "=" in linha and not linha.startswith("#"):
            chave, valor = linha.split("=", 1)
            env[chave.strip()] = valor.strip()
    for obrigatoria in ("INSTAGRAM_USER_ID", "INSTAGRAM_ACCESS_TOKEN"):
        if not env.get(obrigatoria):
            sys.exit(f"{obrigatoria} não encontrada no .env")
    return env


def chamar(metodo: str, caminho: str, token: str, **params) -> dict:
    params["access_token"] = token
    dados = urllib.parse.urlencode(params).encode()
    url = f"{API}/{caminho}"
    if metodo == "GET":
        req = urllib.request.Request(f"{url}?{dados.decode()}")
    else:
        req = urllib.request.Request(url, data=dados, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as erro:
        sys.exit(f"Erro da API ({erro.code}): {erro.read().decode()[:500]}")


def servir_arquivo(pasta: pathlib.Path) -> tuple[http.server.HTTPServer, int]:
    class SoArquivo(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(pasta), **k)

        def log_message(self, *a):
            pass

    servidor = http.server.ThreadingHTTPServer(("127.0.0.1", 0), SoArquivo)
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    return servidor, servidor.server_address[1]


def abrir_tunel(porta: int) -> tuple[subprocess.Popen, str]:
    proc = subprocess.Popen(
        ["cloudflared", "tunnel", "--no-autoupdate", "--protocol", "http2", "--url", f"http://127.0.0.1:{porta}"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    url, limite = None, time.time() + 60
    while time.time() < limite:
        linha = proc.stdout.readline()
        achado = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", linha)
        if achado:
            url = achado.group(0)
        if url and "Registered tunnel connection" in linha:
            # continua lendo a saída em segundo plano para o processo não travar
            threading.Thread(target=lambda: [None for _ in proc.stdout], daemon=True).start()
            return proc, url
    proc.terminate()
    sys.exit("Não consegui abrir o túnel do Cloudflare.")


def esperar_link(url: str) -> None:
    """Checagem local opcional: o Mac costuma guardar em cache que o endereço novo não existe.
    Quem confirma de verdade é o Instagram (o contêiner vira ERROR se não conseguir baixar)."""
    for _ in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=10) as r:
                if r.status == 200:
                    return
        except Exception:
            pass
        time.sleep(2)
    print("aviso: o Mac não enxergou o túnel (cache de DNS local); seguindo, o Instagram baixa de fora")
    time.sleep(10)


def esperar_processamento(conteiner: str, token: str) -> None:
    for _ in range(60):
        estado = chamar("GET", conteiner, token, fields="status_code,status")
        codigo = estado.get("status_code")
        print("  processamento:", codigo)
        if codigo == "FINISHED":
            return
        if codigo in ("ERROR", "EXPIRED"):
            sys.exit(f"O Instagram recusou o vídeo: {estado}")
        time.sleep(5)
    sys.exit("O Instagram demorou demais para processar o vídeo.")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("video", nargs="?")
    p.add_argument("legenda", nargs="?")
    p.add_argument("--conteiner", help="publica um contêiner já preparado, sem subir o vídeo de novo")
    p.add_argument("--capa", help="imagem JPG 1080x1920 da capa (zona segura 4:5 no centro)")
    p.add_argument("--capa-ms", type=int, default=0, help="só com --sem-capa-consciente: instante do vídeo usado como capa, em ms")
    p.add_argument("--sem-capa-consciente", action="store_true", help="aceita publicar sem capa própria (não recomendado)")
    p.add_argument("--publicar", action="store_true", help="publica de verdade (precisa do ok do dono)")
    args = p.parse_args()

    env = carregar_env()
    token, usuario = env["INSTAGRAM_ACCESS_TOKEN"], env["INSTAGRAM_USER_ID"]
    if args.conteiner:
        publicar(args.conteiner, usuario, token)
        return
    if not (args.video and args.legenda):
        sys.exit("Informe <video.mp4> <legenda.txt> ou --conteiner <ID>")
    if not args.capa and not args.sem_capa_consciente:
        sys.exit("Falta a capa (--capa capa.jpg). O Instagram não deixa trocar a capa depois de publicado.")
    if args.capa and not pathlib.Path(args.capa).is_file():
        sys.exit(f"Capa não encontrada: {args.capa}")
    legenda = pathlib.Path(args.legenda).read_text().strip()

    with tempfile.TemporaryDirectory() as tmp:
        nome = f"{secrets.token_urlsafe(16)}.mp4"
        shutil.copy(args.video, pathlib.Path(tmp) / nome)
        nome_capa = None
        if args.capa:
            nome_capa = f"{secrets.token_urlsafe(16)}.jpg"
            shutil.copy(args.capa, pathlib.Path(tmp) / nome_capa)
        servidor, porta = servir_arquivo(pathlib.Path(tmp))
        tunel, base = abrir_tunel(porta)
        try:
            url = f"{base}/{nome}"
            esperar_link(url)
            extras = {"cover_url": f"{base}/{nome_capa}"} if nome_capa else {"thumb_offset": args.capa_ms}
            criado = chamar("POST", f"{usuario}/media", token, media_type="REELS", video_url=url,
                            caption=legenda, share_to_feed="true", **extras)
            conteiner = criado["id"]
            print("Reel preparado (não publicado):", conteiner)
            esperar_processamento(conteiner, token)
        finally:
            tunel.terminate()
            servidor.shutdown()
            print("túnel fechado e arquivo temporário apagado")

    if not args.publicar:
        print(f"Parado antes de publicar. Contêiner {conteiner} expira em 24 h.")
        return

    publicar(conteiner, usuario, token)


def publicar(conteiner: str, usuario: str, token: str) -> None:
    publicado = chamar("POST", f"{usuario}/media_publish", token, creation_id=conteiner)
    midia = chamar("GET", publicado["id"], token, fields="permalink")
    print("PUBLICADO:", midia.get("permalink"))


if __name__ == "__main__":
    main()
