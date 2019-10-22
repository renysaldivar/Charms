from antlr4 import *
from antlr4.tree.Trees import Trees
from CharmsLexer import CharmsLexer
from CharmsParserListener import CharmsParserListener
from CharmsParser import CharmsParser
from Variable import Variable
from VariableTable import VariableTable
import sys

varType = None
varId = None
varScope = "global"

class CharmsPrintListener(CharmsParserListener):
	def enterType_id(self, ctx):
		if ctx.INT() == "int":
			varType = "int"
		elif ctx.CHAR() == "char":
			varType = "char"
		elif ctx.BOOL() == "bool":
			varType = "bool"

	def enterV(self, ctx):
		varId = ctx.ID()

	def exitP_vars(self, ctx):
		varTable = VariableTable({}, ["int", "void", "bool", "char", "if", "else", "while", "print", "read", "return", "function", "id"])
		varTable.insertVariable(varId, varType, varScope)

def main(argv):
    #input = FileStream(argv[1])
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