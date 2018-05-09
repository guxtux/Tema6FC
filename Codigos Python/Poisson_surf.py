#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:34:10 2018

@author: gustavo
"""

import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

mat0 = np.genfromtxt("Poisson.txt", skip_header=1)


x = mat0[:,0]
y = mat0[:,1]
Z = mat0[:,2]

#print(Z)
#
X, Y = plt.meshgrid(x, y)
#
nx = 51; ny = 51                                      # number of mesh points
#
z = [[0]*(ny+1) for i in range(nx+1)]                              # solution



for j in range(1,ny+1):               # initial approximation of the solution
   for i in range(1,nx+1): u[i][j] = Z[]

print(z)

#Z = z0
#
#fig = plt.figure()
#ax = Axes3D(fig)
##ax.plot_wireframe(X, Y, Z, color ='r')
#surf = ax.plot_surface(X, Y, Z)
#ax.set_zlabel('z')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#
#plt.show()