"""Tira fiapos e pelos claros da camisa escura do avatar (imagem ou vídeo), sem perder a textura do tecido.

Roda local, sem crédito. A máscara da camisa vem do SegFormer, o mesmo de avatar_variacoes.py.

Uso (venv em ~/.cache/avatar-tools):
  ~/.cache/avatar-tools/.venv/bin/python scripts/limpar_camisa.py entrada.(jpg|png|mp4) saida.(jpg|png|mp4) [--forca 12]
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import torch  # noqa: E402

from avatar_variacoes import MascaraCamisa, dispositivo  # noqa: E402

# do umbigo para cima a polo às vezes sai como "Dress" (7) em vez de "Upper-clothes" (4)
CLASSES_ROUPA = (4, 7)


class MascaraRoupa(MascaraCamisa):
    @torch.no_grad()
    def mascara(self, bgr: np.ndarray) -> np.ndarray:
        entrada = self.proc(images=bgr[..., ::-1].copy(), return_tensors="pt").to(self.dev)
        logits = torch.nn.functional.interpolate(self.rede(**entrada).logits, size=bgr.shape[:2], mode="bilinear", align_corners=False)[0]
        rotulo = logits.argmax(0).cpu().numpy()
        roupa = np.isin(rotulo, CLASSES_ROUPA).astype(np.float32)
        return cv2.GaussianBlur(roupa, (0, 0), 2.5)

VIDEO = {".mp4", ".mov", ".m4v", ".webm"}


def limpar(bgr: np.ndarray, mascara: np.ndarray, forca: float) -> np.ndarray:
    """Troca só os pontos bem mais claros que a vizinhança (fiapo) pela mediana local, dentro da camisa."""
    escala = max(1, round(bgr.shape[1] / 1080))
    resultado = bgr.copy()
    dentro = (mascara > 0.4).astype(np.uint8)
    for k in (5 * escala | 1, 11 * escala | 1):  # fiapo fino e médio (maior que isso apaga botão e costura)
        mediana = cv2.medianBlur(resultado, k)
        cinza = cv2.cvtColor(resultado, cv2.COLOR_BGR2GRAY).astype(np.float32)
        cinza_med = cv2.cvtColor(mediana, cv2.COLOR_BGR2GRAY).astype(np.float32)
        fiapo = ((cinza - cinza_med) > forca).astype(np.uint8) & dentro
        fiapo = cv2.dilate(fiapo, np.ones((3, 3), np.uint8), iterations=escala)
        peso = np.clip(cv2.GaussianBlur(fiapo.astype(np.float32), (0, 0), 1.0 * escala) * 2.5, 0, 1)[..., None]
        resultado = (resultado * (1 - peso) + mediana * peso).astype(np.uint8)
    return resultado


def imagem(entrada: Path, saida: Path, forca: float) -> None:
    bgr = cv2.imread(str(entrada))
    mascara = MascaraRoupa(dispositivo()).mascara(bgr)
    cv2.imwrite(str(saida), limpar(bgr, mascara, forca), [cv2.IMWRITE_JPEG_QUALITY, 96])


def video(entrada: Path, saida: Path, forca: float) -> None:
    cap = cv2.VideoCapture(str(entrada))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    largura, altura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    ff = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{largura}x{altura}", "-r", str(fps),
         "-i", "-", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(saida)],
        stdin=subprocess.PIPE,
    )
    mascaras = MascaraRoupa(dispositivo())
    while True:
        ok, bgr = cap.read()
        if not ok:
            break
        ff.stdin.write(limpar(bgr, mascaras.mascara(bgr), forca).tobytes())
    ff.stdin.close()
    ff.wait()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("entrada", type=Path)
    p.add_argument("saida", type=Path)
    p.add_argument("--forca", type=float, default=11, help="quanto mais claro que a vizinhança vira fiapo (menor = limpa mais)")
    a = p.parse_args()
    (video if a.entrada.suffix.lower() in VIDEO else imagem)(a.entrada, a.saida, a.forca)
    print(f"pronto: {a.saida}")


if __name__ == "__main__":
    main()
