# -*- coding: utf-8 -*-


from numpy import *
import matplotlib.pylab as pp

r_a = 0.50
r_b = 1
circulos = 6  
lineas  = 20
origen = (0, 0)

for r in linspace(r_a, r_b, circulos):
    pp.gca().add_patch(pp.Circle(origen, radius=r, fill=False, color='black'))

r_ab = array([r_a, r_b])

for theta in linspace(0, 2 * pi, lineas):
    pp.plot(cos(theta) * r_ab, sin(theta) * r_ab, color='red')

pp.axis('scaled')
pp.title('Creando una malla en coordenadas polares')
pp.show()