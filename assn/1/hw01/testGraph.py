
from graphdrv import graph_drv
from var import var
from const import const
from pwr import pwr
from prod import prod
from deriv import deriv
from plus import plus
from tof import tof
from maker import make_pwr, make_const, make_pwr_expr
from deriv import deriv
from tof import tof
import numpy as np
import matplotlib.pyplot as plt
import math


fex = prod(mult1=const(val=2), 
		   mult2=pwr(base=var(name='x'), deg=const(val=5)))
print(fex)
graph_drv(fex, [-3, 3], [-50, 50])

fex = plus(elt1=plus(elt1=pwr(base=var(name='x'), deg=const(val=4)), 
					 elt2=pwr(base=var(name='x'), deg=const(val=3))), 
		   elt2=pwr(base=var(name='x'), deg=const(val=1)))
print(fex)
graph_drv(fex, [-3,3], [-10, 10])
