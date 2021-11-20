#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

N = 1109
N_A = 143
p_1 = N_A/N
std = np.sqrt(N*(p_1)*(1-(p_1)))
uncert1 = std/N

N = 143
N_A = 42
p_2 = N_A/N
std_2 = np.sqrt(N*(p_2)*(1-(p_2)))
uncert2 = std_2/(N)

N = 1109 -143
N_A = 143-42
p_n =  N_A/N
std_n = np.sqrt(N*p_n*(1-p_n))
uncertn = std_n/966

x1 = np.linspace(0, 1, 1109)
x2 = np.linspace(0, 1, 143)
x3 = np.linspace(0, 1, 966)

plt.plot(x1,1109*stats.norm.pdf(x1, p_1, uncert1), label = 'P')
plt.plot(x2,143*stats.norm.pdf(x2, p_2, uncert2), label = 'Pg')
plt.plot(x3,966*stats.norm.pdf(x3, p_n, uncertn), label = 'Pn')

plt.grid()
plt.legend(loc = 'upper right')
plt.show()


# In[ ]:





# In[ ]:




