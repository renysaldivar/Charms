/*
 * Parser Rules
 */

 parser grammar CharmsParser;

 options { tokenVocab = CharmsLexer; }

 program    : p section ;
 p          : p_vars p1 | function ;
 p1			    : function | /* epsilon */ ;

 p_vars     : type_id v ;
 v 			    : ID v1 SEMICOLON v2 ;
 v1			    : COMMA ID v1 | /* epsilon */ ;
 v2         : p_vars | /* epsilon */ ;

 function	  : FUNCTION f ID LPARENTHESES f1 RPARENTHESES LCURLY section RCURLY ;
 f 			    : VOID | type_id ;
 f1			    : type_id ID f2 | /* epsilon */ ;
 f2			    : COMMA type_id ID f2 | /* epsilon */ ;

 section    : assignment section | condition section | write section | read section | loop section | function_return | function_call section | /* epsilon */ ;

 type_id    : INT | BOOL | CHAR ;

 assignment	: ID ASSIGN a SEMICOLON ;
 a : expression | function_call ;

 expression : exp e ;
 e 			    : GREATERTHAN exp | LESSTHAN exp | /* epsilon */ ;

 exp        : term e1 ;
 e1         : PLUS exp | MINUS exp | /* epsilon */ ;

 factor     : LPARENTHESES expression RPARENTHESES | fa var_cte ;
 fa         : PLUS | MINUS | /* epsilon */ ;

 term       : factor t ;
 t          : TIMES factor | DIVIDE factor | /* epsilon */ ;

 condition	: IF LPARENTHESES expression RPARENTHESES LCURLY section RCURLY c ;
 c 			: ELSE LCURLY section RCURLY | /* epsilon */ ;

 loop       : WHILE LPARENTHESES expression RPARENTHESES LCURLY section RCURLY ;

 read       : READ LPARENTHESES ID RPARENTHESES ;

 write      : PRINT LPARENTHESES w RPARENTHESES SEMICOLON ;
 w          : expression w2 | CTE_STRING w2 ;
 w2         : COMMA w | /* epsilon */ ;

 var_cte    : ID | CTE_INT ;

 function_return	: RETURN exp SEMICOLON ;

 function_call		: ID LPARENTHESES arguments RPARENTHESES fc;
 arguments			: exp more_args ;
 more_args			: COMMA exp more_args | /* epsilon */ ;
 fc 				: SEMICOLON | /* epsilon */ ;