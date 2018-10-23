# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("\35\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\33\n\3\3\3\2\3\2\4\2\4\2\4\3\2\17\20\3\2\21\22\2")
        buf.write("\36\2\6\3\2\2\2\4\32\3\2\2\2\6\7\b\2\1\2\7\b\5\4\3\2\b")
        buf.write("\21\3\2\2\2\t\n\f\5\2\2\n\13\t\2\2\2\13\20\5\2\2\6\f\r")
        buf.write("\f\4\2\2\r\16\t\3\2\2\16\20\5\2\2\5\17\t\3\2\2\2\17\f")
        buf.write("\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22")
        buf.write("\3\3\2\2\2\23\21\3\2\2\2\24\25\7\r\2\2\25\26\5\2\2\2\26")
        buf.write("\27\7\16\2\2\27\33\3\2\2\2\30\33\7\n\2\2\31\33\7\6\2\2")
        buf.write("\32\24\3\2\2\2\32\30\3\2\2\2\32\31\3\2\2\2\33\5\3\2\2")
        buf.write("\2\5\17\21\32")
        return buf.getvalue()


class seqParser ( Parser ):

    grammarFileName = "seq.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'last'", "'zero'", "'i'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'&'", "'('", "')'", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "LAST", "ZERO", "I", "ELEM", "ELEM_val", 
                      "ELEM_idx", "IDENT", "NUMBER", "DIGIT", "OPIDX", "OPAR", 
                      "CPAR", "MULT", "DIV", "PLUS", "MINUS", "WS" ]

    RULE_expr = 0
    RULE_atom = 1

    ruleNames =  [ "expr", "atom" ]

    EOF = Token.EOF
    LAST=1
    ZERO=2
    I=3
    ELEM=4
    ELEM_val=5
    ELEM_idx=6
    IDENT=7
    NUMBER=8
    DIGIT=9
    OPIDX=10
    OPAR=11
    CPAR=12
    MULT=13
    DIV=14
    PLUS=15
    MINUS=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return seqParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.ExprContext)
            else:
                return self.getTypedRuleContext(seqParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(seqParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(seqParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.ExprContext)
            else:
                return self.getTypedRuleContext(seqParser.ExprContext,i)

        def MULT(self):
            return self.getToken(seqParser.MULT, 0)
        def DIV(self):
            return self.getToken(seqParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(seqParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = seqParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = seqParser.AtomExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 5
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 13
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = seqParser.MulExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 7
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 8
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.MULT or _la==seqParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 9
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = seqParser.AddExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 10
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 11
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.PLUS or _la==seqParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 12
                        self.expr(3)
                        pass

             
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return seqParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElemAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ELEM(self):
            return self.getToken(seqParser.ELEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemAtom" ):
                listener.enterElemAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemAtom" ):
                listener.exitElemAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemAtom" ):
                return visitor.visitElemAtom(self)
            else:
                return visitor.visitChildren(self)


    class ParExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(seqParser.OPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(seqParser.ExprContext,0)

        def CPAR(self):
            return self.getToken(seqParser.CPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParExpr" ):
                listener.enterParExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParExpr" ):
                listener.exitParExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParExpr" ):
                return visitor.visitParExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(seqParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = seqParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atom)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [seqParser.OPAR]:
                localctx = seqParser.ParExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(seqParser.OPAR)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(seqParser.CPAR)
                pass
            elif token in [seqParser.NUMBER]:
                localctx = seqParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(seqParser.NUMBER)
                pass
            elif token in [seqParser.ELEM]:
                localctx = seqParser.ElemAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(seqParser.ELEM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




