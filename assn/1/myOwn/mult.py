

class mult(object):
	def __init__(self, mult1=None, mult2=None):
		self._mult1 = mult1
		self._mult2 = mult2

	def get_mult1(self):
		return self._mult1

	def get_mult2(self):
		return self._mult2

	def __str__(self):
		return '(' + str(self._mult1) + '*' + str(self._mult2) + ')'