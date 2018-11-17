class VirtualMachine():

    quadruples = []
    func_directory = {}
    type_directory = {}

    def __init__(self, parser, **kwargs):
        self.quadruples = parser.quadruples
        self.func_directory = parser.func_directory
        self.type_directory = parser.type_directory

    def get_value(self, addr):
        return 0

    def set_value(self, addr, value):
        pass

    def run(self):
        for i, quad in enumerate(self.quadruples):
            print(i, quad)
            if quad.operator == 'ASSIGN':
                value_addr = quad.left.address
                value = self.get_value(value_addr)
                result_addr = quad.result.address
                self.set_value(result_addr, value)
            elif quad.operator == '+':
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value + right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == '-':
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value - right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == '*':
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value * right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == '/':
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value / right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == '%':
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value % right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == ">":
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value > right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == ">=":
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value >= right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == "=":
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value == right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == "<":
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value < right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == "<=":
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value <= right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
            elif quad.operator == "!=":
                left_addr = quad.left.address
                left_value = self.get_value(left_addr)
                right_addr = quad.right.address
                right_value = self.get_value(right_addr)
                result = left_value != right_value
                result_addr = quad.result.address
                self.set_value(result_addr, result)
