# Class to store information about a function

class Function:
	def __init__(self, funcId, funcParams, funcReturnType):
		self.funcId = funcId # unique identifier
		self.funcParams = funcParams # list of params
		self.funcReturnType = funcReturnType # type of the value returned by the function
