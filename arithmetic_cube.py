# Cubo aritmético de operaciones

INT = "Int"
STRING = "String"
FLOAT = "Float"
BOOL = "Bool"
NON = "non"
TYPE_ERROR = "Operator {} not defined for types {} and {}"

def check_operation_type(op, t1, t2):
    if op == "+":
        if t1 == STRING and t2 == STRING:
            return STRING
        if t1 == FLOAT:
            if t2 in (INT, FLOAT):
                return FLOAT
        if t1 == INT:
            if t2 == INT:
                return INT
            if t2 == FLOAT:
                return FLOAT
        if t1 == BOOL and t2 == BOOL:
            return BOOL
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "-":
        if t1 == FLOAT:
            if t2 in (INT, FLOAT):
                return FLOAT
        if t1 == INT:
            if t2 == INT:
                return INT
            if t2 == FLOAT:
                return FLOAT
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "*":
        if t1 == FLOAT:
            if t2 in (INT, FLOAT):
                return FLOAT
        if t1 == INT:
            if t2 in (INT, FLOAT):
                return FLOAT
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "/":
        if t1 == FLOAT:
            if t2 in (INT, FLOAT):
                return FLOAT
        if t1 == INT:
            if t2 == INT:
                return INT
            if t2 == FLOAT:
                return FLOAT
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "%":
        if t1 == INT and t2 == INT:
            return INT
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == ">":
        if t1 == STRING and t2 == STRING:
            return BOOL
        if t1 in (INT, FLOAT) and t2 in (INT, FLOAT):
            return BOOL
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == ">=":
        if t1 == STRING and t2 == STRING:
            return BOOL
        if t1 in (INT, FLOAT) and t2 in (INT, FLOAT):
            return BOOL
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "=":
        if t1 == t2:
            return BOOL
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "<":
        if t1 == STRING and t2 == STRING:
            return BOOL
        if t1 in (INT, FLOAT) and t2 in (INT, FLOAT):
            return BOOL
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "<=":
        if t1 == STRING and t2 == STRING:
            return BOOL
        if t1 in (INT, FLOAT) and t2 in (INT, FLOAT):
            return BOOL
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    elif op == "!=":
        if t1 == t2:
            return BOOL
        raise TypeError(TYPE_ERROR.format(op, t1, t2))
    else:
        raise ValueError("Operator {} does not exist".format(op))
