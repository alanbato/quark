grammar Quark;

ID: [a-z][a-zA-Z0-9_]*;
CONST_I: [0-9]+;
CONST_F: [0-9]+[.][0-9]+;
SPACE: [ ] -> skip;

function: 
    'def' ID '(' params '->' typeRule ('\n\t' cond block)* '\n\t' 'default:\n\t' block;
params: 
    ID ':' typeRule moreparams;
moreparams: 
    ',' ID ':' typeRule
    |
    ;
typeRule:
    ID # UserType
    | 'Int' '?'? # Int
    | 'Bool' '?'? # Boolean
    | 'Float' '?'? # Float
    | 'String' '?'? # String
    | '[' typeRule ']' # ListOfType
    ;
typedef:
    'type' ID '<-' (typeRule | typeset);
typeset:
    '(' typeRule | ('|' typeRule)* ')';
cond:
    '(' expression more_expressions '):\n\t';
expression:
    boolRule
    | exp
    | comparator expression
    | 'non'
    ;
boolRule:
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
    typeRule ID '<-' expression;
main:
    things morethings EOF;

things:
    (function | func_call | assignment | expression);
morethings:
    ',' things morethings
    |
    ;