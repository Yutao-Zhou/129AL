import numpy as np
import matplotlib.pyplot as plt
import matplotlib

Sun=np.loadtxt('sunlight.txt')
LED=np.loadtxt('LEDlight.txt')
Sunt=Sun[:,0]
Suny=Sun[:,1]
LEDt=LED[:,0]
LEDy=LED[:,1]
nSun=abs(Suny)**2
nLED=abs(LEDy)**2

sp,sf = matplotlib.mlab.psd(Suny,NFFT = len(Suny),Fs = 920,pad_to = len(Suny))
# The line above is the same as the following:
# sy=abs(np.fft.fft(Suny))**2
# Both of these methood works.
f1,ax1=plt.subplots()
ax1.plot(sf[3:],sp[3:])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Intensity')
plt.title('Sunlight Energy')
plt.savefig("Sunlight.pdf")
plt.show()

lp,lf = matplotlib.mlab.psd(LEDy,NFFT = len(LEDy),Fs = 920,pad_to = len(LEDy))
# The line above is the same as the following:
# ly=abs(np.fft.fft(LEDy))**2
# Both of these methood works.
f2,ax2=plt.subplots()
ax2.plot(lf[3:],lp[3:])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Intensity')
plt.title('LED Energy')
plt.savefig("LED.pdf")
plt.show()

print('From the graph we can see there are more peaks on the sunlight graph than the LED graph.')
print('These graph show sun have more driving frequency than LED.')