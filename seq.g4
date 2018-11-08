

grammar seq;


sequence
    :   OCUR gen CCUR (layer SEMI)+
    ;

gen :   expr;

layer
    :   step (COMMA step)*
    ;

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
    |   SUM expr                        #sumExpr
    |   expr op=(MULT | DIV ) expr      #mulExpr
    |   expr op=(PLUS | MINUS) expr     #addExpr
    |   atom                            #atoExpr
    |   OPIDX atom                      #atoIdx
    ;

atom
    :   OPAR expr CPAR      #parExpr
    |   NUMBER              #numberAtom
    |   elem=(LAST | ZERO | STEP | LAYER | ILAYER | ZEROL)  #elemAtom
    ;



LAST    : 'i';  // index of last element added to the sequence
ZERO    : 'z';  // index of initial element of the sequence
STEP    : 't';  // index of the current step inside the layer
LAYER   : 'l';  // index of the current layer
ILAYER  : 'j';  // index of the last element in the layer
ZEROL   : 'c';  // index of the first element of the previous layer


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
SUM:    '#';  // #4 = 4+3+2+1
COLON:  ':';
SEMI:   ';';
COMMA:  ',';

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
