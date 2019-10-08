/*
 * Lexer Rules
 */

 lexer grammar CharmsLexer;

 PLUS         : '+' ;
 MINUS        : '-' ;
 TIMES        : '*' ;
 DIVIDE       : '/' ;
 EQUAL        : '=' ;
 LESSTHAN     : '<' ;
 GREATERTHAN  : '>' ;
 LPARENTHESES : '(' ;
 RPARENTHESES : ')' ;
 LCURLY       : '{' ;
 RCURLY       : '}' ;
 SEMICOLON    : ';' ;
 COMMA		    : ',' ;
 INT          : 'int' ;
 VOID         : 'void' ;
 BOOL         : 'bool' ;
 CHAR         : 'char' ;
 CTE_INT      : [1-9][0-9]* ;
 CTE_STRING   : [A-Za-z]+ ;
 IF           : 'if' ;
 ELSE         : 'else' ;
 WHILE        : 'while' ;
 PRINT        : 'print' ;
 READ         : 'read' ;
 RETURN       : 'return' ;
 FUNCTION	    : 'function' ;
 ID           : [a-zA-Z]+ ;
 WHITESPACE   : [ \t\r\n]+ -> skip ;
