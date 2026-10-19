from pathlib import Path
import cv2,subprocess,bisect
p=Path(__file__).resolve().parent;root=p.parents[1];source=root/'referencias/_brutos/qahtani-poder-palavras/fonte2.mp4';c=cv2.VideoCapture(str(source));c.set(cv2.CAP_PROP_POS_MSEC,76444.75);cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml');profile=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_profileface.xml');centers=[]
for i in range(225):
 ok,f=c.read()
 if not ok:break
 if i%5:continue
 g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY);boxes=cascade.detectMultiScale(g,1.1,4,minSize=(35,35));boxes=[b for b in boxes if b[1]<300]
 if not boxes:boxes=[b for b in profile.detectMultiScale(g,1.1,4,minSize=(35,35)) if b[1]<300]
 if boxes:
  x,y,w,h=max(boxes,key=lambda b:b[2]*b[3]);centers.append((i/30,x+w/2))
ts=[s[0] for s in centers];lines=[]
for i in range(225):
 t=i/30;j=bisect.bisect_right(ts,t);a=centers[max(j-1,0)];b=centers[min(j,len(centers)-1)];mix=(t-a[0])/(b[0]-a[0]) if b[0]!=a[0] else 0;x=round(a[1]+(b[1]-a[1])*mix-160);x=max(0,min(960,x));lines.append(f'{t:.6f} crop x {x};')
(p/'patch-pan.txt').write_text('\n'.join(lines))
subprocess.run(['ffmpeg','-v','error','-y','-ss','76.44475','-i',str(source),'-t','7.5','-vf',f'sendcmd=f={p}/patch-pan.txt,crop=320:400:400:0,scale=1080:1350,crop=1080:1290:0:60,setsar=1','-an','-r','30','-c:v','libx264','-preset','fast','-crf','20',str(p/'assets/clipes/plano-recuperado.mp4')],check=True)
