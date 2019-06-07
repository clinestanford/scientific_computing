

class pwr(object):
	def __init__(self, base=None, deg=None):
		self._base = base
		self._deg = deg

	def get_base(self):
		return self._base

	def get_deg(self):
		return self._deg

	def __str__(self):
		return '(' + str(self._base) + '^' + str(self._deg) + ')'