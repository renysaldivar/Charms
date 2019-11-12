from Function import Function

class FunctionDirectory:
	def __init__(self):
		self.dictionary = {
			"global": Function(0, 0, {}, 'void'),
			"print": Function(0, 0, {}, 'void'),
			"read": Function(0, 0, {}, 'void'),
			"selectHouse": Function(0, 1, {'cte_string'}, 'void'),
			"performSpell": Function(0, 0, {}, 'void'),
			"addScore": Function(0, 1, {'int'}, 'void')
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
			self.dictionary[funcId] = Function(func.quadCount, func.numParams, func.funcParams, func.funcReturnType)

	def clearDictionary():
		self.dictionary.clear()
		self.dictionary = {
			"global": Function(0, 0, {}, 'void'),
			"print": Function(0, 0, {}, 'void'),
			"read": Function(0, 0, {}, 'void'),
			"selectHouse": Function(0, 1, {'cte_string'}, 'void'),
			"performSpell": Function(0, 0, {}, 'void'),
			"addScore": Function(0, 1, {'int'}, 'void')
		}

	def printDirectory(self):
		for func in self.dictionary:
			print(func)
