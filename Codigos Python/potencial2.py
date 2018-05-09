import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

import numpy as np

max = 100
p = [[0 for i in range(100)] for i in range (100)]

for i in range (100):
    for j in range(100):
        p[i][j]=0.0

for i in range(20,80):
    p[i][40]=100.0
    p[i][60]=-100.0
	
for k in range(1000):
    for i in range (1,(max-1)):
        for j in range (1,(max-1)):
            if(j==40) or (j==60):
                p[i][j]=p[i][j]
            else:
                p[i][j]=0.25*(p[i+1][j]+p[i-1][j]+p[i][j+1]+p[i][j-1])
                
Z = p
X = np.arange(0,100)
Y = np.arange(0,100)
X,Y = np.meshgrid(X,Y)
surf = ax.plot_surface(X,Y,Z,rstride=2,cstride=2,linewidth=0.5,cmap=cm.coolwarm)
surf.set_clim([np.min(Z),np.max(Z)])
ax.set_zlabel('Potencial Electrico')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(surf,shrink=0.5,aspect=5)
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
ax.set_zlim(-100, 100)
plt.show()
