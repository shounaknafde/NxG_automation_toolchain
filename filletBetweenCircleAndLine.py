import math
import numpy as np
import matplotlib.pyplot as plt
from intersection_functions import intersectionCircleLine
#fillet between circle and line
def filletBetweenCircleAndLine(xc, yc, R, m, c, Rf, side):
    d1 = 0
    d2 = 0
    if m<0:
        if side==1:
            d1 = 1
            d2 = -1
        elif side==2:
            d1 = -1
            d2 = -1
        elif side==3:
            d1 = -1
            d2 = 1
        else:
            d1 = 1
            d2 = 1
        cp = c+d1*Rf*math.sqrt(1+m**2)
    else:
        if side==1:
            d1 = 1
            d2 = -1
        elif side==2:
            d1 = -1
            d2 = -1
        elif side==3:
            d1 = -1
            d2 = 1
        else:
            d1 = 1
            d2 = 1
        cp = c-d1*Rf*math.sqrt(1+m**2)
    xf1, yf1, xf2, yf2 = intersectionCircleLine(xc, yc, R-d2*Rf, m, cp)
    return xf1, yf1, xf2, yf2#, cp, d2
#test case
'''xc = 0
yc = 0
R = 6
m = 2.7474774194546216
c = -8.242432258363865
Rf = 1.3
xf1, yf1, xf2, yf2, cp, d2 = filletBetweenCircleAndLine(xc, yc, R, m, c, Rf, 1)
print(xf1, yf1, xf2, yf2)
x_values = np.linspace(-10, 10, 400)
#original line and circle
yc_original = np.sqrt(R**2-x_values**2)
yl_original = m*x_values+c
#parallel line and concentric circle
yc_conc = np.sqrt((R-d2*Rf)**2-x_values**2)
yl_parallel = m*x_values+cp
#plotting
plt.figure(figsize=(8, 8))
#plot original lines
plt.plot(x_values, yc_original, label="Circle (Original)", color="blue")
plt.plot(x_values, -yc_original, color="blue")
plt.plot(x_values, yl_original, label="Line (Original)", color="green")
#plot parallel lines
plt.plot(x_values, yc_conc, '--', label="Circle (Parallel)", color="blue")
plt.plot(x_values, -yc_conc, '--', color="blue")
plt.plot(x_values, yl_parallel, '--', label="Line (Parallel)", color="green")
#plot the intersection point (xf1, yf2)
#plt.plot(xf1, yf1, "ro", label="Fillet Point 1 (xf, yf)")
#plot the intersection point (xf2, yf2)
#plt.plot(xf2, yf2, "ko", label="Fillet Point 2 (xf, yf)")
#labels and formatting
plt.axhline(0, color="black",linewidth=0.5)
plt.axvline(0, color="black",linewidth=0.5)
plt.title("Fillet Between Lines and Their Parallel Counterparts")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
#show the plot
plt.xlim([-15, 15])
plt.ylim([-15, 15])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()'''
