# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:37:58 2012

@author: IIFCES
"""

from visual import *
# Detalle de la cuerda

g = display(width=600,height=300, title = 'Cuerda oscilante')
vibst=curve(x=list(range(0,100)),color=color.yellow)
ball1=sphere(pos=(100,0),color=color.red,radius=2)
ball2=sphere(pos=(-100,0),color=color.red,radius=2)
ball1.pos
ball2.pos
vibst.radius=1.0

# Parametros
rho = 0.01              # Densidad de la cuerda
ten=40.                 # Tension de la cuerda
c=sqrt(ten/rho)         # Velocidad de propagacion
c1 = c                  # Criterio CFL
ratio = c*c/(c1*c1)

# Inicializacion
xi=zeros((101,3), dtype=float)          # 101 x’s y 3 t’s
for i in range(0,81): xi[i,0]= 0.00125*i

for i in range(81,101): xi[i,0]=0.1-0.005*(i-80) # IC

for i in range(0,100):
    vibst.x[i]=2.0*i-100.0      # asignado escala x
    vibst.y[i]=300.*xi[i,0]     # asignando escala y
vibst.pos                       # dibujando la cuerda

# Pasos posteriores de tiempo
for i in range(1,100): xi[i,1] = xi[i,0] + 0.5*ratio*(xi[i+1,0]+ xi[i-1,0]-2*xi[i,0])
while 1:
    rate(50)
    for i in range(1,100):
        xi[i,2]=2.*xi[i,1]- xi[i,0] + ratio*(xi[i+1,1]+ xi[i-1,1]-2*xi[i,1])
    for i in range(1,100):
        vibst.x[i] = 2.*i-100.0
        vibst.y[i] = 300.*xi[i,2]
    vibst.pos
    for i in range(0,101):
        xi[i,0] = xi[i,1]
        xi[i,1] = xi[i,2]