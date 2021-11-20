import matplotlib.pyplot as plt
import numpy as np
import scipy.special

disk=plt.figure()
ax=disk.gca(projection='3d')

x=np.arange(-13,13,0.1)
y=np.arange(-13,13,0.1)
x,y=np.meshgrid(x,y)
r=np.sqrt(x*x+y*y)
z=np.log(((2*scipy.special.j1(r)/r)**2))

surface=ax.plot_surface(x,y,z,cmap='magma',antialiased=True)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z')
ax.set_title('Airy rings')
ax.set_zticks([-5,-10,-15,-20])
ax.set_zticklabels([10**-5,10**-10,10**-15,10**-20])
plt.show()  