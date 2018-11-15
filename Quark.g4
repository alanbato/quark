grammar Quark;

@header {
from collections import namedtuple
from utils import check_operation_type, handle_math_operation
import pprint
pp = pprint.PrettyPrinter()
}

@parser::members {
FuncRecord = namedtuple('FuncRecord', ['type', 'vars'])
VarRecord = namedtuple('VarRecord', ['addr', 'dim'])
Operand = namedtuple("Operand", ['name', 'type', 'address'])

func_directory = {
  "global": FuncRecord('non', {'Int':{}, 'Float':{}}), 
  "append": FuncRecord('[Any]', {}),
  "print": FuncRecord('none', {}),
  "upper": FuncRecord('String', {}),
  "head": FuncRecord('Any', {}),
  "tail": FuncRecord('[Any]', {})
}
type_directory = {}
current_function = "global"
PilaO = []
POper = []
quadruples = []
gotos = []
temp = 0
# Memory = namedtuple('Memory', ['number', 'value'])
# memory = Memory()
}

ID:[a-z][a-zA-Z0-9_]*;
TYPE_ID: [A-Z][a-zA-Z0-9_]*;
CONST_I: [0-9]+;
CONST_F: [0-9]+ [.][0-9]+;
STRING: ["].*? ["];
SPACE: [\t\r\f\n ]+ -> skip;

function:
	'def' ID {
ident = $ID.text
self.current_function = ident
if ident in self.func_directory:
  raise Exception("Function {} already defined".format(ident))
else:
  self.func_directory[ident] = self.FuncRecord(None, {})
} '(' params ')' '->' typeRule {
ident = $ID.text
ret_type = $typeRule.text
self.func_directory[ident] = self.func_directory[ident]._replace(type=ret_type)
} '{' (
		cond '{' block '}' {
ident = self.gotos.pop()
tmp = list(self.quadruples[ident])
tmp[3] = len(self.quadruples) - 1
self.quadruples[ident] = tuple(tmp)
self.quadruples.append(("RETURN", "", "", ""))
self.quadruples.append(("GOTO", "", "", ""))
}
	)* 'default {' block '}' '}' {
self.quadruples.append(("ENDPROC", "", "", ""))
self.current_function = "global"
self.PilaO = []
self.POper = []
};
params:
	ID ':' typeRule {self.func_directory[self.current_function].vars[$ID.text] = self.VarRecord($typeRule.text, 0, None)
    } moreparams;
moreparams:
	',' ID ':' typeRule {self.func_directory[self.current_function].vars[$ID.text] = self.VarRecord($typeRule.text, 0, None)
    }
	|;
moreTypes: ',' typeRule |;
typeRule:
	TYPE_ID {
if $TYPE_ID.text not in self.type_directory:
  raise Exception("Undefined type {}".format($TYPE_ID.text))
  }	# UserType
	| 'Int' '?'?																											# Int
	| 'Bool' '?'?																											# Boolean
	| 'Float' '?'?																											# Float
	| 'String' '?'?																											# String
	| 'non'																													# None
	| 'Any'																													# Any
	| '[' typeRule moreTypes ']'																							# ListOfType;
typevalue: typeRule | typeset;
typedef:
	'type' TYPE_ID '<-' typevalue {
self.type_directory[$TYPE_ID.text] = $typevalue.text
};
typeset:
	'(' typeRule ('|' typeRule)* ')';
cond:
	'(' expression more_expressions ')' {
index = len(self.quadruples) - 1
self.quadruples.append(("GOTOF", index, "", ""))
self.gotos.append(index + 1)
self.temp = self.temp + 1
};
expression: func_call | exp expression | exp | 'non';
exp:
	term # JustTerm
	| '+' {self.POper.append('+')} term {
if self.POper[-1] == "+":
  handle_operation(self)
} # Addition
	| '-' {self.POper.append('-')} term {
if self.POper[-1] == "-":
  handle_operation(self)
} # Substraction
	| '>' {self.POper.append('>')} term {
if self.POper[-1] == ">":
  handle_operation(self)
} # Greater
	| '<' {self.POper.append('<')} term {
if self.POper[-1] == "<":
  handle_operation(self)
} # Lesser
	| '=' {self.POper.append('=')} term {
if self.POper[-1] == "=":
  handle_operation(self)
} # Equal
	| '>=' {self.POper.append('>=')} term {
if self.POper[-1] == ">=":
  handle_operation(self)
} # GreaterEqual
	| '<=' {self.POper.append('<=')} term {
if self.POper[-1] == "<=":
  handle_operation(self)
} # LesserEqual
	| '!=' {self.POper.append('!=')} term {
if self.POper[-1] == "!=":
  handle_operation(self)
} # NotEqual;
term:
	factor # JustFactor
	| '*' {self.POper.append('*')} factor {
if self.POper[-1] == "*":
  handle_operation(self)
} # Multiplication
	| '/' {self.POper.append('/')} factor {
if self.POper[-1] == "/":
  handle_operation(self)
} # Division
	| '%' {self.POper.append('%')} factor {
if self.POper[-1] == "%":
  handle_operation(self)
} # Modulo;
more_expressions: ',' expression more_expressions |;
factor:
	'-'? varconst
	| '(' {self.POper.append('(')} expression ')' {
if self.POper[-1] == '(':
  self.POper.pop()
else:
  raise Exception("Parenthesis mismatch")
}
	| 'True' {self.PilaO.append(('True', "Bool"))}
	| 'False' {self.PilaO.append(('False', "Bool"))}
	| STRING {self.PilaO.append(($STRING.text, "String"))}
	| '[' expression more_expressions ']'
	| '[]' {self.PilaO.append(('[]', "[Any]"))};
varconst:
	ID {
if $ID.text not in self.func_directory[self.current_function].vars:
  raise Exception("ID {} is not defined".format($ID.text))
self.PilaO.append(($ID.text, self.func_directory[self.current_function].vars[$ID.text].type))
}
	| CONST_I {
if $CONST_I.text not in self.func_directory['global'].vars['Int']:
	addr = len(self.func_directory['global'].vars['Int'])
	self.func_directory['global'].vars['Int'][$CONST_I.text] = self.VarRecord(addr, 0)
else:
	addr = self.func_directory['global'].vars['Int'][$CONST_I.text].addr
operand = self.Operand($CONST_I.text, 'Int', addr)
self.PilaO.append(operand)
}
	| CONST_F {
if $CONST_F.text not in self.func_directory['global'].vars['Float']:
	addr = len(self.func_directory['global'].vars['Float'])
	self.func_directory['global'].vars['Float'][$CONST_F.text] = self.VarRecord(addr, 0)
else:
	addr = self.func_directory['global'].vars['Float'][$CONST_F.text].addr
operand = self.Operand($CONST_F.text, 'Float', addr)
self.PilaO.append(operand)
};

block: statement (statement)*;

statement: assignment ';' | expression ';';
func_call:
	ID {
if $ID.text not in self.func_directory:
  raise Exception("Function {} does not exist".format($ID.text))
} '(' expression more_expressions ')' {
self.quadruples.append(($ID.text, "", "", ""))
};
assignment:
	typeRule ID '<-' expression {
current_vars_of_type = self.func_directory[self.current_function].vars[$typeRule.text]
if $ID.text not in current_vars_of_type:
	addr = len(current_vars_of_type)
	current_vars_of_type[$ID.text] = self.VarRecord(addr, None)
	print(current_vars_of_type)
else:
  raise Exception("Variable with that type and name already declared")

self.quadruples.append(('ASSIGN', self.PilaO.pop(), '', $ID.text))
};
main:
	things morethings {
pp.pprint(self.func_directory)
for i, val in enumerate(self.quadruples): 
  print(i, val)
} EOF;
things:
	function
	| func_call ';'
	| assignment
	| expression
	| typedef ';';
morethings: things morethings |;
