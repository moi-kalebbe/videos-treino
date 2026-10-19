from pathlib import Path
import json,re,subprocess,shutil
p=Path(__file__).resolve().parent; root=p.parent.parent
run=lambda a:subprocess.run(a,check=True)
def readjs(path,key): return json.loads(re.search(r'window\.'+key+r' = (.*?);',path.read_text()).group(1))
js=p/'assets/legenda.js'; W=readjs(js,'LEGENDA'); C=readjs(js,'CENAS'); dub=root/'producao/gancho-qahtani/dublagem/beto/assets'; D=readjs(dub/'legenda.js','LEGENDA'); cut=2.358; dubdur=6.212109; split=C[1]; total=64.629+dubdur+1.2
shutil.copy(p/'assets/audio/narracao.mp3',p/'assets/audio/narracao-moises.mp3')
run(['ffmpeg','-v','error','-y','-i',str(dub/'audio/narracao.mp3'),'-i',str(p/'assets/audio/narracao-moises.mp3'),'-filter_complex',f'[0:a]asplit[x][y];[x]atrim=0:{cut},asetpts=PTS-STARTPTS[a];[1:a]asplit[u][v];[u]atrim=0:{split},asetpts=PTS-STARTPTS[b];[y]atrim=start={cut},asetpts=PTS-STARTPTS[c];[v]atrim=start={split},asetpts=PTS-STARTPTS[d];[a][b][c][d]concat=n=4:v=0:a=1[out]','-map','[out]','-c:a','pcm_s16le',str(p/'assets/audio/master.wav')])
words=[dict(w=w['w'],s=w['s']+(cut if w['s']<split else dubdur),e=w['e']+(cut if w['s']<split else dubdur)) for w in W]+[dict(w=w['w'],s=w['s']+(0 if w['s']<cut else split),e=w['e']+(0 if w['s']<cut else split)) for w in D];words.sort(key=lambda w:w['s'])
starts=[0,cut,cut+split]+[c+dubdur for c in C[1:]]; ends=starts[1:]+[total]
(p/'timeline.json').write_text(json.dumps(dict(words=words,starts=starts,ends=ends,total=total),ensure_ascii=False))
for i,(s,e) in enumerate(zip(starts,ends)):
 target=p/f'assets/clipes/bg{i}.mp4'
 if i<3:
  source=root/'referencias/_brutos/qahtani-poder-palavras/original-1080p.mp4'; ss=[43.0,48.52,88.0][i]
  filt='[0:v]split[a][b];[a]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,boxblur=18:2,eq=brightness=-0.18[bg];[b]scale=720:-2[fg];[bg][fg]overlay=0:300,setsar=1[out]'
  run(['ffmpeg','-v','error','-y','-ss',str(ss),'-i',str(source),'-t',str(e-s),'-filter_complex',filt,'-map','[out]','-an','-r','30','-c:v','libx264','-preset','fast','-crf','21',str(target)])
 else:
  name=['reuniao','reuniao2','celular','msg','reuniao2','fone','reuniao','reuniao2','reuniao','fone'][i-3]
  source=root/f'producao/caso-movida/assets/broll/{name}.mp4'
  run(['ffmpeg','-v','error','-y','-stream_loop','-1','-i',str(source),'-t',str(e-s),'-vf','scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1','-an','-r','30','-c:v','libx264','-preset','fast','-crf','23',str(target)])
print('timeline e mídia prontas',total)
