from Function import Function

class FunctionDirectory:
	def __init__(self):
		self.dictionary = {
		}

	def getFunc(funcId):
		if funcId not in self.dictionary:
			Exception("{} does not exist in the directory".format(funcId))
		else:
			self.dictionary[funcId]

	def insertFunc(self, funcId, func):
		if funcId in self.dictionary:
			Exception("{} already exists in the directory".format(funcId))
		else:
			self.dictionary[funcId] = Function(func.startPosition, func.parameterTable, func.funcReturnType)

	def clearDictionary():
		self.dictionary.clear()
		self.dictionary = {
		}

	def printDirectory(self):
		for func in self.dictionary:
			print(func)
