// grammar/DeepLang.g4
grammar DeepLang;

options { language = Python3; }

@header {
# deeplang ANTLR grammar - generated
}

program
    : stmtList EOF
    ;

stmtList
    : (stmt)*
    ;

stmt
    : simple_stmt
    | compound_stmt
    ;

//////////////////////////////////////////////////
// Simple statements
//////////////////////////////////////////////////
simple_stmt
    : small_stmt NEWLINE
    ;

small_stmt
    : assign_stmt
    | return_stmt
    | import_stmt
    | print_stmt
    | expr_stmt
    ;

assign_stmt
    : ID '=' expr
    ;

return_stmt
    : 'return' expr?
    ;

import_stmt
    : 'import' ID (',' ID)*
    ;

print_stmt
    : 'print' '(' expr? ')'
    ;

expr_stmt
    : expr
    ;

//////////////////////////////////////////////////
// Compound statements (require NEWLINE INDENT DEDENT)
//////////////////////////////////////////////////
compound_stmt
    : funcdef
    | if_stmt
    | while_stmt
    | for_stmt
    | classdef
    ;

funcdef
    : 'def' ID '(' paramList? ')' ( '->' type )? ':' NEWLINE INDENT stmtList DEDENT
    ;

paramList
    : param (',' param)*
    ;
param
    : ID (':' type)? ('=' expr)?
    ;

if_stmt
    : 'if' expr ':' NEWLINE INDENT stmtList DEDENT
      ( 'elif' expr ':' NEWLINE INDENT stmtList DEDENT )*
      ( 'else' ':' NEWLINE INDENT stmtList DEDENT )?
    ;

while_stmt
    : 'while' expr ':' NEWLINE INDENT stmtList DEDENT
    ;

for_stmt
    : 'for' ID 'in' expr ':' NEWLINE INDENT stmtList DEDENT
    ;

classdef
    : 'class' ID ('(' ID (',' ID)* ')')? ':' NEWLINE INDENT stmtList DEDENT
    ;

//////////////////////////////////////////////////
// Expressions
//////////////////////////////////////////////////
expr
    : orExpr
    ;

orExpr
    : andExpr ( 'or' andExpr )*
    ;

andExpr
    : notExpr ( 'and' notExpr )*
    ;

notExpr
    : 'not' notExpr
    | comparison
    ;

comparison
    : arithExpr ( ( '==' | '!=' | '<' | '<=' | '>' | '>=' | 'in' | 'is' ) arithExpr )*
    ;

arithExpr
    : term ( ('+'|'-') term )*
    ;

term
    : factor ( ('*'|'/'|'%'|'//') factor )*
    ;

factor
    : ('+'|'-') factor
    | power
    ;

power
    : atom ('**' factor)?
    ;

atom
    : ID
    | TK_INT
    | TK_FLOAT
    | TK_STRING
    | 'None'
    | 'True'
    | 'False'
    | '(' expr ')'
    | listLiteral
    | matrixLiteral
    | callExpr
    | indexing
    ;

callExpr
    : ID '(' argList? ')'
    ;
argList
    : expr (',' expr)* (',')?
    ;

indexing
    : ID '[' expr (',' expr)* ']'
    ;

listLiteral
    : '[' (expr (',' expr)*)? ']'
    ;

matrixLiteral
    : '[' ( '[' expr (',' expr)* ']' (',' '[' expr (',' expr)* ']')* ) ']'
    ;

type
    : ID
    ;

//////////////////////////////////////////////////
// Lexer tokens (keep minimal; pre-lexer must produce NEWLINE/INDENT/DEDENT)
//////////////////////////////////////////////////
TK_INT   : [0-9]+ ;
TK_FLOAT : [0-9]+ '.' [0-9]+ ;
TK_STRING
    : '"' ( ~["\\\r\n] | '\\' . )* '"'
    | '\'' ( ~['\\\r\n] | '\\' . )* '\''
    ;

ID  : [a-zA-Z_] [a-zA-Z_0-9]* ;

COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t]+ -> skip ;  // indentation handled externally
NEWLINE : ('\r'? '\n') ;

PLUS : '+' ;
MINUS: '-' ;
STAR : '*' ;
SLASH: '/' ;
PERC : '%' ;
EQ   : '=' ;
EQEQ : '==' ;
NEQ  : '!=' ;
LT   : '<' ;
LE   : '<=' ;
GT   : '>' ;
GE   : '>=' ;
POW  : '**' ;
FLOORDIV : '//' ;
ARROW : '->' ;
COMMA : ',' ;
COLON : ':' ;
LPAREN: '(' ;
RPAREN: ')' ;
LBRACK: '[' ;
RBRACK: ']' ;
LBRACE: '{' ;
RBRACE: '}' ;

