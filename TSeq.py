import logging
logger = logging.getLogger(__name__)


import antlr4
from gen.seqLexer  import *
from semseq import *
from TElem import *


class TSeq:




    def __init__(self):
        #stream = antlr4.InputStream("(5*2)N[I:2]SE")
        #stream = antlr4.InputStream("(2*1)N[Z:2]")
        #stream = antlr4.InputStream("[Z]N:2W:1")
        #stream = antlr4.InputStream("3[L]N:2W:1")
        # The cube
        stream = antlr4.InputStream("{i}((l+1)/2)E;(l/2)N;((l+1)/2)W;(l/2)S;")
        # The pyramid
        #stream = antlr4.InputStream("{j/2+1} [((l-1)^2)+1]S,(l)[(l^2)+1]EW:(j/2);")
        #stream = antlr4.InputStream("{j} N,E;")

        self.Walker=None
        self.Tree=None
        self.Context={}

        #lexer = seqLexer(antlr4.StdinStream())

        lexer = seqLexer(stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = seqParser(tokens)

        self.Tree=parser.sequence()
        self.Walker=ParseTreeWalker()

        # i is the index of the last element in the sequence
        self.Context['i']=1         # Current element
        self.Context['layer']=0         # Layer
        self.Context['step']=0
        self.Context['ilayer']=0
        self.Context['elems']=[]


        # Initial element to avoid 0 (as we are starting i at 1)
        # WATCH IT OUT! Eventually we may want to select if i starts at 0 or 1
        new=TElem(None,0,0)
        self.Context['elems'].append(new)
        new=TElem(1,0,0)
        self.Context['elems'].append(new)


    def Walk(self):

        seq=SemSeq(self.Context)
        self.Walker.walk(seq,self.Tree)


