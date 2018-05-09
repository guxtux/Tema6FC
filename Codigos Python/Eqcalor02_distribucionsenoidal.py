# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:15:30 2012

@author: IIFCES
"""

from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

Nx = 101
Nt = 3000
Dx = 0.01414                                                # x increment
Dt = 1.
#Dx = 0.03
#Dt = 0.9
KAPPA = 210.
SPH = 900.
RHO = 2700.


T =zeros((Nx,2), dtype=float)
Tpl = zeros ((Nx,31), dtype=float)


for ix in range(1,Nx-1):
    T[ix,0] = sin(3.1415*ix/100)

T[0,0] = 0.0
T[0,1] = 0.0

T[Nx-1,0] = 0.0
T[Nx-1,1] = 0.0

cons = KAPPA/(SPH*RHO)*Dt/(Dx*Dx)

m = 1
for t in range(1,Nt):
    for ix in range(1,Nx-1):
        T[ix,1] = T[ix,0] + cons*(T[ix+1,0] + T[ix-1,0]-2.*T[ix,0])
    if t%100 == 0 or t == 1:
        for ix in range(1,Nx-1,2): Tpl[ix,m] = T[ix,1]
        print (m)
        m = m + 1
    for ix in range(1,Nx-1): T[ix,0] = T[ix,1]


x = list(range(1,Nx-1,2))
y = list(range(1,30))

X, Y = meshgrid(x,y)

def functz(Tpl):
    z = Tpl[X,Y]
    return z
    
Z = functz(Tpl)

surf = ax.plot_surface(X,Y,Z,rstride=1, cstride=1,linewidth=0.5,cmap=cm.coolwarm)
#surf.set_clim([-100,100])
fig.colorbar(surf, shrink=0.5, aspect=5)
#ax.set_zlim(-10, 100)
cset = ax.contourf(X,Y,Z, zdir='z',offset=0, cmap=cm.coolwarm)
ax.set_xlabel('Posicion')
ax.set_ylabel('tiempo')
ax.set_zlabel('Temperatura')
ax.set_title('Distribucion senoidal')
plt.show()