import matplotlib.pyplot as plt
import numpy

x=[]
y=[]
readFile = open('co.txt','r')

sepFile = readFile.read().split('\n')

readFile.close()

fig = plt.figure()

rect = fig.patch

rect.set_facecolor('#12322e')


for plotPair in sepFile:
	XAndY = plotPair.split(',')
	if len(XAndY) > 1:
		x.append(int(XAndY[0]))
		y.append(int(XAndY[1]))
		
ax1 = fig.add_subplot(1,1,1, axisbg = 'grey')

ax1.plot(x,y,'c',linewidth = 2.5)

ax1.tick_params(axis = 'x',colors = 'c')
ax1.tick_params(axis = 'y',colors = 'c')

ax1.spines['bottom'].set_color('w')
ax1.spines['top'].set_color('w')
ax1.spines['left'].set_color('w')
ax1.spines['right'].set_color('w')

ax1.yaxis.label.set_color('c')
ax1.xaxis.label.set_color('c')

ax1.set_title('matplot lib example',color = 'c')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
#plt.plot(x,y)
plt.show()
