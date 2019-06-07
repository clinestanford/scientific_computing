

class const(object):
	
	def __init__(self, val=0.0):
		self._val = val

	def get_val(self):
		return self._val

	def __str__(self):
		return str(self._val)

	@staticmethod
	def add(c1, c2):
		assert isinstance(c1, const)
		assert isinstance(c2, const)
		return (const(val=c1.get_val() + c2.get_val()))

	@staticmethod
	def mult(c1, c2):
		assert isinstance(c1, const)
		assert isinstance(c2, const)
		return (const(val=c1.get_val() * c2.get_val()))

	@staticmethod
	def div(c1, c2):
		assert isinstance(c1, const)
		assert isinstance(c2, const)
		return (const(val=c1.get_val() / c2.get_val()))