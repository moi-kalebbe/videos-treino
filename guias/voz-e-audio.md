# Voz e áudio (regras para todos os estilos)

Aprendido na produção do case Chewy (18/10/2026). Vale para qualquer vídeo.

## Voz
- Voz: **clone do Moisés** `aORS9tvW5qcMM0bnzsRU`, modelo `eleven_multilingual_v2`.
- Configuração aprovada (amostra A): `stability 0.45 · similarity_boost 0.85 · style 0.25 · use_speaker_boost` (padrão do `scripts/narracao.py`).
- **Gerar sempre pelo nosso script** (`python3 scripts/narracao.py <falas.txt> <assets> --voz aORS9tvW5qcMM0bnzsRU`). O nó de TTS do ElevenLabs Flows usa configuração padrão e o "IA" soou robótico.
- **"IA" se escreve "IA"** (normal, junto). Não separar, não escrever "I.A.".
- **Uma fala por linha**: o script gera cada fala separada e junta com **silêncio real de 0,5 s**. **Nunca usar `<break>`**: dentro da pausa o modelo inventa palavras ("falas fantasmas") e cria espaçamento estranho.
- Sigla que a voz pronuncia mal: `{PwC|pê dáblio cê}` no `falas.txt` (legenda mostra a sigla, voz fala a pronúncia).
- Trecho falado pelo avatar: **+0,7 s de silêncio no fim**, senão a última palavra parece cortada.

## Conferência (sempre local, nunca ElevenLabs Scribe)
- Transcrever o áudio final com `whisper-cli` local **em trechos de ~10 s** (no arquivo inteiro o Whisper pula frases).
- Procurar: palavra inventada, nome mal pronunciado, final cortado.

## Mix
- Trilha a ~0,16 de volume sob a voz; efeitos amarrados às palavras (`data-sinc` + `scripts/sincronizar-audio.py`).
- Master final em **-14 LUFS** (`loudnorm=I=-14:TP=-1.5:LRA=11`).
