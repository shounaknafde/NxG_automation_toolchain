from ansys.geometry.core.math import Point2D, UNITVECTOR3D_Z
from ansys.geometry.core.misc import UNITS
from ansys.geometry.core.sketch import Sketch
from pint import Quantity
from ansys.geometry.core import launch_modeler_with_discovery
#modeler = launch_modeler_with_discovery()
sketch = Sketch()#modeler.create_sketch()
def circular_backup(xc, yc, r2):
    #inner radius
    r1 = 3.25
    #outer radius
    #from ansys.geometry.core import launch_modeler_with_discovery
    (
        sketch.circle(Point2D([xc, yc], unit=UNITS.mm), Quantity(r2, UNITS.mm)).
        circle(Point2D([xc, yc], unit=UNITS.mm), Quantity(r1, UNITS.mm))
    )
    sketch.plot()
xc = 0
yc = 0
r2 = 12
circular_backup(xc, yc, r2)
