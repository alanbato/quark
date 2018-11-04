grammar Quark;

@header {
from collections import namedtuple
from arithmetic_cube import check_operation_type
import pprint
pp = pprint.PrettyPrinter(indent=4)
}

@parser::members {
FuncRecord = namedtuple('FuncRecord', ['type', 'vars'])
VarRecord = namedtuple('VarRecord', ['type', 'dir', 'dim'])
func_directory = {
  "global": FuncRecord('non', {}), 
  "append": FuncRecord('[Any]', {}),
  "print": FuncRecord('none', {}),
  "upper": FuncRecord('String', {}),
  "head": FuncRecord('Any', {}),
  "tail": FuncRecord('[Any]', {})
}
type_directory = {}
current_function = "global"
PilaO = []
PTypes = []
POper = []
quadruples = []
temp = 0
# Memory = namedtuple('Memory', ['number', 'value'])
# memory = Memory()
}

ID:[a-z][a-zA-Z0-9_]*;
TYPE_ID: [A-Z][a-zA-Z0-9_]*;
CONST_I: [0-9]+;
CONST_F: [0-9]+ [.][0-9]+;
STRING: ["].*? ["];
SPACE: [\t\n\r\f ]+ -> skip;

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
} '{' (cond '{' block '}')* 'default {' block '}' '}' {self.current_function = "global"};
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
# TODO: This typevalue.text should be replaced by either the aliased type or a list of known types.
self.type_directory[$TYPE_ID.text] = $typevalue.text
};
typeset:
	'(' typeRule ('|' typeRule)* ')' {#TODO: This should return the list of defined types};
cond: '(' expression more_expressions ')';
expression:
	func_call
	| boolRule
	| exp expression
	| exp
	| expression comparator expression
	| 'non';
boolRule: 'True' | 'False' | ID;
comparator:
	'>' {self.POper.append('>')}		# Greater
	| '<' {self.POper.append('<')}		# Lesser
	| '=' {self.POper.append('=')}		# Equal
	| '>=' {self.POper.append('>=')}	# GreaterEqual
	| '<=' {self.POper.append('<=')}	# LesserEqual
	| '!=' {self.POper.append('!=')}	# NotEqual;
exp:
	term # JustTerm
	| '+' {self.POper.append('+')} term {
if self.POper[-1] == "+":
  right_operand, right_type = self.PilaO.pop()
  left_operand, left_type = self.PilaO.pop()
  operator = self.POper.pop()
  self.temp = self.temp + 1
  return_type = check_operation_type(operator, left_type, right_type)
  self.quadruples.append((operator, left_operand, right_operand, self.temp))
  self.PilaO.append(self.temp)
} # Addition
	| '-' {self.POper.append('-')} term {
if self.POper[-1] == "-":
  right_operand, right_type = self.PilaO.pop()
  left_operand, left_type = self.PilaO.pop()
  operator = self.POper.pop()
  self.temp = self.temp + 1
  return_type = check_operation_type(operator, left_type, right_type)
  self.quadruples.append((operator, left_operand, right_operand, self.temp))
  self.PilaO.append(self.temp)
} # Substraction;
term:
	factor # JustFactor
	| '*' {self.POper.append('*')} factor {
if self.POper[-1] == "*":
  right_operand, right_type = self.PilaO.pop()
  left_operand, left_type = self.PilaO.pop()
  operator = self.POper.pop()
  self.temp = self.temp + 1
  return_type = check_operation_type(operator, left_type, right_type)
  self.quadruples.append((operator, left_operand, right_operand, self.temp))
  self.PilaO.append(self.temp)
} # Multiplication
	| '/' {self.POper.append('/')} factor {
if self.POper[-1] == "/":
  right_operand, right_type = self.PilaO.pop()
  left_operand, left_type = self.PilaO.pop()
  operator = self.POper.pop()
  self.temp = self.temp + 1
  return_type = check_operation_type(operator, left_type, right_type)
  self.quadruples.append((operator, left_operand, right_operand, self.temp))
  self.PilaO.append(self.temp)
} # Division
	| '%' {self.POper.append('%')} factor {
if self.POper[-1] == "%":
  right_operand, right_type = self.PilaO.pop()
  left_operand, left_type = self.PilaO.pop()
  operator = self.POper.pop()
  return_type = check_operation_type(operator, left_type, right_type)
  self.temp = self.temp + 1
  self.quadruples.append((operator, left_operand, right_operand, self.temp))
  self.PilaO.append(self.temp)
} # Modulo;
more_expressions: ',' expression more_expressions |;
factor:
	'-'? varconst
	| '(' {self.POper.append('(')} expression ')' {self.POper.append(')')}
	| 'non'
	| STRING {self.POper.append($STRING.text); self.PTypes.append("String")}
	| '[' expression more_expressions ']'
	| '[]';
varconst:
	ID {
if $ID.text not in self.func_directory[self.current_function].vars:
  raise Exception("ID {} is not defined".format($ID.text))
self.PilaO.append(($ID.text, self.func_directory[self.current_function].vars[$ID.text].type))
}
	| CONST_I {self.PilaO.append(($CONST_I.text, "Int"))}
	| CONST_F {self.PilaO.append(($CONST_F.text, "Float"))};

block: statement (statement)*;

statement: assignment | expression;
func_call:
	ID {
if $ID.text not in self.func_directory:
  raise Exception("Function {} does not exist".format($ID.text))
} '(' expression more_expressions ')';
assignment:
	typeRule ID '<-' expression {
if $ID.text not in self.func_directory[self.current_function]:
  self.func_directory[self.current_function].vars[$ID.text] = self.VarRecord($typeRule.text, 0, None)
};
main:
	things morethings {pp.pprint(self.func_directory); pp.pprint(self.quadruples)} EOF;
things:
	function
	| func_call
	| assignment
	| expression
	| typedef;
morethings: things morethings |;
