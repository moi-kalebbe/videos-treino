import sys, shutil
from gradio_client import Client
import os, pathlib
env = pathlib.Path("/Users/moiseskalebbe/Meus Projetos do GitHub/00 - Todos os projetos/videos-treino/.env")
tok = next((l.split("=",1)[1].strip() for l in env.read_text().splitlines() if l.startswith("HF_TOKEN=")), None)
c = Client("mcp-tools/FLUX.1-Krea-dev", verbose=False, token=tok)
saida, prompt = sys.argv[1], sys.argv[2]
r = c.predict(prompt=prompt, seed=7, randomize_seed=False, width=768, height=1344, guidance_scale=4.5, num_inference_steps=28, api_name="/infer")
img = r[0]["path"] if isinstance(r[0], dict) else r[0]
shutil.copy(img, saida); print("ok", saida)
