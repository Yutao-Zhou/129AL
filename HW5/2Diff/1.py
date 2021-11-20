import turtle
import numpy as np
import matplotlib.pyplot as plt
#image size
X = 512
Y = 409
# array for image data (pixel values): x,y,color[0:2]
# color is (r,g,b).
#    Each color level is specified using an 8-bit unsigned integer (0-255)
pvals = np.zeros((X,Y,3), dtype='uint8')
rinc = 255/X
binc = 255/Y
stripetop1 = int(Y/2 + Y/20)
stripebot1 = int(Y/2 - Y/20)
stripetop2 = int(0.8*Y + Y/20)
stripebot2 = int(0.8*Y - Y/20)
# The following loop creat the white background
for j in range(Y):
   for i in range(X):
       pvals[i,j,0] = 0xff  # red
       pvals[i,j,1] = 0xff    # green
       pvals[i,j,2] = 0xff  # blue
# The following loop creat the horizontal side of the triangle that has a length of 400 pixel
#The width of the line are 10 that why y has a range from 38 to 48
for j in range(38,48,1):
    for i in range(52,452,1):
        pvals[i,j,0] = 0x00  # red
        pvals[i,j,1] = 0x00    # green
        pvals[i,j,2] = 0xff  # blue
# The following loop creat the vertical side of the triangle that has a length of 300 pixel
#As you can see the x end at 452 so they over lap, and y start at 38 so they over lap and are connected.
#The width of the line are 10 that why x has a range from 442 to 452
for j in range(38,338,1):
    for i in range(442,452,1):
        pvals[i,j,0] = 0x00  # red
        pvals[i,j,1] = 0x00    # green
        pvals[i,j,2] = 0xff  # blue
# The following loop creat the slope side of the triangle that has a length of 500 pixel
#As you can see the x end at 50 a little bit more left than the horizontal line so they over lap, and the image woun't have a huge gap there. I let y linearly related to x so it creat a lien with slop of 3/4
#The width of the line are 10 that why I make the lineear equation have the form y=ax+b where b is o here and is mving the line in vertical direction. So that the line has a weigth of 10
for o in range(10):    
    for i in range(50,452,1):
        j=int((3*i/4)+o)    
        pvals[i,j,0] = 0x00  # red
        pvals[i,j,1] = 0x00  # green
        pvals[i,j,2] = 0xff  # blue

turtle.forward(100)

#pvals[X//32,Y//20,:] = 0xff
plotarr = np.flipud(pvals.transpose(1,0,2))

f1, ax1 = plt.subplots()
picture = ax1.imshow(plotarr, interpolation='gaussian')
ax1.axis('off')
f1.show()