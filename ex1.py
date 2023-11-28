import numpy as np
from math import sin, pi, log10, asin
x = 1.6453

y = ((sin((pi/6)-1))**2+pow(3+x**2, 0.25)-(log10(x**3-1))**3)/(asin(x/2)-1.756*pow(10, -2))

print("Значение y=", y)