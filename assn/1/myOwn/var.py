

class var(object):
	def __init__(self, name = "var"):
		self._name = name

	def get_name(self):
		return self._name

	def __str__(self):
		return str(self._name)