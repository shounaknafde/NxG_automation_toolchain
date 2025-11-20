import math
import numpy as np
import matplotlib.pyplot as plt
from intersection_functions import intersectionCircleCircle
#fillet between circles
def filletBetweenCircles(xc1, yc1, R1, xc2, yc2, R2, Rf, side):
    d1 = 0
    d2 = 0
    if side==1:
        d1 = -1
        d2 = 1
    elif side==2:
        d1 = -1
        d2 = -1
    elif side==3:
        d1 = 1
        d2 = -1
    else:
        d1 = 1
        d2 = 1
    xf1, yf1, xf2, yf2 = intersectionCircleCircle(xc1, yc1, R1-d1*Rf, xc2, yc2, R2-d2*Rf)
    return xf1, yf1, xf2, yf2#, d1, d2
#test case
'''xc1 = 0
yc1 = 0
R1 = 2
xc2 = 1
yc2 = 0
R2 = 2.5
Rf = 0.5
xf1, yf1, xf2, yf2, d1, d2 = filletBetweenCircles(xc1, yc1, R1, xc2, yc2, R2, Rf, 4)
print(xf1, yf1, xf2, yf2)
x_values = np.linspace(-10, 10, 400)
#original line and circle
yc1_original = np.sqrt(R1**2-x_values**2)
yc2_original = np.sqrt(R2**2-x_values**2)
#parallel line and concentric circle
yc1_conc = np.sqrt((R1-d1*Rf)**2-x_values**2)
yc2_conc = np.sqrt((R2-d2*Rf)**2-x_values**2)
#plotting
plt.figure(figsize=(8, 8))
#plot original lines
plt.plot(x_values, yc1_original, label="Circle 1 (Original)", color="blue")
plt.plot(x_values, -yc1_original, color="blue")
plt.plot(x_values, yc2_original, label="Circle 2 (Original)", color="green")
plt.plot(x_values, -yc2_original, color="green")
#plot parallel lines
plt.plot(x_values, yc1_conc, '--', label="Circle 1 (Parallel)", color="blue")
plt.plot(x_values, -yc1_conc, '--', color="blue")
plt.plot(x_values, yc2_conc, '--', label="Circle 2 (Parallel)", color="green")
plt.plot(x_values, -yc2_conc, '--', color="green")
#plot the intersection point (xf1, yf2)
plt.plot(xf1, yf1, "ro", label="Fillet Point 1 (xf, yf)")
#plot the intersection point (xf2, yf2)
plt.plot(xf2, yf2, "ko", label="Fillet Point 2 (xf, yf)")
#labels and formatting
plt.axhline(0, color="black",linewidth=0.5)
plt.axvline(0, color="black",linewidth=0.5)
plt.title("Fillet Between Lines and Their Parallel Counterparts")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
#show the plot
plt.xlim([-10, 10])
plt.ylim([-5, 5])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()'''
