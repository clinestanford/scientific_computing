


from maker import *
from deriv import deriv, logdiff
from tof import *

from quot import quot
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from ln import ln
from absv import absv
from maker import *

import math
import numpy as np 
import matplotlib.pyplot as plt

func = make_plus(make_pwr('x', 1), make_const(1))
func1 = make_plus(make_prod(make_const(2), make_pwr('x', 1)), make_const(1))
func2 = make_plus(make_prod(make_const(3), make_pwr('x', 1)), make_const(1))

prod1 = make_prod(func, func1)
num = make_prod(prod1, func2)

denom = make_pwr_expr(make_plus(make_prod(make_const(4), make_pwr('x', 1)), make_const(1)), make_const(-.5))

expr = make_quot(num, denom)

print(expr)

def fun(expr, xlim, ylim):
	assert(isinstance(expr, quot))
	num = expr.get_num()
	denom = expr.get_denom()

	der_top = logdiff(num)
	der_bot = deriv(denom)
	
	top = make_plus(make_prod(der_top, denom), make_prod(make_const(-1), make_prod(der_bot, num)))
	print(top)
	bottom = make_pwr_expr(denom, 2)
	print(bottom)

	f_prime = make_quot(top, bottom)	

	der = f_prime
	eqF  = tof(expr)
	derF = tof(der)
	xvals = np.linspace(xlim[0], xlim[1], 10000)
	yvals1 = np.array([eqF(i) for i in xvals])
	yvals2 = np.array([derF(i) for i in xvals])
	fig1 = plt.figure(1)
	fig1.suptitle("f(x) and f'(x)")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.ylim(ylim[0], ylim[1])
	plt.xlim(xlim[0], xlim[1])
	plt.grid()
	plt.plot(xvals, yvals1, label="f(x)="+str(expr), c='r')
	plt.plot(xvals, yvals2, label="f'(x)="+str(der), c='b')
	plt.legend(loc='best')
	plt.show(block=True)


	return True

xlim = [-5, 5]
ylim = [-10, 10]

print(fun(expr, xlim, ylim))



