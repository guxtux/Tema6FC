# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:15:41 2013

@author: areyes
"""

from visual import *
from math import sqrt
from numpy import zeros

g=display(width=600,height=600,title='Cuerda Oscilante')
vibst=curve(x=list(range(0,100)),color=color.yellow)
ball1=sphere(pos=(100,0),color=color.red,radius=2)
ball2=sphere(pos=(-100,0),color=color.red,radius=2)
ball1.pos
ball2.pos
vibst.radius=1.0

rho=0.01
ten=40.
c=sqrt(ten/rho)
c1=c
ratio=c*c/(c1*c1)

#Inicialización
xi=zeros((101,3), dtype=float)
for i in range(0,11):
    xi[i,0]=0.0
    
for i in range(11,21):
    xi[i,0]=(.0005)*(10*i-100)

for i in range(21,31):
    xi[i,0]=(.0005)*(-10*i+300)

for i in range(31,71):
    xi[i,0]=0.0

for i in range(71,81):
    xi[i,0]=(0.0005)*(10*i-700)

for i in range(81,91):
    xi[i,0]=(0.0005)*(-10*i+900)
    
for i in range(91,101):
    xi[i,0]=0.0

for i in range(0,100):
    vibst.x[i]=2.0*i-100.0
    vibst.y[i]=300.*xi[i,0]

vibst.pos

#Pasos porteriores del tiempo

for i in range(1,100):
    xi[i,1]=xi[i,0]+0.5*ratio*(xi[i+1,0]+xi[i-1,0]-2*xi[i,0])

while 1:
    rate(25)
    for i in range(1,100):
        xi[i,2]=2.*xi[i,1]-xi[i,0]+ratio*(xi[i+1,1]+xi[i-1,1]-2*xi[i,1])
    for i in range(1,100):
        vibst.x[i]=2.*i-100.0
        vibst.y[i]=300.*xi[i,2]
    vibst.pos
    for i in range(0,101):
        xi[i,0]=xi[i,1]
        xi[i,1]=xi[i,2]
