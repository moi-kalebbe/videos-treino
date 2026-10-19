import cv2,json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
source=str(root/'referencias/_brutos/qahtani-poder-palavras/trecho-v2-fontes.mp4')
c=cv2.VideoCapture(source);cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
profile=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_profileface.xml');samples=[]
for i in range(176):
 t=i*.5;c.set(cv2.CAP_PROP_POS_MSEC,t*1000);ok,frame=c.read()
 if not ok:break
 small=cv2.resize(frame,(960,540));gray=cv2.cvtColor(small,cv2.COLOR_BGR2GRAY)
 boxes=cascade.detectMultiScale(gray,1.1,5,minSize=(25,25))
 if len(boxes)==0:boxes=profile.detectMultiScale(gray,1.1,4,minSize=(25,25))
 boxes=[(x,y,w,h) for x,y,w,h in boxes if y<330]
 if boxes:
  x,y,w,h=max(boxes,key=lambda b:b[2]*b[3]);samples.append({'t':i*.5,'cx':int((x+w/2)*2),'y':int(y*2),'w':int(w*2)})
(root/'producao/ia-com-precisao-v2/faces-v2.json').write_text(json.dumps(samples));print('faces',len(samples),flush=True)
