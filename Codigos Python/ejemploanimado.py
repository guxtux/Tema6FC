# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:00:10 2013

@author: IIFCES
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure() 
ax  = fig.add_subplot(111) 

ax.set_xlim(0, 1)
ax.set_ylim(-2,2)

dt = 0.01
q  = 0.01
t = np.arange(0,1,dt)
x = np.sin(2*np.pi*t)
images = []

for i in xrange(100):
    x = (1-q) * x + q* np.random.normal(size = len(t))
    line, = ax.plot(t,x, '-')
    images.append((line,))

line_anim = ArtistAnimation(fig, images, interval=50, blit=True)
line_anim.save('my_animation.mp4')
plt.show()