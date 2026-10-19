from pathlib import Path
import json,math,random,wave,array
p=Path(__file__).resolve().parent;t=json.loads((p/'timeline.json').read_text());W=t['words'];r=48000;audio=array.array('h',[0])*int((t['total']+.1)*r)
def cue(word,start):return next(x['s'] for x in W if x['s']>=start and x['w'].lower().strip('.,?!:')==word)
random.seed(7)
def effect(at,kind):
 duration=.10 if kind=='click' else .28
 for i in range(int(duration*r)):
  x=i/r;env=math.exp(-x*65) if kind=='click' else math.sin(math.pi*x/duration)**2
  v=(math.sin(2*math.pi*820*x)*.04+random.uniform(-1,1)*.012) if kind=='click' else random.uniform(-1,1)*.012
  idx=int(at*r)+i
  audio[idx]=max(-32768,min(32767,audio[idx]+int(v*env*32767)))
q=t['starts'][1];pp=t['starts'][2]
effect(cue('aprova',q),'click');effect(cue('custo',q)-.3,'paper')
for w in ['conferidos','cálculo','aprovar']:effect(cue(w,pp),'click')
with wave.open(str(p/'assets/audio/efeitos.wav'),'w') as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(r);f.writeframes(audio.tobytes())
