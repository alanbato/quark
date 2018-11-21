from utils import check_operation_type

import attr
from typing import Any, Dict, List
import pprint
pp = pprint.PrettyPrinter()


# Clase utilizada para guardar el registro de una función
@attr.s
class FuncRecord:
    # The _ is used to avoid a collision with a builtin or restricted name
    type_: str = attr.ib()
    vars_: Dict[str, Any] = attr.ib(attr.Factory(dict))
    params_: int = attr.ib(0)
    start_: int = attr.ib(0)
    params_addrs: List[int] = attr.ib(attr.Factory(list))
    var_counters: Dict[str, int] = attr.ib(attr.Factory(dict))

    # Regresa la siguiente dirección libre en memoria para ese tipo
    def next_addr(self, type_):
        if type_ in self.var_counters:
            self.var_counters[type_] += 1
        else:
            self.var_counters[type_] = 0
        return self.var_counters[type_]

    # Hace un salto para guardar cierta cantidad de memoria
    def update_addr(self, type_, length):
        if type_ in self.var_counters:
            self.var_counters[type_] += length - 1
        else:
            self.var_counters[type_] = length - 1


# Clase para guardar la definición de una lista
@attr.s
class ListDef:
    type_: str = attr.ib(None)
    primitive_type: str = attr.ib(None)
    total: int = attr.ib(0)
    addr: int = attr.ib(None)


# Clase para guardar la definición de una variable
@attr.s
class VarRecord:
    addr: int = attr.ib()
    dim: Any = attr.ib(None)
    is_global: bool = attr.ib(False)


# Clase para guardar la definición de un operando
@attr.s
class Operand:
    name: str = attr.ib()
    type_: str = attr.ib()
    address: int = attr.ib(None)
    is_global: bool = attr.ib(False)
    dim: list = attr.ib(None)


# Clase para guardar la definición de un cuádruplo
@attr.s
class Quad:
    operator = attr.ib()
    left: Operand = attr.ib(None)
    right: Operand = attr.ib(None)
    result: Any = attr.ib(None)


# Clase principal del compilador
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
    list_dims = {}
    list_stack = []
    copy_val_queue = []
    quadruples = []
    constants = {'Int': {}, 'Float': {}, 'String': {},
                 'Bool': {}, 'non': {}, '[Any]': {}}
    gotos = []
    temp = 0  # ID de los temporales

    def set_negative(self):
        """Indica que la siguiente variable es negativa"""
        self.negative = True

    def define_function(self, func_name):
        """Agrega la función al stack y crea su registro en directorio de funciones"""
        self.function_stack.append(func_name)
        if func_name in self.func_directory:
            Exception("Function {} already defined".format(func_name))
        else:
            self.func_directory[func_name] = FuncRecord(
                None, {'Int': {}, 'Float': {}, 'Bool': {},
                       'String': {}, 'Any': {}, 'non': {}, '[Any]': {}, 'PARAMS:': {}
                       }, 0, len(self.quadruples))

    def set_function_return_type(self, func_name, ret_type):
        """Indica el tipo de retorno de la función y su cuádruplo de inicio"""
        self.func_directory[func_name].type_ = ret_type
        self.gotos.append(len(self.quadruples))
        self.quadruples.append(Quad("GOTO"))
        self.func_directory[func_name].start_ = len(self.quadruples)

    def process_function_clause(self):
        """Procesa el final de una cláusula en la función"""
        self.quadruples.append(Quad("RETURN", result=self.operand_stack.pop()))
        quad_idx = self.gotos.pop()
        temp = self.quadruples[quad_idx]
        self.gotos.append(len(self.quadruples))
        self.quadruples.append(Quad("GOTO"))
        temp.result = len(self.quadruples)

    def process_default_clause(self):
        """Procesa la cláusula default en la función"""
        self.quadruples.append(Quad("RETURN", result=self.operand_stack.pop()))

    def process_function_end(self):
        """Final de función: soluciona pila de saltos y agrega cuádruplo de ENDPROC"""
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
        """Crea una dirección para el parámetro y aumenta el contador de parámetros"""
        function_name = self.function_stack[-1]
        function = self.func_directory[function_name]
        function.params_ += 1
        dim = False
        if type_.startswith('['):
            dim = True
            type_ = type_.strip('[]')
        addr = function.next_addr(type_)
        function.vars_[type_][ident] = VarRecord(addr, dim)
        function.params_addrs.append(addr)

    def check_user_def_type(self, type_id):
        """Verifica que el tipo del usuario esté definido"""
        if type_id not in self.type_directory:
            raise Exception(f"Undefined type {type_id}")

    def define_type(self, type_id, type_value):
        """Define un nuevo tipo"""
        if type_value.startswith("("):
            type_value = type_value[1:-1].split("|")

    def condition(self):
        """Crea un cuádruplo de GOTOF para el condicional"""
        self.gotos.append(len(self.quadruples))
        self.quadruples.append(
            Quad("GOTOF", self.operand_stack.pop()))

    def add_operator(self, operator):
        """Agrega operando a la pila"""
        self.operator_stack.append(operator)

    def start_parens(self):
        """Marca el inicio de los paréntesis"""
        self.operator_stack.append('(')

    def end_parens(self):
        """Verifica que el último operando sea un paréntesis"""
        if self.operator_stack[-1] == '(':
            self.operator_stack.pop()
        else:
            raise Exception("Parenthesis mismatch")

    def handle_math_operation(self, *operators):
        """Realiza una operación y crea un temporal con el resultado"""
        if self.operator_stack[-1] in operators:
            right_operand = self.operand_stack.pop()
            left_operand = self.operand_stack.pop()
            operator = self.operator_stack.pop()
            return_type = check_operation_type(
                operator, left_operand.type_, right_operand.type_
            )
            # Create new temp variable
            func_name = self.function_stack[-1]
            addr = self.func_directory[func_name].next_addr(return_type)
            return_operand = Operand(
                f"__T{self.temp}__", return_type, addr, func_name == 'global')
            self.operand_stack.append(return_operand)
            self.quadruples.append(
                Quad(operator, left_operand, right_operand, return_operand)
            )

            self.temp = self.temp + 1

    def get_variable(self, ident, scope=None):
        """Mete la variable a la pila de operandos"""
        if self.negative:
            ident = f'-{ident}'
            self.negative = False

        if scope is None:
            all_vars_ = self.func_directory[self.function_stack[-1]].vars_
            for var_type_, vars_ in all_vars_.items():
                if ident in vars_:
                    variable = vars_[ident]
                    if variable.dim:
                        type_ = f"[{var_type_}]"
                    else:
                        type_ = var_type_
                    self.operand_stack.append(
                        Operand(ident, type_, variable.addr,
                                False, variable.dim)
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
            all_vars_ = self.func_directory['global'].vars_
            for var_type_, vars_ in all_vars_.items():
                if ident in vars_:
                    self.operand_stack.append(
                        Operand(ident, var_type_, vars_[
                                ident].addr, True, vars_[ident].dim)
                    )
                    break
            else:
                raise Exception(f'{ident} is undefined.')
        else:
            raise NotImplementedError(
                'Supplying a specific context is not yet supported.')

    def add_literal(self, value, type_):
        """Crea una nueva constante en el scope global"""
        var_ctx = self.get_var_ctx(type_, is_global=True)
        function = self.func_directory['global']
        addr = function.next_addr(type_)
        var_ctx[value] = VarRecord(addr, None, True)
        self.constants[type_][addr] = value
        return addr

    def get_literal(self, literal, type_):
        """Busca la constante y si no la encuentra, la crea"""
        if self.negative:
            literal = f'-{literal}'
            self.negative = False
        var_ctx = self.get_var_ctx(type_.strip('[]'), is_global=True)
        if literal not in var_ctx:
            addr = self.add_literal(literal, type_.strip('[]'))
        else:
            addr = var_ctx[literal].addr
        self.operand_stack.append(
            Operand(literal, type_, addr, True, literal == '[]')
        )

    def start_list(self):
        """Marca el inicio de una lista"""
        self.list_stack.append(ListDef('[Int]', 'Int'))

    def create_first(self):
        """Ve el primer tipo y marca el tipo de elemento de la lista"""
        operand = self.operand_stack[-1]
        type_ = operand.type_
        self.list_stack[-1].primitive_type = type_.strip('[]')
        self.list_stack[-1].type_ = f'[{type_}]'

    def add_to_list(self):
        """Inserta cuádruplo de COPYVAL para el valor de la lista"""
        operand = self.operand_stack.pop()
        type_ = operand.type_
        list_def = self.list_stack[-1]
        list_def.total += 1
        element_type = list_def.type_[1:-1]
        if type_ != element_type:
            raise TypeError(
                f"Type of elements mismatch: Expected {element_type} and got {type_}")
        if list_def.primitive_type == type_:
            self.copy_val_queue.append(len(self.quadruples))
            self.quadruples.append(
                Quad("COPYVAL", operand, None, None)
            )

    def end_list(self):
        """Marca el final de una lista, crea la dirección en memoria
        y agrega el cuádruplo SET"""
        listdef = self.list_stack[-1]
        function = self.func_directory[self.function_stack[-1]]
        listdef.addr = function.next_addr(listdef.primitive_type)
        for quad_idx in self.copy_val_queue:
            quad = self.quadruples[quad_idx]
            quad.result = listdef.addr
        self.copy_val_queue = []
        self.list_dims = {}
        self.list_stack.pop()
        constant_addr = self.func_directory['global'].next_addr(
            listdef.primitive_type)
        self.constants[listdef.primitive_type][constant_addr] = listdef.addr
        operand = Operand(
            "list", listdef.type_, listdef.addr, self.function_stack[-1] == "global", True
        )
        self.operand_stack.append(operand)
        self.quadruples.append(
            Quad("SET", listdef.addr, result=operand)
        )

    def check_function(self, ident):
        """Verifica que la función esté dada de alta en el directorio"""
        if ident not in self.func_directory:
            raise Exception(f"Function {ident} does not exist.")

    def call_function(self, ident):
        """
        Función que realiza la ejecución del módulo, dependiendo de
        si es una función del sistema o definida por el usuario se
        agregan los cuádruplos correspondientes (para las 
        del usuario ERA, GOSUB y para las del sistema los parámetros y el
        cuádruplo de la función)
        """
        function = self.func_directory[ident]
        for i in range(function.params_):
            self.quadruples.append(
                Quad("PARAM", None, None, self.operand_stack.pop()))
        if ident == 'print':
            self.quadruples.append(Quad("PRINT"))
            self.operand_stack.append(Operand('non', 'non', 0, True))
        elif ident == 'head':
            func_name = self.function_stack[-1]
            addr = self.func_directory[func_name].next_addr('Int')
            self.func_directory[func_name].vars_[
                'Int'][f"__T{self.temp}__"] = VarRecord(addr)
            result_operand = Operand(
                f"__T{self.temp}__head", 'Int', addr, func_name == 'global')
            self.operand_stack.append(result_operand)
            self.quadruples.append(Quad("HEAD", result=result_operand))
            self.temp += 1
        elif ident == 'tail':
            func_name = self.function_stack[-1]
            addr = self.func_directory[func_name].next_addr('Int')
            self.func_directory[func_name].vars_[
                'Int'][f"__T{self.temp}__"] = VarRecord(addr, True)
            result_operand = Operand(
                f"__T{self.temp}__tail", '[Int]', addr, func_name == 'global', dim=True)
            self.operand_stack.append(result_operand)
            self.quadruples.append(Quad("TAIL", result=result_operand))
            self.temp += 1
        elif ident == 'append':
            func_name = self.function_stack[-1]
            addr = self.func_directory[func_name].next_addr('Int')
            self.func_directory[func_name].vars_[
                'Int'][f"__T{self.temp}__"] = VarRecord(addr)
            result_operand = Operand(
                f"__T{self.temp}__append", '[Int]', addr, func_name == 'global', True)
            self.operand_stack.append(result_operand)
            self.quadruples.append(Quad("APPEND", result=result_operand))
            self.temp += 1
        elif ident == 'input':
            func_name = self.function_stack[-1]
            addr = self.func_directory[func_name].next_addr('Int')
            self.func_directory[func_name].vars_[
                function.type_][f"__T{self.temp}__"] = VarRecord(addr)
            result_operand = Operand(
                'input', 'Int', addr, func_name == 'global')
            self.operand_stack.append(result_operand)
            self.quadruples.append(Quad("INPUT", result=result_operand))
            self.temp += 1
        else:
            self.quadruples.append(Quad("ERA", result=ident))
            # Create temp variable
            func_name = self.function_stack[-1]
            new_type = function.type_.strip('[]')
            addr = self.func_directory[func_name].next_addr(new_type)
            self.func_directory[func_name].vars_[
                new_type][f"__T{self.temp}__"] = VarRecord(addr)
            dim = function.type_.startswith('[')
            return_operand = Operand(
                f"__T{self.temp}__", function.type_, addr, func_name == 'global', dim)
            self.operand_stack.append(return_operand)
            self.temp += 1
            # Call function
            self.quadruples.append(Quad("GOSUB", ident, addr, function.start_))

    def get_var_ctx(self, type_, is_global=False):
        """Regera la tabla de variables para el contexto actual"""
        if type_.startswith('['):
            type_ = type_.strip('[]')
        func_name = "global" if is_global else self.function_stack[-1]
        current_function = self.func_directory[func_name]
        var_ctx = current_function.vars_[type_]
        return var_ctx

    def handle_assignment(self, ident, type_):
        """
        Verifica que no esté ya definida la variable, le asigna memoria y crea
        un cuádruplo de ASSIGN
        """
        function = self.func_directory[self.function_stack[-1]]
        all_vars_ = function.vars_
        operand = self.operand_stack.pop()
        for var_type_, vars_ in all_vars_.items():
            if ident in vars_:
                raise Exception(
                    f"Variable {ident} already defined with type {var_type_}")
        else:
            if type_.startswith('['):
                new_type = type_.strip('[]')
            else:
                new_type = type_
            addr = function.next_addr(new_type)
            is_global = self.function_stack[-1] == 'global'
            var_ctx = self.get_var_ctx(new_type)
            var_ctx[ident] = VarRecord(addr, operand.dim, is_global)

        self.quadruples.append(
            Quad('ASSIGN', operand,
                 None, Operand(ident, type_, addr, is_global, operand.dim))
        )
        self.operand_stack.append(Operand('non', 'non', 0, True))

    def print_state(self):
        """Imprime el estado actual del compilador"""
        print("---------COMPILING---------")
        pp.pprint(self.func_directory)
        for i, quad in enumerate(self.quadruples):
            print(i, quad)
        # pp.pprint(self.operand_stack)
        # pp.pprint(self.operator_stack)
        print("---------END COMPILATION---------")

    def save_state(self, parser):
        """Guarda las tablas para pasarlas a la máquina virtual"""
        parser.quadruples = self.quadruples
        parser.func_directory = self.func_directory
        parser.type_directory = self.type_directory
        parser.constants = self.constants
