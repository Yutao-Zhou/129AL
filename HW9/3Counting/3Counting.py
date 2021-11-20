import numpy as np
import matplotlib.pyplot as plt
import scipy.special
#part a
def detection():
    global a
    a=np.random.binomial(1000,0.0045,size=None)
    return a
detection()
print('The total number of detections is: ',a)
#part b
b=[]
b.append(np.random.binomial(1000,0.0045,size=1000))
x=b[:]
bins=np.linspace(1,20,20)
plt.hist(x,bins,density=True)
plt.xlabel('Total number of detections')
plt.ylabel('Probability dencity (%)')
plt.title('The Probability Of Different Number Of Detections')
#part c
def pos(x):
    p=[]
    m=1000*0.0045
    # st=np.std(x)
    x=np.arange(0,20,0.1)
    for i in x:
        p.append((m**i*np.exp(-m))/scipy.special.factorial(i))
    return p
P=pos(x)
x=np.arange(0,20,0.1)
plt.plot(x,P,'orangered')
plt.legend(['Poisson Distribution','Probability Dencity Of Detections'])
plt.savefig('Plot.pdf')