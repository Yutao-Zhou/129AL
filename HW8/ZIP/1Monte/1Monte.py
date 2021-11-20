import numpy as np
import matplotlib.pyplot as plt
#part a
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
def cpi(N):
    rng = np.random.default_rng()
    p=2*rng.random((N,2))+0
    x=p[:,0]
    y=p[:,1]
    c=0
    for i in range (N):
        r=np.sqrt((x[i]-1)**2+(y[i]-1)**2)
        if r<=1:
            c=c+1
    area=c*4/N
    pi=area/(1**2)
    ap=[area,pi]
    return ap

area,pi=cpi(N)
print('The area of the circle is: ',area)
print('Pi is: ',pi)
#part b
xp=[]
yp=[]
for n in range (7):
    yx=N+(10**n)
    xp.append([yx])
    p=cpi(N+10**n)[1]
    yr=(np.pi-p)*100/np.pi
    yp.append([yr])

plt.plot(xp,yp,'o')
plt.xlabel('Number of dot (N)')
plt.ylabel('Determinant (%)')
plt.title('The determined value as N increase')
#Save the plot and show it
plt.savefig("plot.pdf")
plt.show()