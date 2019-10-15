from Function import Function

class FunctionDirectory:
	def __init__(self):
		self.dictionary = {
			"global": Function({}, 'void'),
            "print": Function({}, 'void'),
            "read": Function({}, 'void'),
            "selectHouse": Function({'cte_string'}, 'void'),
            "performSpell": Function({}, 'void'),
            "addScore": Function( {'int'}, 'void')
		}

	def getFunc(funcId):
		if funcId not in self.dictionary:
			Exception("{} does not exist in the directory".format(funcId))
		else:
			self.dictionary[funcId]

	def insertFunc(funcId, func):
		if funcId in self.dictionary:
			Exception("{} already exists in the directory".format(funcId))
		else:
			self.dictionary[funcId] = Function(func.funcParams, func.funcReturnType)

	def clearDictionary():
		self.dictionary.clear()
		self.dictionary = {
			"global": Function({}, 'void'),
            "print": Function({}, 'void'),
            "read": Function({}, 'void'),
            "selectHouse": Function({'cte_string'}, 'void'),
            "performSpell": Function({}, 'void'),
            "addScore": Function( {'int'}, 'void')
		}
