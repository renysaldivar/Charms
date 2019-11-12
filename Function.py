# Class to store information about a function

class Function:
	def __init__(self, quadCount, numParams, funcParams, funcReturnType):
		self.quadCount = quadCount
		self.numParams = numParams # number of parameters
		self.funcParams = funcParams # list of params
		self.funcReturnType = funcReturnType # type of the value returned by the function
