#!/usr/bin/python

####################################
# Your Name
# Your A#
####################################

from quot import quot
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import *
import math

def deriv(expr):
	if isinstance(expr, const):
		return const_deriv(expr)
	elif isinstance(expr, pwr):
		return pwr_deriv(expr)
	elif isinstance(expr, prod):
		return prod_deriv(expr)
	elif isinstance(expr, plus):
		return plus_deriv(expr)
	elif isinstance(expr, quot):
		return quot_deriv(expr)
	else:
		raise Exception('deriv:' + repr(expr))

# the derivative of a consant is 0.
def const_deriv(c):
	assert isinstance(c, const)
	return const(val=0.0)

def plus_deriv(s):
	# your code here
	assert isinstance(s, plus)
	if isinstance(s.get_elt1(), const):
		return deriv(s.get_elt2())
	elif isinstance(s.get_elt2(), const):
		return deriv(s.get_elt1())
	return plus(elt1=deriv(s.get_elt1()), elt2=deriv(s.get_elt2()))
	# my codes ends here

def pwr_deriv(p):
	assert isinstance(p, pwr)
	b = p.get_base()
	d = p.get_deg()
	if isinstance(b, var):
		if isinstance(d, const):
			left  = const(val=d.get_val())
			right = pwr(base=var(name=b.get_name()) , deg=const(d.get_val()-1))
			if d.get_val() == 0.0:
				return const(val = 0.0)
			return prod(mult1=left, mult2=right)
		else:
			raise Exception('pwr_deriv: case 1: ' + str(p))
	if isinstance(b, pwr):
		if isinstance(d, const):
			left  = prod(mult1=const(val=d.get_val()) ,mult2=pwr(base=b, deg=const(val=d.get_val()-1))) 
			right = deriv(b)
			return prod(mult1=left, mult2=right)
			pass
		else:
			raise Exception('pwr_deriv: case 2: ' + str(p))
	elif isinstance(b, plus):
		if isinstance(d, const):
			left  = prod(mult1=const(d.get_val()) , mult2=pwr(base=b, deg=const(d.get_val()-1)))
			right = deriv(b)
			return prod(mult1=left, mult2=right)
		else:
			raise Exception('pwr_deriv: case 3: ' + str(p))
	elif isinstance(b, prod):
		if isinstance(d, const):
			left  = prod(mult1=const(d.get_val()) , mult2=pwr(base=b, deg=const(d.get_val()-1)))
			right = deriv(b)
			return prod(mult1=left, mult2=right)
		else:
			raise Exception('pwr_deriv: case 4: ' + str(p))
	elif isinstance(b, quot):
		if isinstance(d, const):
			left = make_prod(make_const(d.get_val()), make_pwr_expr(b, d.get_val()-1))
			right = deriv(b)
			return make_prod(left, right)
		else:
			raise Exception('pwr_deriv: case 5: ' + str(p))

	else:
		raise Exception('power_deriv: case 6: ' + str(p))

def prod_deriv(p):
	assert isinstance(p, prod)
	m1 = p.get_mult1()
	m2 = p.get_mult2()
	if isinstance(m1, const):
		if isinstance(m2, const):
			return const(val=0)
		elif isinstance(m2, pwr):
			der = deriv(m2)
			if isinstance(der, prod):
				return make_prod(const(val=der.get_mult1().get_val() * m1.get_val()), der.get_mult2())
			else: 
				return prod(mult1=const(val=m1.get_val()), mult2=deriv(m2))
		elif isinstance(m2, plus):
			return deriv(plus(elt1=prod(mult1=const(val=m1.get_val()), mult2=m2.get_elt1()), 
							  elt2=prod(mult1=const(m1.get_val()), mult2=m2.get_elt2())))
		elif isinstance(m2, prod):
			return prod(mult1=const(m1.get_val()),
						mult2=deriv(m2))
		elif isinstance(m2, quot):
			return make_prod(m1, deriv(m2))
		else:
			raise Exception('prod_deriv: case 0' + str(p))
	elif isinstance(m1, plus):
		if isinstance(m2, const):
			return deriv(plus(elt1=prod(mult1=const(val=m2.get_val()), mult2=m1.get_elt1()), 
							  elt2=prod(mult1=const(m2.get_val()), mult2=m1.get_elt2())))
		elif isinstance(m2, plus) or isinstance(m2, prod) or isinstance(m2, pwr) or isinstance(m2, quot):
			return product_rule(m1, m2) 
		else:
			raise Exception('prod_deriv: case 1:' + str(p))
	elif isinstance(m1, pwr):
		if isinstance(m2, const):
			return prod(mult1=deriv(m1), mult2=const(val=m2.get_val()))
		elif isinstance(m2, plus) or isinstance(m2, prod) or isinstance(m2, pwr) or isinstance(m2, quot):
			return product_rule(m1, m2)
		else:
			raise Exception('prod_deriv: case 2:' + str(p))
	elif isinstance(m1, prod):
		if isinstance(m2, const):
			return prod(mult1=deriv(m1), mult2=const(m2.get_val()))
		elif isinstance(m2, plus) or isinstance(m2, prod) or isinstance(m2, pwr) or isinstance(m2, quot):
			return product_rule(m1, m2)
		else:
			raise Exception('prod_deriv: case 3:' + str(p))
	elif isinstance(m1, quot):
		if isinstance(m2, const):
			return make_prod(deriv(m1), m2)
		elif isinstance(m2, plus) or isinstance(m2, prod) or isinstance(m2, pwr) or isinstance(m2, quot):
			return product_rule(m1, m2)
		else:
			raise Exception('prod_deriv: case 4:' + str(p))
	else:
	   raise Exception('prod_deriv: case 5:' + str(p))


# sum and a sum, a sum and a power, a sum and a product, a sum and a
# quotient, a power and a sum, a power and a power, a power and a product, a
# power and a quotient, a product and a sum, a product and a power, a product
# and a product, a product and a quotient, a quotient and a sum, a quotient
# and a power, a quotient and a product, and a quotient and a quotient



def product_rule(expr1, expr2):
	return make_plus(make_prod(deriv(expr1), expr2), make_prod(expr1, deriv(expr2)))

def quot_deriv(expr):
	assert isinstance(expr, quot)
	deriv_top = deriv(expr.get_num())
	deriv_bot = deriv(expr.get_denom())

	top_left = make_prod(deriv_top, expr.get_denom())
	top_right = make_prod(make_prod(make_const(-1), deriv_bot), expr.get_num())
	top = make_plus(top_left, top_right)
	bottom = make_pwr_expr(expr.get_denom(), 2)

	return make_quot(top, bottom)



