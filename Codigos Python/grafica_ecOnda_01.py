#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'

for i in np.arange(0.0, 42.0, 2.5):
    tiempo = '{0:4.2f}'.format(i)
    archivo = 'ArchivosEcOnda/solucion_onda_03_' + tiempo + '.txt'
    arreglos = np.genfromtxt(archivo, skip_header=2)
    
    plt.clf()
    plt.plot(arreglos[:,0], arreglos[:,1])
    plt.axhline(y=0, ls='dashed', lw=0.75, c='k')
    plt.title('Propagación de la onda en t = ' + tiempo)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.xlim([-100,100])
    plt.savefig('../Imagenes/grafica_03_'+ tiempo +'.eps')
    plt.pause(1)
plt.show()