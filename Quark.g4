grammar Quark;

ID: [a-z][a-zA-Z0-9_]*;
TYPE_ID: [A-Z][a-zA-Z0-9_]*;
CONST_I: [0-9]+;
CONST_F: [0-9]+ [.][0-9]+;
STRING: ["].*? ["];
SPACE: [\t\n\r\f ]+ -> skip;

function:
	'def' ID '(' params ')' '->' typeRule '{' (
		cond '{' block '}'
	)* 'default {' block '}' '}';
params: ID ':' typeRule moreparams;
moreparams: ',' ID ':' typeRule |;
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
assignment: typeRule ID '<-' expression;
main: things morethings EOF;

things:
	function
	| func_call
	| assignment
	| expression
	| typedef;
morethings: things morethings |;
