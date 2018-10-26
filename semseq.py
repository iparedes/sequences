
# from gen.seqVisitor import *
#
#
# class SemSeq(seqVisitor):
#
#     # def visitBase(self,ctx):
#     #     print(ctx.getText())
#     #     print ("base")
#
#     def visitExpr(self,ctx):
#         print ("expr")
#
#     def visitTerm(self,ctx):
#         print ("term")
#
#     # def visitFactor(self,ctx):
#     #     print ("factor")

import logging
logger = logging.getLogger(__name__)

from gen.seqListener import *


class SemSeq(seqListener):


    Stack=[]
    Queue=[]


    def enterNumberAtom(self, ctx:seqParser.NumberAtomContext):
        logger.debug("enterNumberAtom %s",ctx.getText())
        self.Stack.append(int(ctx.getText()))

    def exitAddExpr(self, ctx:seqParser.AddExprContext):
        logger.debug("exitAddExpr %s",ctx.getText())
        b=self.Stack.pop()
        a=self.Stack.pop()

        if ctx.op.type == seqParser.PLUS:
            self.Stack.append(a+b)
        else:
            self.Stack.append(a-b)

    def exitMulExpr(self, ctx:seqParser.AddExprContext):
        logger.debug("exitMulExpr %s",ctx.getText())
        b=self.Stack.pop()
        a=self.Stack.pop()

        if ctx.op.type == seqParser.MULT:
            self.Stack.append(a*b)
        else:
            self.Stack.append(int(a/b))

    def exitPowExpr(self, ctx:seqParser.PowExprContext):
        logger.debug("exitPowExpr %s",ctx.getText())

        b=self.Stack.pop()
        a=self.Stack.pop()

        self.Stack.append(a**b)

    def exitMinExpr(self, ctx:seqParser.MinExprContext):
        logger.debug("exitMinExpr %s",ctx.getText())

        a=self.Stack.pop()
        self.Stack.append(-a)


    def exitSequence(self, ctx:seqParser.SequenceContext):
        logger.debug("exitSequence %s",ctx.getText())

        if ctx.offset() is None:
            b=1
        else:
            b=self.Stack.pop()

        if ctx.repet() is None:
            a=1
        else:
            a=self.Stack.pop()

        self.Queue.append(ctx.dire.text)
        self.Queue.append(a)
        self.Queue.append(b)

    def enterSequence(self, ctx:seqParser.SequenceContext):
        pass
