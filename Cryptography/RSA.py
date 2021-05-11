# -*- coding: utf-8 -*-
import numpy as np
"""
Created on Fri Feb 26 17:23:21 2021

@author: USER
"""

p = 1234567897777
q = 1234567892021
N = p * q

phi = (p-1)*(q-1)
e = 7
E = 7**-1

D = 435473682032251190327863
c = 309832009 % N
M = pow(c,D,N)
#A = C**D
#M =  np.power(C,D)  % N
print(M)