

grammar seq;


sequence
//    :   OCUR gen CCUR (step SEMI)+
    :   (step SEMI)+
    ;

gen :   expr;

step
    :   repet? (OBRA base CBRA)? dirs+
    ;

dirs
    :   dire=(N | S | W | E | WE | EW | NS | SN) (COLON offset)?
    ;

repet   :   expr;
offset  :   expr;
base    :   expr;

expr
    :   <assoc=right> expr POW expr     #powExpr
    |   MINUS expr                      #minExpr
    |   expr op=(MULT | DIV ) expr      #mulExpr
    |   expr op=(PLUS | MINUS) expr     #addExpr
    |   atom                            #atoExpr
    |   OPIDX atom                      #atoIdx
    ;

atom
    :   OPAR expr CPAR      #parExpr
    |   NUMBER              #numberAtom
    |   elem=(LAST | ZERO | STEP)  #elemAtom
    ;



LAST    : 'I';  // index of last element added to the sequence
ZERO    : 'Z';  // index of initial element of the sequence
LAYER   : 'L';  // index of the current layer
STEP    : 'T';  // index of the current step



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
OCUR:   '{';
CCUR:   '}';
MULT:   '*';
DIV:    '/';
PLUS:   '+';
MINUS:  '-';
POW:    '^';
COLON:  ':';
SEMI:   ';';

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
