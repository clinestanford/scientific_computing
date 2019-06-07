#!/usr/bin/python

#############################################################
# module: cs3430_s19_exam_01.py
# YOUR NAME
# YOUR A#
##############################################################

## add all your imports here

import unittest
from maker import *
from deriv import deriv, logdiff
from tof import *
from poly12 import find_poly_1_zeros, find_poly_2_zeros


# ************* Problem 1 (1 point) **********************

def test_deriv(fexpr, gt, lwr, uppr, err):
	assert isinstance(lwr, const)
	assert isinstance(uppr, const)
	assert isinstance(err, const)
	
	der = deriv(fexpr)
	f_der = tof(der)

	for i in range(lwr, uppr, 1):
		assert(abs(f_der(i) - gt(i)) < err)


# ************* Problem 2 (2 points) **********************

def max_profit(cost_fun, rev_fun):
	
	expr = make_plus(rev_fun, make_prod(make_const(-1), cost_fun))

	f_expr = tof(expr)

	max_val = 0
	index = 0
	for i in range(10000):
		if f_expr(i) > max_val:
			max_val = f_expr(i)
			index = i 
	return make_const(index)




# ************* Problem 3 (2 points) **********************

def fastest_growth_time(pm, tl, tu):
	assert isinstance(tl, const)
	assert isinstance(tu, const)

	der = deriv(pm)
	f_der = tof(der)
	sec_der = deriv(der)
	f_sec_der = tof(sec_der)

	zero = find_poly_1_zeros(f_sec_der)

	xvals = np.linspace(tl.get_val(), tu.get_val(), 10000)
	yvals1 = np.array([f_der(i) for i in xvals])
	fig1 = plt.figure(1)
	fig1.suptitle("Hive Beetle Population Growth")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.ylim(yvals1.max(), yvals1.min())
	plt.xlim(tl.get_val(), tu.get_val())
	plt.grid()
	# plt.plot(xvals, yvals1, label="f(x)="+str(expr), c='r')
	# plt.plot(xvals, yvals2, label="f'(x)="+str(der), c='b')
	# plt.legend(loc='best')
	plt.show(block=True)


	if zero:
		if f_sec_der(zero.get_val() - .01) > 0 and f_sec_der(zero.get_val() + .01) < 0 and zero.get_val() > tl and zero.get_val < tu:
			return zero

	else:
		max_val = 0 
		index = 0
		for i in range(tl.get_val(), tu.get_val(), .01):
			if f_sec_der(i) < .00001:
				if f_sec_der(i - .01) > 0 and f_sec_der(i + .01) < 0:
					return make_const(i)

		for i in range(tl.get_val(), tu.get_val(), .01):
			if f_der(i) > max_val:
				max_val = f_der(i)
				index = i 
		return make_const(i)
# ************* Problem 4 (2 points) **********************

def max_norman_window_area(p):
	assert isinstance(p, const)
	
	func = make_plus(p, make_prod(make_const(-1), make_prod(make_const(2), make_pwr('x', 1))))
	func1 = make_plus(func, make_prod(make_const(-1), make_prod(make_const(math.pi), make_pwr('x', 1))))
	func2 = make_quot(func1, make_const(2))

	a1 = make_prod(make_const(.5), make_prod(make_const(math.pi), make_pwr('x', 2)))
	a2 = make_prod(make_const(2), make_prod(make_pwr('x'), func2))

	der = deriv(a2)
	f_der = tof(der)

	min_val = 10000
	index = 0
	for i in range(0, p**2, .5):
		if f_der(i) < min_val:
			min_val = f_der(i)
			index = i

	return make_const(index)

# ************* Problem 5 (2 points) **********************

def tumor_volume_change(m, c, k):
	assert isinstance(m, const)
	assert isinstance(c, const)
	assert isinstance(k, const)


	vol = make_prod(k, make_prod(make_const(math.pi * 3.0), make_pwr('x', 2)))
	with_rate = make_prod(vol, c)

	func = tof(with_rate)
	
	return make_const(func(m.get_val()))

# ************* Problem 6 (1 point) **********************

def penicillin_amount(p0, lmbda, t):
	assert isinstance(p0, const)
	assert isinstance(lmbda, const)
	assert isinstance(t, const)
	
	p_init = p0.get_val()
	decay = lmbda.get_val()
	tot_time = t.get_val()

	return make_const(p_init * (math.e ** (decay * tot_time)))
	

def penicillin_half_life(lmbda):
	assert isinstance(lmbda, const)
	

	return make_const(math.log(2)/lmbda.get_val())

class myTester(unittest.TestCase):

	def test_01(self):
		cost = make_pwr('x', 3)
		expr = make_plus(cost, make_prod(make_const(-6), make_pwr('x', 2)))
		expr1 = make_plus(expr, make_prod(make_const(13), make_pwr('x', 1)))
		cost_fun = make_plus(expr1, make_const(15))
		rev_fun = make_prod(make_const(28), make_pwr('x', 1))
		print(max_profit(cost_fun, rev_fun))

	def test_02(self):
		print(tumor_volume_change(make_const(20), make_const(1.5), make_const(5/4)))




if __name__ == '__main__':
	unittest.main()
	
