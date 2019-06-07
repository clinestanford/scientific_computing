
from deriv import *
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_pwr, make_pwr_expr
import math

fex = plus(elt1=pwr(base=var(name="x"), deg=const(val=4)), 
		   elt2=pwr(base=var(name="x"), deg=const(val=4)))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
fex = pwr(base=pwr(var(name='x'), deg=const(val=4)), deg=const(val=3))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
fex = pwr(base=plus(elt1=pwr(base=var(name='x'), deg=const(val=2)), elt2=pwr(base=var(name='x'), deg=const(val=3))), deg=const(val=4))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
fex = pwr(base=prod(mult1=const(val=5), mult2=pwr(base=var(name='x'), deg=const(val=3))), deg=const(val=3))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
fex = prod(mult1=const(val=5), mult2=const(val=6))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
fex = prod(mult1=const(val=3), mult2=plus(elt1=pwr(base=var(name='x'), deg=const(val=2)), elt2=pwr(base=var(name='x'), deg=const(val=1))))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
fex = prod(mult1=const(val=6), mult2=prod(mult1=const(val=3), mult2=pwr(var(name='x'), deg=const(val=4))))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
print('test 8:')
fex = prod(mult1=plus(elt1=pwr(base=var(name='x'), deg=const(val=2)), elt2=pwr(base=var(name='x'), deg=const(val=1))), mult2=const(val=3))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
print('test 9:')
fex = prod(mult1=pwr(base=var(name='x'), deg=const(val=4)), mult2=const(val=3))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()
print('test 10:')
fex = prod(mult1=prod(mult1=const(val=3), mult2=pwr(var(name='x'), deg=const(val=4))), mult2=const(val=6))
print("before: ", fex)
der = deriv(fex)
print("after:  ", der)
print()



