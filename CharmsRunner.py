from antlr4 import *
from antlr4.tree.Trees import Trees
from CharmsLexer import CharmsLexer
from CharmsParserListener import CharmsParserListener
from CharmsParser import CharmsParser
from Quad import Quad
from SemanticCube import arithmeticOperators
from Variable import Variable
from VariableTable import VariableTable
import sys

class CharmsPrintListener(CharmsParserListener):
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
			stackOperands.append(int(myCTE_INT))
			stackTypes.append("int")
		# print("stackOperands:")
		# print(stackOperands)
		# print("stackTypes:")
		# print(stackTypes)

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
		# print("stackOperator:")
		# print(stackOperators)

	def exitTerm(self, ctx):
		if len(stackOperators) > 0:
			if stackOperators[-1] == '+' or stackOperators[-1] == '-':
				right_operand = stackOperands.pop()
				right_type = stackTypes.pop()
				left_operand = stackOperands.pop()
				left_type = stackTypes.pop()
				operator = stackOperators.pop()
				result_type = arithmeticOperators(operator, right_type, left_type)
				# print("right_operand")
				# print(right_operand)
				# print("right_type")
				# print(right_type)
				# print("left_operand")
				# print(left_operand)
				# print("left_type")
				# print(left_type)
				# print("operator")
				# print(operator)
				if result_type == "int":
					global tCount
					tCount +=1
					result = "t"+str(tCount)
					quad = Quad(operator, left_operand, right_operand, result)
					queueQuads.append(quad)
					stackOperands.append(result)
					stackTypes.append(result_type)
					# print("queueQuads")
					# for quad in queueQuads:
					# 	quad.printQuad()
				else:
					Exception("Type mismatch")

	def enterFactor(self, ctx):
		operator = str(ctx.LPARENTHESES())
		if operator != "None":
			stackOperators.append(operator)
			print("stackOperators")
			print(stackOperators)

	def exitFactor(self, ctx):
		operator = str(ctx.RPARENTHESES())
		if operator != "None":
			stackOperators.pop()
			print("stackOperators")
			print(stackOperators)
		if len(stackOperators) > 0:
			if stackOperators[-1] == '*' or stackOperators[-1] == '/':
				right_operand = stackOperands.pop()
				right_type = stackTypes.pop()
				left_operand = stackOperands.pop()
				left_type = stackTypes.pop()
				operator = stackOperators.pop()
				result_type = arithmeticOperators(operator, right_type, left_type)
				# print("right_operand")
				# print(right_operand)
				# print("right_type")
				# print(right_type)
				# print("left_operand")
				# print(left_operand)
				# print("left_type")
				# print(left_type)
				# print("operator")
				# print(operator)
				if result_type == "int":
					global tCount
					tCount +=1
					result = "t"+str(tCount)
					quad = Quad(operator, left_operand, right_operand, result)
					queueQuads.append(quad)
					stackOperands.append(result)
					stackTypes.append(result_type)
					# print("queueQuads")
					# for quad in queueQuads:
					# 	quad.printQuad()
				else:
					Exception("Type mismatch")

	def addVar(self, ctx):
		global varId
		varId = str(ctx.ID()) # cast to string to avoid dealing with TerminalNode objects
		if varId != "None":
			varTable.insertVariable(varId, varType, "global")
			# varTable.printTable()

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
				result_type = arithmeticOperators(operator, right_type, left_type)
				# print("right_operand")
				# print(right_operand)
				# print("right_type")
				# print(right_type)
				# print("left_operand")
				# print(left_operand)
				# print("left_type")
				# print(left_type)
				# print("operator")
				# print(operator)
				if result_type == "int":
					global tCount
					tCount +=1
					result = "t"+str(tCount)
					quad = Quad(operator, left_operand, right_operand, result)
					queueQuads.append(quad)
					stackOperands.append(result)
					stackTypes.append(result_type)
					# print("queueQuads")
					# for quad in queueQuads:
					# 	quad.printQuad()
				else:
					Exception("Type mismatch")

def main(argv):
	global tCount
	global varTable
	global stackOperands
	global stackOperators
	global stackTypes
	global queueQuads
	tCount = 0
	stackOperands = []
	stackOperators = []
	stackTypes = []
	queueQuads = []

	varTable = VariableTable({}, ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"])
	lexer = CharmsLexer(StdinStream())
	stream = CommonTokenStream(lexer)
	parser = CharmsParser(stream)
	printer = CharmsPrintListener()
	walker = ParseTreeWalker()
	tree = parser.program()
	walker.walk(printer, tree)
	# print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)
