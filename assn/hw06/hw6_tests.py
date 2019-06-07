

import unittest
from hw06_s19 import *

class test_hm6(unittest.TestCase):

	def test_01(self):
		plot_retention(make_const(0.5), make_const(15.0),
			make_const(0.0), make_const(30))

		plot_retention(make_const(0.25), make_const(25.0),
			make_const(0.0), make_const(30))

	def test_02(self):
		plot_spread_of_disease(make_const(500000),
								make_const(0.0),
								make_const(200.0),
								make_const(1.0),
								make_const(500.0),
								make_const(0.0),
								make_const(7.0))

	def test_03(self):
		plot_spread_of_news(make_const(50000),
							make_const(0.3),
							make_const(0.0),
							make_const(50.0))

	def test_04(self):
		plot_plant_growth(make_const(55.0),
						make_const(9.0),
						make_const(8.0),
						make_const(25.0),
						make_const(48.0),
						make_const(9.0),
						make_const(50.0))
		

if __name__ == '__main__':
	unittest.main()
