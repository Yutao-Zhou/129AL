import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
#part a
n=1109
na=143
bp=na/n
a=1-bp
sda=np.sqrt(n*bp*a)
print('Part A')
print('The standard deviation of thei distribution is: ',sda)
#part b
sdp=np.sqrt(bp*a)
print('Part B')
print('The standard deviation of thei distribution is: ',sdp)
#part c
sg=(np.sqrt(143*bp*a))**2
b=(1-ss.norm.cdf(42,loc=143*bp,scale=sda))*100
print('Part C')
print('The Probability is: ',b,'%')
#part d
bp1=42/143
a1=1-bp1
sdp1=np.sqrt(bp1*a1)
print('Part D')
print('The Probability is: ',bp1*100,'%')
print('The standard deviation of thei distribution is: ',sdp1)
#part e
c=(143-42)/(1109-101)
a2=1-c
sdp2=np.sqrt(c*a2)
print('Part E')
print('The Probability is: ',c*100,'%')
print('The standard deviation of thei distribution is: ',sdp2)
#part f
x0=np.linspace(0,1,n)
x1=np.linspace(0,1,na)
x2=np.linspace(0,1,n-na)
plt.plot(x0,n*ss.norm.pdf(x0,bp,sg/n), label = 'P')
plt.plot(x1,na*ss.norm.pdf(x1,bp1,sdp1/143), label = 'Pg')
plt.plot(x2,(143-42)*ss.norm.pdf(x2,sdp2/(143-42)), label = 'Pn')
plt.legend(loc = 'upper right')
plt.show()