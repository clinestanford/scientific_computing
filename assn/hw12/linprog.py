#!/usr/bin/python

###################################
# module: linprog.py
# YOUR NAME
# YOUR A#
###################################

## your imports

from line_eq import line_eq
from maker import make_line_eq
from maker import make_var, make_const, make_prod
from maker import make_pwr, make_plus
from maker import make_point2d
from const import const
from var import var
from prod import prod
from pwr import pwr
#from poly12 import is_pwr_1
from plus import plus
from tof import tof
import sys
import numpy as np

### sample line equations
lneq1 = make_line_eq(make_var('y'),
										 make_const(2))
lneq2 = make_line_eq(make_var('y'),
										 make_var('x'))
lneq3 = make_line_eq(make_var('y'),
										 make_var('y'))
lneq4 = make_line_eq(make_var('y'),
										 make_prod(make_const(2.0),
															 make_pwr('x', 1.0)))
lneq5 = make_line_eq(make_var('y'),
										 make_prod(make_const(5.0),
															 make_pwr('y', 1.0)))
lneq6 = make_line_eq(make_var('y'),
										 make_plus(make_prod(make_const(5.0),
																				 make_pwr('x', 1.0)),
															 make_const(4.0)))
lneq7 = make_line_eq(make_var('y'),
										 make_plus(make_prod(make_const(5.0),
																				 make_pwr('y', 1.0)),
															 make_const(4.0)))
lneq8 = make_line_eq(make_var('y'),
										 make_plus(make_prod(make_const(3.0),
																				 make_pwr('x', 1.0)),
															 make_const(-4.0)))

def has_var(eqn):
	if isinstance(eqn, var):
		return True
	elif isinstance(eqn, pwr):
		return has_var(eqn.get_base())
	elif isinstance(eqn, prod):
		return has_var(eqn.get_mult1()) or has_var(eqn.get_mult2())
	else:
		return False


def get_single_cof(eqn):
	x = 0
	if isinstance(eqn, var):
		x = 1
	elif isinstance(eqn, pwr):
		x = 1
	elif isinstance(eqn, const):
		x = eqn.get_val()
	elif isinstance(eqn, prod):
		if isinstance(eqn.get_mult2(), var):
			x = eqn.get_mult1().get_val()
		elif  isinstance(eqn.get_mult2(), pwr) and isinstance(eqn.get_mult2().get_base(), var):
			x = eqn.get_mult1().get_val()
	return make_const(x)

##this function assumes the right hand side is ax + b of some kind
def get_coefficients(lhs, rhs):
	y1, x1, x2 = make_const(0), make_const(0), make_const(0)

	if isinstance(lhs, var):
		if lhs.get_name() == 'x':
			x1 = make_const(1 * -1)
			if isinstance(rhs, const):
				x2 = rhs
				##this should handle the case where x = 4
				return y1.get_val(), x1.get_val(), x2.get_val()
		else:
			y1 = make_const(1)

	if isinstance(rhs, const):
		x2 = rhs
	elif isinstance(rhs, pwr):
		x1 = make_const(1) #this is the value in front of x
	elif isinstance(rhs, prod):
		if has_var(rhs):
			x1 = get_single_cof(rhs)
		else:
			x2 = get_single_cof(rhs)
	elif isinstance(rhs, plus):
		if has_var(rhs.get_elt1()):
			x1 = get_single_cof(rhs.get_elt1())
			x2 = get_single_cof(rhs.get_elt2())
		elif has_var(rhs.get_elt2()):
			x2 = get_single_cof(rhs.get_elt1())
			x1 = get_single_cof(rhs.get_elt2())

	return y1.get_val(), x1.get_val(), x2.get_val()


def line_intersection(lneq1, lneq2):

	print(lneq1)
	print(lneq2)
	
	ay1, ax1, ax2 = get_coefficients(lneq1.get_lhs(), lneq1.get_rhs())
	by1, bx1, bx2 = get_coefficients(lneq2.get_lhs(), lneq2.get_rhs())

	A = np.array([[ax1*-1, ay1],[bx1*-1, by1]])

	b = np.array([ax2, bx2])

	print(A, b)

	x = np.linalg.solve(A, b)

	assert np.allclose(np.dot(A, x), b)	

	return make_point2d(x[0], x[1]) #do not need to convert to const, maker already does that.



		
### a few tests

def test_01():
	ln1 = make_line_eq(make_var('y'), make_const(1.0))
	ln2 = make_line_eq(make_var('x'), make_const(1.0))
	# assert is_const_line(ln1)
	# assert is_const_line(ln2)
	print(line_intersection(ln1, ln2))

def test_02():
	ln1 = make_line_eq(make_var('y'), make_const(2.0))
	ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
																							make_const(-6.0)))
	print(line_intersection(ln1, ln2))
	print(line_intersection(ln2, ln1))

def test_03():
	ln1 = make_line_eq(make_var('y'), make_const(-2.0))
	ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
																							make_const(10.0)))
	print(line_intersection(ln1, ln2))
	print(line_intersection(ln2, ln1))

def test_04():
	ln1 = make_line_eq(make_var('y'), make_const(2.0))
	ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(2.0),
																												make_pwr('x', 1.0)),
																							make_const(-6.0)))
	print(line_intersection(ln1, ln2))
	print(line_intersection(ln2, ln1))

def test_05():
	ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
	ln2 = make_line_eq(make_var('y'), make_prod(make_const(2.0),
																							make_pwr('x', 1.0)))
	ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(3.0),
														make_pwr('x', 1.0)),
														make_const(-10.0)))

	print(line_intersection(ln1, ln3))
	

def test_06():
	ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
	ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
														make_pwr('x', 1.0)),
														make_const(6.0)))
	print(line_intersection(ln1, ln2))

def test_07():
	ln1 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0/5.0),
																												make_pwr('x', 1.0)),
																							make_const(10.0)))
	ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(1.0/5.0),
														make_pwr('x', 1.0)),
														make_const(5.0)))
	print(line_intersection(ln1, ln2))

def test_08():
	ln1 = make_line_eq(make_var('y'), make_const(1.0))
	ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
																												make_pwr('x', 1.0)),
																							make_const(6.0)))
	print(line_intersection(ln1, ln2))

def test_09():
	ln1 = make_line_eq(make_var('y'), make_const(5.0))
	ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
																												make_pwr('x', 1.0)),
																							make_const(6.0)))
	print(line_intersection(ln1, ln2))

def maximize_obj_fun(f, corner_points):
	
	max_x, max_y, val = 0, 0, 0
	for point in corner_points:
		temp = f(point.get_x().get_val(), point.get_y().get_val())
		if temp > val:
			max_x = point.get_x().get_val()
			max_y = point.get_y().get_val()
			val = temp

	return (make_point2d(max_x, max_y), make_const(val))


def minimize_obj_fun(f, corner_points):

	max_x, max_y, val = 0, 0, 1e8
	for point in corner_points:
		temp = f(point.get_x().get_val(), point.get_y().get_val())
		if temp < val:
			max_x = point.get_x().get_val()
			max_y = point.get_y().get_val()
			val = temp

	return (make_point2d(max_x, max_y), make_const(val))

def test_10():
	f1 = lambda x, y: 2*x + y
	corner_points = [make_point2d(1, 1),
									 make_point2d(1, 5),
									 make_point2d(5, 1)]
	p, val = maximize_obj_fun(f1, corner_points)
	print(p, val)
	f2 = lambda x, y: x - 2*y
	p, val = minimize_obj_fun(f2, corner_points)
	print(p, val)
	
def test_11():
	ln1 = make_line_eq(make_var('x'), make_const(1.0))
	ln2 = make_line_eq(make_var('y'), make_prod(make_const(0.5),
																						 make_pwr('x', 1.0)))
	print(line_intersection(ln1, ln2))
	ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-3.0/4),
																												make_pwr('x', 1.0)),
																							make_const(3.0)))
	print(line_intersection(ln1, ln3))
	print(line_intersection(ln2, ln3))


def test_12():
	ln1 = make_line_eq(make_var('x'), make_const(0.0))
	ln2 = make_line_eq(make_var('y'), make_const(0.0))
	ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-4.0/3),
																												make_pwr('x', 1.0)),
																							make_const(160.0)))
	ln4 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-0.5),
																												make_pwr('x', 1.0)),
																							make_const(120.0)))
	print(ln1)
	print(ln3)
	print(line_intersection(ln1, ln3))
	print(ln2)
	print(ln3)
	print(line_intersection(ln2, ln3))
	print(line_intersection(ln3, ln4))

## write your answer to problem 1a as x, y, mv
## max: (5, 1) val = 11.0
def opt_prob_1a():

	ln1 = make_line_eq(make_var('y'), make_const(5.0))
	ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1),make_pwr('x', 1.0)),
												make_const(6.0)))
	ln3 = make_line_eq(make_var('x'), make_const(1.0))
	ln4 = make_line_eq(make_var('y'), make_const(1.0))

	##the entire area will be bounded by these values.
	p1 = line_intersection(ln1, ln2)
	p2 = line_intersection(ln2, ln4)
	p3 = line_intersection(ln3, ln4)
	f = lambda x,y: 2*x + y 
	corner_points = [p1,p2,p3]

	p_max, val_max = maximize_obj_fun(f, corner_points)
	print('max: ', p_max, val_max)

## write your answer to problem 1b as x, y, mv
## min: (0,2) val = 2
def opt_prob_1b():
	ln1 = make_line_eq(make_var('y'), make_const(2.0))
	ln2 = make_line_eq(make_var('x'), make_const(0.0))
	ln3 = make_line_eq(make_var('y'), make_pwr('x', 1))
	ln4 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1),make_pwr('x', 1.0)),
												make_const(6.0)))

	p1 = line_intersection(ln1, ln2)
	p2 = line_intersection(ln1, ln3)
	p3 = line_intersection(ln2, ln4)
	p4 = line_intersection(ln3, ln4)

	f = lambda x, y: x/2 + y 

	corner_points = [p1, p2, p3, p4]

	p, val = minimize_obj_fun(f, corner_points)
	print(p, val)


## write your answer to problem 1c as x, y, mv
## max (2.5, 2.5) val = 2.5
def opt_prob_1c():
	ln1 = make_line_eq(make_var('y'), make_pwr('x', 1))
	ln2 = make_line_eq(make_var('y'), make_prod(make_const(-1), make_pwr('x', 1)))
	ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(.5), make_pwr('x', 1)), make_const(1.25)))

	p1 = line_intersection(ln1, ln2)
	p2 = line_intersection(ln1, ln3)
	p3 = line_intersection(ln2, ln3)

	corner_points = [p1, p2, p3]

	f = lambda x,y: 3*x - 2*y

	p, val = maximize_obj_fun(f, corner_points)	

	print(p, val)																	

if __name__ == '__main__':
	opt_prob_1c()