import math
import numpy as np
import matplotlib.pyplot as plt
from intersection_functions import intersectionCircleLine
#rotation about origin
def rotationAboutOrigin(theta, x1, y1):
    theta_rads = float(format((math.radians(theta)), ".6f"))
    x_rot = float(format((x1*np.cos(theta_rads)-y1*np.sin(theta_rads)), ".6f"))
    y_rot = float(format((x1*np.sin(theta_rads)+y1*np.cos(theta_rads)), ".6f"))
    return x_rot, y_rot
#mirror about a line
def mirrorAboutLine(m, c, x1, y1):
    if np.isinf(m):
        x_mirror = float(format((2*(-c)-x1), ".6f"))
        y_mirror = float(format((y1), ".6f"))
    else:
        d = (x1+(y1-c)*m)/(1+m**2)
        xi = d
        yi = m*d+c
        x_mirror = float(format((2*xi-x1), ".6f"))
        y_mirror = float(format((2*yi-y1), ".6f"))
    return x_mirror, y_mirror
#angle between two lines
def angleBetweenLines(m1, m2):
    if m1==math.inf or m2==math.inf:
        if m1==math.inf:
            m1 = 0
        else:
            m2 = 0
        angle = float(format((90-math.degrees(math.atan(abs((m1-m2)/(1+m1*m2))))), ".6f"))
    else:
        if m1*m2==-1:
            angle = 90
        else:
            angle = float(format((math.degrees(math.atan(abs((m1-m2)/(1+m1*m2))))), ".6f"))
    return angle
#test case
'''m1 = math.sqrt(3)
m2 = math.inf
a = angleBetweenLines(m1, m2)
print(a)'''
