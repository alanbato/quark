class VirtualMachine():

    quadruples = []
    func_directory = {}
    type_directory = {}
    memory = [None]*1000
    memory_stack = [memory]
    params = []
    INT_BASE = 0
    FLOAT_BASE = 250
    BOOL_BASE = 500
    STRING_BASE = 750

    def __init__(self, parser, **kwargs):
        self.quadruples = parser.quadruples
        self.func_directory = parser.func_directory
        self.type_directory = parser.type_directory

        global_vars = self.func_directory['global'].vars_
        for type_, variables in global_vars.items():
            for const, record in variables['__constants__'].items():
                self.set_value(record.addr, const, type_)

    def get_value(self, addr, type_):
        if type_ == "Int":
            return self.memory[self.INT_BASE + addr]
        elif type_ == "Float":
            return self.memory[self.FLOAT_BASE + addr]
        elif type_ == "Bool":
            return self.memory[self.BOOL_BASE + addr]
        elif type_ == "String":
            return self.memory[self.STRING_BASE + addr]

    def set_value(self, addr, value, type_):
        if type_ == "Int":
            self.memory[self.INT_BASE + addr] = int(value)
        elif type_ == "Float":
            self.memory[self.FLOAT_BASE + addr] = float(value)
        elif type_ == "Bool":
            self.memory[self.BOOL_BASE + addr] = bool(value)
        elif type_ == "String":
            self.memory[self.STRING_BASE + addr] = value

    def process_param(self, param):
        self.params.insert(0, param)

    def era(self, func_name):
        new_memory = [None]*1000
        temp_memory = []
        for _, param in enumerate(self.params):
            param_value = self.get_value(param.addr, param.type_)
            temp_memory = self.memory
            self.memory = new_memory
            self.set_value(param.address, param_value, param.type_)
            self.memory = temp_memory
        self.memory_stack.append(new_memory)
        self.memory = new_memory
        self.params = []

    def handle_return(self, op):
        # TODO: Implement return handling, assigning the variable to the address
        pass

    def end_proc(self):
        self.memory_stack.pop()
        self.memory = self.memory_stack[-1]

    def run(self):
        i = 0
        while i < len(self.quadruples):
            quad = self.quadruples[i]
            print(i, quad)
            if quad.operator == 'ASSIGN':
                value_addr = quad.left.address
                value_type = quad.left.type_
                value = self.get_value(value_addr, value_type)
                result = quad.result
                self.set_value(result.addr, value, result.type_)
            elif quad.operator == 'GOTOF':
                value_addr = quad.left.address
                value_type = quad.left.type_
                value = self.get_value(value_addr, value_type)
                if not value:
                    i = quad.result
            elif quad.operator == 'GOTO':
                i = quad.result
            elif quad.operator == '+':
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value + right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == '-':
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value - right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == '*':
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value * right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == '/':
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value / right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == '%':
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value % right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == ">":
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value > right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == ">=":
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value >= right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == "=":
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value = right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == "<":
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value < right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == "<=":
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value <= right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == "!=":
                left = quad.left
                left_value = self.get_value(left.addr, left.type_)
                right = quad.right
                right_value = self.get_value(right.addr, right.type_)
                result = left_value != right_value
                result_op = quad.result.address
                self.set_value(result_op.addr, result, result_op.type_)
            elif quad.operator == "PARAM":
                self.process_param(quad.left)
            elif quad.operator == "ERA":
                self.era(quad.left)
            elif quad.operator == "RETURN":
                self.handle_return(quad.result)
            elif quad.operator == "ENDPROC":
                self.end_proc()
