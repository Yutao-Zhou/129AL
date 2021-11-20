#####################################################################################
## read before running!                                                            ##
##  This is a huge program that take half an hour with 7700HQ                      ##
##  Please "#" out other part when looking at each small part in this problem.     ##
##  Please be patient, It works without any problem. Advanced cooling suggested!   ##
#####################################################################################

FTIME = 32       # function range in seconds
FS = 128         # samples per second
npts = FTIME*FS  # number of sample points
f1 = 0.5  # frequency in Hz
f2 = 1.0  # frequency in Hz

import numpy as np
import matplotlib.pyplot as plt
import time
#Part a##############################################

p=2*np.pi
def DFT(x):
    N=x.shape[0]
    output=np.zeros(N,dtype=complex)
    for k in range(N):
        sum=0
        for n in range(N):
            sum+=x[n]*np.exp(1j*p*k*n/N)
        output[k]=sum
    return output

t = np.linspace(0, FTIME, npts)
y = np.sin(2.0*np.pi*f1*t) + 0.5*np.cos(2.0*np.pi*f2*t)
f1, ax1 = plt.subplots()
ax1.plot(t,y)
plt.title('Original data')
f1.savefig("Part_a.pdf")
f1.show()

ft = DFT(y)
ftnorm = abs(ft)
ps = ftnorm**2
xvals = np.fft.fftfreq(len(ps), 1.0/FS)
f2, ax2 = plt.subplots()
ax2.plot(xvals,ps)
ax2.set_xlim(0,10)
plt.title('DFT')
f2.savefig("Part_a_DFT.pdf")
f2.show()

#part b############################################
z=np.random.randn(1024)
t0=time.perf_counter()
ft = DFT(z)
ftnorm = abs(ft)
ps = ftnorm**2
t1=time.perf_counter()
xvals = np.fft.fftfreq(len(ps), 1.0/FS)
f3, ax3 = plt.subplots()
ax3.plot(xvals,ps)
plt.title('DFT')
f3.savefig("Part_b.pdf")
f3.show()

ta=t1-t0
print('My DFT take this long to run:',ta)

#part C#########################################
t2=time.perf_counter()
ft = np.fft.fft(z, n=16*npts)
ftnorm = abs(ft)
ps = ftnorm**2
t3=time.perf_counter()
xvals = np.fft.fftfreq(len(ps), 1.0/FS)
f4, ax4 = plt.subplots()
ax4.plot(xvals,ps)
plt.title('FFT')
f3.savefig("Part_c.pdf")
f4.show()

tb=t3-t2
print('The time it takes for the fft is:',tb)
print('FFT took',(ta-tb),'shorter')

#part d#######################################
N=6
dtt=[0]*N
ftt=[0]*N
y=[0]*N
for i in range (N):
    y[i]=2**(8+i)
    yr=np.random.rand(2**(i+8))
    t10=time.perf_counter()
    dftt=DFT(yr)
    t11=time.perf_counter() 
    dtt[i]=t11-t10
    t12=time.perf_counter()
    fftt=np.fft.fft(yr)
    t13=time.perf_counter()    
    ftt[i]=t13-t12
    
plt.xlabel('Length of the data')
plt.ylabel('Calculation time (second)')
plt.title('DFT calculation time vs FTT calculation time')
plt.loglog(y,dtt,'o',y,ftt,'o')
plt.title('DFT and FTT')
plt.savefig("Part_d.pdf")
plt.show()
DFT_slope=((t11-t10)/(2**(i+8)))
FTT_slope=((t13-t12)/(2**(i+8)))
print('The slope of the DFT line is: ',DFT_slope)
#The slope of DFT is parabola that concave up. My graph looks like a stright line because it only have 3 data point 
#As the length of the data get larger it will the time would increase substantially. Also, the calculation power of
#my laptop is really unstable be cause it takes too short to finish.
#This is also why the shape would be more stable after the length of the data increase.
#change N to 3 if it take too long to run for DFT.
print('The slope of the FTT line is: ',FTT_slope)
#the same apply to FTT exceped that it take shorter for FTT and the slope does not increase as fest as DFT.
#The slope of FTT are generally speaking smaller than DFT.
