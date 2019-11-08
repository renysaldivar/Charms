from Variable import Variable

class VariableTable:
	def __init__(self, vars, keywords):
		self.vars = {}
		self.keywords = ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"]

	def getVariable(self, varId):
		if varId in self.vars.keys():
			return self.vars[varId]
		else:
			Exception("{} does not exist in the directory".format(varId))

	def getVariableType(self, varId):
		variable = self.getVariable(varId)
		return variable.varType

	def insertVariable(self, varId, varType, varScope):
		if varId in self.vars:
			# print("Variables not added successfully!")
			Exception("{} already exists in the directory".format(varId))
		elif varId in self.keywords:
			# print("Variables not added successfully!")
			Exception("{} is a reserved word".format(varId))
		else:
			# print("Variables added successfully!")
			v = Variable(varType, varScope)
			self.vars[varId] = v

	def printTable(self):
		for var in self.vars:
			print(var, self.vars[var].varType)
