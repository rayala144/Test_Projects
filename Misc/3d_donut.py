import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

ranger = np.linspace(0, 2 * np.pi, 50)

s = np.sin(ranger)
c = np.cos(ranger)

x, y = c, s
z = np.zeros_like(x)

ax = plt.axes(projection="3d")
ax.plot(x, y, z, label="Donut")
ax.legend()


def compound_rotate(axes):
    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)


compound_rotate(ax)
