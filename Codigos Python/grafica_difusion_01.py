#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:39:00 2018

@author: gustavo
"""

import matplotlib.pyplot as plt
import numpy as np



def PropagFTCS(u0, u, nx, D, hx, ht):
#----------------------------------------------------------------------------
#  Propagates the solution u0[] of the diffusion equation
#     du/dt = D d2u/dx2,  D - diffusion coefficient (constant)
#  over the time intervat ht, using an explicit FTCS difference scheme on
#  a spatial grid with nx nodes and spacing hx. Returns the solution in u[].
#----------------------------------------------------------------------------
   lam = D * ht/(hx*hx) 
   lam1 = 1e0 - 2e0*lam

   u[1] = u0[1]; u[nx] = u0[nx]
   for i in range(2,nx):
      u[i] = lam*u0[i-1] + lam1*u0[i] + lam*u0[i+1]
      
   return u

def Init(u, x, nx):             # initial solution for the diffusion equation
   global L                                        # extent of spatial domain
   for i in range(1,nx+1): u[i] = np.sin(np.pi*x[i]/L)
   
  
# main

D    = 0.1e0                                          # diffusion coefficient
L    = 1e0                                             # [0,L] spatial domain
nx   = 21                                     # number of spatial mesh points
tmax = 5.0e0                                               # propagation time
tmax2 = 5.5e0
tmax3 = 6.0e0
ht   = 1.25e-2                                                    # time step


u0 = [0]*(nx+1); u = [0]*(nx+1)
u2 = [0]*(nx+1); u1 = [0]*(nx+1)                                    # solution 
u4 = [0]*(nx+1); u3 = [0]*(nx+1)

x = [0]*(nx+1)                                                 # spatial mesh

hx = L/(nx-1)
for i in range(1,nx+1): x[i] = (i-1)*hx                        # spatial mesh



Init(u0,x,nx)                                              # initial solution


t = 0e0

while (t < tmax):                                             # temporal loop
   t += ht                                                    # increase time
   PropagFTCS(u0,u,nx,D,hx,ht)                           # propagate solution

   for i in range(1,nx): u0[i] = u[i]                  

f = np.exp(-np.pi*np.pi*D*t/(L*L))

exacta = []

for i in range(nx+1):
   exacta.append(f*np.sin(np.pi*x[i]/L))


Init(u2,x,nx)   

t = 0e0

while (t < tmax2):                                             # temporal loop
   t += ht                                                    # increase time
   PropagFTCS(u2,u1,nx,D,hx,ht)                           # propagate solution

   for i in range(1,nx): u2[i] = u1[i]                  

f2 = np.exp(-np.pi*np.pi*D*t/(L*L))

exacta2 = []

for i in range(nx+1):
   exacta2.append(f2*np.sin(np.pi*x[i]/L))

Init(u4,x,nx)   

t = 0e0

while (t < tmax3):                                             # temporal loop
   t += ht                                                    # increase time
   PropagFTCS(u4,u3,nx,D,hx,ht)                           # propagate solution

   for i in range(1,nx): u4[i] = u3[i]                  

f3 = np.exp(-np.pi*np.pi*D*t/(L*L))

exacta3 = []

for i in range(nx+1):
   exacta3.append(f3*np.sin(np.pi*x[i]/L))


#plt.plot(x, u, 'r', label='FTCS', ls='dashed')
#plt.plot(x, exacta, 'b', label='Exacta')
#plt.text(0.15, 0.006, '$t=5.0$')
#plt.plot(x, u1, 'r', ls='dashed')
#plt.plot(x, exacta2, 'b')
#plt.text(0.3, 0.0045, '$t=5.5$')
#plt.plot(x, u3, 'r', ls='dashed')
#plt.plot(x, exacta3, 'b')
#plt.text(0.35, 0.0028, '$t=6.0$')
plt.plot(x, u3, 'r', ls='dashed', label='FTCS')
plt.plot(x, exacta3, 'b', label='Exacta')
plt.text(0.45, 0.002, '$t=6.0$')
plt.title('Solución numérica para el problema de difusión con $\lambda=0.50$')
plt.xlabel('x')
plt.ylabel('u')
plt.legend(loc=1)
plt.xlim([0,1])
plt.ylim(ymin=0)
plt.show()