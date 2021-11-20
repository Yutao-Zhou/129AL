import numpy as np
import matplotlib.pyplot as plt
#Making the sin and cos plot
x=np.arange(0,5*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
#Creat axis label and title
plt.plot(x,y,x,z)
plt.xlabel('Theta(radius)')
plt.ylabel('Value')
plt.title('Sin and Cos graph')
#Save the plot and show it
#plt.savefig("plot.eps")
plt.show()