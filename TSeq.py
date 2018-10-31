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
        #stream = antlr4.InputStream("((T+1)/2)E;(T/2)N;((T+1)/2)W;(T/2)S;")
        stream = antlr4.InputStream("{Z+1} (I+1)N;")

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
        self.Context['i']=0         # Current element
        self.Context['layer']=1         # Layer
        self.Context['step']=1
        self.Context['elems']=[]

        # Initial element
        new=TElem(1,0,0)
        self.Context['elems'].append(new)

    def NextVal(self):
        a=self.Context['elems'][self.Context['i']]

        #This is where the generating function should be created
        a=a+1
        return a


    def Walk(self):

        seq=SemSeq(self.Context)
        self.Walker.walk(seq,self.Tree)


