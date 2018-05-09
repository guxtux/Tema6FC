# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:47:06 2012

@author: IIFCES
"""

import numpy as np

u= [[0 for i in range(2)] for i in range(101)]

sph=0.113
thk=0.12
ro=7.8
cons = thk/(sph*ro)

#numero de iteraciones
max=30000

# en t=0 (i=1) todos los puntos estÃ¡n an 100 C
for i in range(101):
     u[i][0] = 100.0
     

u[0][0]  = 0.0
u[100][0]  = 0.0
u[0][1]  = 0.0
u[100][1]  = 0.0

for k in range(1,max):
# loop sobre la posicion, los extremos quedan fijos
    for i in range(1,99):
        u[i][1] = u[i][0] + cons*(u[i+1][0] + u[i-1][0]-2.0*u[i][0])
        u[i][0] = u[i][1]

#u[101][0] = 0.0
print u
Z = u[:][1]

#	
X = np.arange(0,101)
Y = np.arange(0,101)

print len(u[1][:]), len(X), len(Y)