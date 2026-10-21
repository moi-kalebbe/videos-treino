"""Gera variações de um vídeo base do avatar: fundo novo e/ou cor de camisa nova.

Roda local (Apple Silicon, MPS), sem crédito pago:
- recorte da pessoa: RobustVideoMatting (resnet50)
- máscara da camisa: SegFormer "mattmdjaga/segformer_b2_clothes" (classe Upper-clothes)

Uso (venv em ~/.cache/avatar-tools):
  ~/.cache/avatar-tools/.venv/bin/python -I scripts/avatar_variacoes.py \
      entrada.mp4 saida.mp4 [--fundo imagem.jpg|video.mp4|#RRGGBB] [--camisa #RRGGBB]

A entrada deve ser um trecho já cortado e em SDR (ver guias/avatar-variacoes.md).
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
import torch

MODELOS = Path.home() / ".cache/avatar-tools/modelos"
SEGFORMER = "mattmdjaga/segformer_b2_clothes"
CLASSE_CAMISA = 4
SUAVIZACAO_MASCARA = 0.6  # peso do quadro anterior (tira tremor da máscara)


def dispositivo() -> torch.device:
    return torch.device("mps" if torch.backends.mps.is_available() else "cpu")


def hex_para_bgr(cor: str) -> tuple[int, int, int]:
    cor = cor.lstrip("#")
    r, g, b = (int(cor[i : i + 2], 16) for i in (0, 2, 4))
    return b, g, r


class Fundo:
    """Imagem, vídeo em loop ou cor lisa, sempre no tamanho do quadro."""

    def __init__(self, origem: str, largura: int, altura: int):
        self.tamanho = (largura, altura)
        self.video = None
        self.fixo = None
        if origem.startswith("#"):
            self.fixo = np.full((altura, largura, 3), hex_para_bgr(origem), np.uint8)
        elif Path(origem).suffix.lower() in {".mp4", ".mov", ".webm", ".m4v"}:
            self.video = cv2.VideoCapture(origem)
        else:
            self.fixo = self._cobrir(cv2.imread(origem))

    def _cobrir(self, img: np.ndarray) -> np.ndarray:
        largura, altura = self.tamanho
        escala = max(largura / img.shape[1], altura / img.shape[0])
        img = cv2.resize(img, None, fx=escala, fy=escala, interpolation=cv2.INTER_AREA)
        y = (img.shape[0] - altura) // 2
        x = (img.shape[1] - largura) // 2
        return img[y : y + altura, x : x + largura]

    def proximo(self) -> np.ndarray:
        if self.fixo is not None:
            return self.fixo
        ok, quadro = self.video.read()
        if not ok:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ok, quadro = self.video.read()
        return self._cobrir(quadro)


class Recorte:
    """Alpha da pessoa com memória entre quadros (RVM)."""

    def __init__(self, dev: torch.device):
        sys.path.insert(0, str(MODELOS / "RobustVideoMatting"))
        from model import MattingNetwork  # noqa: E402  (repo clonado)

        self.dev = dev
        self.rede = MattingNetwork("resnet50").eval().to(dev)
        self.rede.load_state_dict(torch.load(MODELOS / "rvm_resnet50.pth", map_location="cpu"))
        self.memoria = [None] * 4

    @torch.no_grad()
    def alpha(self, bgr: np.ndarray) -> np.ndarray:
        rgb = torch.from_numpy(bgr[..., ::-1].copy()).to(self.dev)
        src = rgb.permute(2, 0, 1)[None].float() / 255
        _, pha, *self.memoria = self.rede(src, *self.memoria, downsample_ratio=0.25)
        return pha[0, 0].float().cpu().numpy()


class MascaraCamisa:
    def __init__(self, dev: torch.device):
        from transformers import AutoModelForSemanticSegmentation, SegformerImageProcessor

        self.dev = dev
        self.proc = SegformerImageProcessor.from_pretrained(SEGFORMER)
        self.rede = AutoModelForSemanticSegmentation.from_pretrained(SEGFORMER).eval().to(dev)
        self.anterior = None

    @torch.no_grad()
    def mascara(self, bgr: np.ndarray) -> np.ndarray:
        entrada = self.proc(images=bgr[..., ::-1].copy(), return_tensors="pt").to(self.dev)
        logits = self.rede(**entrada).logits
        logits = torch.nn.functional.interpolate(
            logits, size=bgr.shape[:2], mode="bilinear", align_corners=False
        )[0]
        # só onde a camisa vence todas as outras classes (evita barba e pescoço)
        camisa = (logits.argmax(0) == CLASSE_CAMISA).float().cpu().numpy()
        camisa = cv2.morphologyEx(camisa, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
        if self.anterior is not None:
            camisa = SUAVIZACAO_MASCARA * self.anterior + (1 - SUAVIZACAO_MASCARA) * camisa
        self.anterior = camisa
        mascara = camisa
        return cv2.GaussianBlur(mascara, (0, 0), 2.5)


def recolorir(bgr: np.ndarray, mascara: np.ndarray, cor: str) -> np.ndarray:
    """Troca a cor mantendo dobras e sombras do tecido (canal L do Lab)."""
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    alvo = cv2.cvtColor(np.uint8([[hex_para_bgr(cor)]]), cv2.COLOR_BGR2LAB)[0, 0].astype(np.float32)
    dentro = mascara > 0.5
    if dentro.sum() < 500:
        return bgr
    luz = lab[..., 0]
    media = luz[dentro].mean()
    novo = lab.copy()
    # brilho médio vai para o da cor nova; dobras e sombras ficam, encolhidas
    # na mesma proporção (camisa clara virando preta não fica cinza)
    contraste = np.clip(alvo[0] / max(media, 1), 0.35, 1.0)
    novo[..., 0] = np.clip(alvo[0] + (luz - media) * contraste, 0, 255)
    sombra = np.clip(novo[..., 0] / max(alvo[0], 1), 0.3, 1.2)  # tecido escuro satura menos
    novo[..., 1] = 128 + (alvo[1] - 128) * sombra
    novo[..., 2] = 128 + (alvo[2] - 128) * sombra
    pintado = cv2.cvtColor(novo.astype(np.uint8), cv2.COLOR_LAB2BGR).astype(np.float32)
    m = mascara[..., None]
    return (pintado * m + bgr.astype(np.float32) * (1 - m)).astype(np.uint8)


def codificador_alpha(saida: Path, largura: int, altura: int, fps: float):
    """WebM VP9 com transparência: a pessoa recortada, sem fundo (para pôr por cima de outra cena)."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{largura}x{altura}", "-r", f"{fps}", "-i", "-",
        "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "6M", "-auto-alt-ref", "0", str(saida),
    ]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE)


def codificador(saida: Path, largura: int, altura: int, fps: float, audio_de: Path):
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{largura}x{altura}", "-r", f"{fps}", "-i", "-",
        "-i", str(audio_de), "-map", "0:v", "-map", "1:a?", "-c:a", "aac", "-b:a", "192k",
        "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-shortest", str(saida),
    ]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE)


def main() -> None:
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("entrada", type=Path)
    args.add_argument("saida", type=Path)
    args.add_argument("--fundo", help="imagem, vídeo ou #RRGGBB")
    args.add_argument("--camisa", help="#RRGGBB")
    args.add_argument("--alpha", action="store_true", help="sai .webm com fundo transparente")
    opcoes = args.parse_args()

    video = cv2.VideoCapture(str(opcoes.entrada))
    largura = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    dev = dispositivo()
    recorte = Recorte(dev) if (opcoes.fundo or opcoes.alpha) else None
    fundo = Fundo(opcoes.fundo, largura, altura) if opcoes.fundo else None
    camisa = MascaraCamisa(dev) if opcoes.camisa else None
    if opcoes.alpha:
        saida = codificador_alpha(opcoes.saida, largura, altura, fps)
    else:
        saida = codificador(opcoes.saida, largura, altura, fps, opcoes.entrada)

    n = 0
    while True:
        ok, quadro = video.read()
        if not ok:
            break
        if camisa:
            quadro = recolorir(quadro, camisa.mascara(quadro), opcoes.camisa)
        if opcoes.alpha:
            a = (recorte.alpha(quadro) * 255).astype(np.uint8)
            quadro = np.dstack([quadro, a])
        elif recorte:
            a = recorte.alpha(quadro)[..., None]
            quadro = (quadro * a + fundo.proximo() * (1 - a)).astype(np.uint8)
        saida.stdin.write(quadro.tobytes())
        n += 1
        if n % 30 == 0:
            print(f"{n}/{total}", flush=True)
    saida.stdin.close()
    saida.wait()
    print(f"pronto: {opcoes.saida}")


if __name__ == "__main__":
    main()
