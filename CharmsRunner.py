from antlr4 import *
from antlr4.tree.Trees import Trees
from CharmsLexer import CharmsLexer
from CharmsParserListener import CharmsParserListener
from CharmsParser import CharmsParser
from Variable import Variable
from VariableTable import VariableTable
import sys

class CharmsPrintListener(CharmsParserListener):
	def exitType_id(self, ctx):
		global varType
		# print(ctx.INT())
		# if ctx.INT() == "int":
		# 	varType = "int"
		# elif ctx.CHAR() == "char":
		# 	varType = "char"
		# elif ctx.BOOL() == "bool":
		# 	varType = "bool"
		varType = ctx.INT()

	def exitV(self, ctx):
		global varId
		varId = ctx.ID()

	def exitP_vars(self, ctx):
		varTable.insertVariable(varId, varType, "global")
		varTable.printTable()

def main(argv):
	global varTable
	varTable = VariableTable({}, ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"])
	lexer = CharmsLexer(StdinStream())
	stream = CommonTokenStream(lexer)
	parser = CharmsParser(stream)
	printer = CharmsPrintListener()
	walker = ParseTreeWalker()
	tree = parser.program()
	walker.walk(printer, tree)
    #print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)