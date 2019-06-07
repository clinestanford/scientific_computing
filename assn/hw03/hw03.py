#!/usr/bin/python

#######################################
# module: hw03.py
# YOUR NAME
# YOUR A#
#######################################

# place all necessary imports here.
#
# I placed the updated version of maker.py
# Use it as you see fit.

from poly12 import find_poly_2_zeros
from maker import *
from deriv import deriv
from tof import tof

def get_power_coef(expr, pow):
	if isinstance(expr, pwr) and expr.get_deg().get_val() == pow:
		return 1
	elif isinstance(expr, prod) and isinstance(expr.get_mult2(), pwr) and expr.get_mult2().get_deg().get_val() == pow:
		return expr.get_mult1().get_val()
	elif isinstance(expr, const) and pow == 0:
		return expr.get_val()
	else:
		try:
			return get_power_coef(expr.get_elt1(), pow) or get_power_coef(expr.get_elt2(), pow)
		except AttributeError:
			pass
def maximize_revenue(dmnd_eq, constraint=lambda x: x >= 0):
	f = tof(dmnd_eq)
	two = get_power_coef(dmnd_eq, 2)
	one = get_power_coef(dmnd_eq, 1)
	zero = get_power_coef(dmnd_eq, 0)
	twoE = make_prod(make_const(two), make_pwr('x', 3))
	oneE = make_prod(make_const(one), make_pwr('x', 2))
	zeroE = make_prod(make_const(zero), make_pwr('x', 1))
	e1 = make_plus(twoE, oneE)
	e2 = make_plus(e1, zeroE)
	revF = tof(e2)
	zeros = find_poly_2_zeros(deriv(e2))
	# [z, rev, price]
	maxRev = [0.0, 0, 0]
	for z in zeros:
		if constraint(z):
			if revF(z) > maxRev[1]:
				maxRev[0] = z
				maxRev[1] = revF(z)
				maxRev[2] = f(z)

	return (maxRev[0], maxRev[1], maxRev[2])

def dydt_given_x_dxdt(yt, x, dxdt):
	# your code here
	der = deriv(yt)
	derF = tof(der)
	return make_const(derF(x.get_val())*dxdt.get_val())

def oil_disk_test():
	yt = make_prod(make_const(0.02*math.pi),
					make_pwr('r', 2.0))
	print(yt)
	dydt = dydt_given_x_dxdt(yt, make_const(150.0),
							 make_const(20.0))
	assert not dydt is None
	assert isinstance(dydt, const)
	print(dydt)

def arm_tumor_test():
	expr = make_prod(make_const(math.pi*.003), make_pwr('x', 3))
	print(expr)
	x = 10.3
	dxdt = -1.75
	dydt = dydt_given_x_dxdt(expr, make_const(x), make_const(dxdt))
	assert not dydt is None
	assert isinstance(dydt, const)
	print(dydt)
	return dydt
	
