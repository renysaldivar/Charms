/*
 * Lexer Rules
 */

 lexer grammar CharmsLexer;

 PLUS          : '+' ;
 MINUS         : '-' ;
 TIMES         : '*' ;
 DIVIDE        : '/' ;
 EQUAL         : '=' ;
 LESSTHAN      : '<' ;
 GREATERTHAN   : '>' ;
 LPARENTHESES  : '(' ;
 RPARENTHESES  : ')' ;
 LCURLY        : '{' ;
 RCURLY        : '}' ;
 SEMICOLON     : ';' ;
 INT           : 'int' ;
 VOID          : 'void' ;
 BOOL          : 'bool' ;
 CHAR          : 'char' ;
 IF            : 'if' ;
 ELSE          : 'else' ;
 WHILE         : 'while' ;
 PRINT         : 'print' ;
 READ          : 'read' ;
 RETURN        : 'return' ;
 ID            : [a-zA-Z]+ ;
 WHITESPACE    : [ \t\r\n]+ -> skip ;
