#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import numpy as np

def PropagOnda(u0, u1, u, nx, c, hx, ht):
   lam = c * ht/hx
   lam = lam * lam
   lam2 = 2e0 * (1e0 - lam)

   u[1] = u0[1]
   u[nx] = u0[nx]
   for i in range(2, nx):
      u[i] = lam * u1[i-1] + lam2 * u1[i] + lam * u1[i+1] - u0[i]

#====================================================================================
      
def Init(u0, u1, x, nx, c, dk, hx, ht):
#----------------------------------------------------------------------------
#  Devuelve las soluciones iniciales u0 and u1, para los dos primeros pasos temporales
#     u0(x,0) = sin(x*dk) / (x*dk)                   solucion inicial
#     v0(x,0) = 0                                    derivada temporal inicial
#  x - malla espacial, nx - numero de nodos
#  c - velocidad de fase de la onda, dk - intervalo del numero de onda
#  hx - espaciamento en x, ht - tamaño de paso temporal
#----------------------------------------------------------------------------
   for i in range(1, nx+1):                                         # tiempo en el paso 0
      u0[i] = np.sin(dk * x[i])/(dk * x[i]) if dk * x[i] else 1e0   # solucion inicial

   lam = c * ht/hx
   lam = lam * lam                                                  # paso temporal 1
   lam2 = 2e0 * (1e0 - lam)
   u1[1] = u0[1]
   u1[nx] = u0[nx]                                                  # valores de la CDF
   for i in range(2,nx):
      v0 = 0e0                                                      # valor de la derivada temporal
      u1[i] = 0.5e0 * (lam*u0[i-1] + lam2 * u0[i] + lam * u0[i+1]) - ht * v0

#====================================================================================
      
def generaArchivo(t, x, u, nx):
    archivo = "ArchivosEcOnda/solucion_onda_01_{0:4.2f}.txt".format(t)
    out = open(archivo, "w")
    out.write("t = {0:4.2f}\n".format(t))
    out.write("     x          u\n")
    for i in range(1, nx+1):
        out.write("{0:10.5f}{1:10.5f}\n".format(x[i], u[i]))
      
    print('Se guardaron los datos en el archivo ' + archivo)
    out.close

