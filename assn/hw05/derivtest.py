#!/usr/bin/python

#########################################
# module: derivtest.py
# YOUR NAME
# YOUR A#
#########################################

from maker import *
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from deriv import deriv
from poly12 import find_poly_1_zeros
from poly12 import find_poly_2_zeros
from tof import tof
from point2d import point2d

ERR = 0.000001

def get_highest_power(expr):
	el1 = expr.get_elt1()
	while isinstance(el1, plus):
		el1 = el1.get_elt1()
	if isinstance(el1, prod):
		return el1.get_mult2().get_deg()
	elif isinstance(el1, pwr):
		return el1.get_deg()

def test_zeros(zeros, expr, der):
	f_expr = tof(expr)
	f_der = tof(der)
	sol = []
	for z in zeros:
		if f_der(z - .1) < 0 and f_der(z + .1) > 0:
			sol.append(('min', make_point2d(z, f_expr(z))))
		elif f_der(z - .1) > 0 and f_der(z + .1) < 0:
			sol.append(('max', make_point2d(z, f_expr(z))))
	if not sol:
		return None
	else:
		return sol

def second_der_test_zero_3_deg(possible_z, der, expr):
	second_der = deriv(der)
	f = tof(expr)
	sol = []
	for z in possible_z:
		if f_sec_der(z) > 0:
			sol.append(("min", make_point2d(z, f(z))))
		elif f_sec_der(z) < 0:
			sol.append(("max", make_point2d(z, f(z))))
	if not sol:
		return None
	else:
		return sol

def second_der_test_zero_2_deg(possible_z, der, expr):
	second_der = deriv(der)
	f = tof(expr)
	if isinstance(second_der, plus):
		second_der = second_der.get_elt1()
	if isinstance(second_der, prod):
		val = second_der.get_mult1()
		zero = possible_z.get_val()
		if isinstance(val, const):
			if val.get_val() > 0:
				return ("min", make_point2d(zero, f(zero)))
			elif val.get_val() < 0:
				return ("max", make_point2d(zero, f(zero)))


def handle_3_deg(expr):
	der = deriv(expr)
	possible_z = find_poly_2_zeros(der)
	return test_zeros(possible_z, expr, der)

def handle_2_deg(expr):
	der = deriv(expr)
	possible_z = find_poly_1_zeros(der)
	return test_zeros(possible_z, expr, der)

def second_der_handle_3(expr):
	der = deriv(expr)
	possible_z = find_poly_2_zeros(der)
	return second_der_test_zero(possible_z, der, expr)

def second_der_handle_2(expr):
	der = deriv(expr)
	possible_z = find_poly_1_zeros(der)
	return second_der_test_zero_2_deg(possible_z, der, expr)

def loc_xtrm_1st_drv_test(expr):
	p = int(get_highest_power(expr).get_val())
	local_xtrm = []
	if p == 3:
		local_xtrm = handle_3_deg(expr)
	elif p == 2:
		local_xtrm = handle_2_deg(expr)
	return local_xtrm

def loc_xtrm_2nd_drv_test(expr):
	p = int(get_highest_power(expr).get_val())
	local_xtrm = []
	if p == 3:
		local_xtrm = second_der_handle_3(expr)
	elif p == 2:
		local_xtrm = second_der_handle_2(expr)
	return local_xtrm

