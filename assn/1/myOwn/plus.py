

class plus(object):
	def __init__(self, elt1=None, elt2=None):
		self._elt1 = elt1
		self._elt2 = elt2

	def __str__(self):
		return str(self._elt1) + '+' + str(self._elt2)