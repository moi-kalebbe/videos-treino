from pathlib import Path
import subprocess,json,re
p=Path(__file__).resolve().parent;root=p.parents[1];out=root/'saida';valid=out/'qahtani-v2-validacao';raw=out/'ia-com-precisao-v2-bruto.mp4';final=out/'ia-com-precisao-v2.mp4'
def run(a):return subprocess.run(a,check=True,capture_output=True,text=True)
def measure(f,name):
 r=run(['ffmpeg','-hide_banner','-i',str(f),'-af','loudnorm=I=-14:TP=-2:LRA=11:print_format=json','-f','null','-']);(valid/name).write_text(r.stderr);return json.loads(re.findall(r'\{\s*"input_i".*?\}',r.stderr,re.S)[-1])
mixed=out/'ia-com-precisao-v2-mix.mp4'
run(['ffmpeg','-v','error','-y','-i',str(raw),'-vf','crop=1080:180:0:0','-frames:v','1',str(p/'assets/clipes/cabecalho.png')])
run(['ffmpeg','-v','error','-y','-i',str(raw),'-i',str(p/'assets/audio/efeitos.wav'),'-i',str(p/'assets/clipes/plano-recuperado.mp4'),'-i',str(p/'assets/clipes/cabecalho.png'),'-filter_complex',"[2:v]setpts=PTS-STARTPTS+65/TB[patch];[0:v][patch]overlay=0:180:eof_action=pass:enable='gte(t,65)*lt(t,72.5)'[v0];[v0][3:v]overlay=0:0:enable='gte(t,65)*lt(t,72.5)'[v];[0:a][1:a]amix=inputs=2:normalize=0:duration=first[a]",'-map','[v]','-map','[a]','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','pcm_s16le',str(mixed.with_suffix('.mov'))])
raw=mixed.with_suffix('.mov')
m=measure(raw,'loudness-bruto.txt');flt=f"loudnorm=I=-14:TP=-2:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=false"
run(['ffmpeg','-v','error','-y','-i',str(raw),'-c:v','copy','-af',flt,'-ar','48000','-c:a','aac','-b:a','192k','-movflags','+faststart',str(final)])
print('final',measure(final,'loudness-final.txt'),flush=True)
run(['ffmpeg','-v','error','-y','-i',str(final),'-vf','scale=720:1280','-c:v','libx264','-preset','fast','-crf','24','-c:a','copy','-movflags','+faststart',str(out/'ia-com-precisao-v2-celular.mp4')])
run(['ffmpeg','-v','error','-y','-i',str(final),'-vf','fps=1,scale=180:320,tile=6x4','-frames:v','6',str(valid/'final-%02d.jpg')])
run(['ffmpeg','-v','error','-y','-i',str(final),'-frames:v','1',str(valid/'primeiro-quadro.jpg')])
run(['ffmpeg','-v','error','-y','-i',str(final),'-vn','-ar','16000','-ac','1',str(valid/'audio-renderizado.wav')])
print('exportação pronta',flush=True)
