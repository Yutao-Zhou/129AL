# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:10:11 2021

@author: 84186
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

# Part a
# This is can be modeled by using binomial distribution where
N = 1109
NA = 143
p1 = NA/N
sd = np.sqrt(N*(p1)*(1-(p1)))
sigma = sd ** 2
mu1 = N*(NA/N)
print('The standard deviation is',sd)

# Part b
'''
The one standard deviation uncertainty will just be the expected value add or
minus standard deviation we got previously and calculate the corresponding p
'''
uncert1 = sd/(N)
print('The uncertainty is', uncert1)

# Part c
std = np.sqrt(143*p1*(1-p1))
sig = std**2
mu2 = 143*p1
#pdf = (1/sig*np.sqrt(2*np.pi))*np.exp((-1/2)*((x-mu)/sig)**2)
a = 1-stats.norm(mu2,std).cdf(42)
print('The probability is',a)

# Part d
NN = 143
NNA = 42
p2 = NNA/NN
sd2 = np.sqrt(NN*(p2)*(1-(p2)))
sigma2 = sd2 ** 2
mu2 = NN*p2
print('The best estimate is',p2)
uncert2 = sd2/(NN)
print('The uncertainty is', uncert2)

# Part e

notin = N-NA
NA3 = 143-42
pn =  NA3/notin
sdn = np.sqrt(notin*pn*(1-pn))
sigman = sdn ** 2
mun = pn * notin
print('The best estimate is', pn)
uncertn = sdn/(notin)
print('1-standard deviation uncertainty is',uncertn)


# Part f
x1 = np.linspace(0, 1, 1109)
x2 = np.linspace(0, 1, 143)
x3 = np.linspace(0, 1, 966)

plt.plot(x1,1109*stats.norm.pdf(x1, p1, uncert1), label = 'P')
plt.plot(x2,143*stats.norm.pdf(x2, p2, uncert2), label = 'Pg')
plt.plot(x3,966*stats.norm.pdf(x3, pn, uncertn), label = 'Pn')

plt.grid()
plt.legend(loc = 'upper left')