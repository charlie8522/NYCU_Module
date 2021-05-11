# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:37:44 2021

@author: USER
"""
import random

#Victor sends e to Peggy.
C,y,g,p= map(int, input().split(' '))
e = random.randint(1,100)
print(e)

#Victor verify g^t=y^eC
t= int(input())
if g**t == (y**e)*C: 
    print('1')
else: 
    print('0')