

grammar seq;

expr    :   term (('+' | '-') term)* ;
term    :   factor (('*' | '/') factor)*;
factor  :   base ('^' base )*;
base
        :   '(' expr ')'    #baseexpr
        |   ELEM            #baseelem
        |   NUMBER          #basenumber
        ;

//expr    :   term '+' term;
//term    :   NUMBER;



LAST    : 'last';   // ast element added to the sequence (i-1)
ZERO    : 'zero';   // initial element of the sequence
I       : 'i';      // current element of the sequence

ELEM
    :   ELEM_val
    |   ELEM_idx
    ;

ELEM_val
    :   LAST
    |   ZERO
    |   I
    ;

ELEM_idx
    :   OP_IDX ELEM_val;

IDENT
   : VALID_ID_START VALID_ID_CHAR*
   ;

NUMBER  :   DIGIT+;

fragment VALID_ID_START
   : ('a' .. 'z') | ('A' .. 'Z') | '_'
   ;

fragment VALID_ID_CHAR
   : VALID_ID_START | ('0' .. '9')
   ;

DIGIT
   : [0-9]
   ;

OP_IDX  : '&';

WS
   : [ \r\n] + -> skip
   ;
