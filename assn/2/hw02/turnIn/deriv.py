#!/usr/bin/python

####################################
# Your Name
# Your A#
####################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_pwr, make_pwr_expr, make_prod
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
			# your code here
			left  = const(val=d.get_val())
			right = pwr(base=var(name=b.get_name()) , deg=const(d.get_val()-1))
			#need to handle for x ^ 0
			if d.get_val() == 0.0:
				return const(val = 0.0)
			return prod(mult1=left, mult2=right)
			# my code ends here
		else:
			raise Exception('pwr_deriv: case 1: ' + str(p))
	if isinstance(b, pwr):
		if isinstance(d, const):
			# your code here
			left  = prod(mult1=const(val=d.get_val()) ,mult2=pwr(base=b, deg=const(val=d.get_val()-1))) 
			right = deriv(b)
			return prod(mult1=left, mult2=right)
			# my code ends here
			pass
		else:
			raise Exception('pwr_deriv: case 2: ' + str(p))
	elif isinstance(b, plus):
		if isinstance(d, const):
			# your code here
			left  = prod(mult1=const(d.get_val()) , mult2=pwr(base=b, deg=const(d.get_val()-1)))
			right = deriv(b)
			return prod(mult1=left, mult2=right)
			# my code ends here
			# pass
		else:
			raise Exception('pwr_deriv: case 3: ' + str(p))
	elif isinstance(b, prod):
		if isinstance(d, const):
			# your code here
			left  = prod(mult1=const(d.get_val()) , mult2=pwr(base=b, deg=const(d.get_val()-1)))
			right = deriv(b)
			return prod(mult1=left, mult2=right)
			# my code ends here
			# pass
		else:
			raise Exception('pwr_deriv: case 4: ' + str(p))
	else:
		raise Exception('power_deriv: case 5: ' + str(p))

def prod_deriv(p):
	assert isinstance(p, prod)
	m1 = p.get_mult1()
	m2 = p.get_mult2()
	if isinstance(m1, const):
		if isinstance(m2, const):
			# your code here
			return const(val=0)
			# my code ends here
			# pass
		elif isinstance(m2, pwr):
			# your code here
			der = deriv(m2)
			if isinstance(der, prod):
				return make_prod(const(val=der.get_mult1().get_val() * m1.get_val()), der.get_mult2())
			else: 
				return prod(mult1=const(val=m1.get_val()), mult2=deriv(m2))
			# my code ends here
			# pass
		elif isinstance(m2, plus):
			# your code here
			return deriv(plus(elt1=prod(mult1=const(val=m1.get_val()), mult2=m2.get_elt1()), 
							  elt2=prod(mult1=const(m1.get_val()), mult2=m2.get_elt2())))
			# my code ends here
			#pass
		elif isinstance(m2, prod):
			# your code here
			return prod(mult1=const(m1.get_val()),
						mult2=deriv(m2))
			# my code ends here
			# pass
		else:
			raise Exception('prod_deriv: case 0' + str(p))
	elif isinstance(m1, plus):
		if isinstance(m2, const):
			# your code here
			# test 8
			return deriv(plus(elt1=prod(mult1=const(val=m2.get_val()), mult2=m1.get_elt1()), 
							  elt2=prod(mult1=const(m2.get_val()), mult2=m1.get_elt2())))
			# my code ends here
			# pass
		else:
			raise Exception('prod_deriv: case 1:' + str(p))
	elif isinstance(m1, pwr):
		if isinstance(m2, const):
			# your code here
			# test 9
			return prod(mult1=deriv(m1), mult2=const(val=m2.get_val()))
			# my code ends here
			# pass
		else:
			raise Exception('prod_deriv: case 2:' + str(p))
	elif isinstance(m1, prod):
		if isinstance(m2, const):
			# your code here
			# test 10
			return prod(mult1=deriv(m1), mult2=const(m2.get_val()))
			# my code ends here
			# pass
		else:
			raise Exception('prod_deriv: case 3:' + str(p))
	else:
	   raise Exception('prod_deriv: case 4:' + str(p))



