from copy import deepcopy


class VirtualMachine():

    quadruples = []
    func_directory = {}
    type_directory = {}
    memory = [None]*10000
    memory_stack = [memory]
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
                value
                self.set_value(addr, value, type_, True)

    def get_value(self, addr, type_, is_global=False):
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
        if type_.startswith('['):
            type_ = type_.strip('[]')
        if is_global:
            search_memory = self.memory_stack[0]
        else:
            search_memory = self.memory
        if type_ == "Int":
            search_memory[self.INT_BASE + addr] = int(value)
        elif type_ == "Float":
            search_memory[self.FLOAT_BASE + addr] = float(value)
        elif type_ == "Bool":
            search_memory[self.BOOL_BASE +
                          addr] = value
        elif type_ == "String":
            search_memory[self.STRING_BASE + addr] = value
        elif type_ == "Any":
            search_memory[self.EMPTY_ARR + addr] = None

    def process_param(self, param):
        self.params.insert(0, param)

    def process_param_def(self, param):
        self.param_defs.append(param)  # Es append o insert(0,) ?

    def print_(self):
        counter = 0

        def recursive_print(param):
            nonlocal counter
            if len(param.dim) == 1:
                counter += 1
            else:
                print('[', end='')
                for dim in range(param.dim[0][1]):
                    value = self.get_value(param.address + i,
                                           param.type_, param.is_global)
                    print(value, end=',')
                print(']')
        param = self.params.pop()
        if param.dim:
            print(param)
            recursive_print(param)
        else:
            param_value = self.get_value(
                param.address, param.type_, param.is_global)
            print("DEBUG:", param_value)

    def head(self, operand):
        param = self.params.pop()
        value = self.get_value(param.address, param.type_, param.is_global)
        if value is None:
            self.set_value(operand.address, '[]',
                           '[Any]', param.is_global)
            return
        else:
            self.set_value(operand.address, value,
                           param.type_, param.is_global)

    def tail(self, operand):
        param = self.params.pop()
        param_address = param.address + 1
        value = self.get_value(
            param_address, param.type_, param.is_global)
        if value is None:
            self.set_value(operand.address, '[]',
                           '[Any]', param.is_global)
            return
        for i in range(5):
            value = self.get_value(
                param_address + i, param.type_, param.is_global)
            if value is None:
                break
            self.set_value(operand.address + i, value,
                           param.type_, param.is_global)

    def input_(self, op):
        value = input("Enter your input: ")
        self.set_value(op.address, value, op.type_, op.is_global)

    def era(self, func_name):
        new_memory = [None]*10000
        temp_memory = []
        self.param_defs = self.func_directory[func_name].params_addrs
        for i, param in enumerate(self.params):
            if param.dim:
                for j in range(param.dim[0][0]):
                    param_value = self.get_value(
                        param.address + j, 'Int')
                    if param_value is None:
                        continue
                    temp_memory = self.memory
                    self.memory = new_memory
                    param_def_addr = self.param_defs[i]
                    self.set_value(param_def_addr + j,
                                   param_value, 'Int')
                    self.memory = temp_memory
            else:
                param_value = self.get_value(param.address, param.type_)
                temp_memory = self.memory
                self.memory = new_memory
                param_def_addr = self.param_defs[i]
                self.set_value(param_def_addr, param_value, param.type_)
                self.memory = temp_memory
        self.memory_stack.append(new_memory)
        self.memory = new_memory
        self.params = []
        self.param_defs = []

    def handle_return(self, op):
        value = self.get_value(op.address, op.type_, op.is_global)
        go_sub_idx = self.call_stack[-1] - 1
        right_address = self.quadruples[go_sub_idx].right
        search_memory = self.memory_stack[-2]
        if op.type_ == "Int":
            search_memory[self.INT_BASE + right_address] = int(value)
        elif op.type_ == "Float":
            search_memory[self.FLOAT_BASE + right_address] = float(value)
        elif op.type_ == "Bool":
            search_memory[self.BOOL_BASE +
                          right_address] = value
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
            # print(i, quad)
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
            elif quad.operator == 'COPYVAL':
                from_ = quad.left
                value = self.get_value(
                    from_.address, from_.type_, from_.is_global)
                address = quad.result
                self.set_value(address, value, 'Int')
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
                i = self.call_stack.pop()
                continue
            i += 1
