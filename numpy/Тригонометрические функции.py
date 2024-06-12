import numpy
import numpy as np
a = np.array([0,30,45,60,90])
sin = np.sin(a*np.pi/180)
print(sin)
c = np.degrees(sin)
print(numpy.around(c, decimals = -1))

