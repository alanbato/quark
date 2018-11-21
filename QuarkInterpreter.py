import sys
from tempfile import NamedTemporaryFile
from antlr4 import *
from QuarkLexer import QuarkLexer
from QuarkParser import QuarkParser
from virtual_machine import VirtualMachine


def main(argv):
    while True:
        input_ = input("|> ")
        with NamedTemporaryFile(mode="wb") as input_file:
            print(input_.encode('utf-8'), file=input_file)
            filename = input_file.name
            lexer = QuarkLexer(FileStream(filename))
            stream = CommonTokenStream(lexer)
            parser = QuarkParser(stream)
            tree = parser.main()
            virtual_machine = VirtualMachine(parser)
            virtual_machine.run()


if __name__ == '__main__':
    main(sys.argv)