class Row:
	'''
	Parameters:
	t = table
	'''
	def __init__(self, t):
		self.cells = t
		self.cooked = None
		self.isEvaled = False