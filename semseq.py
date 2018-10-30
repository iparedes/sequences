
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
from TElem import *


class SemSeq(seqListener):



    # Queue is a set of registers
    # Each register is Movement, Repeat, Base, Offset
    #   Movement: N,S,W,E,NS,SN,EW,WE
    #   Repeat: Times that the register will be appliced
    #   Base: Index of the element to move from
    #   Offset: Movements from the Base in the Movement direction

    def __init__(self,context):
        self.Stack=[]
        self.Queue=[]
        self.Dirs=[]
        self.Context=context

    def push(self,val,type='number'):
        self.Stack.append((val,type))

    def pop(self):
        a=self.Stack.pop()
        return a

    def enterNumberAtom(self, ctx:seqParser.NumberAtomContext):
        logger.debug("enterNumberAtom %s",ctx.getText())
        #self.Stack.append(int(ctx.getText()))
        self.push(int(ctx.getText()),"number")

    def exitElemAtom(self, ctx:seqParser.ElemAtomContext):
        logger.debug("exitElemAtom %s",ctx.getText())

        if ctx.elem.type == seqParser.LAST:
            a=self.Context['i']
            b="i"
        elif ctx.elem.type == seqParser.ZERO:
            a=0
            b="zero"
        elif ctx.elem.type == seqParser.LAYER:
            a=self.Context['layer']
            b="layer"
        elif ctx.elem.type == seqParser.STEP:
            a=self.Context['step']
            b='step'
        else:
            pass
        #self.Stack.append(a)
        self.push(a,b)



    def exitAddExpr(self, ctx:seqParser.AddExprContext):
        logger.debug("exitAddExpr %s",ctx.getText())
        # b=self.Stack.pop()
        # a=self.Stack.pop()
        (a, typea) = self.pop()
        (b, typeb) = self.pop()

        if ctx.op.type == seqParser.PLUS:
            #self.Stack.append(a+b)
            self.push(a + b,"number")
        else:
            #self.Stack.append(a-b)
            self.push(a - b, "number")

    def exitAtoIdx(self, ctx:seqParser.AtoIdxContext):
        logger.debug("exitAtoIdx %s",ctx.getText())

        #a=self.Stack.pop()
        (a,typea) = self.pop()

        # If the index is out of bounds reverts to the last available index
        try:
            b=self.Context['elems'][b]
        except IndexError:
            logger.debug("IndexError %d",a)
            b=self.Context['i']
        #self.Stack.append(b)
        self.push(b, "number")


    def exitMulExpr(self, ctx:seqParser.AddExprContext):
        logger.debug("exitMulExpr %s",ctx.getText())
        #b=self.Stack.pop()
        #a=self.Stack.pop()
        (b, typeb) = self.pop()
        (a, typea) = self.pop()

        if ctx.op.type == seqParser.MULT:
            #self.Stack.append(a*b)
            self.push((a * b), "number")
        else:
            #self.Stack.append(int(a/b))
            self.push(int(a / b), "number")

    def exitPowExpr(self, ctx:seqParser.PowExprContext):
        logger.debug("exitPowExpr %s",ctx.getText())

        #b=self.Stack.pop()
        #a=self.Stack.pop()
        (b, typeb) = self.pop()
        (a, typea) = self.pop()

        self.Stack.append(a**b)

    def exitMinExpr(self, ctx:seqParser.MinExprContext):
        logger.debug("exitMinExpr %s",ctx.getText())

        #a=self.Stack.pop()
        (a, typea) = self.pop()
        #self.Stack.append(-a)
        self.push(-a, "number")


    def exitStep(self, ctx:seqParser.StepContext):
        logger.debug("exitStep %s",ctx.getText())

        # At this time base should be a number representing an index
        # At this point I cannot have a number, as I miss the semantic meaning of the index, and
        #   for instance, 'last' could not keep growing
        # Base
        if ctx.base() is None:
            base=self.Context['i']
            typebase='i'
        else:
            #base=self.Stack.pop()
            (base, typebase) = self.pop()

        # Repeat
        if ctx.repet() is None:
            repe=1
            typerepe='number'
        else:
            #repe=self.Stack.pop()
            (repe, typerepe) = self.pop()

        #logger.info("Rep:%d Base,%d",repe,base)
        # Dirs should have a number of entries (dir,offset)
        for t in range(0,repe):
            i=self.Context['i']
            base_elem=self.Context['elems'][base]
            new_elem=copy.deepcopy(base_elem)
            pos=new_elem.pos
            for p in self.Dirs:
                pos.Move(p[0],p[1])

            self.Context['elems'].append(new_elem)
            self.Context['i']=i+1

            if typebase=='i':
                base=self.Context['i']

        self.Dirs=[]
        a=self.Context['step']
        self.Context['step']=a+1


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

    # def exitLayer(self, ctx:seqParser.LayerContext):
    #     logger.debug("exitLayer %s",ctx.getText())
    #
    #     l=self.Context['layer']
    #     self.Context['layer']=l+1

    def exitDirs(self, ctx:seqParser.DirsContext):
        logger.debug("exitDirs %s",ctx.getText())

        dir=ctx.dire.text
        if ctx.offset() is None:
            offset=1
        else:
            #offset=self.Stack.pop()
            (offset,type) = self.pop()

        self.Dirs.append((dir,offset))



    def enterSequence(self, ctx:seqParser.SequenceContext):
        pass
