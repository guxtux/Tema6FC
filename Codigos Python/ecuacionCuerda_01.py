# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:27:14 2017

@author: Master Chief
"""

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
plt.style.use('dark_background')
 
fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1, 1, 1)
 
#longitud de la cuerda (m)
L = pi
 
#masa de la cuerda (kg)
m = pi
 
#densidad (kg/m)
mu = L/m
 
#tension (N)
T = 1
 
#velocidad de la onda
c = np.sqrt(T/mu)
 
#tiempo inicial
t0 = 0
 
#incremento en el tiempo
dt = 0.05
 
#eje x
x0 = np.linspace(0, L, 10000)
 
print('Longitud de la cuerda', L, 'm')
print('Masa de la cuerda', m, 'kg')
print('Densidad de la cuerda', mu, 'kg/m')
print('Tension aplicada', T, 'N')
print('Velocidad de onda', c, 'm/s')
print('Tiempo inicial', t0, 's')
print('Tiempo de incremento elegido', dt, 's')
 
#Onda
def u(x, t):
    return 0.5*(np.sin(x + c*t) + np.sin(x - c*t))
 
a = []
 
for i in range(500):
    valor = u(x0, t0)
    t0 = t0 + dt
    a.append(valor)
 
k = 0
def animacion(i):
    global k
    x = a[k]
    k += 1
    ax1.clear()
    plt.plot(x0, x, color='cyan')
    plt.grid(True)
    plt.ylim([-2, 2])
    plt.xlim([0, L])
     
anim = animation.FuncAnimation(fig, animacion, frames=360, interval=20)
plt.show()