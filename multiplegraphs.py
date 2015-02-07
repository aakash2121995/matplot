import matplotlib.pyplot as plt
import numpy

x=[]
y=[]

x2=[]
y2=[]

readFile = open('co.txt','r')
readFile2 = open('co2.txt','r')

sepFile = readFile.read().split('\n')

readFile.close()

sepFile2 = readFile2.read().split('\n')

readFile2.close()

fig = plt.figure()

rect = fig.patch

rect.set_facecolor('#12322e')


for plotPair in sepFile:
	XAndY = plotPair.split(',')
	if len(XAndY) > 1:
		x.append(int(XAndY[0]))
		y.append(int(XAndY[1]))

for plotPair in sepFile2:
	XAndY = plotPair.split(',')
	if len(XAndY) > 1:
		x2.append(int(XAndY[0]))
		y2.append(int(XAndY[1]))
		
ax1 = fig.add_subplot(2,2,1, axisbg = 'grey')

ax1.plot(x,y,'c',linewidth = 2.5)

ax1.tick_params(axis = 'x',colors = 'c')
ax1.tick_params(axis = 'y',colors = 'c')

ax1.spines['bottom'].set_color('w')
ax1.spines['top'].set_color('w')
ax1.spines['left'].set_color('w')
ax1.spines['right'].set_color('w')

ax1.yaxis.label.set_color('c')
ax1.xaxis.label.set_color('c')

ax1.set_title('matplot lib example 1',color = 'c')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')




ax2 = fig.add_subplot(2,2,2, axisbg = 'grey')

ax2.plot(x2,y2,'c',linewidth = 2.5)

ax2.tick_params(axis = 'x',colors = 'c')
ax2.tick_params(axis = 'y',colors = 'c')

ax2.spines['bottom'].set_color('w')
ax2.spines['top'].set_color('w')
ax2.spines['left'].set_color('w')
ax2.spines['right'].set_color('w')

ax2.yaxis.label.set_color('c')
ax2.xaxis.label.set_color('c')

ax2.set_title('matplot lib example 2',color = 'c')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')


ax3 = fig.add_subplot(2,1,2, axisbg = 'grey')

ax3.plot(x2,y2,'c',linewidth = 2.5)

ax3.tick_params(axis = 'x',colors = 'c')
ax3.tick_params(axis = 'y',colors = 'c')

ax3.spines['bottom'].set_color('w')
ax3.spines['top'].set_color('w')
ax3.spines['left'].set_color('w')
ax3.spines['right'].set_color('w')

ax3.yaxis.label.set_color('c')
ax3.xaxis.label.set_color('c')

ax3.set_title('matplot lib example 3',color = 'c')
ax3.set_xlabel('X axis')
ax3.set_ylabel('Y axis')

#plt.plot(x,y)
plt.show()
