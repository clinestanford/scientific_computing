


from tof import *
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_pwr, make_pwr_expr
import math

def test(f, lam):
	for i in range(1000):
		if f(i) != lam(i):
			return False
	return True

fex = pwr(base=const(val=4), deg=const(val=5))
tf = tof(fex)
tempLambda = lambda x: 4 ** 5
print("test 1:")
print(test(tf, tempLambda))

fex = pwr(base=var(name='x'), deg=const(val=2))
tf = tof(fex)
tempLambda = lambda x: x ** 2
print("test 2:")
print(test(tf, tempLambda))

fex = pwr(base=plus(elt1=pwr(base=var(name='x'), deg=const(2)), elt2=const(val=4)), deg=const(val=3))
tf = tof(fex)
tempLambda = lambda x: ((x ** 2) + 4) ** 3
print("test 3:")
print(test(tf, tempLambda))

fex = pwr(base=pwr(base=var(name='x'), deg=const(val=4)), deg=const(val=2))
tf = tof(fex)
tempLambda = lambda x: (x ** 4) ** 2
print("test 4:")
print(test(tf, tempLambda))

fex = pwr(base=prod(mult1=const(val=5), mult2=pwr(base=var(name='x'), deg=const(val=3))), deg=const(val=2))
tf = tof(fex)
tempLambda = lambda x: (5 *  x ** 3) ** 2
print("test 5:")
print(test(tf, tempLambda))

fex = prod(mult1=const(val=5), mult2=pwr(base=var(name='x'), deg=const(val=3)))
tf = tof(fex)
tempLambda = lambda x: (5 *  x ** 3)
print("test 6:")
print(test(tf, tempLambda))

fex = plus(elt1=const(val=5), elt2=pwr(base=var(name='x'), deg=const(val=3)))
tf = tof(fex)
tempLambda = lambda x: (5 +  x ** 3)
print("test 6:")
print(test(tf, tempLambda))
