grammar Quark;

@header {
from collections import namedtuple
}

@parser::members {
FuncRecord = namedtuple('FuncRecord', ['type', 'vars'])
VarRecord = namedtuple('VarRecord', ['type', 'dir', 'dim'])
func_directory = {"global": FuncRecord('non', {})}
current_function = "global"
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
	TYPE_ID							# UserType
	| 'Int' '?'?					# Int
	| 'Bool' '?'?					# Boolean
	| 'Float' '?'?					# Float
	| 'String' '?'?					# String
	| 'non'							# None
	| '[' typeRule moreTypes ']'	# ListOfType;
typedef: 'type' TYPE_ID '<-' (typeRule | typeset);
typeset: '(' typeRule ('|' typeRule)* ')';
cond: '(' expression more_expressions ')';
expression:
	boolRule
	| exp expression
	| exp
	| expression comparator expression
	| 'non'
	| func_call;
boolRule: 'True' | 'False' | ID;
comparator:
	'>'		# Greater
	| '<'	# Lesser
	| '='	# Equal
	| '>='	# GreaterEqual
	| '<='	# LesserEqual
	| '!='	# NotEqual;
exp:
	term		# JustTerm
	| '+' term	# Addition
	| '-' term	# Substraction;
term:
	factor			# JustFactor
	| '*' factor	# Multiplication
	| '/' factor	# Division
	| '%' factor	# Modulo;
more_expressions: ',' expression more_expressions |;
factor:
	'-'? varconst
	| '(' expression ')'
	| 'non'
	| STRING
	| '[' expression more_expressions ']'
	| '[]';
varconst: ID | CONST_I | CONST_F;

block: statement (statement)*;

statement: assignment | expression;
func_call: ID '(' expression more_expressions ')';
assignment:
	typeRule ID '<-' expression {
print(type($ctx.parentCtx))
if $ID.text not in self.func_directory[self.current_function]:
  self.func_directory[self.current_function].vars[$ID.text] = self.VarRecord($typeRule.text, 0, None)
};
main: things morethings {print(self.func_directory)} EOF;
things:
	function
	| func_call
	| assignment
	| expression
	| typedef;
morethings: things morethings |;
