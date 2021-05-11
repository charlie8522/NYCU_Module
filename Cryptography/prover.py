# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

#Peggy picks an random value r and send C=g^r to Victor
x,g,p= map(int, input().split(' '))
r = random.randint(1,p-1)
C = g**r
print(C)

e = int(input())
#Peggy sends t=ex+r to Victor
t = e*x+r
print(t)