# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .seqParser import seqParser
else:
    from seqParser import seqParser

# This class defines a complete generic visitor for a parse tree produced by seqParser.

class seqVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by seqParser#addExpr.
    def visitAddExpr(self, ctx:seqParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#mulExpr.
    def visitMulExpr(self, ctx:seqParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#atomExpr.
    def visitAtomExpr(self, ctx:seqParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#parExpr.
    def visitParExpr(self, ctx:seqParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#numberAtom.
    def visitNumberAtom(self, ctx:seqParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#elemAtom.
    def visitElemAtom(self, ctx:seqParser.ElemAtomContext):
        return self.visitChildren(ctx)



del seqParser