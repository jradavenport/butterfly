# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:06:24 2014

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt

amt,num,tot = np.loadtxt('rr.txt', unpack=True, skiprows=1)

plt.figure()
plt.plot(amt,num, 'bo-')
plt.xscale('log')
plt.xlabel('Amount per Donation ($)')
plt.ylabel('# of Backers')
#plt.yscale('log')
plt.show()


plt.figure()
plt.plot(amt,tot,'go-')
plt.xscale('log')
plt.xlabel('Amount per Donation ($)')
plt.ylabel('Total Donated per Level ($)')
plt.show()



plt.figure()
plt.plot(num,tot,'ro')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('# of Backers')
plt.ylabel('Total Donated per Level ($)')
plt.show()



