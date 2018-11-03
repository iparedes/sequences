# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .seqParser import seqParser
else:
    from seqParser import seqParser

# This class defines a complete generic visitor for a parse tree produced by seqParser.

class seqVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by seqParser#sequence.
    def visitSequence(self, ctx:seqParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#gen.
    def visitGen(self, ctx:seqParser.GenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#layer.
    def visitLayer(self, ctx:seqParser.LayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#step.
    def visitStep(self, ctx:seqParser.StepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#dirs.
    def visitDirs(self, ctx:seqParser.DirsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#repet.
    def visitRepet(self, ctx:seqParser.RepetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#offset.
    def visitOffset(self, ctx:seqParser.OffsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#base.
    def visitBase(self, ctx:seqParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#minExpr.
    def visitMinExpr(self, ctx:seqParser.MinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#sumExpr.
    def visitSumExpr(self, ctx:seqParser.SumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#addExpr.
    def visitAddExpr(self, ctx:seqParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#mulExpr.
    def visitMulExpr(self, ctx:seqParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#atoExpr.
    def visitAtoExpr(self, ctx:seqParser.AtoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#powExpr.
    def visitPowExpr(self, ctx:seqParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by seqParser#atoIdx.
    def visitAtoIdx(self, ctx:seqParser.AtoIdxContext):
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