# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:59:51 2013

@author: alberto
"""

#Importamos los modulos necesarios
from numpy import *
import matplotlib 
from matplotlib import cm 
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

#Definimos nuestra area de trbajo
fig=plt.figure()
ax=fig.add_subplot(111, projection="3d")

#Creamos la rejilla circular
r_a=0.5
r_b=5.0
circulos=50
lineas=50
origen=(0,0)
r,t=meshgrid(linspace(r_a,r_b,circulos),linspace(0,2*pi,lineas))
x=r*cos(t)
y=r*sin(t)
dr=abs(r[0][1]-r[0][0])
dt=abs(t[1][0]-t[0][0])

#Damos el valor de p para una malla
max=50
p=array([[0.0 for i in range(50)]for i in range (50)])

#Inicializamos la malla en zeros
for i in range(50):
    for j in range(50):
        p[i][j]=0.0

#Colocamos valores de frontera
#La primera entrada es la coordenada angular
#La segunda entrada es la coordenada radial.
for i in range(max):
    p[i][0]=-50.0
    p[i][49]=85.0
    
#Algoritmo de iteracion
for k in range(100):
    for i in range (0,max-1):
        for j in range (0,max-1):
            if (j==0):
                p[i][j]=p[i][j]
            elif (j==49):
                p[i][j]=p[i][j]
            else:
                #En caso de dejarlo en cero solo tendremos 2 cilindros concentricos, el interior a 100 y el exterior a -50.
                #p[i][j]=0.0
                
                #Expresion para el laplaciano en coordenadas polares. Sin termino de densidad de corriente tenemos solo la ecuacion de Laplace en coordenadas polares.
                #p[i][j]=((dt*dr**2.*r[i][j]**2.)/(2.*dt*r[i][j]**2.+dr**2.))*((p[i][j-1]+p[i][j+1])/dr**2.+(1/(2.*r[i][j]*dr))*(p[i][j+1]-p[i][j-1])+(1/r[i][j]**2.0)*(p[i-1][j]+p[i+1][j]))
                
                #Si agregamos un termino de densidad de corriente tenemos la solucion para la ecuacion de Poisson en coordenadas polares.
                #En este ejemplo una dependencia del inverso del radio al cubo
                p[i][j]=((dt*dr**2.*r[i][j]**2.)/(2.*dt*r[i][j]**2.+dr**2.))*((2.*r[i][j]**3.)+(p[i][j-1]+p[i][j+1])/dr**2.+(1/(2.*r[i][j]*dr))*(p[i][j+1]-p[i][j-1])+(1/r[i][j]**2.0)*(p[i-1][j]+p[i+1][j]))
                
z=p
#Graficamos X,Y,Z y agregamos mapa de color
surf=ax.plot_surface(x,y,z, rstride=2, cstride=2, linewidth=0.5, cmap=cm.coolwarm)
#Colocamos etiquetas en los ejes
ax.set_zlabel("Potencial electrico")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Poisson. inverso radial al cubo")
#Agregamos una barra indicadora
fig.colorbar(surf, shrink=0.5, aspect=5)
#Dibujamos las lineas de nivel en un plano inferior a la grafica
cset=ax.contourf(x,y,z, zdir="z", offset=-100, cmap=cm.coolwarm)
#Delimitamos nuestra grafica
ax.set_zlim(-100,100)
#Mostramos la gráfica
plt.show()