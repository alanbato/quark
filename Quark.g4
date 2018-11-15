grammar Quark;

@header {
from compiler import Compiler
c = Compiler()
}

ID:[a-z][a-zA-Z0-9_]*;
TYPE_ID: [A-Z][a-zA-Z0-9_]*;
CONST_I: [0-9]+;
CONST_F: [0-9]+ [.][0-9]+;
STRING: ["].*? ["];
SPACE: [\t\r\f\n ]+ -> skip;

function:
	'def' ID {c.define_function($ID.text)} '(' params ')' '->' typeRule {
c.set_function_return_type($ID.text, $typeRule.text)
} '{' (cond '{' block '}' {c.process_function_clause()})* 'default {' block '}' '}' {c.process_function_end()
		};
params:
	ID ':' typeRule {c.process_param($ID.text, $typeRule.text)} moreparams;
moreparams:
	',' ID ':' typeRule {c.process_param($ID.text, $typeRule.text)}
	|;
moreTypes: ',' typeRule |;
typeRule:
	TYPE_ID {c.check_user_def_type($TYPE_ID.text)}	# UserType
	| 'Int' '?'?									# Int
	| 'Bool' '?'?									# Boolean
	| 'Float' '?'?									# Float
	| 'String' '?'?									# String
	| 'non'											# None
	| 'Any'											# Any
	| '[' typeRule moreTypes ']'					# ListOfType;
typevalue: typeRule | typeset;
typedef:
	'type' TYPE_ID '<-' typevalue {c.define_type($TYPE_ID.text)};
typeset: '(' typeRule ('|' typeRule)* ')';
cond: '(' expression more_expressions ')' {c.condition()};
expression: func_call | exp expression | exp | 'non';
exp:
	term																						# JustTerm
	| '+' {c.add_operator('+')} term {c.handle_math_operation("+", "-")}						# Addition
	| '-' {c.add_operator('-')} term {c.handle_math_operation("-", "+")}						# Substraction
	| '>' {c.add_operator('>')} term {c.handle_math_operation(">", "<", "=", ">=", "<=", "!=")}	#
		Greater
	| '<' {c.add_operator('<')} term {c.handle_math_operation(">", "<", "=", ">=", "<=", "!=")} #
		Lesser
	| '=' {c.add_operator('=')} term {c.handle_math_operation(">", "<", "=", ">=", "<=", "!=")} #
		Equal
	| '>=' {c.add_operator('>=')} term {c.handle_math_operation(">", "<", "=", ">=", "<=", "!=")} #
		GreaterEqual
	| '<=' {c.add_operator('<=')} term {c.handle_math_operation(">", "<", "=", ">=", "<=", "!=")} #
		LesserEqual
	| '!=' {c.add_operator('!=')} term {c.handle_math_operation(">", "<", "=", ">=", "<=", "!=")} #
		NotEqual;
term:
	factor																		# JustFactor
	| '*' {c.add_operator('*')} factor {c.handle_math_operation("*", "/", "%")}	# Multiplication
	| '/' {c.add_operator('/')} factor {c.handle_math_operation("*", "/", "%")}	# Division
	| '%' {c.add_operator('%')} factor {c.handle_math_operation("*", "/", "%")}	# Modulo;
more_expressions: ',' expression more_expressions |;
factor:
	varconst													# Positive
	| '(-' {c.set_negative()} varconst ')'						# Negative
	| '(' {c.start_parens()} expression ')' {c.end_parens()}	# Parens
	| 'True' {c.add_literal('True', "Bool")}					# True
	| 'False' {c.add_literal('False', "Bool")}					# False
	| STRING {c.add_literal($STRING.text, "String")}			# StringLiteral
	| '[' expression more_expressions ']' {#TODO Handle Lists}	# List
	| '[]' {c.add_literal('[]', "[Any]")}						# EmptyList;
varconst:
	ID {c.get_variable($ID.text)}
	| CONST_I {c.get_math_literal($CONST_I.text, "Int")}
	| CONST_F {c.get_math_literal($CONST_F.text, "Float")};

block: statement (statement)*;

statement: assignment ';' | expression ';';
func_call:
	ID {c.check_function($ID.text)} '(' expression more_expressions ')' {c.call_function($ID.text)};
assignment:
	typeRule ID '<-' expression {c.handle_assignment($ID.text, $typeRule.text)};
main: things morethings {c.print_state()} EOF;
things:
	function
	| func_call ';'
	| assignment
	| expression
	| typedef ';';
morethings: things morethings |;
