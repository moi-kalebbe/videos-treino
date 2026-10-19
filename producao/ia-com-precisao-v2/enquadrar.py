from pathlib import Path
import json,subprocess,bisect
p=Path(__file__).resolve().parent;root=p.parents[1]
f=json.loads((p/'faces-v2.json').read_text());ts=[x['t'] for x in f];lines=[]
for k in range(2628):
 t=k/30;j=bisect.bisect_right(ts,t);a=f[max(0,j-1)];b=f[min(len(f)-1,j)]
 delta=b['cx']-a['cx'];mix=(t-a['t'])/(b['t']-a['t']) if b['t']!=a['t'] else 0
 center=a['cx']+delta*mix if abs(delta)<220 else (a['cx'] if mix<.5 else b['cx'])
 x=max(0,min(1056,round(center-432)))
 lines.append(f'{t:.6f} crop x {x};')
(p/'pan.txt').write_text('\n'.join(lines))
subprocess.run(['ffmpeg','-v','error','-y','-i',str(root/'referencias/_brutos/qahtani-poder-palavras/trecho-v2-fontes.mp4'),'-vf',f'sendcmd=f={p}/pan.txt,crop=864:1080:528:0,setsar=1','-an','-r','30','-c:v','libx264','-preset','fast','-crf','20','-g','30',str(p/'assets/clipes/palestra.mp4')],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(p/'assets/clipes/palestra.mp4'),'-vf','scale=180:226,boxblur=6','-an','-c:v','libx264','-preset','fast','-crf','28','-g','30',str(p/'assets/clipes/ambiente.mp4')],check=True)
