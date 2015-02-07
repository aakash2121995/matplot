import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
gr1 = fig.add_subplot(1,1,1)

def animate(i):
	pullData = open('co.txt','r').read()
	dataArray = pullData.split('\n')
	xar = []
	yar = []
	for eachline in dataArray:
		if len(eachline)>1:
			x,y = eachline.split(',')
			xar.append(int(x))
			yar.append(int(y))
	gr1.clear()
	gr1.plot(xar,yar)
ani = animation.FuncAnimation(fig,animate, interval = 1000)
plt.show()	
	
