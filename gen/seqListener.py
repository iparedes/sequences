# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .seqParser import seqParser
else:
    from seqParser import seqParser

# This class defines a complete listener for a parse tree produced by seqParser.
class seqListener(ParseTreeListener):

    # Enter a parse tree produced by seqParser#addExpr.
    def enterAddExpr(self, ctx:seqParser.AddExprContext):
        pass

    # Exit a parse tree produced by seqParser#addExpr.
    def exitAddExpr(self, ctx:seqParser.AddExprContext):
        pass


    # Enter a parse tree produced by seqParser#mulExpr.
    def enterMulExpr(self, ctx:seqParser.MulExprContext):
        pass

    # Exit a parse tree produced by seqParser#mulExpr.
    def exitMulExpr(self, ctx:seqParser.MulExprContext):
        pass


    # Enter a parse tree produced by seqParser#atomExpr.
    def enterAtomExpr(self, ctx:seqParser.AtomExprContext):
        pass

    # Exit a parse tree produced by seqParser#atomExpr.
    def exitAtomExpr(self, ctx:seqParser.AtomExprContext):
        pass


    # Enter a parse tree produced by seqParser#parExpr.
    def enterParExpr(self, ctx:seqParser.ParExprContext):
        pass

    # Exit a parse tree produced by seqParser#parExpr.
    def exitParExpr(self, ctx:seqParser.ParExprContext):
        pass


    # Enter a parse tree produced by seqParser#numberAtom.
    def enterNumberAtom(self, ctx:seqParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by seqParser#numberAtom.
    def exitNumberAtom(self, ctx:seqParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by seqParser#elemAtom.
    def enterElemAtom(self, ctx:seqParser.ElemAtomContext):
        pass

    # Exit a parse tree produced by seqParser#elemAtom.
    def exitElemAtom(self, ctx:seqParser.ElemAtomContext):
        pass

