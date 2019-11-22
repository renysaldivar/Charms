from QuadruplesHelper import printQuadruples
from QuadruplesHelper import convertQuadruples

class VirtualMachine:
	quadruples = []
	functionDirectory = {}
	constants = {}
	memory = [None]*900
	memoryStack = [memory] * 4
	charmsMemoryStack = [None]*3000
	memoryStartingPoint = { 'global': 0, 'local': 900, 'temp': 1800, 'const': 2700 }

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

		# Initialize memory stack
		self.memoryStack[0] = [None]*900
		self.memoryStack[1] = [None]*900
		self.memoryStack[2] = [None]*900
		self.memoryStack[3] = [None]*900

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
			self.updateTemporalMemoryStack(tempVariableTable)

		# Convert quadruples
		convertQuadruples(quadruples, functionDirectory, constantTable, varTable)
		printQuadruples(quadruples)

		# Print memory stack
		self.printCharmsMemoryStack()

	def updateConstantAddresses(self, constantTable):
		constants = constantTable.constants
		for key in constants:
			constant = constants[key]
			currentAddr = constant.constantAddress
			startingPoint = self.memoryStartingPoint['const']
			newAddr = startingPoint + self.CONSTINT + currentAddr
			constant.updateAddress(newAddr)

	def updateVarAddresses(self, varTable):
		vars = varTable.vars
		for key in vars:
			var = vars[key]
			currentAddr = var.varAddress
			startingPoint = self.memoryStartingPoint['global']
			varType = var.varType
			if varType == 'int':
				newAddr = startingPoint + self.GLOBALINT + currentAddr
			elif varType == 'bool':
				newAddr = startingPoint + self.GLOBALBOOL + currentAddr
			else:
				newAddr = startingPoint + self.GLOBALCHAR + currentAddr
			var.updateAddress(newAddr)

	def updateParameterAddresses(self, parameterTable):
		parameters = parameterTable.parameters
		for key in parameters:
			parameter = parameters[key]
			currentAddr = parameter.parameterAddress
			startingPoint = self.memoryStartingPoint['local']
			parameterType = parameter.parameterType
			if parameterType == 'int':
				newAddr = startingPoint + self.LOCALINT + currentAddr
			elif parameterType == 'bool':
				newAddr = startingPoint + self.LOCALBOOL + currentAddr
			else:
				newAddr = startingPoint + self.LOCALCHAR + currentAddr
			parameter.updateAddress(newAddr)

	def updateTempVariableAddresses(self, tempVariableTable):
		tempVariables = tempVariableTable.tempVariables
		for key in tempVariables:
			tempVariable = tempVariables[key]
			currentAddr = tempVariable.tempVariableAddress
			startingPoint = self.memoryStartingPoint['temp']
			tempVariableType = tempVariable.tempVariableType
			if tempVariableType == 'int':
				newAddr = startingPoint + self.TEMPINT + currentAddr
			elif tempVariableType == 'bool':
				newAddr = startingPoint + self.TEMPBOOL + currentAddr
			else:
				newAddr = startingPoint + self.TEMPCHAR + currentAddr
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
		elif scope == 'local':
			currentMemory = self.memoryStack[1]
		elif scope == 'temp':
			currentMemory = self.memoryStack[2]
		else: #const
			currentMemory = self.memoryStack[3]
		startingPoint = self.memoryStartingPoint[scope]
		currentMemory[addr-startingPoint] = value
		self.charmsMemoryStack[addr] = value

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

	def printCharmsMemoryStack(self):
		charmsMemoryStack = self.charmsMemoryStack
		for value in charmsMemoryStack:
			if value != None:
				addr = charmsMemoryStack.index(value)
				print(addr, value)
