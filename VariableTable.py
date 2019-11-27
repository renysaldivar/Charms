# Class that stores the variable table structure, composed of several variables

from Variable import Variable

class VariableTable:
	def __init__(self, vars, keywords):
		self.vars = {}
		self.keywords = ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"]

	def getVariable(self, varId):
		if varId in self.vars.keys():
			return self.vars[varId]
		else:
			raise Exception("{} does not exist in the directory".format(varId))

	def getVariableType(self, varId):
		variable = self.getVariable(varId)
		return variable.varType

	# Checks if variable name has already been used or is a keyword.
	# If not, creates a new variable and inserts it into the table.
	def insertVariable(self, varId, varType, varScope, varAddress):
		if varId in self.vars:
			raise Exception("{} already exists in the directory".format(varId))
		elif varId in self.keywords:
			raise Exception("{} is a reserved word".format(varId))
		else:
			v = Variable(varType, varScope, varAddress)
			self.vars[varId] = v

	def printTable(self):
		for var in self.vars:
			print(var, self.vars[var].varType, self.vars[var].varScope, self.vars[var].varAddress)

	def clearVariableTable(self):
		self.vars = {}
		self.keywords = ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"]
