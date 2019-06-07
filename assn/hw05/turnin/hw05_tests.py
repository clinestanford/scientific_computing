

import unittest
from maker import *
from hw05 import *
from tof import *



class hw05_unittests(unittest.TestCase):

	def test_01(self):
		eq = solve_pdeq(make_const(1.0), make_const(1.0))
		assert not eq is None
		print(eq)
		eqf = tof(eq)
		assert not eqf is None
		err = 0.0001
		gt = lambda t: math.e**t
		for t in range(100):
			assert abs(gt(t) - eqf(t)) <= err
		print('test_01 passed')

	def test_02(self):
		eq = solve_pdeq(make_const(4.0), make_const(1.0/3.0))
		assert not eq is None
		print(eq)
		eqf = tof(eq)
		assert not eqf is None
		gt = lambda t: math.e**((1.0/12.0)*t)
		for t in range(100):
			assert abs(gt(t) - eqf(t)) <= 0.0001
		print('test_02 passed')

	def test_03(self):
		eq = solve_pdeq_with_init_cond(make_const(1.0),
		make_const(3.0))
		assert not eq is None
		print(eq)
		eqf = tof(eq)
		assert not eqf is None
		def gt(t): return math.e**(3.0*t)
		err = 0.0001
		for t in range(100):
			assert abs(gt(t) - eqf(t)) <= err
		print('test_03 passed')

	def test_04(self):
		expr = find_growth_model(make_const(20000), make_const(48), make_const(4))
		f_expr = tof(expr)
		print(expr)
		assert not f_expr is None
		err = .00001
		assert int(f_expr(12)) == 28284
		print('test_04 passed')

	def test_05(self):
		expr = radioactive_decay(make_const(.021), make_const(8), make_const(10))
		print(expr)
		f_expr = tof(expr)
		assert not f_expr is None
		print(f_expr(10))
		err = 0.00001
		assert abs(f_expr(10) - 6.4846739677) <= err
		print('test_05 passed')

	def test_06(self):
		val = c14_carbon_dating(make_const(.8))
		print(val)
		assert val.get_val() == 1860
		print('test_06 passed')

	def test_07(self):
		expr = make_plus(make_const(100), make_prod(make_const(-2), make_pwr('x', 1)))
		elasticity = demand_elasticity(expr, make_const(30))
		err = .00001
		print(elasticity)
		assert (elasticity.get_val() - (3/2)) <= err
		print('test_07 passed')

	def test_08(self):
		expr = make_plus(make_quot(make_const(18000), make_pwr('x',1)), make_const(-1500))
		print(expr)

		elasticity = demand_elasticity(expr, make_const(6))
		in_money = expected_rev_dir(expr, make_const(6), make_const(1))
		if elasticity:
			assert in_money.get_val() == -1
		else:
			assert in_money.get_val() == 1
		

		print('test_07 passed')



if __name__ == '__main__':
	unittest.main()