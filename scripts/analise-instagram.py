"""Entrada compatível com prompts/codex-analise-instagram.md."""
from pathlib import Path
import os
import sys
base=Path(__file__).resolve().parents[1]/'ferramentas/instagram-mcp'
python=base/'.venv/bin/python'
if not python.exists():
    sys.exit('Instale ferramentas/instagram-mcp conforme README.md antes de executar.')
os.execv(str(python),[str(python),str(base/'coletar.py'),*sys.argv[1:]])
