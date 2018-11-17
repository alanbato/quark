class VirtualMachine():

    quadruples = []
    func_directory = {}
    type_directory = {}
    memory = [None]*1000
    memory_stack = [memory]
    params = []
    param_defs = []
    call_stack = []
    INT_BASE = 0
    FLOAT_BASE = 250
    BOOL_BASE = 500
    STRING_BASE = 750

    def __init__(self, parser, **kwargs):
        self.quadruples = parser.quadruples
        self.func_directory = parser.func_directory
        self.type_directory = parser.type_directory
        constants = parser.constants

        for type_, variables in constants.items():
            for addr, value in variables.items():
                self.set_value(addr, value, type_, True)

    def get_value(self, addr, type_, is_global=False):
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

    def set_value(self, addr, value, type_, is_global=False):
        if is_global:
            search_memory = self.memory_stack[0]
        else:
            search_memory = self.memory
        if type_ == "Int":
            search_memory[self.INT_BASE + addr] = int(value)
        elif type_ == "Float":
            search_memory[self.FLOAT_BASE + addr] = float(value)
        elif type_ == "Bool":
            search_memory[self.BOOL_BASE + addr] = bool(value)
        elif type_ == "String":
            search_memory[self.STRING_BASE + addr] = value

    def process_param(self, param):
        self.params.insert(0, param)

    def process_param_def(self, param):
        self.param_defs.append(param) # Es append o insert(0,) ?

    def print_(self):
        param = self.params.pop()
        param_value = self.get_value(param.address, param.type_)
        print("DEBUG:", param_value)

    def era(self, func_name):
        new_memory = [None]*1000
        temp_memory = []
        print(self.params, self.param_defs)
        for i, param in enumerate(self.params):
            print('hi')
            param_value = self.get_value(param.address, param.type_)
            temp_memory = self.memory
            self.memory = new_memory
            param_def_addr = self.param_defs[i]
            print(param_value)
            self.set_value(param_def_addr, param_value, param.type_)
            self.memory = temp_memory
        self.memory_stack.append(new_memory)
        self.memory = new_memory
        self.params = []
        self.param_defs = []

    def handle_return(self, op):
        print(self.call_stack)
        value = self.get_value(op.address, op.type_, op.is_global)
        go_sub_idx = self.call_stack[-1] - 1
        right_address = self.quadruples(go_sub_idx).right
        self.memory_stack[-2][right_address] = value

    def perform_operaton(self, method, quad):
        left = quad.left
        left_value = self.get_value(
            left.address, left.type_, left.is_global)
        right = quad.right
        right_value = self.get_value(
            right.address, right.type_, right.is_global)
        type_ = type(left_value)
        operation = getattr(type_, method)
        result = operation(left_value, right_value)
        print(left_value, right_value)
        if result is NotImplemented:
            type_ = type(right_value)
            method = method[:2] + 'r' + method[2:]
            operation = getattr(type_, method)
            result = operation(right_value, left_value)
        result_op = quad.result
        print(result, result_op.type_)
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
                self.set_value(result.address, value, result.type_)
            elif quad.operator == 'PRINT':
                self.print_()
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
                self.perform_operaton('__add__', quad)
            elif quad.operator == '-':
                self.perform_operaton('__sub__', quad)
            elif quad.operator == '*':
                self.perform_operaton('__mul__', quad)
            elif quad.operator == '/':
                self.perform_operaton('__truediv__', quad)
            elif quad.operator == '%':
                self.perform_operaton('__mod__', quad)
            elif quad.operator == ">":
                self.perform_operaton('__gt__', quad)
            elif quad.operator == ">=":
                self.perform_operaton('__ge__', quad)
            elif quad.operator == "=":
                self.perform_operaton('__eq__', quad)
            elif quad.operator == "<":
                self.perform_operaton('__lt__', quad)
            elif quad.operator == "<=":
                self.perform_operaton('__le__', quad)
            elif quad.operator == "!=":
                self.perform_operaton('__ne__', quad)
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
