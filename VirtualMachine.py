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

		# Update addresses in constant, global, and local tables
		self.updateConstantAddresses(self.constantTable)
		self.updateVarAddresses(self.varTable)
		functions = self.functionDirectory.dictionary
		for key in functions:
			function = functions[key]
			parameterTable = function.parameterTable
			self.updateParameterAddresses(parameterTable)
			tempVariableTable = function.tempVariableTable
			self.updateTempVariableAddresses(tempVariableTable)

		# Update memory stack
		self.updateConstantMemoryStack(constantTable)
		self.updateGlobalMemoryStack(varTable)
		functions = self.functionDirectory.dictionary
		for key in functions:
			function = functions[key]
			parameterTable = function.parameterTable
			self.updateLocalMemoryStack(parameterTable)
			tempVariableTable = function.tempVariableTable
			self.updateTemporalMemoryStack(tempVariableTable)V

	def updateConstantAddresses(self, constantTable):
		constants = constantTable.constants
		for key in constants:
			constant = constants[key]
			currentAddr = constant.constantAddress
			newAddr = self.CONSTINT + currentAddr
			constant.updateAddress(newAddr)

	def updateVarAddresses(self, varTable):
		vars = varTable.vars
		for key in vars:
			var = vars[key]
			currentAddr = var.varAddress
			varType = var.varType
			if varType == 'int':
				newAddr = self.GLOBALINT + currentAddr
			elif varType == 'bool':
				newAddr = self.GLOBALBOOL + currentAddr
			else:
				newAddr = self.GLOBALCHAR + currentAddr
			var.updateAddress(newAddr)

	def updateParameterAddresses(self, parameterTable):
		parameters = parameterTable.parameters
		for key in parameters:
			parameter = parameters[key]
			currentAddr = parameter.parameterAddress
			parameterType = parameter.parameterType
			if parameterType == 'int':
				newAddr = self.LOCALINT + currentAddr
			elif parameterType == 'bool':
				newAddr = self.LOCALBOOL + currentAddr
			else:
				newAddr = self.LOCALCHAR + currentAddr
			parameter.updateAddress(newAddr)

	def updateTempVariableAddresses(self, tempVariableTable):
		tempVariables = tempVariableTable.tempVariables
		for key in tempVariables:
			tempVariable = tempVariables[key]
			currentAddr = tempVariable.tempVariableAddress
			tempVariableType = tempVariable.tempVariableType
			if tempVariableType == 'int':
				newAddr = self.TEMPINT + currentAddr
			elif tempVariableType == 'bool':
				newAddr = self.TEMPBOOL + currentAddr
			else:
				newAddr = self.TEMPCHAR + currentAddr
			tempVariable.updateAddress(newAddr)

	def updateGlobalMemoryStack(self, varTable):
		vars = varTable.vars
		for key in vars:
			var = vars[key]
			self.setValue(var.varAddress, key, 'global')

	def updateLocalMemoryStack(self, parameterTable):
		self.memoryStack[1] = [None]*900
		parameters = parameterTable.parameters
		for key in parameters:
			parameter = parameters[key]
			self.setValue(parameter.parameterAddress, key, 'local')

	def updateTemporalMemoryStack(self, tempVariableTable):
		self.memoryStack[2] = [None]*900
		tempVariables = tempVariableTable.tempVariables
		for key in tempVariables:
			tempVariable = tempVariables[key]
			self.setValue(tempVariable.tempVariableAddress, key, 'temp')

	def updateConstantMemoryStack(self, constantTable):
		constants = constantTable.constants
		for key in constants:
			constant = constants[key]
			self.setValue(constant.constantAddress, key, 'const')

	def setValue(self, addr, value, scope): # scope refers to global, local, temp, const
		if scope == 'global':
			currentMemory = self.memoryStack[0]
			currentMemory[addr] = value
		elif scope == 'local':
			currentMemory = self.memoryStack[1]
			currentMemory[addr] = value
		elif scope == 'temp':
			currentMemory = self.memoryStack[2]
			currentMemory[addr] = value
		else: #const
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
