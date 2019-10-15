from antlr4 import *
from CharmsLexer import CharmsLexer
from CharmsParser import CharmsParser
import sys

def main(argv):
    #input = FileStream(argv[1])
    lexer = CharmsLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = CharmsParser(stream)
    tree = parser.program()

if __name__ == '__main__':
    main(sys.argv)