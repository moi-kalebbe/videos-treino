"""Renderiza o piloto vertical de Lições para a Vida com uma narração pronta."""

from __future__ import annotations

import argparse
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1080
HEIGHT = 1920
FPS = 24
DURATION = 25.8
BACKGROUND = "#F6F1E8"
INK = "#17243A"
MUTED = "#68717D"
ORANGE = "#C9503B"
TEAL = "#157D78"
FONT_REGULAR = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/seguisb.ttf")
FONT_SERIF = Path("C:/Windows/Fonts/georgia.ttf")


def ease(value: float) -> float:
    progress = max(0.0, min(1.0, value))
    return 1 - (1 - progress) ** 3


def between(time: float, start: float, end: float) -> float:
    return ease((time - start) / (end - start))


def font(size: int, *, bold: bool = False, serif: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_SERIF if serif else FONT_BOLD if bold else FONT_REGULAR
    return ImageFont.truetype(str(path), size)


def centered(draw: ImageDraw.ImageDraw, text: str, y: int, size: int, color: str,
             *, bold: bool = False, serif: bool = False) -> None:
    face = font(size, bold=bold, serif=serif)
    bounds = draw.textbbox((0, 0), text, font=face)
    x = (WIDTH - (bounds[2] - bounds[0])) / 2
    draw.text((x, y), text, font=face, fill=color)


def label(draw: ImageDraw.ImageDraw, text: str, y: int, color: str = MUTED) -> None:
    centered(draw, text, y, 31, color, bold=True)


def base_frame(time: float) -> Image.Image:
    frame = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(frame)
    for x in range(0, WIDTH, 108):
        draw.line((x, 0, x, HEIGHT), fill="#E8E4DC", width=1)
    for y in range(0, HEIGHT, 108):
        draw.line((0, y, WIDTH, y), fill="#E8E4DC", width=1)
    draw.rounded_rectangle((64, 72, 274, 126), radius=27, fill=INK)
    draw.text((91, 82), "LIÇÕES / 01", font=font(26, bold=True), fill="white")
    draw.text((814, 84), "ESCOLHA", font=font(25, bold=True), fill=INK)
    draw.rounded_rectangle((64, 1812, 1016, 1822), radius=5, fill="#D7D4CB")
    draw.rounded_rectangle((64, 1812, 64 + int(952 * time / DURATION), 1822),
                           radius=5, fill=TEAL)
    return frame


def draw_character(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float,
                   mood: str = "neutral") -> None:
    def box(coords: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return tuple(int(origin + offset * scale) for origin, offset in
                     zip((x, y, x, y), coords))

    draw.ellipse(box((-150, 315, 150, 680)), fill="#405A65")
    draw.rounded_rectangle(box((-115, 45, 115, 350)), radius=int(92 * scale),
                           fill="#DBA879")
    draw.pieslice(box((-128, 5, 128, 210)), 180, 355, fill=INK)
    draw.ellipse(box((-60, 194, -44, 210)), fill=INK)
    draw.ellipse(box((42, 194, 58, 210)), fill=INK)
    if mood == "angry":
        draw.line(box((-42, 267, 42, 244)), fill=INK, width=max(2, int(8 * scale)))
        draw.line(box((-81, 172, -30, 184)), fill=INK, width=max(2, int(9 * scale)))
        draw.line(box((30, 184, 81, 172)), fill=INK, width=max(2, int(9 * scale)))
    else:
        draw.arc(box((-42, 236, 42, 285)), 15, 165, fill=INK,
                 width=max(2, int(7 * scale)))
    draw.ellipse(box((-150, 430, -100, 570)), fill="#DBA879")
    draw.ellipse(box((100, 430, 150, 570)), fill="#DBA879")


def draw_phone(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float = 1.0,
               message: bool = True) -> None:
    w, h = int(490 * scale), int(685 * scale)
    draw.rounded_rectangle((x + 20, y + 20, x + w + 20, y + h + 20),
                           radius=int(50 * scale), fill="#17243A33")
    draw.rounded_rectangle((x, y, x + w, y + h), radius=int(50 * scale),
                           fill=INK)
    inset = int(17 * scale)
    draw.rounded_rectangle((x + inset, y + inset, x + w - inset, y + h - inset),
                           radius=int(38 * scale), fill="#FFFDF9")
    draw.rounded_rectangle((x + int(160 * scale), y + int(22 * scale),
                            x + int(330 * scale), y + int(48 * scale)),
                           radius=12, fill=INK)
    if message:
        draw.text((x + int(48 * scale), y + int(112 * scale)), "11:42 · MENSAGEM",
                  font=font(int(25 * scale), bold=True), fill=MUTED)
        draw.rounded_rectangle((x + int(44 * scale), y + int(190 * scale),
                                x + w - int(44 * scale), y + int(390 * scale)),
                               radius=int(30 * scale), fill="#EEEAE4")
        draw.text((x + int(72 * scale), y + int(228 * scale)), "Você errou",
                  font=font(int(43 * scale), bold=True), fill=INK)
        draw.text((x + int(72 * scale), y + int(292 * scale)), "de novo.",
                  font=font(int(43 * scale), bold=True), fill=INK)
        draw.rounded_rectangle((x + int(44 * scale), y + int(502 * scale),
                                x + w - int(44 * scale), y + int(598 * scale)),
                               radius=int(32 * scale), outline="#C7C9C9", width=3)
        draw.text((x + int(75 * scale), y + int(520 * scale)), "Responder...",
                  font=font(int(30 * scale)), fill=MUTED)


def opening(frame: Image.Image, time: float) -> None:
    draw = ImageDraw.Draw(frame)
    rise = int(90 * (1 - between(time, 0, 0.8)))
    label(draw, "UMA SITUAÇÃO COMUM", 320 + rise)
    centered(draw, "UMA MENSAGEM.", 420 + rise, 91, INK, bold=True)
    centered(draw, "DUAS RESPOSTAS.", 540 + rise, 91, TEAL, bold=True)
    draw_character(draw, 540, 850 + rise, 0.95)
    draw.rounded_rectangle((755, 1140, 956, 1260), radius=36, fill="white",
                           outline="#E0D7C9", width=4)
    draw.text((794, 1164), "• • •", font=font(45, bold=True), fill=ORANGE)


def notification(frame: Image.Image, time: float) -> None:
    draw = ImageDraw.Draw(frame)
    label(draw, "AQUELA MENSAGEM", 314)
    draw_phone(draw, 295, 460 + int(170 * (1 - between(time, 3.2, 4.2))))
    centered(draw, "chega na hora errada.", 1280, 59, INK, serif=True)
    draw.ellipse((90, 585, 252, 747), outline=ORANGE, width=11)
    draw.text((144, 612), "!", font=font(105, bold=True), fill=ORANGE)


def impulse(frame: Image.Image, time: float) -> None:
    draw = ImageDraw.Draw(frame)
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill="#F0D8CE")
    draw_character(draw, 540, 760, 1.15, mood="angry")
    label(draw, "PRIMEIRA REAÇÃO", 290, ORANGE)
    centered(draw, "RESPONDER", 390, 111, INK, bold=True)
    centered(draw, "NA HORA.", 510, 111, ORANGE, bold=True)
    for index in range(4):
        spread = 26 * math.sin(time * 7 + index)
        x = 180 + index * 235
        draw.line((x, 1490, x + spread, 1560), fill=ORANGE, width=12)


def choice(frame: Image.Image, time: float) -> None:
    draw = ImageDraw.Draw(frame)
    label(draw, "ENTRE O FATO E A RESPOSTA", 295)
    centered(draw, "EXISTE UM INSTANTE.", 390, 71, INK, bold=True)
    draw.rounded_rectangle((58, 625, 526, 1475), radius=48, fill="#F1D8CE")
    draw.rounded_rectangle((554, 625, 1022, 1475), radius=48, fill="#D7EBE5")
    draw_character(draw, 292, 870, 0.58, mood="angry")
    draw_character(draw, 788, 870, 0.58)
    draw.text((112, 700), "01 / IMPULSO", font=font(38, bold=True), fill=ORANGE)
    draw.text((606, 700), "02 / PAUSA", font=font(38, bold=True), fill=TEAL)
    draw.text((105, 1300), "Reagir", font=font(61, bold=True), fill=INK)
    draw.text((601, 1300), "Escolher", font=font(61, bold=True), fill=INK)
    progress = between(time, 11.5, 13.1)
    draw.rounded_rectangle((592, 1510, 984, 1525), radius=8, fill="#B0CCC5")
    draw.rounded_rectangle((592, 1510, 592 + int(392 * progress), 1525),
                           radius=8, fill=TEAL)
    draw.ellipse((765, 1510, 813, 1558), fill=TEAL)


def pause(frame: Image.Image, time: float) -> None:
    draw = ImageDraw.Draw(frame)
    pulse = math.sin(time * 2.5) * 22
    draw.ellipse((155 - pulse, 520 - pulse, 925 + pulse, 1290 + pulse),
                 outline="#B8D9D1", width=8)
    draw.ellipse((250, 615, 830, 1195), fill="#D7EBE5")
    draw_character(draw, 540, 700, 0.67)
    label(draw, "O SEGUNDO CAMINHO", 285, TEAL)
    centered(draw, "RESPIRA.", 1260, 114, TEAL, bold=True)
    centered(draw, "ESCOLHE.", 1390, 114, INK, bold=True)


def ending(frame: Image.Image, time: float) -> None:
    draw = ImageDraw.Draw(frame)
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=INK)
    draw.ellipse((150, 270, 930, 1050), outline="#347F80", width=5)
    draw.ellipse((260, 380, 820, 940), outline="#347F80", width=3)
    label(draw, "PRA LEVAR COM VOCÊ", 375, "#A9D8CF")
    centered(draw, "VOCÊ PODE", 565, 96, "white", bold=True)
    centered(draw, "ESCOLHER O", 675, 96, "white", bold=True)
    centered(draw, "PRÓXIMO PASSO.", 785, 96, "#81D4BE", bold=True)
    draw.line((262, 1080, 818, 1080), fill="#74B6AC", width=3)
    centered(draw, "Inspiração: Os 7 Hábitos das Pessoas", 1190, 34, "#D7E9E4")
    centered(draw, "Altamente Eficazes · Stephen R. Covey", 1240, 34, "#D7E9E4")
    centered(draw, "LIÇÕES PARA A VIDA", 1610, 32, "#91B8B4", bold=True)


def render_frame(time: float) -> Image.Image:
    frame = base_frame(time)
    if time < 3.2:
        opening(frame, time)
    elif time < 7.2:
        notification(frame, time)
    elif time < 10.8:
        impulse(frame, time)
    elif time < 17.2:
        choice(frame, time)
    elif time < 20.8:
        pause(frame, time)
    else:
        ending(frame, time)
    return frame


def render_video(audio: Path, output: Path, ffmpeg: str) -> None:
    if not audio.is_file():
        raise FileNotFoundError(f"Narração não encontrada: {audio}")
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{WIDTH}x{HEIGHT}",
        "-r", str(FPS), "-i", "-", "-i", str(audio),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-t", str(DURATION), "-movflags", "+faststart", str(output),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    try:
        assert process.stdin is not None
        for index in range(round(DURATION * FPS)):
            process.stdin.write(render_frame(index / FPS).tobytes())
        process.stdin.close()
        if process.wait() != 0:
            raise RuntimeError(f"FFmpeg terminou com código {process.returncode}")
    except Exception:
        process.kill()
        process.wait()
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audio", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--ffmpeg", default="ffmpeg")
    args = parser.parse_args()
    render_video(args.audio, args.output, args.ffmpeg)


if __name__ == "__main__":
    main()
