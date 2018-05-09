#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:25:17 2017

@author: gustavo
"""

from numpy import zeros
import matplotlib.pylab as p;
from mpl_toolkits.mplot3d import Axes3D
print('Iniciando')
Nmax = 100; Niter = 70; V = zeros((Nmax, Nmax), float)
# float maybe Float
#print( "Working hard, wait for the figure while I count to 60")
for k in range(0, Nmax-1): V[k,0] = 100.0
# line at 100V
for iter in range(Niter):
# iterations over algorithm
    if iter%10 == 0: print( iter)
    for i in range(1, Nmax-2):
        for j in range(1,Nmax-2): V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
x = range(0, Nmax-1, 2); y = range(0, 50, 2)
# plot every other point
X, Y = p.meshgrid(x,y)
def functz(V):
    z = V[X,Y]
    return z

Z = functz(V)
fig = p.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color = 'r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potencial')
p.show()