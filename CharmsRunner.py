from antlr4 import *
from antlr4.tree.Trees import Trees
from CharmsLexer import CharmsLexer
from CharmsParserListener import CharmsParserListener
from CharmsParser import CharmsParser
from Quad import Quad
from SemanticCube import arithmeticOperators
from SemanticCube import relationalOperators
from SemanticCube import assignmentOperator
from Variable import Variable
from VariableTable import VariableTable
from TempVariable import TempVariable
from TempVariableTable import TempVariableTable
from Constant import Constant
from ConstantTable import ConstantTable
from Function import Function
from FunctionDirectory import FunctionDirectory
from ParameterTable import ParameterTable
from VirtualMachine import VirtualMachine
from QuadruplesHelper import printQuadruples
import sys

class CharmsPrintListener(CharmsParserListener):
	def enterProgram(self, ctx):
		operator = "goto"
		left_operand = ""
		right_operand = ""
		result = ""
		global qCount
		qCount += 1
		quad = Quad(operator, left_operand, right_operand, result)
		queueQuads.append(quad)

	def exitType_id(self, ctx):
		global varType
		if ctx.INT():
			varType = "int"
		elif ctx.CHAR():
			varType = "char"
		elif ctx.BOOL():
			varType = "bool"
		else:
			Exception("{} is not a valid data type".format(varType))

	def exitVar_cte(self, ctx):
		myId = str(ctx.ID())
		myCTE_INT = str(ctx.CTE_INT())
		if myId != "None":
			stackOperands.append(myId)
			stackTypes.append(varTable.getVariableType(myId))
		else:
			constantInt = int(myCTE_INT)
			stackOperands.append(constantInt)
			stackTypes.append("int")
			global constIntAddr
			constantTable.insertConstant(constantInt, 'int', constIntAddr)
			constIntAddr = constIntAddr + 1

	def enterE1(self, ctx):
		operator = ctx.PLUS() or ctx.MINUS()
		operator = str(operator)
		if operator != "None":
			stackOperators.append(operator)

	def enterT(self, ctx):
		operator = ctx.TIMES() or ctx.DIVIDE()
		operator = str(operator)
		if operator != "None":
			stackOperators.append(operator)

	def exitTerm(self, ctx):
		if len(stackOperators) > 0:
			if stackOperators[-1] == '+' or stackOperators[-1] == '-':
				right_operand = stackOperands.pop()
				right_type = stackTypes.pop()
				left_operand = stackOperands.pop()
				left_type = stackTypes.pop()
				operator = stackOperators.pop()
				result_type = arithmeticOperators(operator, right_type, left_type)
				if result_type == "int":
					global tempVarIntAddr
					result = "ti"+str(tempVarIntAddr+1)
					tempVarIntAddr += 1
					global qCount
					qCount += 1
					quad = Quad(operator, left_operand, right_operand, result)
					queueQuads.append(quad)
					stackOperands.append(result)
					stackTypes.append(result_type)
				else:
					Exception("Type mismatch")

	def enterFactor(self, ctx):
		operator = str(ctx.LPARENTHESES())
		if operator != "None":
			stackOperators.append(operator)

	def exitFactor(self, ctx):
		operator = str(ctx.RPARENTHESES())
		if operator != "None":
			stackOperators.pop()
		if len(stackOperators) > 0:
			if stackOperators[-1] == '*' or stackOperators[-1] == '/':
				right_operand = stackOperands.pop()
				right_type = stackTypes.pop()
				left_operand = stackOperands.pop()
				left_type = stackTypes.pop()
				operator = stackOperators.pop()
				result_type = arithmeticOperators(operator, right_type, left_type)
				if result_type == "int":
					global tempVarIntAddr
					result = "ti"+str(tempVarIntAddr+1)
					tempVarIntAddr += 1
					global qCount
					qCount += 1
					quad = Quad(operator, left_operand, right_operand, result)
					queueQuads.append(quad)
					stackOperands.append(result)
					stackTypes.append(result_type)
				else:
					Exception("Type mismatch")

	def addVar(self, ctx):
		global varId
		varId = str(ctx.ID()) # cast to string to avoid dealing with TerminalNode objects
		if varId != "None":
			if varType == 'int':
				global varIntAddr
				varTable.insertVariable(varId, varType, "global", varIntAddr)
				varIntAddr = varIntAddr + 1
			elif varType == 'bool':
				global varBoolAddr
				varTable.insertVariable(varId, varType, "global", varBoolAddr)
				varBoolAddr = varBoolAddr + 1
			else:
				global varCharAddr
				varTable.insertVariable(varId, varType, "global", varCharAddr)
				varCharAddr = varCharAddr + 1

	def enterV(self, ctx):
		self.addVar(ctx)

	def enterV1(self, ctx):
		self.addVar(ctx)

	def enterE(self, ctx):
		operator = ctx.GREATERTHAN() or ctx.LESSTHAN()
		operator = str(operator)
		if operator != "None":
			stackOperators.append(operator)
		# print("stackOperator:")
		# print(stackOperators)

	def exitE(self, ctx):
		if len(stackOperators) > 0:
			if stackOperators[-1] == '<' or stackOperators[-1] == '>':
				right_operand = stackOperands.pop()
				right_type = stackTypes.pop()
				left_operand = stackOperands.pop()
				left_type = stackTypes.pop()
				operator = stackOperators.pop()
				result_type = relationalOperators(operator, right_type, left_type)
				if result_type == "bool":
					global tempVarBoolAddr
					result = "tb"+str(tempVarBoolAddr+1)
					tempVarBoolAddr += 1
					global qCount
					qCount += 1
					quad = Quad(operator, left_operand, right_operand, result)
					queueQuads.append(quad)
					stackOperands.append(result)
					stackTypes.append(result_type)
				else:
					Exception("Type mismatch")

	def enterAssignment(self, ctx):
		operator = str(ctx.ASSIGN())
		if operator != "None":
			assignmentId = str(ctx.ID())
			stackOperators.append(operator)
			stackOperands.append(assignmentId)
			stackTypes.append(varTable.getVariableType(assignmentId))

	def exitAssignment(self, ctx):
		if len(stackOperators) > 0:
			if stackOperators[-1] == '=':
				left_operand = stackOperands.pop()
				left_type = stackTypes.pop()
				right_operand = stackOperands.pop()
				right_type = stackTypes.pop()
				operator = stackOperators.pop()
				result_type = assignmentOperator(operator, right_type, left_type)
				if result_type == "true":
					result = ""
					global qCount
					qCount += 1
					quad = Quad(operator, left_operand, right_operand, result)
					queueQuads.append(quad)
				else:
					Exception("Type mismatch")

	def exitW1(self, ctx):
		left_operand = stackOperands.pop()
		right_operand = ""
		operator = "PRINT"
		result = ""
		global qCount
		qCount += 1
		quad = Quad(operator, left_operand, right_operand, result)
		queueQuads.append(quad)

	def enterRead(self, ctx):
		operator = str(ctx.READ())
		if operator != "None":
			assignmentId = str(ctx.ID())
			stackOperators.append(operator)
			stackOperands.append(assignmentId)

	def exitRead(self, ctx):
		if len(stackOperators) > 0:
			if stackOperators[-1] == 'read':
				left_operand = stackOperands.pop()
				right_operand = ""
				operator = stackOperators.pop()
				result = ""
				global qCount
				qCount += 1
				quad = Quad(operator, left_operand, right_operand, result)
				queueQuads.append(quad)

	def enterLoop(self, ctx):
		stackJumps.append(qCount+1)
		global executionSource
		executionSource = "loop"

	def exitLoop(self, ctx):
		end = stackJumps.pop()
		operator = "goto"
		left_operand = stackJumps.pop()
		right_operand = ""
		result = ""
		global qCount
		qCount += 1
		quad = Quad(operator, left_operand, right_operand, result)
		queueQuads.append(quad)
		queueQuads[end-1].rightOperand = qCount+1

	def enterSection(self, ctx):
		global executionSource
		if executionSource == "loop" or executionSource == "condition":
			exp_type = stackTypes.pop()
			if exp_type == "bool":
				operator = "gotoF"
				left_operand = stackOperands.pop()
				right_operand = ""
				result = ""
				global qCount
				qCount += 1
				quad = Quad(operator, left_operand, right_operand, result)
				queueQuads.append(quad)
				stackJumps.append(qCount)
				executionSource = ""
		if executionSource == "function":
			functionDirectory.dictionary[functionName].startPosition = qCount
			executionSource = ""


	def enterCondition(self, ctx):
		global executionSource
		executionSource = "condition"

	def enterC(self, ctx):
		operator = str(ctx.ELSE())
		if operator == "else":
			global qCount
			qCount += 1
			operator = "goto"
			left_operand = ""
			right_operand = ""
			result = ""
			quad = Quad(operator, left_operand, right_operand, result)
			queueQuads.append(quad)
			false = stackJumps.pop()
			stackJumps.append(qCount)
			queueQuads[false-1].rightOperand = qCount+1

	def exitC(self, ctx):
		end = stackJumps.pop()
		queueQuads[end-1].result = qCount+1

	def enterFunction(self, ctx):
		global executionSource
		global functionName
		executionSource = "function"
		functionName = str(ctx.ID())
		if functionName == 'main':
			firstQuad = queueQuads[0]
			firstQuad.result = qCount+1
		if functionName != "None":
			global parameterTable
			global tempVariableTable
			parameterTable = ParameterTable({})
			tempVariableTable = TempVariableTable({})
			function = Function(0, parameterTable, tempVariableTable, "")
			functionDirectory.insertFunc(functionName, function)

	def exitF(self, ctx):
		returnType = str(ctx.VOID())
		if returnType == "None":
			returnType = varType
			if returnType == 'int':
				global varIntAddr
				varTable.insertVariable(functionName, varType, "global", varIntAddr)
				varIntAddr = varIntAddr + 1
			elif returnType == 'bool':
				global varBoolAddr
				varTable.insertVariable(functionName, varType, "global", varBoolAddr)
				varBoolAddr = varBoolAddr + 1
			else:
				global varCharAddr
				returnType.insertVariable(functionName, varType, "global", varCharAddr)
				varCharAddr = varCharAddr + 1
		functionDirectory.dictionary[functionName].funcReturnType = returnType

	def enterF1(self, ctx):
		parameterId = str(ctx.ID())
		if parameterId != "None":
			parameterType = varTable.vars[parameterId].varType
			if parameterType == 'int':
				global parameterIntAddr
				parameterTable.insertParameter(parameterId, parameterType, parameterIntAddr)
				parameterIntAddr = parameterIntAddr + 1
			elif parameterType == 'bool':
				global parameterBoolAddr
				parameterTable.insertParameter(parameterId, parameterType, parameterBoolAddr)
				parameterBoolAddr = parameterBoolAddr + 1
			else:
				global parameterCharAddr
				parameterTable.insertParameter(parameterId, parameterType, parameterCharAddr)
				parameterCharAddr = parameterCharAddr + 1

	def enterF2(self, ctx):
		parameterId = str(ctx.ID())
		if parameterId != "None":
			parameterType = varTable.vars[parameterId].varType
			if parameterType == 'int':
				global parameterIntAddr
				parameterTable.insertParameter(parameterId, parameterType, parameterIntAddr)
				parameterIntAddr = parameterIntAddr + 1
			elif parameterType == 'bool':
				global parameterBoolAddr
				parameterTable.insertParameter(parameterId, parameterType, parameterBoolAddr)
				parameterBoolAddr = parameterBoolAddr + 1
			else:
				global parameterCharAddr
				parameterTable.insertParameter(parameterId, parameterType, parameterCharAddr)
				parameterCharAddr = parameterCharAddr + 1

	def exitFunction(self, ctx):
		global qCount
		global tempVarIntAddr
		global tempVarBoolAddr
		global tempVarCharAddr
		global parameterIntAddr
		global parameterBoolAddr
		global parameterCharAddr
		operator = "ENDPROC"
		left_operand = ""
		right_operand = ""
		result = ""
		qCount += 1
		quad = Quad(operator, left_operand, right_operand, result)
		queueQuads.append(quad)
		tempVarIntAddr = 0
		tempVarBoolAddr = 0
		tempVarCharAddr = 0
		parameterIntAddr = 0
		parameterBoolAddr = 0
		parameterCharAddr = 0
		functionDirectory.dictionary[functionName].parameterTable = parameterTable

	def exitFunction_return(self, ctx):
		operator = "RETURN"
		left_operand = stackOperands.pop()
		right_operand = ""
		result = ""
		global qCount
		qCount += 1
		quad = Quad(operator, left_operand, right_operand, result)
		queueQuads.append(quad)

	def enterFunction_call(self, ctx):
		global functionId
		functionId = str(ctx.ID())
		if functionId in functionDirectory.dictionary:
			operator = "ERA"
			left_operand = functionId
			right_operand = ""
			result = ""
			global qCount
			qCount += 1
			global pCount
			pCount = 1
			quad = Quad(operator, left_operand, right_operand, result)
			queueQuads.append(quad)

	def enterMore_args(self, ctx):
		global pCount
		argument = stackOperands.pop()
		argumentType = stackTypes.pop()
		funcCallParamTable = functionDirectory.dictionary[functionId].parameterTable
		funcCallParamsList = list(funcCallParamTable.parameters)
		key = funcCallParamsList[pCount-1]
		if argumentType == funcCallParamTable.parameters[key].parameterType:
			operator = "PARAMETER"
			left_operand = argument
			right_operand = ""
			result = "parameter"+str(pCount);
			global qCount
			qCount += 1
			quad = Quad(operator, left_operand, right_operand, result)
			queueQuads.append(quad)
		else:
			Exception("Type mismatch")
		pCount += 1

	def exitArguments(self, ctx):
		parameterTableSize = len(parameterTable.parameters)
		if pCount != parameterTableSize:
			Exception("Argument size is different from function parameter size")

	def enterFc(self, ctx):
		operator = "GOSUB"
		left_operand = functionId
		right_operand = ""
		result = ""
		global qCount
		qCount += 1
		quad = Quad(operator, left_operand, right_operand, result)
		queueQuads.append(quad)
		funcReturnType = functionDirectory.dictionary[functionId].funcReturnType
		if funcReturnType != "void":
			operator = "="
			left_operand = functionId
			right_operand = ""
			global tempVarIntAddr
			result = "ti"+str(tempVarIntAddr+1)
			tempVarIntAddr += 1
			qCount += 1
			quad = Quad(operator, left_operand, right_operand, result)
			queueQuads.append(quad)
			stackOperands.append(result)

def main(argv):
	global stackOperands
	global stackOperators
	global stackTypes
	global stackJumps
	global queueQuads
	global executionSource # to indicate if "Section" block is being called from a condition or loop
	global qCount # quadruple count
	global pCount # parameter count (for functions)

	# Memory address
	global functionDirectory
	global constantTable
	global varTable
	global constIntAddr
	global varIntAddr
	global varBoolAddr
	global varCharAddr
	global tempVarIntAddr
	global tempVarBoolAddr
	global tempVarCharAddr
	global parameterIntAddr
	global parameterBoolAddr
	global parameterCharAddr

	qCount = 0
	pCount = 0
	stackOperands = []
	stackOperators = []
	stackTypes = []
	stackJumps = []
	queueQuads = []
	executionSource = ""

	# Memory address
	constIntAddr = 0
	varIntAddr = 0
	varBoolAddr = 0
	varCharAddr = 0
	tempVarIntAddr = 0
	tempVarBoolAddr = 0
	tempVarCharAddr = 0
	parameterIntAddr = 0
	parameterBoolAddr = 0
	parameterCharAddr = 0

	functionDirectory = FunctionDirectory()
	constantTable = ConstantTable({})
	varTable = VariableTable({}, ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"])

	lexer = CharmsLexer(StdinStream())
	stream = CommonTokenStream(lexer)
	parser = CharmsParser(stream)
	printer = CharmsPrintListener()
	walker = ParseTreeWalker()
	tree = parser.program()
	walker.walk(printer, tree)
	virtualMachine = VirtualMachine(queueQuads, functionDirectory, constantTable, varTable)
	printQuadruples(queueQuads)
	# print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)
