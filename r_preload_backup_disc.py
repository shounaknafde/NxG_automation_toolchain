import math
import numpy as np
import matplotlib.pyplot as plt
from intersection_functions import line, intersectionCircleLine, intersectionCircleCircle
from fillet_between_circle_and_line import filletBetweenCircleAndLine
from rotate_mirror_angle import rotationAboutOrigin, mirrorAboutLine
#from ansys.geometry.core import launch_modeler_with_discovery
from ansys.geometry.core.math import Point2D, UNITVECTOR3D_Z
from ansys.geometry.core.misc import UNITS
from ansys.geometry.core.sketch import Sketch
from pint import Quantity
sketch = Sketch()
def r_preload_backup_disc(xc, yc):
    #geometry
    #number of petals
    n = 4
    a = 360/n
    #inclination
    incl = 9
    #outer circle
    xc1 = xc
    yc1 = xc
    r1 = 11.75
    #middle circle
    r2 = 6
    #inner circle
    r3 = 3.25
    #circle for holes
    r4 = 9.45
    #hole dia
    r5 = 2.3
    incl2 = 10
    #line 1
    a1 = 90+incl
    xp1 = 5
    yp1 = 0
    m1, c1 = line(a1, xp1, yp1)
    #line for hole
    a2 = 90+incl2
    xp2 = 0
    yp2 = 0
    m2, c2 = line(a2, xp2, yp2)
    #mirror line 1
    a3 = 90-incl
    xp3 = -5
    yp3 = 0
    m3, c3 = line(a3, xp3, yp3)
    #with fillet
    x = []
    y = []
    xc = []
    yc = []
    xh = []
    yh = []
    rf1 = 1.7
    rf2 = 2.1
    x1, y1, x2, y2 = filletBetweenCircleAndLine(xc1, yc1, r2, m1, c1, rf1, 1)
    if x1<x2:
        xc.append(x1)
        yc.append(y1)
    else:
        xc.append(x2)
        yc.append(y2)
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
    x19, y19, x20, y20 = intersectionCircleLine(xc1, yc1, r4, m2, c2)
    if y19<0:
        xh.append(x20)
        yh.append(y20)
    else:
        xh.append(x19)
        yh.append(y19)
    x13, y13, x14, y14 = intersectionCircleCircle(xh[0], yh[0], r5, xc1, yc1, r1)
    if y13>y14:
        x.append(x13)
        y.append(y13)
    else:
        x.append(x14)
        y.append(y14)
    x21, y21, x22, y22 = intersectionCircleLine(xh[0], yh[0], r5, m3, c3)
    if y21>y22:
        x.append(x22)
        y.append(y22)
    else:
        x.append(x21)
        y.append(y21)
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
    for i in range(n-1):
        angle = (i+1)*a
        for j in range(8):
            xt, yt = rotationAboutOrigin(angle, x[j], y[j])
            x.append(xt)
            y.append(yt)
        for j in range(4):
            xct, yct = rotationAboutOrigin(angle, xc[j], yc[j])
            xc.append(xct)
            yc.append(yct)
        xht, yht = rotationAboutOrigin(angle, xh[0], yh[0])
        xh.append(xht)
        yh.append(yht)
    for xi, yi in zip(x, y):
        plt.plot(xi, yi, "ro")
    for xci, yci in zip(xc, yc):
        plt.plot(xci, yci, "ko")
    for xhi, yhi in zip(xh, yh):
        plt.plot(xhi, yhi, "go")
    plt.axhline(0, color="black",linewidth=0.5)
    plt.axvline(0, color="black",linewidth=0.5)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.xlim([-15, 15])
    plt.ylim([-15, 15])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    #ansys
    for i in range(n):
        if i!=n-1:
            (
                sketch.arc(Point2D([x[0+i*8], y[0+i*8]], unit=UNITS.mm), Point2D([x[1+i*8], y[1+i*8]], unit=UNITS.mm), Point2D([xc[0+i*4], yc[0+i*4]], unit=UNITS.mm), clockwise=True).
                segment_to_point(Point2D([x[2+i*8], y[2+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[3+i*8], y[3+i*8]], unit=UNITS.mm), Point2D([xc[1+i*4], yc[1+i*4]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[4+i*8], y[4+i*8]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm)).
                arc_to_point(Point2D([x[5+i*8], y[5+i*8]], unit=UNITS.mm), Point2D([xh[i], yh[i]], unit=UNITS.mm), clockwise=True).
                segment_to_point(Point2D([x[6+i*8], y[6+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[7+i*8], y[7+i*8]], unit=UNITS.mm), Point2D([xc[3+i*4], yc[3+i*4]], unit=UNITS.mm), clockwise=True).
                arc_to_point(Point2D([x[8+i*8], y[8+i*8]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm))
            )
        else:
            (
                sketch.arc(Point2D([x[0+i*8], y[0+i*8]], unit=UNITS.mm), Point2D([x[1+i*8], y[1+i*8]], unit=UNITS.mm), Point2D([xc[0+i*4], yc[0+i*4]], unit=UNITS.mm), clockwise=True).
                segment_to_point(Point2D([x[2+i*8], y[2+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[3+i*8], y[3+i*8]], unit=UNITS.mm), Point2D([xc[1+i*4], yc[1+i*4]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[4+i*8], y[4+i*8]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm)).
                arc_to_point(Point2D([x[5+i*8], y[5+i*8]], unit=UNITS.mm), Point2D([xh[i], yh[i]], unit=UNITS.mm), clockwise=True).
                segment_to_point(Point2D([x[6+i*8], y[6+i*8]], unit=UNITS.mm)).
                arc_to_point(Point2D([x[7+i*8], y[7+i*8]], unit=UNITS.mm), Point2D([xc[3+i*4], yc[3+i*4]], unit=UNITS.mm), clockwise=True).
                arc_to_point(Point2D([x[0], y[0]], unit=UNITS.mm), Point2D([xc1, yc1], unit=UNITS.mm)).
                circle(Point2D([xc1, yc1], unit=UNITS.mm), Quantity(r3, UNITS.mm))
            )
    sketch.plot()
xc = 0
yc = 0
r_preload_backup_disc(xc, yc)
