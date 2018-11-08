import logging
logger = logging.getLogger(__name__)


import antlr4
from gen.seqLexer  import *
from semseq import *
from TElem import *


class TSeq:

    def __init__(self,stream):
        self.Walker=None
        self.Tree=None
        self.Context={}

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
        self.Context['zerol']=1
        self.Context['zerolprov']=1
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


