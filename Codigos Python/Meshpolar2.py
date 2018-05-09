# -*- coding: utf-8 -*-


from numpy import *
import matplotlib.pylab as pp
#import pylab

r_a = 0.50
r_b = 1
circulos = 6  
lineas  = 30
origen = (0, 0)

r, t   = meshgrid(linspace(r_a, r_b, circulos), linspace(0, 2 * pi, lineas))
x = r * cos(t)
y = r * sin(t)

pp.plot(x, y)

pp.plot(vstack((x[:,0], x[:, -1])),vstack((y[:,0], y[:, -1])))
           
pp.axis('scaled')
pp.title('Otra manera de generar una malla circular')
pp.show()