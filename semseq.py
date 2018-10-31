
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

    vars=['i','zero','layer','step']

    # Queue is a set of registers
    # Each register is Movement, Repeat, Base, Offset
    #   Movement: N,S,W,E,NS,SN,EW,WE
    #   Repeat: Times that the register will be appliced
    #   Base: Index of the element to move from
    #   Offset: Movements from the Base in the Movement direction

    def __init__(self,context):
        self.Stack=[]
        self.Repet=[]
        self.Offset=[]
        self.Base=[]

        self.Queue=[]
        self.Dirs=[]
        self.Context=context
        self.SExpr=[]

    def push(self,val):
        self.Stack.append(val)

    def pop(self):
        a=self.Stack.pop()
        return a

    def enterNumberAtom(self, ctx:seqParser.NumberAtomContext):
        logger.debug("enterNumberAtom %s",ctx.getText())

        self.push(int(ctx.getText()))

    def exitElemAtom(self, ctx:seqParser.ElemAtomContext):
        logger.debug("exitElemAtom %s",ctx.getText())

        if ctx.elem.type == seqParser.LAST:
            b="i"
        elif ctx.elem.type == seqParser.ZERO:
            b="zero"
        elif ctx.elem.type == seqParser.LAYER:
            b="layer"
        elif ctx.elem.type == seqParser.STEP:
            b='step'
        else:
            pass
        self.push(b)



    def exitAddExpr(self, ctx:seqParser.AddExprContext):
        logger.debug("exitAddExpr %s",ctx.getText())

        if ctx.op.type == seqParser.PLUS:
            self.push("+")
        else:
            self.push("-")

    def exitAtoIdx(self, ctx:seqParser.AtoIdxContext):
        logger.debug("exitAtoIdx %s",ctx.getText())

        self.push("&")


    def exitMulExpr(self, ctx:seqParser.AddExprContext):
        logger.debug("exitMulExpr %s",ctx.getText())

        if ctx.op.type == seqParser.MULT:
            self.push("*")
        else:
            self.push("/")

    def exitPowExpr(self, ctx:seqParser.PowExprContext):
        logger.debug("exitPowExpr %s",ctx.getText())

        self.push("^")

    def exitMinExpr(self, ctx:seqParser.MinExprContext):
        logger.debug("exitMinExpr %s",ctx.getText())

        self.push("neg")


    def exitStep(self, ctx:seqParser.StepContext):
        logger.debug("exitStep %s",ctx.getText())

        if not self.Repet:
            repe=1
        else:
            repe=self.evaluate(self.Repet)




        for t in range(0,repe):
            i=self.Context['i']
            if not self.Base:
                # Take the last element by default
                base=self.Context['i']
            else:
                base=self.evaluate(self.Base)
            base_elem=self.Context['elems'][base]
            new_elem=copy.deepcopy(base_elem)
            pos=new_elem.pos
            for p in self.Dirs:
                pos.Move(p[0],p[1])

            self.Context['elems'].append(new_elem)
            self.Context['i']=i+1

        self.Dirs=[]
        a=self.Context['step']
        self.Context['step']=a+1



    def exitDirs(self, ctx:seqParser.DirsContext):
        logger.debug("exitDirs %s",ctx.getText())

        dir=ctx.dire.text
        if not self.Offset:
            offset=1
        else:
            offset=self.evaluate(self.Offset)
        self.Dirs.append((dir,offset))


    def exitGen(self, ctx:seqParser.GenContext):
        logger.debug("exitGen %s",ctx.getText())

        self.SExpr=self.Stack
        self.Stack=[]


    def exitRepet(self, ctx:seqParser.RepetContext):
        logger.debug("exitRepet %s",ctx.getText())

        self.Repet=self.Stack
        self.Stack=[]

    def exitOffset(self, ctx:seqParser.OffsetContext):
        logger.debug("exitOffset %s",ctx.getText())

        self.Offset=self.Stack
        self.Stack=[]

    def exitBase(self, ctx:seqParser.BaseContext):
        logger.debug("exitBase %s",ctx.getText())

        self.Base=self.Stack
        self.Stack=[]

    def enterSequence(self, ctx:seqParser.SequenceContext):
        pass

    def evaluate(self,pila):
        logger.debug("evaluate")

        aux=[]
        item=0
        t=copy.copy(pila)
        t.reverse()
        while t:
            item=t.pop()
            if item in self.vars:
                a=self.Context[item]
                aux.append(a)
            elif self.isValue(item):
                aux.append(item)
            else:
                # operator
                if item == '+':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(a+b)
                elif item == '-':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(a-b)
                elif item == '*':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(a*b)
                elif item == '/':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(int(b/a))
                elif item == '':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(b**a)
                elif item == 'neg':
                    a=aux.pop()
                    aux.append(-a)
                else:
                    pass
        a=aux.pop()
        return a

    def isValue(self,item):
        return type(item)==int

