#!/usr/bin/python


###########################################
# module: tof.py
# Your Name
# Your A#
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from absv import absv
from maker import *
import math

def tof(expr):
	if isinstance(expr, const):
		return const_tof(expr)
	elif isinstance(expr, pwr):
		return pwr_tof(expr)
	elif isinstance(expr, prod):
		return prod_tof(expr)
	elif isinstance(expr, plus):
		return plus_tof(expr)
	elif isinstance(expr, quot):
		return quot_tof(expr)
	elif isinstance(expr, ln):
		return ln_tof(expr)
	elif isinstance(expr, absv):
		return absv_tof(expr)
	else:
		print(type(expr))
		raise Exception('tof: ' + str(expr))

## here is how you can implement converting
## a constant to a function.
def const_tof(c):
	assert isinstance(c, const)
	def f(x):
		return c.get_val()
	return f

def pwr_tof(expr):
	assert isinstance(expr, pwr)
	expb = expr.get_base()
	d = expr.get_deg()
	if isinstance(expb, const):
		if isinstance(d, const):
		# your code here
		# test 1
			print(type(expb.get_val()), type(d.get_val()), type(d), d)
			return lambda x: expb.get_val() ** d.get_val()
		# my code ends here
		# pass

		elif isinstance(d, prod) or isinstance(d, plus) \
				or isinstance(d, pwr) or isinstance(d, quot) \
				or isinstance(d, ln) or isinstance(d, absv):
			return lambda x: expb.get_val() ** tof(d)(x)
		else:
			raise Exception("wasn't raising to a constant")

	elif isinstance(expb, var):
		if isinstance(d, const):
			if isinstance(d.get_val(), const):
				print(d)
			# your code here
			# test 2
			return lambda x: x ** d.get_val()
			# my code ends here
			# pass
		else:
			raise Exception('pw_tof: case 1:' + str(expr))
	elif isinstance(expb, plus):
		if isinstance(d, const):
			# your code here
			# test 3
			return lambda x: (tof(expb.get_elt1())(x) + tof(expb.get_elt2())(x)) ** d.get_val() 
			# my code ends here
			# pass
		else:
			raise Exception('pw_tof: case 2:' + str(expr))
	elif isinstance(expb, pwr):
		if isinstance(d, const):
			# your code here
			# test 4
			return lambda x: tof(expb)(x) ** d.get_val()
			# my code ends here
			# pass
		else:
			raise Exception('pw_tof: case 3:' + str(expr))
	elif isinstance(expb, prod):
		if isinstance(d, const):
			return lambda x: (tof(expb.get_mult1())(x) * tof(expb.get_mult2())(x)) ** d.get_val()
		else:
			raise Exception('pw_tof: case 4:' + str(expr))
	elif isinstance(expb, quot):
		if isinstance(d, const):
			return lambda x: (tof(expb)(x)) ** d.get_val()

	elif isinstance(expb, ln):
		if isinstance(d, const):
			return lambda x: (tof(expb)(x)) ** d.get_val()

		elif isinstance(d, pwr):
			return lambda x: (tof(expb)(x)) ** tof(d)(x)
			
	else:
		raise Exception('pw_tof: case 5:' + str(expr))

def prod_tof(expr):
	return lambda x: tof(expr.get_mult1())(x) * tof(expr.get_mult2())(x)

def plus_tof(expr):
	return lambda x: tof(expr.get_elt1())(x) + tof(expr.get_elt2())(x)
	
def quot_tof(expr):
	assert isinstance(expr, quot)
	def divide_expr(x):
		num = tof(expr.get_num())(x)
		denom = tof(expr.get_denom())(x)
		if denom == 0:
			return 0
		else:
			return num / denom
	#return lambda x: (tof(expr.get_num())(x)) / (tof(expr.get_denom())(x))
	return divide_expr

def ln_tof(expr):
	assert isinstance(expr, ln)
	return lambda x: math.log(tof(expr.get_expr())(x), math.e)

def absv_tof(expr):
	assert isinstance(expr, absv)
	return lambda x: tof(expr.get_expr())(abs(x))