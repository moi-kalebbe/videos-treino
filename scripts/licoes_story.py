"""Monta um Story da série Lições para a Vida a partir de um arquivo de configuração (JSON).

Uso:
    python3 scripts/licoes_story.py <config.json> <pasta-do-story>

A pasta precisa ter assets/audio/<voz>.mp3 + assets/<voz>.json (de scripts/licoes_voz.py) e
assets/img/<cenas>.png. O script copia sons e fontes do modelo, recorta o personagem da 1ª cena
(efeito capa de revista) e escreve o index.html para o HyperFrames.

Formato aprovado pelo dono em 20/10/2026 (Story 1 v3): cenas ilustradas em tela cheia com Ken Burns,
título atrás do personagem, cartão do livro com título completo, autor e capítulo, rabisco à mão,
checklist, legenda grande com palavra-chave em amarelo, sons em cada corte e fechamento com resumo,
próxima lição (ou "amanhã tem mais três") e botão seguir.
"""

import json
import pathlib
import shutil
import subprocess
import sys

MODELO = pathlib.Path(__file__).resolve().parent.parent / "producao/licoes-para-a-vida-01/modelo"
FOLGA_FINAL = 2.6

CIRCULO = ("M50 4 C 82 2, 98 30, 97 52 C 96 80, 70 97, 46 96 C 18 95, 2 74, 4 48 C 6 24, 28 3, 58 6")


def palavras_com_inicio(pasta: pathlib.Path, audios: list[dict]) -> list[dict]:
    todas = []
    for a in audios:
        for w in json.loads((pasta / "assets" / a["json"]).read_text()):
            todas.append({"w": w["w"], "s": round(w["s"] + a["inicio"], 3), "e": round(w["e"] + a["inicio"], 3)})
    return todas


def recortar_capa(pasta: pathlib.Path, img: str) -> None:
    destino = pasta / "assets/img/capa-recorte.png"
    if destino.exists():
        return
    subprocess.run(["npx", "--yes", "hyperframes@0.8.171", "remove-background", str(pasta / "assets/img" / img),
                    "-o", str(destino)], check=True, capture_output=True)


def tamanho_titulo(cfg: dict) -> int:
    """Título longo encolhe para a palavra de destaque não ficar atrás da cabeça do personagem."""
    letras = len(cfg["titulo"]) + len(cfg["titulo_destaque"])
    return 158 if letras <= 22 else 124 if letras <= 30 else 108


def html(cfg: dict, palavras: list[dict], duracao: float) -> str:
    livro = cfg.get("livro")
    cenas = cfg["cenas"]
    passos = cfg.get("passos", [])
    fim = cfg["fim"]
    divs_cenas = "\n".join(
        f'      <div class="cena" id="cena{i}" style="background-image:url(assets/img/{c["img"]})"></div>'
        + ('\n      <p id="capa-titulo" style="font-size:' + str(tamanho_titulo(cfg)) + 'px">' + cfg["titulo"] + ' <em>' + cfg["titulo_destaque"] + '</em></p>\n      <div id="capa-rec"></div>' if i == 0 else "")
        for i, c in enumerate(cenas))
    marca = cfg.get("circula_passo")
    itens = []
    for i, p in enumerate(passos):
        texto = p["texto"]
        if marca and marca["passo"] == i + 1:
            texto = texto.replace(marca["texto"], f'<span class="marca">{marca["texto"]}<svg class="doodle" style="left:-18px;top:-14px;width:calc(100% + 36px);height:calc(100% + 28px)" viewBox="0 0 100 100" preserveAspectRatio="none"><path id="circ-passo" vector-effect="non-scaling-stroke" style="stroke:#e2502f" d="{CIRCULO}" /></svg></span>', 1)
        itens.append(f'        <div class="passo"><i>{i + 1}<b>✓</b></i><p>{texto}</p></div>')
    overlays = "\n".join(f'      <p class="bolha{" flutua" if o.get("flutua") else ""}" id="ov{i}" style="{o["estilo"]}">{o["texto"]}</p>' for i, o in enumerate(cfg.get("overlays", [])))
    resumo = "".join(f"<p><span>✓</span> {r}</p>" for r in cfg.get("resumo", []))
    if fim["tipo"] == "proximo":
        rotulo = fim.get("rotulo", f'PRÓXIMO STORY · LIÇÃO {cfg["numero"] + 1} DE {cfg["total"]}')
        extras = (f'<p class="t">📖 {fim["livro"]}</p>' if fim.get("livro") else "") + (f'<p class="a">{fim["autor"]}</p>' if fim.get("autor") else "")
        cartao_fim = (f'<div id="amanha"><p class="r">{rotulo}</p><h4>{fim["titulo"]}</h4>{extras}</div>'
                      f'<p id="proximo">{fim.get("botao", "Toque para a próxima ▶")}</p>')
    else:
        cartao_fim = (f'<div id="amanha"><p class="r">AMANHÃ CEDO</p><h4>{fim.get("titulo", "Mais uma lição")}</h4>'
                      f'<p class="t">{fim.get("subtitulo", "Uma ideia de livro + como aplicar no dia a dia")}</p></div>'
                      '<p id="seguir">Seguir @moiseskalebbe</p><div id="toque"></div>')
    audios = "\n".join(
        f'      <audio id="voz{i}" src="assets/audio/{a["arquivo"]}" data-start="{a["inicio"]}" data-duration="{a["duracao"]}" data-volume="1"></audio>'
        for i, a in enumerate(cfg["audios"]))
    sons = "\n".join(
        f'      <audio id="som{i}" src="assets/sons/{s["arquivo"]}" data-start="{s["t"]:.2f}" data-duration="{s["d"]}" data-volume="{s["vol"]}"></audio>'
        for i, s in enumerate(cfg["_sons"]))
    js_cfg = json.dumps({k: cfg[k] for k in ("cenas", "momentos", "frase", "passos", "fim", "chaves", "overlays", "circula_passo", "resumo", "passos_sai", "visor") if k in cfg}, ensure_ascii=False)
    bloco_livro = ""
    if livro:
        bloco_livro = (f'<div id="livro"><p class="r">📖 DE QUAL LIVRO É</p><h2>{livro["titulo"]}</h2><p class="autor">{livro["autor"]}</p>'
                       f'<p class="cap">{livro["capitulo"]}<svg class="doodle" style="left:-26px;top:-20px;width:calc(100% + 52px);height:calc(100% + 40px)" viewBox="0 0 100 100" preserveAspectRatio="none"><path id="circ-cap" vector-effect="non-scaling-stroke" d="{CIRCULO}" /></svg></p></div>')
    bloco_frase = f'<p id="frase">{cfg["frase"]["texto"]}</p>' if cfg.get("frase") else ""
    bloco_passos = (f'<div class="cartao" id="hoje"><h3>{cfg.get("passos_titulo", "Testa hoje")}</h3>\n' + "\n".join(itens) + "\n      </div>") if passos else ""
    bloco_resumo = f'<div id="resumo">{resumo}</div>' if resumo else ""
    bloco_visor = ('<div id="visor"><i class="c1"></i><i class="c2"></i><i class="c3"></i><i class="c4"></i>'
                   '<p class="rec"><b>●</b> REC</p><p class="tc">15:15:04</p></div>') if cfg.get("visor") else ""
    return (MODELO / "molde.html").read_text() \
        .replace("{{TITULO_PAGINA}}", f'Lições para a Vida · {cfg["numero"]}/{cfg["total"]} · {cfg["titulo"]} {cfg["titulo_destaque"]}') \
        .replace("{{DURACAO}}", f"{duracao:.2f}").replace("{{CSS_EXTRA}}", cfg.get("css_extra", "")) \
        .replace("{{SELO}}", cfg.get("selo", f'LIÇÕES PARA A VIDA · {cfg["numero"]}/{cfg["total"]}')) \
        .replace("{{CENAS}}", divs_cenas) \
        .replace("{{LIVRO}}", bloco_livro).replace("{{VISOR}}", bloco_visor).replace("{{OVERLAYS}}", overlays) \
        .replace("{{FRASE}}", bloco_frase).replace("{{PASSOS}}", bloco_passos) \
        .replace("{{RESUMO}}", bloco_resumo).replace("{{FIM}}", cartao_fim) \
        .replace("{{AUDIOS}}", audios).replace("{{SONS}}", sons) \
        .replace("{{PALAVRAS}}", json.dumps(palavras, ensure_ascii=False)) \
        .replace("{{CFG}}", js_cfg)


def achar(palavras: list[dict], alvo: str, n: int = 1, ultimo: bool = False) -> float:
    limpar = lambda s: s.lower().strip('.,?!:;"…')
    achados = [w["s"] for w in palavras if limpar(w["w"]) == alvo]
    if not achados:
        raise SystemExit(f'palavra "{alvo}" não está na fala')
    return achados[-1] if ultimo else achados[n - 1]


def musica_do_dia(cfg: dict) -> tuple[str, float]:
    """Reveza 5 trilhas calmas (uma por dia, sem repetir na semana); volume já igualado entre elas."""
    import datetime
    trilhas = [linha.split() for linha in (MODELO / "musicas.txt").read_text().split("\n") if linha.strip()]
    if cfg.get("musica"):
        return next((a, float(v)) for a, v in trilhas if a == cfg["musica"])
    dia = datetime.date.fromisoformat(cfg["data"]) if cfg.get("data") else datetime.date.today()
    arquivo, volume = trilhas[dia.toordinal() % len(trilhas)]
    return arquivo, float(volume)


def montar_sons(cfg: dict, palavras: list[dict], duracao: float) -> list[dict]:
    """Sons padrão do formato (a cada corte, livro, passos, final) + os sons próprios da lição."""
    trilha, volume = musica_do_dia(cfg)
    sons = [{"arquivo": trilha, "t": 0, "d": round(duracao, 2), "vol": volume},
            {"arquivo": "s_hit2.mp3", "t": 0.05, "d": 2, "vol": 0.45}]
    for c in cfg["cenas"][1:]:
        t = achar(palavras, *c["entra"]) - 0.15 if isinstance(c["entra"], list) else c["entra"]
        sons.append({"arquivo": "whoosh.mp3", "t": t, "d": 0.68, "vol": 0.33})
    m = cfg.get("momentos", {})
    if cfg.get("livro"):
        sons.append({"arquivo": "s_papel.mp3", "t": achar(palavras, *m["livro"]) - 0.2, "d": 1, "vol": 0.5})
        sons.append({"arquivo": "s_papel.mp3", "t": achar(palavras, *m["capitulo"]), "d": 1, "vol": 0.4})
    if cfg.get("frase"):
        sons.append({"arquivo": "ding.mp3", "t": achar(palavras, *cfg["frase"]["entra"]), "d": 1, "vol": 0.4})
    for p in cfg.get("passos", []):
        sons.append({"arquivo": "s_ponto.mp3", "t": achar(palavras, *p["check"]), "d": 1, "vol": 0.45})
    if cfg.get("resumo"):
        t_fim = achar(palavras, "então", ultimo=True)
        sons.append({"arquivo": "whoosh.mp3", "t": t_fim - 0.3, "d": 0.68, "vol": 0.35})
    t_card = achar(palavras, *cfg["fim"]["entra"])
    sons.append({"arquivo": "s_hit2.mp3", "t": t_card - 0.05, "d": 2, "vol": 0.35})
    sons.append({"arquivo": "s_clique.mp3", "t": t_card + 1.1, "d": 0.65, "vol": 0.7})
    sons.append({"arquivo": "vinheta.mp3", "t": min(duracao - 2.6, t_card + 1.4), "d": 2.6, "vol": 0.35})
    for s in cfg.get("sons", []):
        sons.append({"arquivo": s["arquivo"], "t": max(0, achar(palavras, *s["palavra"]) + s.get("desloc", 0)),
                     "d": s.get("d", 1), "vol": s.get("vol", 0.4)})
    return sons


def main() -> None:
    cfg = json.loads(pathlib.Path(sys.argv[1]).read_text())
    pasta = pathlib.Path(sys.argv[2])
    (pasta / "assets/sons").mkdir(parents=True, exist_ok=True)
    (pasta / "assets/fonts").mkdir(parents=True, exist_ok=True)
    for f in (MODELO / "sons").iterdir():
        shutil.copy(f, pasta / "assets/sons" / f.name)
    for f in (MODELO / "fonts").iterdir():
        shutil.copy(f, pasta / "assets/fonts" / f.name)
    shutil.copy(MODELO / "hyperframes.json", pasta / "hyperframes.json")
    for a in cfg["audios"]:
        a["duracao"] = round(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(pasta / "assets/audio" / a["arquivo"])],
            capture_output=True, text=True).stdout), 2)
    palavras = palavras_com_inicio(pasta, cfg["audios"])
    duracao = max(a["inicio"] + a["duracao"] for a in cfg["audios"]) + cfg.get("folga_final", FOLGA_FINAL)
    cfg["_sons"] = montar_sons(cfg, palavras, duracao)
    recortar_capa(pasta, cfg["cenas"][0]["img"])
    (pasta / "index.html").write_text(html(cfg, palavras, duracao))
    print(f"pronto: {pasta}/index.html ({duracao:.1f} s, {len(cfg['_sons'])} sons)")


if __name__ == "__main__":
    main()
