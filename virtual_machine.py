from copy import deepcopy
from collections import defaultdict


class VirtualMachine():
    """Clase principal de la máquina virtual"""
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
        """Da de alta las tablas e inicializa las constantes"""
        self.quadruples = parser.quadruples
        self.func_directory = parser.func_directory
        self.type_directory = parser.type_directory
        constants = parser.constants

        for type_, variables in constants.items():
            for addr, value in variables.items():
                if type_ == 'Int':
                    value = int(value) if value != '[]' else value
                elif type_ == 'Float':
                    value = float(value)
                self.set_value(addr, value, type_, True)

    def get_value(self, addr, type_, is_global=False):
        """Busca un valor en memoria, verifica si es global"""
        # print(f"Get value at {addr} of {type_}. Global {is_global}")
        # Las listas están guardadas en su tipo primitivo, por eso se quitan los '[]'
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
        """Asigna un valor a la dirección de memoria"""
        # print(f"Set value {value} in {addr} of {type_}. Global {is_global}")
        # Las listas están guardadas en su tipo primitivo, por eso se quitan los '[]'
        if type_.startswith('['):
            type_ = type_.strip('[]')
        if is_global:
            search_memory = self.memory_stack[0]
        else:
            search_memory = self.memory
        if type_ == "Int":
            if value == '[]':
                self.list_table[addr] = []
                self.memory[self.INT_BASE + addr] = addr
                return
            search_memory[self.INT_BASE + addr] = value
        elif type_ == "Float":
            search_memory[self.FLOAT_BASE + addr] = value
        elif type_ == "Bool":
            search_memory[self.BOOL_BASE +
                          addr] = value
        elif type_ == "String":
            search_memory[self.STRING_BASE + addr] = value
        elif type_ == "Any":
            search_memory[self.EMPTY_ARR + addr] = addr

    def get_list_helper(self, param):
        """Regresa la lista guardada en memoria"""
        if param.name == 'list':
            address = param.address
        else:
            address = self.get_value(
                param.address, param.type_, param.is_global)
        return self.list_table[address]

    def process_param(self, param):
        """Inserta el parámetro a la pila"""
        self.params.insert(0, param)

    def print_(self):
        """Función de print del lenguaje"""
        param = self.params.pop()
        if param.dim:
            param_value = self.get_value(
                param.address, param.type_, param.is_global)
            print("PRINT:", self.list_table[param_value])
        else:
            param_value = self.get_value(
                param.address, param.type_, param.is_global)
            print("PRINT:", param_value)

    def append_(self, operand):
        """Función que junta dos listas y crea una nueva"""
        param2 = self.params.pop()
        param1 = self.params.pop()
        list1 = self.get_list_helper(param1)
        list2 = self.get_list_helper(param2)
        final_list = list1 + list2
        self.list_table[operand.address] = final_list
        self.set_value(operand.address, operand.address,
                       param1.type_, param1.is_global)

    def head(self, operand):
        """Regresa el primer elemento de la lista y lo asigna en memoria"""
        param = self.params.pop()
        list_ = self.get_list_helper(param)
        if len(list_) > 0:
            value = list_[0]
            self.set_value(operand.address, value,
                           param.type_, param.is_global)
        else:
            self.set_value(operand.address, 'non',
                           '[Int]', param.is_global)
            return

    def tail(self, operand):
        """Regresa el resto de la lista y la asigna en memoria"""
        param = self.params.pop()
        list_ = self.get_list_helper(param)
        if list_ == []:
            self.list_table[operand.adress] = []
            self.set_value(operand.address, operand.adress,
                           '[Any]', param.is_global)
            return
        else:
            list_ = list_[1:]
            self.list_table[operand.address] = list_
            self.set_value(operand.address, operand.address,
                           operand.type_, param.is_global)

    def input_(self, op):
        """Maneja el input (Int) del usuario"""
        value = input("Enter your input: ")
        self.set_value(op.address, value, op.type_, op.is_global)

    def era(self, func_name):
        """
          Crea una nueva memoria para la llamada de función y un nuevo stack
          de listas. Mueve cada valor del parámetro del contexto pasado al contexto
          nuevo y marca como memoria actual la nueva que se creo.
        """
        new_memory = [None]*10000
        new_list_memory = defaultdict(list)
        temp_memory = []
        self.param_defs = self.func_directory[func_name].params_addrs
        for i, param in enumerate(self.params):
            param_def_addr = self.param_defs[i]
            if param.dim:
                param_list = self.get_list_helper(param)
                new_list_memory[param_def_addr] = param_list
                temp_memory = self.memory
                self.memory = new_memory
                # Not sure if this should be the way
                self.set_value(param_def_addr, param_def_addr, param.type_)
            else:
                param_value = self.get_value(param.address, param.type_)
                temp_memory = self.memory
                self.memory = new_memory
                self.set_value(param_def_addr, param_value, param.type_)
            self.memory = temp_memory
        self.memory_stack.append(new_memory)
        self.memory = new_memory
        self.list_table_stack.append(new_list_memory)
        self.list_table = new_list_memory
        self.params = []
        self.param_defs = []

    def handle_return(self, op):
        """Mueve el valor de retorno al contexto pasado"""
        value = self.get_value(op.address, op.type_, op.is_global)
        if value is None:
            return
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

    def get_list(self, address, is_global=False):
        """Regresa la lista dependiendo del contexto"""
        if is_global:
            return self.list_table_stack[0][address]
        else:
            return self.list_table[address]

    def perform_operation(self, method, quad):
        """Realiza operación matemática"""
        left = quad.left
        left_value = self.get_value(
            left.address, left.type_, left.is_global)
        right = quad.right
        right_value = self.get_value(
            right.address, right.type_, right.is_global)
        # Saca el tipo del elemento
        type_ = type(left_value)
        result_op = quad.result
        # Compara dos listas si ambas son dimensionadas
        if left.dim and right.dim:
            left_value = self.get_list(left_value, left.is_global)
            right_value = self.get_list(right_value, right.is_global)
            operation = getattr(list, method)
            result = operation(left_value, right_value)
            self.set_value(result_op.address, result,
                           result_op.type_, result_op.is_global)
        elif left_value == 'non' or right_value == 'non':
            result = False if result_op.type_ == 'Bool' else 'non'
            self.set_value(result_op.address, result,
                           result_op.type_, result_op.is_global)
        else:
            # Dinámicamente obtiene la función a ejecutar
            # usando el nombre dle método y el tipo
            operation = getattr(type_, method)
            result = operation(left_value, right_value)
            # Realiza la operación y si hay un error trata de hacerla al revés
            # (Python necesita que si es suma de Float el Float esté a la izq)
            # Sin embargo, no se pierde la asociatividad
            if result is NotImplemented:
                type_ = type(right_value)
                method = method[:2] + 'r' + method[2:]
                operation = getattr(type_, method)
                result = operation(right_value, left_value)
            self.set_value(result_op.address, result,
                           result_op.type_, result_op.is_global)

    def run(self):
        """
          Recorre todos los cuádruplos y ejecuta las funciones de su
          código de operación
        """
        i = 0
        for j, quad in enumerate(self.quadruples):
            print(j, quad)
        # print("===========")
        while i < len(self.quadruples):
            quad = self.quadruples[i]
            if quad.operator == 'ASSIGN':
                value_addr = quad.left.address
                value_type = quad.left.type_
                is_global = quad.left.is_global
                value = self.get_value(value_addr, value_type, is_global)
                if quad.left.dim:
                    value = value_addr
                result = quad.result
                self.set_value(result.address, value,
                               result.type_, result.is_global)
            elif quad.operator == "SET":
                value = quad.left
                result = quad.result
                self.set_value(
                    result.address, value, result.type_, result.is_global
                )
            elif quad.operator == 'PRINT':
                self.print_()
            elif quad.operator == 'HEAD':
                self.head(quad.result)
            elif quad.operator == 'TAIL':
                self.tail(quad.result)
            elif quad.operator == 'INPUT':
                self.input_(quad.result)
            elif quad.operator == 'APPEND':
                self.append_(quad.result)
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
                if value == False:
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
                self.era(quad.result)
            elif quad.operator == "RETURN":
                self.handle_return(quad.result)
            elif quad.operator == "ENDPROC":
                self.memory_stack.pop()
                self.memory = self.memory_stack[-1]
                self.list_table_stack.pop()
                self.list_table = self.list_table_stack[-1]
                i = self.call_stack.pop()
                continue
            i += 1
