# Class to store information about a variable

class Variable:
	def __init__(self, varId, varType, varScope):
		self.varId = varId # unique identifier
		self.varType = varType # int, char, bool
		self.varScope = varScope # local or global