# Class to store information about a variable

class Variable:
	def __init__(self, varType, varScope, varAddress):
		self.varType = varType # int, char, bool
		self.varScope = varScope # local or global
		self.varAddress = varAddress # memory address

	def updateAddress(self, newAddress):
		self.varAddress = newAddress
