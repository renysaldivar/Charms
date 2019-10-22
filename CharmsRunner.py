from antlr4 import *
from antlr4.tree.Trees import Trees
from CharmsLexer import CharmsLexer
from CharmsParserListener import CharmsParserListener
from CharmsParser import CharmsParser
import sys

class CharmsPrintListener(CharmsParserListener):
	def enterType_id(self, ctx):
		print(ctx.INT()) # Esto imprime "int" porque el ejemplo que uso es int.
		# Si pongo ctx.BOOL o ctx.CHAR esto imprime "None",
		# así que es una manera curiosa de obtener el tipo.

	def enterV(self, ctx):
		print("Hello: %s" % ctx.ID())
		# Esto regresa el ID de la variable. 

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