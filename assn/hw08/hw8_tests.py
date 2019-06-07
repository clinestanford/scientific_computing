

import unittest
from maker import *
from riemann import riemann_approx_with_gt, riemann_approx, plot_riemann_error
from defintegralapprox import midpoint_rule, trapezoidal_rule, simpson_rule
from antideriv import antiderivdef
from tof import tof


class test_ch_8(unittest.TestCase):

	def test_01(self):
		fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
		fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
		print(fex)
		err_list = riemann_approx_with_gt(fex,
										make_const(-1.0),
										make_const(1.0),
										make_const(4.35),
										make_const(10),
										pp=0)

		for n, err in err_list:
			pass
			#print(n, err)
		print('passed test_01')

	def test_02(self):
		fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
		fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
		print(fex)
		err_list = riemann_approx_with_gt(fex,
										make_const(-1.0),
										make_const(1.0),
										make_const(4.35),
										make_const(10),
										pp=-1)
		for n, err in err_list:
			#print(n, err)
			pass
		print('passed test_02')


	def test_03(self):
		fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
		fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
		print(fex)
		err_list = riemann_approx_with_gt(fex, make_const(-1.0),
										make_const(1.0),
										make_const(4.35),
										make_const(10),
										pp=+1)
		for n, err in err_list:
			#print(n, err)
			pass
		print('passed test_03')

	def test_04(self):
		fex = make_ln(make_pwr('x', 1.0))
		print(fex)
		err = 0.0001
		approx = riemann_approx(fex,
								make_const(1.0),
								make_const(2.0),
								make_const(100),
								pp=0)
		assert abs(approx.get_val() - 0.386296444432) <= err
		print('passed test_04')

	def test_graph_1(self):
		fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
		fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
		# plot_riemann_error(fex, make_const(-1.0),
		# 						make_const(1.0),
		# 						make_const(4.35),
		# 						make_const(10))

	def test_graph_2(self):
		fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
		fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
		# plot_riemann_error(fex, make_const(-1.0),
		# 						make_const(1.0),
		# 						make_const(4.35),
		# 						make_const(50))

	def test_05(self):
		fexpr = make_plus(make_pwr('x', 2.0),
						  make_const(5.0))
		a, b, n = make_const(0.0), make_const(4.0), make_const(250)
		approx = midpoint_rule(fexpr, a, b, n)
		err = 0.0001
		iv = antiderivdef(fexpr, a, b)
		print('antiderivdef: ', iv, ' approx: ', approx)
		assert abs(approx.get_val() - iv.get_val()) <= err
		print('passed test_05')

	def test_06(self):
		fex = make_plus(make_pwr('x', 2.0), make_const(5.0))
		a, b, n = make_const(0.0), make_const(4.0), make_const(350)
		approx = trapezoidal_rule(fex, a, b, n)
		err = 0.0001
		iv = antiderivdef(fex, a, b)
		print('antiderivdef: ', iv, ' approx: ', approx)
		assert abs(approx.get_val() - iv.get_val()) <= err
		print('passed test_06')

	def test_07(self):
		fex = make_plus(make_pwr('x', 2.0), make_const(5.0))
		a, b, n = make_const(0.0), make_const(4.0), make_const(10)
		approx = simpson_rule(fex, a, b, n)
		err = 0.0001
		iv = antiderivdef(fex, a, b)
		print('antiderivdef: ', iv, ' approx: ', approx)
		assert abs(approx.get_val() - iv.get_val()) <= err
		print('passed test_07')

	def test_08(self):
		fex = make_prod(make_prod(make_const(2.0),
		make_pwr('x', 1.0)),
		make_e_expr(make_pwr('x', 2.0)))
		a, b, n = make_const(0.0), make_const(2.0), make_const(100)
		approx = simpson_rule(fex, a, b, n)
		err = 0.0001
		print(approx)
		assert abs(approx.get_val() - 53.5981514272) <= err
		print('passed test_08')

	def test_09(self):
		fex = make_plus(make_const(1.0),
		make_pwr('x', 3.0))
		fex = make_pwr_expr(fex, 0.5)
		a, b, n = make_const(0.0), make_const(2.0), make_const(100)
		approx = simpson_rule(fex, a, b, n)
		print(approx)
		err = 0.0001
		assert abs(approx.get_val() - 3.24124) <= err
		print('passed test_09')


if __name__ == '__main__':
	unittest.main()