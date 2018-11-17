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
    run(parser)


def get_value(addr):
    return 0


def set_value(addr, value):
    pass


def run(parser):
    quadruples = parser.quadruples
    func_directory = parser.func_directory
    type_directory = parser.type_directory

    for i, quad in enumerate(quadruples):
        print(i, quad)
        if quad.operator == 'ASSIGN':
            value_addr = quad.left.address
            value = get_value(value_addr)
            result_addr = quad.result.address
            set_value(result_addr, value)
        elif quad.operator == '+':
            left_addr = quad.left.address
            left_value = get_value(left_addr)
            right_addr = quad.right.address
            right_value = get_value(right_addr)
            result = left_value + right_value
            result_addr = quad.result.address
            set_value(result_addr, result)


if __name__ == '__main__':
    main(sys.argv)
