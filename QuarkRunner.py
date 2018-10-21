import sys
from antlr4 import *
from QuarkLexer import QuarkLexer
from QuarkParser import QuarkParser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = QuarkLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QuarkParser(stream)
    tree = parser.main()
 
if __name__ == '__main__':
    main(sys.argv)