class VirtualMachine:
	quadruples = []
	functionDirectory = {}
	constants = {}
	memory = [None]*900
	memoryStack = [memory] * 4

	GLOBALINT = 0
	GLOBALBOOL = 300
	GLOBALCHAR = 600
	LOCALINT = 0
	LOCALBOOL = 300
	LOCALCHAR = 600
	TEMPINT = 0
	TEMPBOOL = 300
	TEMPCHAR = 600
	CONSTINT = 0

	def __init__(self, quadruples, functionDirectory, constantTable, varTable):
		self.quadruples = quadruples
		self.functionDirectory = functionDirectory
		self.constantTable = constantTable
		self.varTable = varTable

		# for type, variables in constants.items():
		# 	for value, addr in variables.items():
		# 		self.setValue(addr, int(value), type, 'const')

		# self.printMemory('const')

	def setValue(self, addr, value, type, scope): # scope refers to global, local, temp, const
		if scope == 'global':
			currentMemory = self.memoryStack[0]
			if type == 'int':
				currentMemory[self.GLOBALINT + addr] = value
			elif type == 'bool':
				currentMemory[self.GLOBALBOOL + addr] = value
			else:
				currentMemory[self.GLOBALCHAR + addr] = value
		elif scope == 'local':
			currentMemory = self.memoryStack[1]
			if type == 'int':
				currentMemory[self.LOCALINT + addr] = value
			elif type == 'bool':
				currentMemory[self.LOCALBOOL + addr] = value
			else:
				currentMemory[self.LOCALCHAR + addr] = value
		elif scope == 'temp':
			currentMemory = self.memoryStack[2]
			if type == 'int':
				currentMemory[self.TEMPINT + addr] = value
			elif type == 'bool':
				currentMemory[self.TEMPBOOL + addr] = value
			else:
				currentMemory[self.TEMPCHAR + addr] = value
		else: #const
			if type == 'int':
				currentMemory = self.memoryStack[3]
				currentMemory[self.CONSTINT + addr] = value

	def getValue(self, addr, scope):
		index = self.getIndexFromScope(scope)
		currentMemory = self.memoryStack[index]
		return currentMemory[addr]

	def getIndexFromScope(self, scope):
		if scope == 'global':
			return 0
		elif scope == 'local':
			return 1
		elif scope == 'temp':
			return 2
		else:
			return 3

	def printMemory(self, scope):
		index = self.getIndexFromScope(scope)
		currentMemory = self.memoryStack[index]
		print(currentMemory)
