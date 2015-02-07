import matplotlib.pyplot as plt
import numpy

x=[]

y=[]

readFile = open('co.txt','r')

sepFile = readFile.read().split('\n')

readFile.close()

for plotPair in sepFile:
	XAndY = plotPair.split(',')
	if len(XAndY) > 1:
		x.append(int(XAndY[0]))
		y.append(int(XAndY[1]))
		

plt.title('matplot lib example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x,y)
plt.show()
