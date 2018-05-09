# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:40:17 2013

@author: IIFCES
"""
from numpy import *

rho = 0.01
ten = 40.
c = sqrt(ten/rho)
c1 = c
ratio = c*c/(c1*c1)


xi = zeros ((101,3),float)

for i in range(0,81):
    xi[i,0] = 0.00125*i;
    
for i in range(81,101):
    xi[i,0] = 0.1-0.005*(i-81)

for i in range(1,100):
    xi[i,1] = xi[i,0] + 0.5 * ratio *(xi[i+1,0]+ xi[i-1,0]- 2*xi[i,0])

for i in range(1,100):
    xi[i,2] = 2.* xi[i,1]-xi[i,0]+ ratio*(xi[i+1,1]+ xi[i-1,1]-2*xi[i,1])

for i in range(0,101):
    xi[i,0] = xi[i,1]
    xi[i,1] = xi[i,2]


