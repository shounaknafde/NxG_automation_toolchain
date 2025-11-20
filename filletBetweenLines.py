#fillet between lines
import math
import numpy as np
import matplotlib.pyplot as plt
def filletBetweenLines(m1, c1, m2, c2, Rf, side):
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
    if m1==m2:
        return None, None
    if (m1>=0 and m2>=0) or (m1<0 and m2>=0):
        cp1 = c1-d1*Rf*math.sqrt(1+m1**2)
        cp2 = c2-d2*Rf*math.sqrt(1+m2**2)
    elif (m1>=0 and m2<0) or (m1<0 and m2<0):
        cp1 = c1-d1*Rf*math.sqrt(1+m1**2)
        cp2 = c2+d2*Rf*math.sqrt(1+m2**2)
    xf = float(format((-(cp1-cp2)/(m1-m2)), ".6f"))
    yf = float(format((m1*xf+cp1), ".6f"))
    return xf, yf#, cp1, cp2
#test case
'''a1 = 179
a2 = 91
c1 = 1
Rf = 1
m1 = math.tan(math.radians(a1))
m2 = math.tan(math.radians(a2))
c2 = -m2
print(m1, m2)
xf, yf, cp1, cp2 = filletBetweenLines(m1, c1, m2, c2, Rf, 3)
print(xf, yf)
x_values = np.linspace(-2, 2, 400)
#original lines
y1_original = m1*x_values+c1
y2_original = m2*x_values+c2
# Parallel lines (offset)
y1_parallel = m1*x_values+cp1
y2_parallel = m2*x_values+cp2
#plotting
plt.figure(figsize=(8, 8))
#plot original lines
plt.plot(x_values, y1_original, label="Line 1 (Original)", color='blue')
plt.plot(x_values, y2_original, label="Line 2 (Original)", color='green')
#plot parallel lines
plt.plot(x_values, y1_parallel, '--', label="Line 1 (Parallel)", color='blue')
plt.plot(x_values, y2_parallel, '--', label="Line 2 (Parallel)", color='green')
#plot the intersection point (xf, yf)
plt.plot(xf, yf, 'ro', label="Fillet Point (xf, yf)")
#labels and formatting
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Fillet Between Lines and Their Parallel Counterparts")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
#show the plot
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()'''
