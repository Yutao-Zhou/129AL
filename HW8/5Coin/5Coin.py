import numpy as np
import matplotlib.pyplot as plt

#part a
def coin():
    c=np.random.randint(2, size=100)
    global h
    h=0
    for i in range (100):
        d=c[i]
        if d==1:
                h=h+1
def gas(x):
    G=[]
    mu=np.mean(x)
    di=np.std(x)
    x=np.arange(0,100)
    for i in x:
        G.append(np.exp(-(i-mu)**2/(2*di**2))/(di*((2*np.pi)**0.5)))
    return G

coin()
print('The number of head in 100 tosses is: ',h)
#part b
hi=[]
for i in range (1000):
    coin()
    hi.append(h)
x=hi[:]
bins=np.linspace(1,100,100)

plt.hist(x,bins,density=True)
plt.xlabel('Number of heads thrown')
plt.ylabel('Probability dencity (%)')
plt.title('The Probability Of Different Number Of Heads Thrown')

#part c
Ga=gas(x)
x=np.arange(0,100)
plt.plot(x,Ga,'orangered')
plt.legend(['Gaussian Distribution','Coin Flip'])
plt.savefig('plot.png')