# Class to store information about a parameter

class Parameter:
	def __init__(self, parameterType, parameterAddress):
		self.parameterType = parameterType # int, char, bool
		self.parameterAddress = parameterAddress # memory address

	def updateAddress(self, newAddress):
		self.parameterAddress = newAddress
