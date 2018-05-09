# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:19:28 2012

@author: IIFCES
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

import numpy as np

max=100
p= [[0 for i in range(100)] for i in range(100)]


# inicializamos todos los puntos del cuadrado, incluyendo las fronteras   	
	
for i in range(100):
    for j in range(100):
        p[i][j] = 0.0

# aqui asignamos los valores de potencial en la frontera
for i in range(20,max-20):
    p[i][30]=100.0
    p[i][70]=-100.0

# Algortimo de iteracion, si es necesario contar con un ciclo de repeticion de 1000 veces
	

for k in range(1000):
    for i in range(2,(max-1)):
        for j in range (2,(max-1)):
            if (j == 30 or j==70):
                if (i>=20 and i<=80):
                    p[i][j] = p[i][j]
            else:
                p[i][j]=0.25*(p[i+1][j]+p[i-1][j]+p[i][j+1]+p[i][j-1])


Z = p

X = np.arange(0,100)
Y = np.arange(0,100)

X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, Z,rstride=2, cstride=2,linewidth=0.5,cmap=cm.coolwarm)
surf.set_clim([np.min(Z),np.max(Z)])

ax.set_zlabel('Potencial electrico')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(surf, shrink=0.5, aspect=5)
cset = ax.contourf(X,Y,Z, zdir='z',offset=-100, cmap=cm.coolwarm)
ax.set_zlim(-100, 100)
plt.show()