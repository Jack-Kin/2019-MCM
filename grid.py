import numpy
import matplotlib.pyplot as plt
from math import pi
from numpy import cos, sin
plt.rcParams['figure.figsize'] = (8.0, 8.0)
fig = plt.figure() 
ax = fig.gca() 
ax.set_xticks(numpy.arange(-1, 21, 1))
ax.set_yticks(numpy.arange(-1, 21, 1))

angles_circle = [i * pi / 180 for i in range(0, 361)]  # i先转换成double
# angles_circle = [i/np.pi for i in np.arange(0,360)]             # <=>
# angles_circle = [i/180*pi for i in np.arange(0,360)]    X
x = 7 * cos(angles_circle) + 7.5
y = 7 * sin(angles_circle) + 7.5
plt.plot(x, y, 'k')

plt.grid()

plt.show() 