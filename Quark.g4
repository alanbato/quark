grammar Quark;

ID: '[a-z]+[a-zA-Z0-9_]*';
CONST_I: '[0-9]+';
CONST_F: '[0-9]+[.][0-9]+';

function: 
    'def' ID '(' params '->' type ('\n\t' cond block)* '\n\t' 'default:\n\t' block;
params: 
    ID ':' type moreparams;
moreparams: 
    ',' ID ':' type
    |
    ;
type:
    ID # UserType
    | 'Int' '?'? # Int
    | 'Bool' '?'? # Boolean
    | 'Float' '?'? # Float
    | 'String' '?'? # String
    | '[' type ']' # ListOfType
    ;
typedef:
    'type' ID '<-' (type | typeset);
typeset:
    '(' type | ('|' type)* ')';
cond:
    '(' expression more_expressions '):\n\t';
expression:
    bool
    | exp
    | comparator expression
    ;
bool:
    'True'
    | 'False'
    | ID
    ;
comparator:
    '>' # Greater
    | '<' # Lesser
    | '=' # Equal
    | '>=' # GreaterEqual
    | '<=' # LesserEqual
    | '!=' # NotEqual
    ;
exp:
    term # JustTerm
    | '+' term # Addition
    | '-' term # Substraction
    ;
term:
    factor # JustFactor
    | '*' factor # Multiplication
    | '/' factor # Division
    ;
more_expressions:
    ',' expression more_expressions
    |
    ;
factor:
    '-'? varconst
    | '(' expression ')'
    ;
varconst:
    ID
    | CONST_I
    | CONST_F
    ;

block:
    statement ('\n\t' statement)+;

statement:
    func_call
    | assignment
    | expression
    ;
func_call:
    ID '(' expression more_expressions ')';
assignment:
    type ID '<-' expression;
main:
    (function | func_call | assignment | expression) ('\n' main)*;
