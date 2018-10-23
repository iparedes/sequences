
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


from gen.seqListener import *


class SemSeq(seqListener):


    Stack=[]


    def enterNumberAtom(self, ctx:seqParser.NumberAtomContext):
        print ("NumberAtom",ctx.getText())
        self.Stack.append(int(ctx.getText()))

    def exitAddExpr(self, ctx:seqParser.AddExprContext):
        print("AddExpr",ctx.getText())
        a=self.Stack.pop()
        b=self.Stack.pop()
        self.Stack.append(a+b)
