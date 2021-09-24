import numpy as np
import matplotlib.pyplot as plt
#image size
X = 512
Y = 384
# array for image data (pixel values): x,y,color[0:2]
# color is (r,g,b).
#    Each color level is specified using an 8-bit unsigned integer (0-255)
pvals = np.zeros((X,Y), dtype='uint8')

xinc=1000/X
yinc=1000/Y
Max=512*xinc+384*yinc

for a in range(X):
    for b in range (Y):
        z=0
        c=complex(a/X,b/Y)
        for i in range(250):
                z=z*z+c
                if abs(z)>2:
                    break
        if i==249:
            pvals[a,b]=0

        else:
            pvals[a,b]=abs(Max*(i/250)-Max)
print(pvals)
plotarr = np.flipud(pvals.transpose())
f1, ax1 = plt.subplots()
picture = ax1.imshow(plotarr, interpolation='gaussian',cmap='inferno')
ax1.axis('off')
f1.show()