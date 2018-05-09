# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 21:09:22 2014

@author: Master Chief
"""

from numpy import *
import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D

Nx = 101; Nt = 3000; Dx = 0.03 ; Dt = 0.9
KAPPA = 210. ; SPH = 900. ; RHO = 2700. # c o n d u c t i v i t y , s p e c f he a t , d e n s i t y
T = zeros((Nx,2),float) ; Tpl = zeros((Nx,31), float)
print("Working, wait for figure after count to 10")
for ix in range(1,Nx-1) : T[ix,0] = 100.0; # i n i t i a l t emp e r a t u r e
T[0,0] = 0.0; T[0,1] = 0. # f i r s t and l a s t p o i n t s a t 0
T[Nx-1,0] = 0. ; T[Nx-1,1] = 0.0
cons = KAPPA/( SPH*RHO)*Dt/(Dx*Dx); # c o n s t a n t
m = 1 # c o u n t e r f o r rows , one e v e r y 300 t ime s t e p s
for t in range(1,Nt):
    # t ime i t e r a t i o n
    for ix in range(1,Nx-1): # F i n i t e d i f f e r e n c e s
        T[ix,1] = T[ix,0] + cons*(T[ix+1,0] + T[ix-1,0] - 2.*T[ix,0])
    if t%300 == 0 or t == 1: # f o r t = 1 and e v e r y 300 t ime s t e p s
        for ix in range(1,Nx-1,2): Tpl[ix,m] = T[ix,1]
        print (m)
        m = m + 1 # i n c r e a s e m e v e r y 300 t ime s t e p s
    for ix in range(1,Nx-1): T[ix,0] = T[ix,1]# 100 p o s i t o n s a t t =m

x = list(range(1,Nx-1,2)) # p l o t e v e r y o t h e r x p o i n t
y = list(range(1,30)) # e v e r y 10 p o i n t s i n y ( t ime )
X,Y = p.meshgrid(x,y) # g r i d f o r p o s i t i o n and t ime

def functz(Tpl): # Fu n c t i o n r e t u r n s t emp e r a t u r e
    z = Tpl[X,Y]
    return z

Z = functz(Tpl)
fig = p.figure() # c r e a t e f i g u r e
ax = Axes3D(fig) # p l o t s a x i s
ax.plot_wireframe(X,Y,Z,color = 'r') # r e d wi r e f r ame
ax.set_xlabel('Position') # l a b e l a xe s
ax.set_ylabel('time')
ax.set_zlabel('Temperature')
p.show() # shows f i g u r e , c l o s e Python s h e l l