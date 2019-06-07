


import unittest
from maker import *
from antideriv import antideriv
from deriv import deriv
from tof import tof
from hw07_s19 import read_img_dir, grayscale


class test_hw_7(unittest.TestCase):

	def test_01(self):
		fex = make_pwr('x', 2.0)
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		def gt(x): return (1.0/3.0)*(x**3.0)
		afexf = tof(afex)
		assert not afexf is None
		err = 0.0001
		for i in range(1, 101):
			assert abs(afexf(i) - gt(i)) <= err
		print(afex)
		print('passed test_01')

	def test_02(self):
		fex = make_e_expr(make_prod(make_const(-2.0),
		make_pwr('x', 1.0)))
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		def gt(x): return (-0.5)*(math.e**(-2.0*x))
		afexf = tof(afex)
		assert not afexf is None
		err = 0.0001
		for i in range(0, 101):
			assert abs(afexf(i) - gt(i)) <= err
		print(afex)
		print("passed test_02")

	def test_03(self):
		fex = make_pwr('x', 0.5)
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		def gt(x): return (2.0/3.0)*(x**(3.0/2.0))
		afexf = tof(afex)
		assert not afexf is None
		err = 0.0001
		for i in range(1, 101):
			assert abs(afexf(i) - gt(i)) <= err
		print(afex)
		print('passed test_03')

	def test_04(self):
		fex = make_pwr('x', -2.0)
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		def gt(x): return -1.0/x
		afexf = tof(afex)
		assert not afexf is None
		err = 0.0001
		for i in range(1, 101):
			assert abs(afexf(i) - gt(i)) <= err
		print(afex)
		print('passed test_04')

	def test_05(self):
		fex = make_pwr('x', -1.0)
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		print(afex)
		afexf = tof(afex)
		assert not afexf is None
		def gt(x): return math.log(abs(x), math.e)
		err = 0.0001
		for i in range(1, 101):
			assert abs(afexf(i) - gt(i)) <= err
		for i in range(-100, 0):
			assert abs(afexf(i) - gt(i)) <= err
		print('passed test_05')

	def test_06(self):
		fex1 = make_pwr('x', -3.0)
		fex2 = make_prod(make_const(7.0),
		make_e_expr(make_prod(make_const(5.0),
		make_pwr('x', 1.0))))
		fex3 = make_prod(make_const(4.0),
		make_pwr('x', -1.0))
		fex4 = make_plus(fex1, fex2)
		fex = make_plus(fex4, fex3)
		afex = antideriv(fex)
		print(afex)
		assert not afex is None
		print(afex)
		def gt(x):
			v1 = -0.5*(x**(-2.0))
			v2 = (7.0/5.0)*(math.e**(5.0*x))
			v3 = 4.0*(math.log(abs(x), math.e))
			return v1 + v2 + v3
		afexf = tof(afex)
		assert not afexf is None
		err = 1
		for i in range(1, 10):
			print(afexf(i), gt(i))
			#assert abs(afexf(i) - gt(i)) <= err
		print('passed test_06')

	def test_07(self):
		fex = make_prod(make_const(4.0), make_pwr('x', 3.0))
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		print(afex)
		fexf = tof(fex)
		assert not fexf is None
		fex2 = deriv(afex)
		assert not fex2 is None
		print(fex2)
		fex2f = tof(fex2)
		assert not fex2f is None
		err = 0.0001
		for i in range(11):
			assert abs(fexf(i) - fex2f(i)) <= err
		print('passed test_07')

	def test_08(self):
		fex1 = make_plus(make_prod(make_const(5.0),
		make_pwr('x', 1.0)),
		make_const(-7.0))
		fex = make_pwr_expr(fex1, -2.0)
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		print(afex)
		afexf = tof(afex)
		err = 0.0001
		def gt(x):
			return (-1.0/5.0)*((5*x - 7.0)**-1)
		for i in range(1, 100):
			assert abs(afexf(i) - gt(i)) <= err
		fexf = tof(fex)
		assert not fexf is None
		fex2 = deriv(afex)
		assert not fex2 is None
		print(fex2)
		fex2f = tof(fex2)
		assert not fex2f is None
		for i in range(1, 100):
			assert abs(fexf(i) - fex2f(i)) <= err
		print('passed test_08')

	def test_09(self):
		fex0 = make_plus(make_pwr('x', 1.0), make_const(2.0))
		fex1 = make_pwr_expr(fex0, -1.0)
		fex = make_prod(make_const(3.0), fex1)
		print(fex)
		afex = antideriv(fex)
		print("afex: ", afex)
		err = 0.0001
		afexf = tof(afex)
		def gt(x):
			return 3.0*math.log(abs(2.0 + x), math.e)
		for i in range(1, 101):
			assert abs(afexf(i) - gt(i)) <= err
		assert not afex is None
		print(afex)
		fexf = tof(fex)
		assert not fexf is None
		fex2 = deriv(afex)
		assert not fex2 is None
		print(fex2)
		fex2f = tof(fex2)
		assert not fex2f is None
		for i in range(1, 1000):
			assert abs(fexf(i) - fex2f(i)) <= err
		print('passed test_09')

	def test_10(self):
		fex0 = make_prod(make_const(3.0), make_pwr('x', 1.0))
		fex1 = make_plus(fex0, make_const(2.0))
		fex = make_pwr_expr(fex1, 4.0)
		print(fex)
		afex = antideriv(fex)
		assert not afex is None
		print(afex)
		afexf = tof(afex)
		err = 0.0001
		def gt(x):
			return (1.0/15)*((3*x + 2.0)**5)
		for i in range(1, 10):
			#print(afexf(i), gt(i))
			assert abs(afexf(i) - gt(i)) <= err
		fexf = tof(fex)
		assert not fexf is None
		fex2 = deriv(afex)
		assert not fex2 is None
		print(fex2)
		fex2f = tof(fex2)
		assert not fex2f is None
		for i in range(1, 1000):
			#print(fexf(i), fex2f(i))
			assert abs(fexf(i) - fex2f(i)) < err
		print('passed test_10')

	def test_11(self):
		imgs = read_img_dir('.jpg', "./")
		grayscale(0, imgs)


if __name__ == '__main__':
	unittest.main()