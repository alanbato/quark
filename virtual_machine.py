from copy import deepcopy
from collections import defaultdict


class VirtualMachine():

    quadruples = []
    func_directory = {}
    type_directory = {}
    memory = [None]*10000
    memory_stack = [memory]
    list_table = defaultdict(list)
    list_table_stack = [list_table]
    params = []
    param_defs = []
    call_stack = []
    INT_BASE = 0
    FLOAT_BASE = 250
    BOOL_BASE = 500
    STRING_BASE = 750
    EMPTY_ARR = 1000

    def __init__(self, parser, **kwargs):
        self.quadruples = parser.quadruples
        self.func_directory = parser.func_directory
        self.type_directory = parser.type_directory
        constants = parser.constants

        for type_, variables in constants.items():
            for addr, value in variables.items():
                if type_ == 'Int':
                    value = int(value)
                elif type_ == 'Float':
                    value = float(value)
                self.set_value(addr, value, type_, True)

    def get_value(self, addr, type_, is_global=False):
        # print(f"Get value at {addr} of {type_}. Global {is_global}")
        if type_.startswith('['):
            type_ = type_.strip('[]')
        if is_global:
            search_memory = self.memory_stack[0]
        else:
            search_memory = self.memory
        if type_ == "Int":
            return search_memory[self.INT_BASE + addr]
        elif type_ == "Float":
            return search_memory[self.FLOAT_BASE + addr]
        elif type_ == "Bool":
            return search_memory[self.BOOL_BASE + addr]
        elif type_ == "String":
            return search_memory[self.STRING_BASE + addr]
        elif type_ == "Any":
            return search_memory[self.EMPTY_ARR + addr]

    def set_value(self, addr, value, type_, is_global=False):
        # print(f"Set value {value} in {addr} of {type_}. Global {is_global}")
        if type_.startswith('['):
            type_ = type_.strip('[]')
        if is_global:
            search_memory = self.memory_stack[0]
        else:
            search_memory = self.memory
        if type_ == "Int":
            search_memory[self.INT_BASE + addr] = value
        elif type_ == "Float":
            search_memory[self.FLOAT_BASE + addr] = value
        elif type_ == "Bool":
            search_memory[self.BOOL_BASE +
                          addr] = value
        elif type_ == "String":
            search_memory[self.STRING_BASE + addr] = value
        elif type_ == "Any":
            search_memory[self.EMPTY_ARR + addr] = value

    def process_param(self, param):
        self.params.insert(0, param)

    def process_param_def(self, param):
        self.param_defs.append(param)  # Es append o insert(0,) ?

    def print_(self):
        param = self.params.pop()
        if param.dim:
            param_value = self.get_value(
                param.address, param.type_, param.is_global)
            print("DEBUG:", self.list_table[param_value])
        else:
            param_value = self.get_value(
                param.address, param.type_, param.is_global)
            print("DEBUG:", param_value)

    def append_(self, operand):
        param1 = self.params.pop()
        param2 = self.params.pop()
        print(param1, param2)
        counter = 0
        for i in range(5):
            value = self.get_value(
                param1.address + counter, param1.type_, param1.is_global)
            counter += 1
            if value is None:
                break
            self.set_value(operand.address + counter, value,
                           param1.type_, param1.is_global)
        for i in range(5):
            value = self.get_value(
                param2.address + counter, param2.type_, param2.is_global)
            counter += 1
            if value is None:
                break
            self.set_value(operand.address + counter, value,
                           param2.type_, param2.is_global)

    def head(self, operand):
        param = self.params.pop()
        if param.address in self.list_table:
            value = self.list_table[0]
            self.set_value(operand.address, value,
                           param.type_, param.is_global)
        else:
            self.set_value(operand.address, '[]',
                           '[Any]', param.is_global)
            return
        value = self.get_value(param.address, param.type_, param.is_global)

    def tail(self, operand):
        param = self.params.pop()
        param_address = param.address
        value = self.get_value(
            param_address, param.type_, param.is_global)
        if value == '[]':
            self.set_value(operand.address, '[]', '[Any]', param.is_global)
            return
        else:
            lst = self.list_table[value][1:]
            self.set_value(operand.address, operand.address,
                           operand.type_, param.is_global)
            for elem in lst:
                self.list_table[operand.address].append(elem)

    def input_(self, op):
        value = input("Enter your input: ")
        self.set_value(op.address, value, op.type_, op.is_global)

    def era(self, func_name):
        new_memory = [None]*10000
        new_list_memory = defaultdict(list)
        temp_memory = []
        self.param_defs = self.func_directory[func_name].params_addrs
        for i, param in enumerate(self.params):
            temp_memory = self.memory
            self.memory = new_memory
            if param.dim:
                param_list = self.list_table[param.address]
                param_def_addr = self.param_defs[i]
                new_list_memory[param_def_addr] = param_list
                # Not sure if this should be the way
                self.set_value(param_def_addr, param_def_addr, param.type_)
            else:
                param_value = self.get_value(param.address, param.type_)
                param_def_addr = self.param_defs[i]
                self.set_value(param_def_addr, param_value, param.type_)
            self.memory = temp_memory
        self.memory_stack.append(new_memory)
        self.memory = new_memory
        self.list_table_stack.append(new_list_memory)
        self.list_table = new_list_memory
        self.params = []
        self.param_defs = []

    def handle_return(self, op):
        value = self.get_value(op.address, op.type_, op.is_global)
        go_sub_idx = self.call_stack[-1] - 1
        right_address = self.quadruples[go_sub_idx].right
        search_memory = self.memory_stack[-2]
        if op.dim:
            self.list_table_stack[-2][right_address] = self.list_table[value]
            search_memory[self.INT_BASE + right_address] = right_address
            return

        if op.type_ == "Int":
            search_memory[self.INT_BASE + right_address] = int(value)
        elif op.type_ == "Float":
            search_memory[self.FLOAT_BASE + right_address] = float(value)
        elif op.type_ == "Bool":
            search_memory[self.BOOL_BASE +
                          right_address] = value
        elif op.type_ == "Any":
            search_memory[self.EMPTY_ARR + right_address] = value
        elif op.type_ == "String":
            search_memory[self.STRING_BASE + right_address] = value

    def perform_operation(self, method, quad):
        left = quad.left
        left_value = self.get_value(
            left.address, left.type_, left.is_global)
        right = quad.right
        right_value = self.get_value(
            right.address, right.type_, right.is_global)
        type_ = type(left_value)
        result_op = quad.result
        if left_value is None or right_value is None:
            if left_value is right_value:
                self.set_value(result_op.address, True,
                               result_op.type_, result_op.is_global)
            else:
                self.set_value(result_op.address, False,
                               result_op.type_, result_op.is_global)
            return
        operation = getattr(type_, method)
        result = operation(left_value, right_value)
        if result is NotImplemented:
            type_ = type(right_value)
            method = method[:2] + 'r' + method[2:]
            operation = getattr(type_, method)
            result = operation(right_value, left_value)
        self.set_value(result_op.address, result,
                       result_op.type_, result_op.is_global)

    def run(self):
        i = 0
        while i < len(self.quadruples):
            quad = self.quadruples[i]
            if quad.operator == 'ASSIGN':
                value_addr = quad.left.address
                value_type = quad.left.type_
                is_global = quad.left.is_global
                value = self.get_value(value_addr, value_type, is_global)
                result = quad.result
                self.set_value(result.address, value,
                               result.type_, result.is_global)
            elif quad.operator == 'PRINT':
                self.print_()
            elif quad.operator == 'HEAD':
                self.head(quad.left)
            elif quad.operator == 'TAIL':
                self.tail(quad.left)
            elif quad.operator == 'INPUT':
                self.input_(quad.left)
            elif quad.operator == 'APPEND':
                self.append_(quad.left)
            elif quad.operator == 'COPYVAL':
                from_ = quad.left
                value = self.get_value(
                    from_.address, from_.type_, from_.is_global)
                address = quad.result
                lst = self.list_table[address]
                lst.append(value)
            elif quad.operator == 'GOSUB':
                self.call_stack.append(i + 1)
                i = quad.result
                continue
            elif quad.operator == 'GOTOF':
                value_addr = quad.left.address
                value_type = quad.left.type_
                is_global = quad.left.is_global
                value = self.get_value(value_addr, value_type, is_global)
                if not value:
                    i = quad.result
                    continue
            elif quad.operator == 'GOTO':
                i = quad.result
                continue
            elif quad.operator == '+':
                self.perform_operation('__add__', quad)
            elif quad.operator == '-':
                self.perform_operation('__sub__', quad)
            elif quad.operator == '*':
                self.perform_operation('__mul__', quad)
            elif quad.operator == '/':
                self.perform_operation('__truediv__', quad)
            elif quad.operator == '%':
                self.perform_operation('__mod__', quad)
            elif quad.operator == ">":
                self.perform_operation('__gt__', quad)
            elif quad.operator == ">=":
                self.perform_operation('__ge__', quad)
            elif quad.operator == "=":
                self.perform_operation('__eq__', quad)
            elif quad.operator == "<":
                self.perform_operation('__lt__', quad)
            elif quad.operator == "<=":
                self.perform_operation('__le__', quad)
            elif quad.operator == "!=":
                self.perform_operation('__ne__', quad)
            elif quad.operator == "PARAM":
                self.process_param(quad.result)
            elif quad.operator == "PARAMDEF":
                self.process_param_def(quad.result)
            elif quad.operator == "ERA":
                self.era(quad.left)
            elif quad.operator == "RETURN":
                self.handle_return(quad.left)
            elif quad.operator == "ENDPROC":
                self.memory_stack.pop()
                self.memory = self.memory_stack[-1]
                self.list_table_stack.pop()
                self.list_table = self.list_table_stack[-1]
                i = self.call_stack.pop()
                continue
            i += 1
