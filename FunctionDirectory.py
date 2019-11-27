# Class that stores the function directory structure, composed of several functions

from Function import Function

class FunctionDirectory:
	def __init__(self):
		self.dictionary = {
		}

	def getFunc(self, funcId):
		if funcId not in self.dictionary:
			raise Exception("{} does not exist in the directory".format(funcId))
		else:
			self.dictionary[funcId]

	# Checks if function name has already been used.
	# If not, creates a new function and inserts it into the table.
	def insertFunc(self, funcId, func):
		if funcId in self.dictionary:
			raise Exception("{} already exists in the directory".format(funcId))
		else:
			self.dictionary[funcId] = Function(func.startPosition, func.parameterTable, func.tempVariableTable, func.funcReturnType)

	def clearDictionary():
		self.dictionary.clear()
		self.dictionary = {
		}

	def printDirectory(self):
		for func in self.dictionary:
			print(func)
