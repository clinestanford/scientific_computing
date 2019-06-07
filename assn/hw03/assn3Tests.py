

import unittest
from maker import *
from deriv import *
from tof import tof
from hw03 import *

ERR = .000001

class assn3Tests(unittest.TestCase):

	def test_sum_sum_diff(self):
		e1 = make_plus(make_pwr('x', 1.0), make_const(1.0))
		e2 = make_pwr('x', 3.0)
		e3 = make_prod(make_const(5.0), make_pwr('x', 1.0))
		e4 = make_plus(e2, e3)
		e5 = make_plus(e4, make_const(2.0))
		e6 = make_prod(e5, e1)
		der = deriv(e6)
		fe6 = tof(der)
		gt = lambda x: 4*(x**3) + 3*(x**2) + 10*x + 7
		for i in range(10):
			# print(fe6(i), gt(i))
			self.assertLess(abs(fe6(i)-gt(i)), ERR)

	def test_sum_sum_diff2(self):
		e1 = make_prod(make_const(2.0), make_pwr('x', 4.0))
		e2 = make_prod(make_const(-1.0), make_pwr('x', 1.0))
		e3 = make_plus(e1, e2)
		e4 = make_plus(e3, make_const(1.0))
		e5 = make_prod(make_const(-1.0), make_pwr('x', 5.0))
		e6 = make_plus(e5, make_const(1.0))
		e7 = make_prod(e6, e4)
		der = deriv(e7)
		fe7 = tof(der)
		gt = lambda x: -18.0*(x**8) + 6.0*(x**5) - 5.0*(x**4) + 8.0*(x**3) - 1.0
		for i in range(10):
			self.assertLess(abs(fe7(i) - gt(i)), ERR)

	def test_quot_pwr_diff(self):
		q = make_quot(make_plus(make_pwr('x', 1.0),
					make_const(11.0)),
					make_plus(make_pwr('x', 1.0), make_const(-3.0)))
		pex = make_pwr_expr(q, 3.0)
		der = deriv(pex)
		fpex = tof(der)
		gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
		for i in range(10):
			try:
				self.assertLess(abs(fpex(i)-gt(i)), ERR)
			except ZeroDivisionError:
				pass

	def test_max_revenue(self):
		e1 = make_prod(make_const(1.0/12.0), make_pwr('x', 2.0))
		e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
		sum1 = make_plus(e1, e2)
		dmndf_expr = make_plus(sum1, make_const(300.0))
		num_units, rev, price = maximize_revenue(dmndf_expr, constraint=lambda x: 0 <= x <= 60)
		self.assertEqual(num_units, 20)
		self.assertLess(abs(rev - 2666.66666666), ERR)
		self.assertLess(abs(price - 133.33333333), ERR)

	def test_related_rates(self):
		yt = make_prod(make_const(0.02*math.pi), make_pwr('r', 2))
		dydt = dydt_given_x_dxdt(yt, make_const(150), make_const(20))
		self.assertLess(abs(dydt.get_val() - 376.99111843), ERR)

	def test_tumor_function(self):
		arm_tumor_test()

	def test_oil_function(self):
		oil_disk_test()





if __name__ == '__main__':
	unittest.main()

