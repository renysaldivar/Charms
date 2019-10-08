/*
 * Parser Rules
 */

 parser grammar CharmsParser;

 options { tokenVocab = CharmsLexer; }

 program	: p section ;
 p			: vars p1 | func ;
 p1			: func | /* epsilon */ ;

 vars		: type v ;
 v 			: ID v1 SEMICOLON ;
 v1			: COMMA ID v1 | /* epsilon */ ;

 function	: FUNCTION f ID LPARENTHESES f1 RPARENTHESES LCURLY section RCURLY ;
 f 			: VOID | type ;
 f1			: type ID f2 | /* epsilon */ ;
 f2			: COMMA type ID f2 | /* epsilon */ ;

 section	: assignment section | condition section | write section | read section | loop section | funcCall section | /* epsilon */ ;

 type		: INT | BOOL | CHAR ;

 assignment	: ID EQUAL expression SEMICOLON ;

 expression	: exp e ;
 e 			: GREATERTHAN exp | LESSTHAN exp | /* epsilon */ ;

 exp 		: term e1 ;
 e1			: PLUS exp | MINUS exp | /* epsilon */ ;

 factor		: LPARENTHESES expression RPARENTHESIS | f varcte ;
 f 			: PLUS | MINUS | /* epsilon */ ;

 term		: factor t ;
 t 			: TIMES factor | DIVIDE factor | /* epsilon */ ;

 condition	: IF LPARENTHESES expression RPARENTHESES LCURLY section RCURLY ELSE LCURLY section RCURLY ;

 loop		: WHILE LPARENTHESES expression RPARENTHESES LCURLY section RCURLY ;