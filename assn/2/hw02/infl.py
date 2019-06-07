#!/usr/bin/python

#######################################
# module: infl.py
# YOUR NAME
# YOUR A#
#######################################

from const import const
from deriv import deriv
from poly12 import find_poly_1_zeros
from tof import tof
from point2d import point2d
from plus import plus
from prod import prod
from pwr import pwr
from maker import make_point2d

def get_highest_power(expr):
	el1 = expr.get_elt1()
	while isinstance(el1, plus):
		el1 = el1.get_elt1()
	if isinstance(el1, prod):
		return el1.get_mult2().get_deg()
	elif isinstance(el1, pwr):
		return el1.get_deg()

def test_zeros(zeros, expr, second_der):
	f_expr = tof(expr)
	f_der = tof(second_der)
	sol = []
	for z in zeros:
		val = z.get_val()
		if f_der(val - .1) < 0 and f_der(val + .1) > 0:
			sol.append(make_point2d(val, f_expr(val)))
		elif f_der(val - .1) > 0 and f_der(val + .1) < 0:
			sol.append(make_point2d(val, f_expr(val)))
	if not sol:
		return None
	else:
		return sol

def find_infl_pnts(expr):
	p = get_highest_power(expr).get_val()
	der = deriv(expr)
	second_der = deriv(der)
	zeros = []
	if p == 3:
		zeros = [find_poly_1_zeros(second_der)]
	elif p < 3:
		raise Exception("needed a function of at least deg 3")
	return test_zeros(zeros, expr, second_der)
