from Parameter import Parameter

class ParameterTable:
	def __init__(self, parameters):
		self.parameters = {}

	def insertParameter(self, parameterName, parameterType, parameterAddress):
		if parameterName in self.parameters:
			raise Exception("{} already exists in the directory".format(parameterName))
		else:
			parameter = Parameter(parameterType, parameterAddress)
			self.parameters[parameterName] = parameter

	def printTable(self):
		for param in self.parameters:
			print(param, self.parameters[param].parameterType, self.parameters[param].parameterAddress)

	def getParameter(self, parameterName):
		if parameterName in self.parameters.keys():
			return sef.parameters[parameterName]
		else:
			raise Exception("{} does not exist in the directory".format(parameterName))

	def getParameterType(self, parameterName):
		parameter = self.getParameter(parameterName)
		return parameter.parameterType
