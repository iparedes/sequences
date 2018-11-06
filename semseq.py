
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

    vars=['i','zero','layer','step','ilayer']

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
        self.Gen=[]

        self.Queue=[]
        self.Dirs=[]
        self.Context=context

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
        elif ctx.elem.type == seqParser.ILAYER:
            b='ilayer'
        else:
            pass
        self.push(b)


    def enterLayer(self, ctx:seqParser.LayerContext):
        logger.debug("enterLayer %s",ctx.getText())
        i=self.Context['layer']
        self.Context['layer']=i+1
        logger.debug("Starting layer %d",self.Context['layer'])
        self.Context['ilayer']=0
        self.Context['step']=0

    def exitLayer(self, ctx:seqParser.LayerContext):
        logger.debug("enterLayer %s",ctx.getText())
        pass


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

    def exitSumExpr(self, ctx:seqParser.SumExprContext):
        logger.debug("exitSumExpr %s",ctx.getText())

        self.push("sum")

    def enterStep(self, ctx:seqParser.StepContext):
        logger.debug("enterStep %s",ctx.getText())

        i=self.Context['step']
        self.Context['step']=i+1
        self.Base=[]
        self.Dirs=[]
        self.Repet=[]

    def exitStep(self, ctx:seqParser.StepContext):
        logger.debug("exitStep %s",ctx.getText())

        if not self.Repet:
            repe=1
        else:
            repe=self.evaluate(self.Repet)


        for t in range(0,repe):


            if not self.Base:
                # Take the last element by default
                base=self.Context['i']
            else:
                base=self.evaluate(self.Base)

            i=self.Context['i']
            self.Context['i']=i+1
            j=self.Context['ilayer']
            self.Context['ilayer']=j+1

            logger.debug("Taking elem %d as base",base)
            base_elem=self.Context['elems'][base]
            new_elem=copy.deepcopy(base_elem)
            pos=new_elem.pos
            logger.debug("its pos is %s and its val is %d",pos.getText(),new_elem.val)
            val=self.evaluate(self.Gen)
            logger.debug("The value of the new elem (%d) is %d",self.Context['i'],val)
            new_elem.val=val
            for p in self.Dirs:
                logger.debug("Now I am moving to %s",p)
                offset=self.evaluate(p[1])
                if len(p[0])==2:
                    pos.Move(p[0][0],offset)
                    logger.debug("which results in a new pos of %s",pos.getText())
                    self.Context['elems'].append(new_elem)
                    new_elem=copy.deepcopy(base_elem)
                    new_elem.val=val
                    pos=new_elem.pos
                    offset=self.evaluate(p[1])
                    pos.Move(p[0][1],offset)

                    i=self.Context['i']
                    self.Context['i']=i+1
                    j=self.Context['ilayer']
                    self.Context['ilayer']=j+1

                    logger.debug("and an additional element (%d) at %s",self.Context['i'],pos.getText())
                    self.Context['elems'].append(new_elem)
                else:
                    pos.Move(p[0],offset)
                    logger.debug("which results in a new pos of %s",pos.getText())
                    self.Context['elems'].append(new_elem)


        self.Dirs=[]


    def enterDirs(self, ctx:seqParser.DirsContext):
        logger.debug("enterDirs %s",ctx.getText())

        self.Offset=[]

    def exitDirs(self, ctx:seqParser.DirsContext):
        logger.debug("exitDirs %s",ctx.getText())

        dir=ctx.dire.text
        if not self.Offset:
            self.Offset=[1]
#        else:
#            offset=self.evaluate(self.Offset)
        self.Dirs.append((dir,self.Offset))




    def exitGen(self, ctx:seqParser.GenContext):
        logger.debug("exitGen %s",ctx.getText())

        self.Gen=self.Stack
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
        logger.debug("enterSequence %s",ctx.getText())

        self.Gen=[]
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
                    aux.append(b-a)
                elif item == '*':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(a*b)
                elif item == '/':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(int(b/a))
                elif item == '^':
                    a=aux.pop()
                    b=aux.pop()
                    aux.append(b**a)
                elif item == 'neg':
                    a=aux.pop()
                    aux.append(-a)
                elif item == 'sum':
                    a=aux.pop()
                    b=sum(range(1,a+1))
                    aux.append(b)
                elif item == '&':
                    a=aux.pop()
                    try:
                        n=self.Context['elems'][a]
                    except IndexError:
                        n=self.Context['elems'][self.Context['i']]
                    aux.append(n)
                else:
                    pass
        a=aux.pop()
        return a

    def isValue(self,item):
        return type(item)==int

