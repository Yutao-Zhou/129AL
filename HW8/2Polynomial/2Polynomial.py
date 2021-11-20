import numpy as np
import matplotlib.pyplot as plt
while True:
    N=input ("Enter integer: ")
    try:
        N=int(N)
        assert N>0
    except ValueError:
            print("Your input was not a number, or it is not a integer. Try again!")
    except AssertionError:
            print("Your input was not greater than 0, try again!")
    else:
        break
    
rng = np.random.default_rng()
p=1000*rng.random((N,2))+0
x=p[:,0]
y=p[:,1]
print(p)

fit1=np.polyfit(x,y,1)               
yf1=np.polyval(fit1,x)
xf1=np.linspace(np.min(x),np.max(x),1000)
yf1 = np.polyval(fit1,xf1)

fit2=np.polyfit(x,y,N-1)               
yf2=np.polyval(fit2,x)
xf2=np.linspace(np.min(x),np.max(x),1000)
yf2 = np.polyval(fit2,xf2)

fit3=np.polyfit(x,y,N-3)               
yf3=np.polyval(fit3,x)
xf3=np.linspace(np.min(x),np.max(x),1000)
yf3 = np.polyval(fit3,xf3)

plt.plot(x,y,'o')
plt.plot(xf1,yf1)
plt.plot(xf2,yf2,'-')
plt.plot(xf3,yf3,'--')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.ylim(-30,1030)
plt.xlim(-30,1030)
plt.title('N Random generated points')
plt.legend(['Random Point','1st Order Fit','N-1 Order Fit','N-3 Order Fit'])
#Save the plot and show it
plt.savefig("plot.pdf")
plt.show()
