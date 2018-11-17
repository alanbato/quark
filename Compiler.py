from utils import check_operation_type

import attr
from typing import Any, Dict
import pprint
pp = pprint.PrettyPrinter()


@attr.s
class FuncRecord:
    # The _ is used to avoid a collision with a builtin or restricted name
    type_: str = attr.ib()
    vars_: Dict[str, Any] = attr.ib(attr.Factory(dict))
    params_: int = attr.ib(0)


@attr.s
class VarRecord:
    addr: int = attr.ib()
    dim: Any = attr.ib(None)


@attr.s
class Operand:
    name: str = attr.ib()
    type_: str = attr.ib()
    address: int = attr.ib(None)


@attr.s
class Quad:
    operator = attr.ib()
    left: Operand = attr.ib(None)
    right: Operand = attr.ib(None)
    result: Any = attr.ib(attr.Factory(str))


class Compiler:
    """Compiler logic and state."""
    func_directory = {
        "global": FuncRecord('non',
                             {'Int': {'__constants__': {}},
                              'Float': {'__constants__': {}},
                              'String': {'__constants__': {}},
                              'Any': {}, '[Any]': {}
                              }),
        "append": FuncRecord('[Any]', {}, 2),
        "print": FuncRecord('none', {}, 1),
        "upper": FuncRecord('String', {}, 1),
        "head": FuncRecord('Any', {}, 1),
        "tail": FuncRecord('[Any]', {}, 1),
    }
    negative = False
    type_directory = {}
    function_stack = ["global"]
    operand_stack = []
    operator_stack = []
    quadruples = []
    gotos = []
    temp = 0  # <- Es el id de variables temporales?
    # Memory = namedtuple('Memory', ['number', 'value'])
    # memory = Memory()

    def set_negative(self):
        self.negative = True

    def define_function(self, func_name):
        self.function_stack.append(func_name)
        if func_name in self.func_directory:
            Exception("Function {} already defined".format(func_name))
        else:
            self.func_directory[func_name] = FuncRecord(
                None, {'Int': {}, 'Float': {}, 'String': {}, 'Any': {}, '[Any]': {}})

    def set_function_return_type(self, func_name, ret_type):
        self.func_directory[func_name].type_ = ret_type

    def process_function_clause(self):
        ident = self.gotos.pop()
        temp = self.quadruples[ident]
        temp.result = len(self.quadruples) - 1
        self.quadruples.append(Quad("RETURN"))
        self.quadruples.append(Quad("GOTO"))

    def process_function_end(self):
        self.quadruples.append(Quad("ENDPROC"))
        self.function_stack.pop()
        self.operand_stack = []
        self.operator_stack = []

    def process_param(self, ident, type_):
        function_name = self.function_stack[-1]
        function = self.func_directory[function_name]
        function.params_ += 1
        function.vars_[type_][ident] = VarRecord(
            len(function.vars_[type_]), None)

    def check_user_def_type(self, type_id):
        if type_id not in self.type_directory:
            raise Exception(f"Undefined type {type_id}")

    def define_type(type_id, type_value):
        if type_value.startswith("("):
            type_value = type_value[1:-1].split("|")

    def condition(self):
        quad_idx = len(self.quadruples) - 1
        self.quadruples.append(Quad("GOTOF", quad_idx, None, self.temp))
        self.gotos.append(quad_idx + 1)
        self.temp = self.temp + 1

    def add_operator(self, operator):
        self.operator_stack.append(operator)

    def start_parens(self):
        self.operator_stack.append('(')

    def end_parens(self):
        if self.operator_stack[-1] == '(':
            self.operator_stack.pop()
        else:
            raise Exception("Parenthesis mismatch")

    def add_literal(self, value, type_):
        # TODO: Since this are literals, make them global constants first,
        #       and then add them with their addresses.
        var_ctx = self.func_directory['global'].vars_[type_]['__constants__']
        addr = len(var_ctx)
        var_ctx[value] = VarRecord(addr)
        return addr

    def handle_math_operation(self, *operators):
        if self.operator_stack[-1] in operators:
            right_operand = self.operand_stack.pop()
            left_operand = self.operand_stack.pop()
            operator = self.operator_stack.pop()
            return_type = check_operation_type(
                operator, left_operand.type_, right_operand.type_
            )
            # Create new temp variable
            return_operand = Operand(f"T{self.temp}", return_type, self.temp)
            self.operand_stack.append(return_operand)
            self.quadruples.append(
                Quad(operator, left_operand, right_operand, return_operand)
            )

            self.temp = self.temp + 1

    def get_variable(self, ident, scope=None):
        if self.negative:
            ident = f'-{ident}'
            self.negative = False

        if scope is None:
            var_ctx = self.func_directory[self.function_stack[-1]].vars_
            for var_type_, vars_ in var_ctx.items():
                if ident in vars_:
                    self.operand_stack.append(
                        Operand(ident, var_type_, vars_[ident].addr)
                    )
                    break
            else:
                try:
                    self.get_variable(ident, scope='global')
                except Exception as e:
                    raise e
                else:
                    # Global lookup succeeded, short-fuse
                    return
        elif scope == 'global':
            var_ctx = self.func_directory['global'].vars_
            for var_type_, vars_ in var_ctx.items():
                if ident in vars_:
                    self.operand_stack.append(
                        Operand(ident, var_type_, vars_[ident].addr)
                    )
                break
            else:
                raise Exception(f'{ident} is undefined.')
        else:
            raise NotImplementedError(
                'Supplying a specific context is not yet supported.')

    def get_math_literal(self, literal, type_):
        if self.negative:
            literal = f'-{literal}'
            self.negative = False
        var_ctx = self.func_directory['global'].vars_[type_]['__constants__']
        if literal not in var_ctx:
            addr = self.add_literal(literal, type_)
        else:
            addr = var_ctx[literal].addr
        self.operand_stack.append(
            Operand(literal, type_, addr)
        )

    def check_function(self, ident):
        if ident not in self.func_directory:
            raise Exception(f"Function {ident} does not exist.")

    def call_function(self, ident):
        function = self.func_directory[ident]
        for i in range(function.params_):
            self.quadruples.append(Quad("PARAM", self.operand_stack.pop()))
        self.quadruples.append(Quad("ERA", ident, None, None))
        # This should be the result of the function
        self.operand_stack.append(Operand("return", function.type_, 0))

    def handle_assignment(self, ident, type_):
        var_ctx = self.func_directory[self.function_stack[-1]].vars_
        for var_type_, vars_ in var_ctx.items():
            if ident in vars_:
                raise Exception(
                    f"Variable {ident} already defined with type {var_type_}")
        else:
            addr = len(var_ctx[type_])
            if self.function_stack[-1] == 'global':
                addr -= 1  # Don't count the constants
            var_ctx[type_][ident] = VarRecord(addr, None)
        self.quadruples.append(
            Quad('ASSIGN', self.operand_stack.pop(),
                 None, Operand(ident, type_, addr))
        )

    def print_state(self):
        pp.pprint(self.func_directory)
        for i, quad in enumerate(self.quadruples):
            print(i, quad)
        pp.pprint(self.operand_stack)
        pp.pprint(self.operator_stack)

    def save_state(self, parser):
        parser.quadruples = self.quadruples
        parser.func_directory = self.func_directory
        parser.type_directory = self.type_directory
