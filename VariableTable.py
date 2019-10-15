from Variable import Variable

class VariableTable:
	def __init__(self, vars, keywords):
		self.vars = {}
		self.keywords = ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"]

	def getVariable(varId):
		if varId in self.vars.keys():
			return self.vars[varId]
		else:
			Exception("{} does not exist in the directory".format(varId))

	def insertVariable(varId, varType, varScope):
		if varId in self.vars.keys():
			Exception("{} already exists in the directory".format(varId))
		elif varId in self.keywords:
			Exception("{} is a reserved word".format(varId))
		else:
			v = Variable(varType, varScope)
			self.vars[varId] = v