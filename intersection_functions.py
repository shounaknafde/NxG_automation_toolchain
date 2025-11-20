import math
import numpy as np
import matplotlib.pyplot as plt
#line passing through a point(x1, y1)
def line(slope, x1, y1):
    m = float(format(math.tan(math.radians(slope)), ".6f"))
    c = float(format(y1-m*x1, ".6f"))
    return m, c
#test case
'''slope = 70
x1 = 3
y1 = 0
m, c = line(slope, x1, y1)
print(m, c)'''
#circle and line
def intersectionCircleLine(xc, yc, R, m, c):
    A = (1+m**2)
    B = (-2*(xc+m*(yc-c)))
    C = (xc**2+yc**2+c**2-2*c*yc-R**2)
    D = (B**2-4*A*C)
    if D<0 and D<-0.001:
        print("No real roots, do not intersect")
        return None, None, None, None
    elif (D<0 and D>=-0.001) or (D>0 and D<=0.001):
        D = 0
    x1 = float(format(((-B+math.sqrt(D))/(2*A)), ".6f"))
    y1 = float(format((m*x1+c), ".6f"))
    x2 = float(format(((-B-math.sqrt(D))/(2*A)), ".6f"))
    y2 = float(format((m*x2+c), ".6f"))
    return x1, y1, x2, y2
#test case
'''xc = 5.931979
yc = 4.254600
R = 1.3
m = 2.747477
c = -8.242432
x1, y1, x2, y2 = intersectionCircleLine(xc, yc, R, m, c)
print(x1, y1, x2, y2)'''
#point on a circle between two other points
def midOfTwoPointsOnACircle(xc, yc, R, x1, y1, x2, y2):
    x = ((x1+x2)/2 - xc)
    y = ((y1+y2)/2 - yc)
    dis = math.sqrt(x**2+y**2)
    xm = xc+x*R/dis
    ym = yc+y*R/dis
    return xm, ym
#circle and circle
def intersectionCircleCircle(xc1, yc1, R1, xc2, yc2, R2):
    R = (xc2-xc1)**2+(yc2-yc1)**2
    if R==0:
        print("Concentric Circles")
        return None, None, None, None
    A = (R1**2-R2**2)/2/R
    val = ( 2*(R1**2+R2**2)/R - (R1**2-R2**2)**2/(R**2) - 1)
    if val<0 and val<-0.001:
        print("No real roots, do not intersect")
        return None, None, None, None
    elif val<0 and val>=-0.001:
        val = 0
    B1 = float(format((math.sqrt(val)/2), ".6f"))
    B2 = float(format((math.sqrt(val)/2), ".6f"))
    x1 = float(format(((xc1+xc2)/2+A*(xc2-xc1)+B1*(yc2-yc1)), ".6f"))
    y1 = float(format(((yc1+yc2)/2+A*(yc2-yc1)+B1*(xc1-xc2)), ".6f"))
    x2 = float(format(((xc1+xc2)/2+A*(xc2-xc1)+B2*(yc2-yc1)), ".6f"))
    y2 = float(format(((yc1+yc2)/2+A*(yc2-yc1)+B2*(xc1-xc2)), ".6f"))
    return x1, y1, x2, y2
#test case
'''xc1 = 0
yc1 = 0
R1 = 6
xc2 = 5.931979
yc2 = 4.254600
R2 = 1.3
x1, y1, x2, y2 = intersectionCircleCircle(xc1, yc1, R1, xc2, yc2, R2)
print(x1, y1, x2, y2)'''
#3 point circle
def cirle3Point(x1, y1, x2, y2, x3, y3):
    A = float(format((x1*(y2-y3)-y1*(x2-x3)+x2*y3-x3*y2), ".6f"))
    B = float(format(((x1**2+y1**2)*(y3-y2)+(x2**2+y2**2)*(y1-y3)+(x3**2+y3**2)*(y2-y1)), ".6f"))
    C = float(format(((x1**2+y1**2)*(x2-x3)+(x2**2+y2**2)*(x3-x1)+(x3**2+y3**2)*(x1-x2)), ".6f"))
    D = float(format(((x1**2+y1**2)*(x3*y2-x2*y3)+(x2**2+y2**2)*(x1*y3-x3*y1)+(x3**2+y3**2)*(x2*y1-x1*y2)), ".6f"))
    xc = float(format((-B/(2*A)), ".6f"))
    yc = float(format((-C/(2*A)), ".6f"))
    rc = float(format((math.sqrt((B**2+C**2-4*A*D)/(4*A**2))), ".6f"))
    return xc, yc, rc
#intersection between lines
def intersectionBetweenLines(m1, c1, m2, c2):
    if (m1!=m2):
        xp = float(format(((c1-c2)/(m2-m1)), ".6f"))
        yp = float(format(((m2*c1-m1*c2)/(m2-m1)), ".6f"))
    else:
        print("Parallel lines")
        return None, None
    return xp, yp
