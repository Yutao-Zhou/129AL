import numpy as np
import matplotlib.pyplot as plt
#part a


def RT(N):
    yl=[]
    global n
    n=0.001
    x=-20
    r=20
    N=int((r-x)/n)
    for x in np.linspace(x,r,num=N):
        y=np.exp(-x**2)
        yl.append(y)
    
    s=np.sum(yl)
    global area1
    area1=s*n
RT(1000)
print('The total area of the rectangles is: ',area1)
#part b

def MC(N):
    global xx
    global yy
    global ff
    xp=[]
    yp=[]
    yf=[]
    x=-20
    r=20
    global c
    c=0
    for x in np.linspace(x,r,num=N):
           xx=np.random.uniform(x,r,N)
           xp.append(xx)
           ff=[np.exp(-xi**2) for xi in xx]
           yf.append(ff)
           yy=np.random.uniform(0,1.1,N)
           yp.append(yy)
           for i in range(N):
               if yy[i]<ff[i]:
                   c=c+1
                   global area2
                   area2=c*1.1*(r-x)/(N*316)
                    # print('The Result Of Monte Carlo Simulation Is: ',area2)
MC(1000)
plt.plot(xx,yy,'o')
plt.plot(xx,ff,'o')
plt.show()