import  numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
plt.rcParams['animation.ffmpeg_path']='M:\\файлы\\ffmpeg-6.0\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'

fig = plt.figure()
l, = plt.plot([],[],'k-')
l2, = plt.plot([],[],'m--')

plt.xlabel('ось x')
plt.ylabel('Ось y ')
plt.title('Синусоида')

plt.xlim(-5, 5)
plt.ylim(-5,5)

def func(x):
    return np.sin(x)*3

def func2(x):
    return np.cos(x)*3

metadata = dict(title='Movie',artist='codinglikemad')
writer = FFMpegWriter(fps=15,metadata=metadata)
# metadata - информация о другой информации

xlist = []
ylist = []
ylist2 = []

with writer.saving(fig,'sinWave.mp4',100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
        ylist2.append(func2(xval))

        l.set_data(xlist,ylist)
        l2.set_data(xlist,ylist2)

        writer.grab_frame()
