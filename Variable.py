# Class to store information about a variable

class Variable:
	def __init__(self, varType, varScope):
		self.varType = varType # int, char, bool
		self.varScope = varScope # local or global