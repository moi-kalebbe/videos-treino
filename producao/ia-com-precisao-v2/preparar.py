from pathlib import Path
import json,re,subprocess,shutil
p=Path(__file__).resolve().parent; root=p.parent.parent
run=lambda a:subprocess.run(a,check=True)
def read(n,k):return json.loads(re.search(r'window\.'+k+r' = (.*?);',(p/n).read_text()).group(1))
def dur(f):return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
(p/'assets/audio').mkdir(parents=True,exist_ok=True);(p/'assets/clipes').mkdir(exist_ok=True)
D=read('dub/legenda.js','LEGENDA'); C=read('dub/legenda.js','CENAS'); W=read('voz/legenda.js','LEGENDA'); V=read('voz/legenda.js','CENAS')
# Preserve all source footage, 42.1–129.7. Translation windows follow original paragraphs.
start=42.1; end=129.7; speech=end-start
windows=[(42.1,44.6),(46.2,59.0),(63.5,79.0),(80.5,93.1),(99.6,105.4),(109.0,116.7),(116.9,129.3)]
filters=[];labels=[]; words=[]
segments=[]
for j,(a,b) in enumerate(windows):
 ws=[x for x in D if x['s']>=C[j]-.001 and (j==len(C)-1 or x['s']<C[j+1]-.001)]
 if j==3:
  for lo,hi,aa,bb in [(0,7,80.5,83.8),(7,11,84.9,86.7),(11,16,87.1,89.7),(16,len(ws),90.4,92.5)]:segments.append((ws[lo:hi],aa,bb))
 else:segments.append((ws,a,b))
for i,(ws,a,b) in enumerate(segments):
 s=ws[0]['s'];e=ws[-1]['e']+.06;target=b-a;rate=max(.85,(e-s)/target)
 filters.append(f'[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,atempo={rate},adelay={round((a-start)*1000)}:all=1[d{i}]');labels.append(f'[d{i}]')
 words.extend(dict(w=x['w'],s=(x['s']-s)/rate+a-start,e=(x['e']-s)/rate+a-start,who='speaker') for x in ws)
filters.append(f"{''.join(labels)}amix=inputs={len(segments)}:normalize=0,apad,atrim=0:{speech}[dub]")
# Original room reactions only; original speech kept inaudible under the dub.
filters.append(f"[1:a]atrim={start}:{end},asetpts=PTS-STARTPTS,volume='if(between(t,17.2,21.2)+between(t,51.0,57.2)+between(t,63.5,66.7),0.38,0)':eval=frame[room]")
filters.append('[dub][room]amix=inputs=2:normalize=0[a]')
run(['ffmpeg','-v','error','-y','-i',str(p/'dub/audio/narracao.mp3'),'-i',str(root/'referencias/_brutos/qahtani-poder-palavras/original-1080p.mp4'),'-filter_complex',';'.join(filters),'-map','[a]','-ar','48000',str(p/'assets/audio/palestra.wav')])
vd=dur(p/'voz/audio/narracao.mp3'); total=speech+vd+1.1
run(['ffmpeg','-v','error','-y','-i',str(p/'assets/audio/palestra.wav'),'-i',str(p/'voz/audio/narracao.mp3'),'-filter_complex','[0:a][1:a]concat=n=2:v=0:a=1,apad=pad_dur=1.1[out]','-map','[out]','-ar','48000',str(p/'assets/audio/master.wav')])
words.extend(dict(w=x['w'],s=x['s']+speech,e=x['e']+speech,who='moises') for x in W)
(p/'timeline.json').write_text(json.dumps(dict(words=words,bridge=speech,starts=[v+speech for v in V],total=total),ensure_ascii=False))
import sys
if '--audio-only' in sys.argv:sys.exit(0)
# Manual pan follows the recorded camera positions, preserving full image height.
centers=[1140,1335,1145,1285,1150,1100,1020,1010,750,920,800,1025,1205,1265,1075,1075,950,1200,1125,1075,925,925,1050]
expr=str(centers[-1]-432)
for i in range(len(centers)-2,-1,-1):
 x=centers[i]-432; delta=centers[i+1]-centers[i]
 expr=f'if(lt(t,{(i+1)*4}),{x}+({delta})*(t-{i*4})/4,{expr})'
source=root/'referencias/_brutos/qahtani-poder-palavras/original-1080p.mp4'
run(['ffmpeg','-v','error','-y','-ss',str(start),'-i',str(source),'-t',str(speech),'-vf',f"crop=864:1080:x='{expr}':y=0,scale=864:1080,setsar=1",'-an','-r','30','-c:v','libx264','-preset','fast','-crf','20',str(p/'assets/clipes/palestra.mp4')])
# A real desk/phone video remains moving behind the authored motion.
run(['ffmpeg','-v','error','-y','-stream_loop','-1','-i',str(root/'producao/caso-movida/assets/broll/celular.mp4'),'-t',str(vd+1.1),'-vf','scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280','-an','-c:v','libx264','-preset','fast','-crf','24',str(p/'assets/clipes/mesa.mp4')])
shutil.copy(root/'producao/ia-com-precisao/assets/audio/trilha.mp3',p/'assets/audio/trilha.mp3')
print('seconds',total,'bridge',speech)
