
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
import copy

from gen.seqListener import *


class SemSeq(seqListener):


    Stack=[]
    Queue=[]
    Dirs=[]
    Context=None

    # Queue is a set of registers
    # Each register is Movement, Repeat, Base, Offset
    #   Movement: N,S,W,E,NS,SN,EW,WE
    #   Repeat: Times that the register will be appliced
    #   Base: Index of the element to move from
    #   Offset: Movements from the Base in the Movement direction

    def __init__(self,context):
        self.Context=context

    def enterNumberAtom(self, ctx:seqParser.NumberAtomContext):
        logger.debug("enterNumberAtom %s",ctx.getText())
        self.Stack.append(int(ctx.getText()))

    def exitElemAtom(self, ctx:seqParser.ElemAtomContext):
        logger.debug("exitElemAtom %s",ctx.getText())

        if ctx.elem.type == seqParser.LAST:
            a=self.Context['i']
        elif ctx.elem.type == seqParser.ZERO:
            a=0
        else:
            pass
        self.Stack.append(a)



    def exitAddExpr(self, ctx:seqParser.AddExprContext):
        logger.debug("exitAddExpr %s",ctx.getText())
        b=self.Stack.pop()
        a=self.Stack.pop()

        if ctx.op.type == seqParser.PLUS:
            self.Stack.append(a+b)
        else:
            self.Stack.append(a-b)

    def exitAtoIdx(self, ctx:seqParser.AtoIdxContext):
        logger.debug("exitAtoIdx %s",ctx.getText())

        a=self.Stack.pop()
        # If the index is out of bounds reverts to the last available index
        try:
            b=self.Context['elems'][b]
        except IndexError:
            logger.debug("IndexError %d",a)
            b=self.Context['i']
        self.Stack.append(b)


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


    def exitStep(self, ctx:seqParser.StepContext):
        logger.debug("exitStep %s",ctx.getText())

        # At this time base should be a number representing an index
        # Base
        if ctx.base() is None:
            base=self.Context['i']
        else:
            base=self.Stack.pop()

        # Repeat
        if ctx.repet() is None:
            repe=1
        else:
            repe=self.Stack.pop()



        logger.info("Rep:%d Base,%d",repe,base)



        self.Dirs=[]


        # dir=ctx.dire.text
        #
        #
        # # Offset
        # if ctx.offset() is None:
        #     offset=1
        # else:
        #     offset=self.Stack.pop()
        #
        # # Repeat
        # if ctx.repet() is None:
        #     repe=1
        # else:
        #     repe=self.Stack.pop()
        #
        # # Base
        # if ctx.base() is None:
        #     base='L'
        # else:
        #     base=ctx.base().getText()
        #
        # for f in range(repe):
        #     i=self.Context['i']
        #     if base=='L':
        #         basei=i
        #     elif base=='Z':
        #         basei=0
        #
        #     old=self.Context['elems'][basei]
        #     new=copy.deepcopy(old)
        #     new.Move(dir,offset)
        #
        #     i=i+1
        #     self.Context['i']=i
        #     self.Context['elems'].append(new)

        # self.Queue.append(ctx.dire.text)
        # self.Queue.append(repe)
        # self.Queue.append(base)
        # self.Queue.append(offset)


    def exitDirs(self, ctx:seqParser.DirsContext):
        logger.debug("exitDirs %s",ctx.getText())

        dir=ctx.dire.text
        if ctx.offset() is None:
            offset=1
        else:
            offset=self.Stack.pop()

        self.Dirs.append((dir,offset))



    def enterSequence(self, ctx:seqParser.SequenceContext):
        pass
