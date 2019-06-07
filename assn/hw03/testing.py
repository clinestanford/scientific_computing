


import unittest
from maker import *
from poly12 import *
from derivtest import loc_xtrm_1st_drv_test, loc_xtrm_2nd_drv_test
from infl import find_infl_pnts

class TestAllFunctions(unittest.TestCase):

	def test_find_poly_1_zeros1(self):
		expr = make_prod(make_const(2.0), make_pwr('x', 1.0))
		expr = make_plus(expr, make_const(5.0))
		z = find_poly_1_zeros(expr)
		func = tof(expr)
		self.assertEqual(func(z.get_val()), 0)

	def test_find_poly_1_zeros2(self):
		expr = make_pwr('x', 1.0)
		expr = make_plus(expr, make_const(5.0))
		z = find_poly_1_zeros(expr)
		func = tof(expr)
		self.assertEqual(func(z.get_val()), 0)

	def test_find_poly_2_zeros(self):
		f0 = make_prod(make_const(0.5), make_pwr('x', 2.0))
		f1 = make_prod(make_const(6.0), make_pwr('x', 1.0))
		f2 = make_plus(f0, f1)
		poly = make_plus(f2, make_const(0.0))
		zeros = find_poly_2_zeros(poly)
		f = tof(poly)
		self.assertEqual(f(zeros[0]), 0)
		self.assertEqual(f(zeros[1]), 0)

	def test_loc_xtrm_1st_drv_test1(self):
		f1 = make_prod(make_const(1.0/3.0), make_pwr('x', 3.0))
		f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
		f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
		f4 = make_plus(f1, f2)
		f5 = make_plus(f4, f3)
		poly = make_plus(f5, make_const(1.0))
		xtrma = loc_xtrm_1st_drv_test(poly)
		self.assertEqual(xtrma[0][0], "min")
		self.assertEqual(xtrma[0][1].get_x().get_val(), 3.0)
		self.assertEqual(xtrma[1][0], "max")
		self.assertEqual(xtrma[1][1].get_x().get_val(), 1.0)

	def test_loc_xtrm_1st_drv_test_without(self):
		f1 = make_prod(make_const(27.0), make_pwr('x', 3.0))
		f2 = make_prod(make_const(-27.0), make_pwr('x', 2.0))
		f3 = make_prod(make_const(9.0), make_pwr('x', 1.0))
		f4 = make_plus(f1, f2)
		f5 = make_plus(f4, f3)
		f6 = make_plus(f5, make_const(-1.0))
		drv = deriv(f6)
		xtrma = loc_xtrm_1st_drv_test(f6)
		self.assertEqual(xtrma, None)

	def test_loc_xtrm_inflection_point(self):
		f1 = prod(mult1=make_const(1.0/4.0),
		mult2=make_pwr('x', 2.0))
		f2 = prod(mult1=make_const(-1.0),
		mult2=make_pwr('x', 1.0))
		f3 = plus(elt1=f1, elt2=f2)
		f4 = plus(elt1=f3, elt2=make_const(2.0))
		xtrma = loc_xtrm_2nd_drv_test(f4)
		self.assertEqual(xtrma[0], "min")
		self.assertEqual(xtrma[1].get_x().get_val(), 2)
		self.assertEqual(xtrma[1].get_y().get_val(), 1)

	def test_get_inflection_point(self):
		f1 = make_pwr('x', 3.0)
		f2 = make_prod(make_const(-3.0), make_pwr('x', 2.0))
		f3 = make_plus(f1, f2)
		f4 = make_plus(f3, make_prod(make_const(0.0), make_pwr('x', 1.0)))
		poly = make_plus(f4, make_const(5.0))
		infls = find_infl_pnts(poly)
		der = deriv(poly)
		sec_der = deriv(der)
		sec_f = tof(sec_der)
		for pt in infls:
			self.assertEqual(sec_f(pt.get_x().get_val()), 0)


if __name__ == '__main__':
	unittest.main()