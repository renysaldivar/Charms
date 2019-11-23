from QuadruplesHelper import printQuadruples
from QuadruplesHelper import convertQuadruples

class VirtualMachine:
	quadruples = []
	functionDirectory = {}
	constants = {}
	memoryStack = {}
	for key in range(0, 3000):
		memoryStack[key] = None
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

		# Execute quadruples
		self.executeQuadruples()

		# Print memory stack
		self.printMemoryStack()

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
			addr = var.varAddress
			self.memoryStack[addr] = key

	def updateLocalMemoryStack(self, parameterTable):
		self.clearMemorySection('local')
		parameters = parameterTable.parameters
		for key in parameters:
			parameter = parameters[key]
			addr = parameter.parameterAddress
			self.memoryStack[addr] = key

	def updateTemporalMemoryStack(self, tempVariableTable):
		self.clearMemorySection('temp')
		tempVariables = tempVariableTable.tempVariables
		for key in tempVariables:
			tempVariable = tempVariables[key]
			addr = tempVariable.tempVariableAddress
			self.memoryStack[addr] = key

	def updateConstantMemoryStack(self, constantTable):
		constants = constantTable.constants
		for key in constants:
			constant = constants[key]
			addr = constant.constantAddress
			self.memoryStack[addr] = key

	def clearMemorySection(self, scope):
		if scope == 'global':
			memorySection = range(0, 900)
		elif scope == 'local':
			memorySection = range(900, 1800)
		elif scope == 'temp':
			memorySection = range(1800, 2700)
		else: #const
			memorySection = range(2700, 3000)
		for addr in memorySection:
			self.memoryStack[addr] = None

	def executeQuadruples(self):
		quadruples = self.quadruples
		# self.executeQuad(quadruples[0])
		for quad in quadruples:
			self.executeQuad(quad)

	def executeQuad(self, quad):
		operator = quad.operator
		leftOperand = quad.leftOperand
		rightOperand = quad.rightOperand
		result = quad.result
		if operator == 'goto':
			newQuad = self.quadruples[result-1]
			self.executeQuad(newQuad)
		elif operator == '+':
			value = self.memoryStack[leftOperand] + self.memoryStack[rightOperand]
			self.memoryStack[result] = value
		elif operator == '-':
			value = self.memoryStack[leftOperand] - self.memoryStack[rightOperand]
			self.memoryStack[result] = value
		elif operator == '*':
			value = self.memoryStack[leftOperand] * self.memoryStack[rightOperand]
			self.memoryStack[result] = value
		elif operator == '/':
			value = self.memoryStack[leftOperand] / self.memoryStack[rightOperand]
			self.memoryStack[result] = int(value)
		elif operator == '=':
			# Get value
			self.memoryStack[rightOperand] = self.memoryStack[leftOperand]
		elif operator == 'ERA':
			self.clearMemorySection('local')
			self.clearMemorySection('temp')

	def printMemoryStack(self):
		memoryStack = self.memoryStack
		for key in memoryStack:
			if memoryStack[key] != None:
				print(key, memoryStack[key])