

grammar seq;


sequence
    :   layer+
    ;

layer
    :   step+
    ;

step
    :   repet? dire=(N | S | W | E | WE | EW | NS | SN) (OBRA offset CBRA)?
    ;

repet   :   expr;
offset  :   expr;

expr
    :   <assoc=right> expr POW expr     #powExpr
    |   MINUS expr                      #minExpr
    |   expr op=(MULT | DIV ) expr      #mulExpr
    |   expr op=(PLUS | MINUS) expr     #addExpr
    |   atom                            #atoExpr
    ;

atom
    :   OPAR expr CPAR  #parExpr
    |   NUMBER          #numberAtom
    |   ELEM            #elemAtom
    ;



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
    :   OPIDX ELEM_val;

//IDENT
//   : VALID_ID_START VALID_ID_CHAR*
//   ;

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

OPIDX:  '&';
OPAR:   '(';
CPAR:   ')';
OBRA:   '[';
CBRA:   ']';
MULT:   '*';
DIV:    '/';
PLUS:   '+';
MINUS:  '-';
POW:    '^';

N:      'N';
S:      'S';
W:      'W';
E:      'E';
WE:      'WE';
EW:      'EW';
NS:      'NS';
SN:      'SN';

WS
   : [ \r\n] + -> skip
   ;
