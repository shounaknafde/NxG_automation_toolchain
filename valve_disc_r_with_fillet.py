import math
import numpy as np
import matplotlib.pyplot as plt
from intersection_functions import line, intersectionCircleLine, intersectionCircleCircle
from fillet_between_circle_and_line import filletBetweenCircleAndLine
from rotate_mirror_angle import rotationAboutOrigin, mirrorAboutLine
from ansys.geometry.core import launch_modeler_with_spaceclaim    ##### 1st make changes here
from ansys.geometry.core.math import Plane, Point2D, Point3D, Vector2D, Vector3D, UNITVECTOR3D_Z
from ansys.geometry.core.misc import UNITS, Distance
from ansys.geometry.core.sketch import Sketch
from pint import Quantity
#import cadquery as cq
modeler = launch_modeler_with_spaceclaim() #########try with different modelers (go to line 7)
sketch = Sketch()  ##### after changing prevous line, you get an error here!!!!
def r_valve_disc(xc, yc):
    #geometry
    #number of petals
    n = 3
    a = 360/n
    #inclination
    incl = 9
    #outer circle
    xc1 = xc
    yc1 = yc
    r1 = 11.75
    #middle circle
    r2 = 6
    #inner circle
    r3 = 3.25
    #line 1
    a1 = 90+incl
    xp1 = 5
    yp1 = 0
    m1, c1 = line(a1, xp1, yp1)
    #with fillet
    x = []
    y = []
    xc = []
    yc = []
    rf1 = 1.7
    rf2 = 2.1
    x1, y1, x2, y2 = filletBetweenCircleAndLine(xc1, yc1, r2, m1, c1, rf1, 1)
    if x1<x2:
        xc.append(x1)
        yc.append(y1)
    else:
        xc.append(x2)
        yc.append(y2)
    '''x_vals = np.linspace(-12, 12, 400)
    yc_vals = np.sqrt(r2**2-x_vals**2)
    yl_vals = m1*x_vals+c1
    plt.plot(x_vals, yc_vals, label="middle circle", color="black")
    plt.plot(x_vals, -yc_vals, label="middle circle", color="black")
    plt.plot(x_vals, yl_vals, label="line 1", color="green")
    plt.plot(x1, y1, "ro")
    plt.plot(x2, y2, "ko")
    plt.axhline(0, color="black",linewidth=0.5)
    plt.axvline(0, color="black",linewidth=0.5)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.xlim([-15, 15])
    plt.ylim([-15, 15])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()'''
    #0
    x3, y3, x4, y4 = intersectionCircleCircle(xc[0], yc[0], rf1, xc1, yc1, r2)
    x.append(x4)
    y.append(y4)
    #1
    x5, y5, x6, y6 = intersectionCircleLine(xc[0], yc[0], rf1, m1, c1)
    x.append(x5)
    y.append(y5)
    x7, y7, x8, y8 = filletBetweenCircleAndLine(xc1, yc1, r1, m1, c1, rf2, 3)
    if x7<x8:
        xc.append(x7)
        yc.append(y7)
    else:
        xc.append(x8)
        yc.append(y8)
    #2
    x11, y11, x12, y12 = intersectionCircleLine(xc[1], yc[1], rf2, m1, c1)
    x.append(x11)
    y.append(y11)
    #3
    x9, y9, x10, y10 = intersectionCircleCircle(xc[1], yc[1], rf2, xc1, yc1, r1)
    x.append(x9)
    y.append(y9)
    '''x_vals = np.linspace(-22, 22, 400)
    yf_vals = np.sqrt(rf2**2-(xc[1]-x_vals)**2)+yc[1]
    yc_vals = np.sqrt(r1**2-x_vals**2)
    plt.plot(x_vals, yf_vals, label="fillet circle", color="black")
    plt.plot(x_vals, -yf_vals, label="fillet circle", color="black")
    plt.plot(x_vals, yc_vals, label="outer circle", color="green")
    plt.plot(x_vals, -yc_vals, label="outer circle", color="green")
    plt.axhline(0, color="black",linewidth=0.5)
    plt.axvline(0, color="black",linewidth=0.5)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.xlim([-25, 25])
    plt.ylim([-25, 25])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()'''
    x13, y13 = mirrorAboutLine(math.inf, 0, x[3], y[3])
    x.append(x13)
    y.append(y13)
    x14, y14 = mirrorAboutLine(math.inf, 0, x[2], y[2])
    x.append(x14)
    y.append(y14)
    x15, y15 = mirrorAboutLine(math.inf, 0, x[1], y[1])
    x.append(x15)
    y.append(y15)
    x16, y16 = mirrorAboutLine(math.inf, 0, x[0], y[0])
    x.append(x16)
    y.append(y16)
    x17, y17 = mirrorAboutLine(math.inf, 0, xc[1], yc[1])
    xc.append(x17)
    yc.append(y17)
    x18, y18 = mirrorAboutLine(math.inf, 0, xc[0], yc[0])
    xc.append(x18)
    yc.append(y18)
    '''print(xc)
    print(yc)
    print(x)
    print(y)'''
    for i in range(n-1):
        for j in range(len(x)):
            angle = (i+1)*a
            xt, yt = rotationAboutOrigin(angle, x[j], y[j])
            x.append(xt)
            y.append(yt)
        for j in range(len(xc)):
            angle = (i+1)*a
            xct, yct = rotationAboutOrigin(angle, xc[j], yc[j])
            xc.append(xct)
            yc.append(yct)
    '''for xi, yi in zip(x, y):
        plt.plot(xi, yi, "ro")
    for xci, yci in zip(xc, yc):
        plt.plot(xci, yci, "ko")
    plt.axhline(0, color="black",linewidth=0.5)
    plt.axvline(0, color="black",linewidth=0.5)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.xlim([-15, 15])
    plt.ylim([-15, 15])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()'''
    #ansys
    for i in range(n):
        #first petal
        if i!=n-1:
            (
                sketch.arc(Point2D([x[0+i*8], y[0+i*8]], unit=UNITS.mm), Point2D([x[1+i*8], y[1+i*8]], unit=UNITS.mm), Point2D([xc[0+i*4], yc[0+i*4]], unit=UNITS.mm), clockwise=True).
                segment_to_point(Point2D([x[2+i*8], y[2+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[3+i*8], y[3+i*8]], unit=UNITS.mm), Point2D([xc[1+i*4], yc[1+i*4]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[4+i*8], y[4+i*8]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm)).
                arc_to_point(Point2D([x[5+i*8], y[5+i*8]], unit=UNITS.mm), Point2D([xc[2+i*4], yc[2+i*4]], unit=UNITS.mm)).
                segment_to_point(Point2D([x[6+i*8], y[6+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[7+i*8], y[7+i*8]], unit=UNITS.mm), Point2D([xc[3+i*4], yc[3+i*4]], unit=UNITS.mm), clockwise=True).
                arc_to_point(Point2D([x[8+i*8], y[8+i*8]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm))
            )
        #remaining petal
        else:
            (
                sketch.arc(Point2D([x[0+i*8], y[0+i*8]], unit=UNITS.mm), Point2D([x[1+i*8], y[1+i*8]], unit=UNITS.mm), Point2D([xc[0+i*4], yc[0+i*4]], unit=UNITS.mm), clockwise=True).
                segment_to_point(Point2D([x[2+i*8], y[2+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[3+i*8], y[3+i*8]], unit=UNITS.mm), Point2D([xc[1+i*4], yc[1+i*4]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[4+i*8], y[4+i*8]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm)).
                arc_to_point(Point2D([x[5+i*8], y[5+i*8]], unit=UNITS.mm), Point2D([xc[2+i*4], yc[2+i*4]], unit=UNITS.mm)).
                segment_to_point(Point2D([x[6+i*8], y[6+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[7+i*8], y[7+i*8]], unit=UNITS.mm), Point2D([xc[3+i*4], yc[3+i*4]], unit=UNITS.mm), clockwise=True).
                arc_to_point(Point2D([x[0], y[0]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm)).
                circle(Point2D([xc1, yc1], unit=UNITS.mm), Quantity(r3, UNITS.mm))
            )
    sketch.plot()
    design = modeler.create_design("ExtrudedValveProfile")
xc = 0
yc = 0
r_valve_disc(xc, yc)
