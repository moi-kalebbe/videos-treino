"""Teste local do LTX-Video 2B destilado (0.9.8) no Mac (MPS).

Uso:
  python gerar.py texto  "<prompt>"     # etapa 1: T5 codifica o prompt e sai da memória
  python gerar.py video  saida.mp4      # etapa 2: gera o vídeo a partir dos embeddings
"""
import sys
import time
import resource
from pathlib import Path

import torch

AQUI = Path(__file__).parent
EMB = AQUI / "prompt.pt"
REPO = "Lightricks/LTX-Video"
PESOS = "ltxv-2b-0.9.8-distilled.safetensors"
T5 = "city96/t5-v1_1-xxl-encoder-bf16"
DISPOSITIVO = "mps"
DTYPE = torch.bfloat16


def pico_gb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9  # macOS: bytes


def codificar(prompt: str) -> None:
    from transformers import AutoTokenizer, T5EncoderModel

    tok = AutoTokenizer.from_pretrained(REPO, subfolder="tokenizer")
    t5 = T5EncoderModel.from_pretrained(T5, torch_dtype=DTYPE).to(DISPOSITIVO)
    ids = tok(prompt, padding="max_length", max_length=128, truncation=True, return_tensors="pt")
    with torch.no_grad():
        emb = t5(ids.input_ids.to(DISPOSITIVO), attention_mask=ids.attention_mask.to(DISPOSITIVO))[0]
    torch.save({"emb": emb.cpu(), "mask": ids.attention_mask}, EMB)
    print(f"prompt codificado · pico de memória {pico_gb():.1f} GB")


def gerar(saida: str, largura=int(__import__("os").environ.get("LARG", 512)), altura=int(__import__("os").environ.get("ALT", 768)), quadros=int(__import__("os").environ.get("QUADROS", 97))) -> None:
    from diffusers import AutoencoderKLLTXVideo, LTXConditionPipeline, LTXVideoTransformer3DModel
    from diffusers.utils import export_to_video
    from huggingface_hub import hf_hub_download

    caminho = hf_hub_download(REPO, PESOS)
    transformer = LTXVideoTransformer3DModel.from_single_file(caminho, torch_dtype=DTYPE)
    vae = AutoencoderKLLTXVideo.from_single_file(caminho, torch_dtype=DTYPE)
    pipe = LTXConditionPipeline.from_pretrained(
        REPO, transformer=transformer, vae=vae, text_encoder=None, tokenizer=None, torch_dtype=DTYPE
    ).to(DISPOSITIVO)
    from diffusers import FlowMatchEulerDiscreteScheduler
    pipe.scheduler = FlowMatchEulerDiscreteScheduler.from_config(pipe.scheduler.config, use_dynamic_shifting=False)
    pipe.vae.enable_tiling()

    dados = torch.load(EMB)
    import os
    extra = {}
    if os.environ.get("IMAGEM"):
        from diffusers.pipelines.ltx.pipeline_ltx_condition import LTXVideoCondition
        from diffusers.utils import load_image
        img = load_image(os.environ["IMAGEM"]).resize((largura, altura))
        extra["conditions"] = [LTXVideoCondition(image=img, frame_index=0)]
    inicio = time.time()
    video = pipe(
        prompt_embeds=dados["emb"].to(DISPOSITIVO, DTYPE),
        prompt_attention_mask=dados["mask"].to(DISPOSITIVO),
        width=largura,
        height=altura,
        num_frames=quadros,
        timesteps=[1000, 993, 987, 981, 975, 909, 725, 0.03],
        guidance_scale=1.0,
        decode_timestep=0.05,
        decode_noise_scale=0.025,
        generator=torch.Generator().manual_seed(42),
        **extra,
    ).frames[0]
    export_to_video(video, saida, fps=24)
    print(f"vídeo {saida} · {quadros} quadros {largura}x{altura} · {time.time() - inicio:.0f} s · pico {pico_gb():.1f} GB")


if __name__ == "__main__":
    etapa, arg = sys.argv[1], sys.argv[2]
    codificar(arg) if etapa == "texto" else gerar(arg)
