from utils import check_operation_type

import attr
from typing import Any, Dict, List
import pprint
pp = pprint.PrettyPrinter()


@attr.s
class FuncRecord:
    # The _ is used to avoid a collision with a builtin or restricted name
    type_: str = attr.ib()
    vars_: Dict[str, Any] = attr.ib(attr.Factory(dict))
    params_: int = attr.ib(0)
    start_: int = attr.ib(0)
    params_addrs: List[int] = attr.ib(attr.Factory(list))


@attr.s
class VarRecord:
    addr: int = attr.ib()
    dim: Any = attr.ib(None)
    is_global: bool = attr.ib(False)


@attr.s
class Operand:
    name: str = attr.ib()
    type_: str = attr.ib()
    address: int = attr.ib(None)
    is_global: bool = attr.ib(False)


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
                             {'Int': {},
                              'Float': {},
                              'String': {},
                              'Bool': {},
                              'non': {},
                              'Any': {}, '[Any]': {},
                              }),
        "append": FuncRecord('[Any]', {}, 2),
        "print": FuncRecord('non', {}, 1),
        "upper": FuncRecord('String', {}, 1),
        "head": FuncRecord('Any', {}, 1),
        "tail": FuncRecord('[Any]', {}, 1),
        "input": FuncRecord('Int', {}, 0)
    }
    negative = False
    type_directory = {}
    function_stack = ["global"]
    operand_stack = []
    operator_stack = []
    quadruples = []
    constants = {'Int': {}, 'Float': {}, 'String': {}}
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
                None, {'Int': {}, 'Float': {}, 'Bool': {},
                       'String': {}, 'Any': {}, 'non': {}, '[Any]': {}, 'PARAMS:': {}
                       }, 0, len(self.quadruples))

    def set_function_return_type(self, func_name, ret_type):
        self.func_directory[func_name].type_ = ret_type
        self.gotos.append(len(self.quadruples))
        self.quadruples.append(Quad("GOTO"))
        self.func_directory[func_name].start_ = len(self.quadruples)

    def process_function_clause(self):
        self.quadruples.append(Quad("RETURN", self.operand_stack.pop()))
        quad_idx = self.gotos.pop()
        temp = self.quadruples[quad_idx]
        self.gotos.append(len(self.quadruples))
        self.quadruples.append(Quad("GOTO"))
        temp.result = len(self.quadruples)

    def process_default_clause(self):
        self.quadruples.append(Quad("RETURN", self.operand_stack.pop()))

    def process_function_end(self):
        while len(self.gotos) > 1:
            quad_idx = self.gotos.pop()
            quad = self.quadruples[quad_idx]
            quad.result = len(self.quadruples)
        self.quadruples.append(Quad("ENDPROC"))
        goto_idx = self.gotos.pop()
        self.quadruples[goto_idx].result = len(self.quadruples)
        self.function_stack.pop()
        self.operand_stack = []
        self.operator_stack = []
        self.temp = 0

    def process_param(self, ident, type_):
        function_name = self.function_stack[-1]
        function = self.func_directory[function_name]
        function.params_ += 1
        addr = len(function.vars_[type_])
        function.vars_[type_][ident] = VarRecord(addr, None)
        function.params_addrs.append(addr)
        # self.quadruples.append(
        #     Quad("PARAMDEF", ident, type_, addr)
        # )

    def check_user_def_type(self, type_id):
        if type_id not in self.type_directory:
            raise Exception(f"Undefined type {type_id}")

    def define_type(self, type_id, type_value):
        if type_value.startswith("("):
            type_value = type_value[1:-1].split("|")

    def condition(self):
        self.gotos.append(len(self.quadruples))
        self.quadruples.append(
            Quad("GOTOF", self.operand_stack.pop()))

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
        var_ctx = self.func_directory['global'].vars_[type_]
        addr = len(var_ctx)
        var_ctx[value] = VarRecord(addr, None, True)
        self.constants[type_][addr] = value
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
            func_name = self.function_stack[-1]
            addr = len(self.func_directory[func_name].vars_[return_type])
            self.func_directory[func_name].vars_[
                return_type][f"__T{self.temp}__"] = VarRecord(addr)
            return_operand = Operand(
                f"__T{self.temp}__", return_type, addr, func_name == 'global')
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
                        Operand(ident, var_type_, vars_[ident].addr, True)
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
        var_ctx = self.func_directory['global'].vars_[type_]
        if literal not in var_ctx:
            addr = self.add_literal(literal, type_)
        else:
            addr = var_ctx[literal].addr
        self.operand_stack.append(
            Operand(literal, type_, addr, True)
        )

    def check_function(self, ident):
        if ident not in self.func_directory:
            raise Exception(f"Function {ident} does not exist.")

    def call_function(self, ident):
        function = self.func_directory[ident]
        for i in range(function.params_):
            self.quadruples.append(
                Quad("PARAM", None, None, self.operand_stack.pop()))
        if ident == 'print':
            self.quadruples.append(Quad("PRINT"))
            self.operand_stack.append(Operand('non', 'non', 0, True))
        elif ident == 'input':
            func_name = self.function_stack[-1]
            addr = len(self.func_directory[func_name].vars_['Int'])
            self.func_directory[func_name].vars_[
                function.type_][f"__T{self.temp}__"] = VarRecord(addr)
            result_operand = Operand(
                'input', 'Int', addr, func_name == 'global')
            self.operand_stack.append(result_operand)
            self.quadruples.append(Quad("INPUT", result_operand))
        else:
            self.quadruples.append(Quad("ERA", ident, None, None))
            # Create temp variable
            func_name = self.function_stack[-1]
            addr = len(self.func_directory[func_name].vars_[function.type_])
            self.func_directory[func_name].vars_[
                function.type_][f"__T{self.temp}__"] = VarRecord(addr)
            return_operand = Operand(
                f"__T{self.temp}__", function.type_, addr, func_name == 'global')
            self.operand_stack.append(return_operand)
            self.temp += 1
            # Call function
            self.quadruples.append(Quad("GOSUB", ident, addr, function.start_))

    def handle_assignment(self, ident, type_):
        var_ctx = self.func_directory[self.function_stack[-1]].vars_
        for var_type_, vars_ in var_ctx.items():
            if ident in vars_:
                raise Exception(
                    f"Variable {ident} already defined with type {var_type_}")
        else:
            addr = len(var_ctx[type_])
            is_global = self.function_stack[-1] == 'global'
            var_ctx[type_][ident] = VarRecord(addr, None)
        self.quadruples.append(
            Quad('ASSIGN', self.operand_stack.pop(),
                 None, Operand(ident, type_, addr, is_global))
        )
        self.operand_stack.append(Operand('non', 'non', 0, True))

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
        parser.constants = self.constants
