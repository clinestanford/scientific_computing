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
from ln import ln
from absv import absv
from maker import *
import math

ERR = .000001

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
	elif isinstance(expr, ln):
		return ln_deriv(expr)
	else:
		raise Exception('deriv:' + repr(expr), type(expr))

# the derivative of a consant is 0.
def const_deriv(c):
	assert isinstance(c, const)
	return const(val=0.0)

def plus_deriv(s):
	assert isinstance(s, plus)
	if isinstance(s.get_elt1(), const):
		return deriv(s.get_elt2())
	elif isinstance(s.get_elt2(), const):
		return deriv(s.get_elt1())
	return plus(elt1=deriv(s.get_elt1()), elt2=deriv(s.get_elt2()))

def pwr_deriv(p):
	assert isinstance(p, pwr)
	b = p.get_base()
	d = p.get_deg()
	if isinstance(b, var):
		if isinstance(d, const):
			if d.get_val() == 1.0:
				return make_const(1.0)
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

	elif isinstance(b, ln):
		if isinstance(d, const):
			left = make_prod(d, make_pwr_expr(b, make_const(d.get_val() - 1.0)))
			right = deriv(b)
			return make_prod(left, right)
			# return make_prod(make_pwr_expr(make_prod(make_const(d.get_val()), b), make_const(d.get_val() - 1.0)), deriv(b))

	elif isinstance(b, const):
		if isinstance(d, prod) or isinstance(d, plus) or isinstance(d, pwr) or isinstance(d, quot)  or isinstance(d, ln) or isinstance(d, absv):
			if abs(math.log(b.get_val()) - 1.0) < ERR:
				return make_prod(deriv(d), make_e_expr(d))
			else:
				return make_prod(make_prod(deriv(d), make_pwr_expr(b, d)), make_ln(b))
		elif isinstance(d, const):
			return make_const(0.0)

		else:
			raise Exception('e^somthing you can\'t handle')
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

			if isinstance(m2.get_base(), var):
				if isinstance(m2.get_deg(), const):
					
					print(m1, m2)
					if m2.get_deg().get_val() > 1 or m2.get_deg().get_val() < 0:
						return make_prod(make_const(m1.get_val() * m2.get_deg().get_val()), 
									 make_pwr(m2.get_base().get_name(), make_const(m2.get_deg().get_val()-1)))
					elif m2.get_deg().get_val() == 0.0:
						return make_const(0.0)
					elif m2.get_deg().get_val() == 1.0:
						return m1

					elif isinstance(m2.get_deg().get_val(), float):
						return make_prod(make_const(m1.get_val() * m2.get_deg().get_val()), 
									 make_pwr(m2.get_base().get_name(), make_const(m2.get_deg().get_val()-1.0)))
					else:
						raise Exception("m1 const, m2 pwr, m2.deg const, m2.base val")
				else:
					raise Exception("m2.get_deg() didn't return a const")
			# der = deriv(m2)
			# print(der)
			# elif isinstance(der, prod):
			# 	return make_prod(const(val=der.get_mult1().get_val() * m1.get_val()), der.get_mult2())
			else: 
				return prod(mult1=const(val=m1.get_val()), mult2=deriv(m2))
		elif isinstance(m2, plus):
			return deriv(plus(elt1=prod(mult1=const(val=m1.get_val()), mult2=m2.get_elt1()), 
							  elt2=prod(mult1=const(m1.get_val()), mult2=m2.get_elt2())))
		elif isinstance(m2, prod):
			if isinstance(m2.get_mult1(), const):
				return make_prod(make_const(m1.get_val() * m2.get_mult1()), m2.get_mult2())
			elif isinstance(m2.get_mult2(), const):
				return make_prod(make_const(m1.get_val() * m2.get_mult2().get_val()), m2.get_mult1())
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
		elif isinstance(m2, plus) or isinstance(m2, prod) \
				or isinstance(m2, pwr) or isinstance(m2, quot) \
				or isinstance(m2, ln):
			return product_rule(m1, m2)
		else:
			raise Exception('prod_deriv: case 2:' + str(p))
	

	elif isinstance(m1, prod):
		if isinstance(m2, const):
			return prod(mult1=deriv(m1), mult2=const(m2.get_val()))
		elif isinstance(m2, plus) or isinstance(m2, prod) \
				or isinstance(m2, pwr) or isinstance(m2, quot) \
				or isinstance(m2, ln):
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

	elif isinstance(m1, ln):
		if isinstance(m2, const):
			return make_prod(m2, deriv(m1))
		elif isinstance(m2, plus) or isinstance(m2, prod) \
				or isinstance(m2, pwr) or isinstance(m2, quot) \
				or isinstance(m2, ln):
			return product_rule(m1, m2)
		else:
			raise Exception("ln * something you can't handle")
	
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

def ln_deriv(expr):
	########start implementing ln(x)################
	assert isinstance(expr, ln)
	inner = expr.get_expr()
	if isinstance(inner, const):
		return make_const(0)
	elif isinstance(inner, plus) or isinstance(inner, prod)\
		 or isinstance(inner, pwr) or isinstance(inner, quot):
		return make_quot(deriv(inner), inner)
	elif isinstance(inner, absv):
		return make_quot(deriv(inner.get_expr()), inner.get_expr())

def get_plus_pwr_elements(expr):
	elements = []
	def r_get_elements(expr):
		if isinstance(expr, plus) or isinstance(expr, pwr):
			elements.append(expr)
		elif isinstance(expr, prod):
			r_get_elements(expr.get_mult1()) or r_get_elements(expr.get_mult2())
		else:
			pass
	r_get_elements(expr)
	return elements


def logdiff(expr):
	sum_func = 0
	elements = get_plus_pwr_elements(expr)
	if len(elements) > 1:
		sum_func = make_plus(deriv(make_ln(elements[0])), deriv(make_ln(elements[1])))
	elif len(elements) == 1:
		return make_prod(expr, deriv(make_ln(elements[0])))
	else:
		raise Exception("logdiff couldn't parse expr for sum elements")

	for i in range(2, len(elements)):
		sum_func = make_plus(sum_func, deriv(make_ln(elements[i])))

	return make_prod(expr, sum_func)


