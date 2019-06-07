#!/usr/bin/python

############################################
# module: poly12.py
# YOUR NAME
# YOUR A#
############################################

from prod import prod
from const import const
from pwr import pwr
from plus import plus
from var import var
from deriv import deriv
from tof import tof
import math

def quadratic(a, b, c):
	quad = math.sqrt(b**2 - 4 * a * c)
	return ((-b+quad)/(2*a), (-b-quad)/(2*a))

def get_pwr_2_el(expr):
	if isinstance(expr, prod) and isinstance(expr.get_mult2(), pwr) and expr.get_mult2().get_deg().get_val() == 2:
		return expr.get_mult1().get_val()
	elif isinstance(expr, pwr) and expr.get_deg().get_val() == 2:
		return 1.0
	else:
		try:
			return get_pwr_2_el(expr.get_elt1()) or get_pwr_2_el(expr.get_elt2())
		except AttributeError:
			pass

def get_pwr_1_el(expr):
	if isinstance(expr, prod) and isinstance(expr.get_mult2(), pwr) and expr.get_mult2().get_deg().get_val() == 1:
		return expr.get_mult1().get_val()
	elif isinstance(expr, pwr) and expr.get_deg().get_val() == 1:
		return 1.0
	else:
		try:
			return get_pwr_1_el(expr.get_elt1()) or get_pwr_1_el(expr.get_elt2())
		except AttributeError:
			pass

def get_pwr_0_el(expr):
	if isinstance(expr, prod) and isinstance(expr.get_mult2(), pwr) and expr.get_mult2().get_deg().get_val() == 0:
		return expr.get_mult1().get_val()
	elif isinstance(expr, const):
		return expr.get_val()
	else:
		try:
			return get_pwr_0_el(expr.get_elt2()) or get_pwr_0_el(expr.get_elt1())
		except AttributeError:
			pass

def find_poly_1_zeros(expr):
	denom = get_pwr_1_el(expr)
	num = get_pwr_0_el(expr)
	
	return const(val=-num/denom)

def find_poly_2_zeros(expr):

	second = expr.get_elt2()
	first = expr.get_elt1()
	a = get_pwr_2_el(expr)
	b = get_pwr_1_el(expr)
	c = get_pwr_0_el(expr)

	if c == None:
		c = 0

	return quadratic(a, b, c)

	
	
	
			
	




