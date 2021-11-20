import numpy as np
import matplotlib.pyplot as plt
open('wind.dat','r')
wind=np.loadtxt('wind.dat')
t=wind[:,0]
w=wind[:,1]
e=wind[:,2]
fig,ax1=plt.subplots()
ax1.plot(t,w,'o')
ax1.set_xlim(-1,24)
ax1.set_xlabel('Time (hours)')
ax1.set_ylim(4.5,10)
ax1.set_ylabel('Average wind speed (knots)')
ax1.errorbar(t,w,yerr=e,fmt='o')
ax1.set_title('Average wind speed of local time of day')
fig.show()

print(wind)