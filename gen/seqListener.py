# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .seqParser import seqParser
else:
    from seqParser import seqParser

# This class defines a complete listener for a parse tree produced by seqParser.
class seqListener(ParseTreeListener):

    # Enter a parse tree produced by seqParser#sequence.
    def enterSequence(self, ctx:seqParser.SequenceContext):
        pass

    # Exit a parse tree produced by seqParser#sequence.
    def exitSequence(self, ctx:seqParser.SequenceContext):
        pass


    # Enter a parse tree produced by seqParser#gen.
    def enterGen(self, ctx:seqParser.GenContext):
        pass

    # Exit a parse tree produced by seqParser#gen.
    def exitGen(self, ctx:seqParser.GenContext):
        pass


    # Enter a parse tree produced by seqParser#layer.
    def enterLayer(self, ctx:seqParser.LayerContext):
        pass

    # Exit a parse tree produced by seqParser#layer.
    def exitLayer(self, ctx:seqParser.LayerContext):
        pass


    # Enter a parse tree produced by seqParser#step.
    def enterStep(self, ctx:seqParser.StepContext):
        pass

    # Exit a parse tree produced by seqParser#step.
    def exitStep(self, ctx:seqParser.StepContext):
        pass


    # Enter a parse tree produced by seqParser#dirs.
    def enterDirs(self, ctx:seqParser.DirsContext):
        pass

    # Exit a parse tree produced by seqParser#dirs.
    def exitDirs(self, ctx:seqParser.DirsContext):
        pass


    # Enter a parse tree produced by seqParser#repet.
    def enterRepet(self, ctx:seqParser.RepetContext):
        pass

    # Exit a parse tree produced by seqParser#repet.
    def exitRepet(self, ctx:seqParser.RepetContext):
        pass


    # Enter a parse tree produced by seqParser#offset.
    def enterOffset(self, ctx:seqParser.OffsetContext):
        pass

    # Exit a parse tree produced by seqParser#offset.
    def exitOffset(self, ctx:seqParser.OffsetContext):
        pass


    # Enter a parse tree produced by seqParser#base.
    def enterBase(self, ctx:seqParser.BaseContext):
        pass

    # Exit a parse tree produced by seqParser#base.
    def exitBase(self, ctx:seqParser.BaseContext):
        pass


    # Enter a parse tree produced by seqParser#minExpr.
    def enterMinExpr(self, ctx:seqParser.MinExprContext):
        pass

    # Exit a parse tree produced by seqParser#minExpr.
    def exitMinExpr(self, ctx:seqParser.MinExprContext):
        pass


    # Enter a parse tree produced by seqParser#sumExpr.
    def enterSumExpr(self, ctx:seqParser.SumExprContext):
        pass

    # Exit a parse tree produced by seqParser#sumExpr.
    def exitSumExpr(self, ctx:seqParser.SumExprContext):
        pass


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


    # Enter a parse tree produced by seqParser#atoExpr.
    def enterAtoExpr(self, ctx:seqParser.AtoExprContext):
        pass

    # Exit a parse tree produced by seqParser#atoExpr.
    def exitAtoExpr(self, ctx:seqParser.AtoExprContext):
        pass


    # Enter a parse tree produced by seqParser#powExpr.
    def enterPowExpr(self, ctx:seqParser.PowExprContext):
        pass

    # Exit a parse tree produced by seqParser#powExpr.
    def exitPowExpr(self, ctx:seqParser.PowExprContext):
        pass


    # Enter a parse tree produced by seqParser#atoIdx.
    def enterAtoIdx(self, ctx:seqParser.AtoIdxContext):
        pass

    # Exit a parse tree produced by seqParser#atoIdx.
    def exitAtoIdx(self, ctx:seqParser.AtoIdxContext):
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


