
import math
import unittest
from maker import *
from cs3430_s19_hw11 import nra

class testAll(unittest.TestCase):

	def test_01(self):
		fexpr = make_plus(make_pwr('x', make_const(2)), make_const(-2))
		assert abs(nra(fexpr, make_const(1.0), make_const(10000)).get_val() - math.sqrt(2)) < .00001

	def test_02(self):
		fexpr = make_plus(make_pwr('x', make_const(2)), make_const(-3))
		assert abs(nra(fexpr, make_const(1.0), make_const(10000)).get_val() - math.sqrt(3)) < .00001

	def test_03(self):
		fexpr = make_plus(make_pwr('x', make_const(2)), make_const(-5))
		assert abs(nra(fexpr, make_const(1.0), make_const(10000)).get_val() - math.sqrt(5)) < .00001

	def test_04(self):
		fexpr = make_plus(make_pwr('x', make_const(3)), make_const(-11))
		assert abs(nra(fexpr, make_const(1.0), make_const(10000)).get_val() - (11 ** (1/3))) < .00001

	def test_05(self):
		fexpr = make_e_expr(make_prod(make_const(-1.0),make_pwr('x', 1.0)))
		fexpr = make_plus(fexpr,make_prod(make_const(-1.0),make_pwr('x', 2.0)))
		answer = nra(fexpr, make_const(1.0), make_const(10000))
		assert abs(answer.get_val() - 0.703467422498) < .000001

	def test_06(self):
		fexpr = make_e_expr(make_plus(make_const(5.0),make_prod(make_const(-1.0),make_pwr('x', 1.0))))
		fexpr = make_plus(fexpr, make_pwr('x', 1.0))
		fexpr = make_plus(fexpr, make_const(-10.0))
		x = nra(fexpr, make_const(1.0), make_const(10000)).get_val()
		assert math.e**(5-x) + x - 10 < .00001


if __name__ == '__main__':
	unittest.main()




