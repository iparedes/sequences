# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write(")\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3\21\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3\34\n\3\f\3\16\3\37\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\'\n\4\3\4\2\3\4\5\2\4\6\2\5\3\2\23\32\3\2\16\17\3\2\20")
        buf.write("\21\2+\2\b\3\2\2\2\4\20\3\2\2\2\6&\3\2\2\2\b\t\5\4\3\2")
        buf.write("\t\n\t\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f\r\b\3\1\2\r\16")
        buf.write("\7\21\2\2\16\21\5\4\3\6\17\21\5\6\4\2\20\f\3\2\2\2\20")
        buf.write("\17\3\2\2\2\21\35\3\2\2\2\22\23\f\7\2\2\23\24\7\22\2\2")
        buf.write("\24\34\5\4\3\7\25\26\f\5\2\2\26\27\t\3\2\2\27\34\5\4\3")
        buf.write("\6\30\31\f\4\2\2\31\32\t\4\2\2\32\34\5\4\3\5\33\22\3\2")
        buf.write("\2\2\33\25\3\2\2\2\33\30\3\2\2\2\34\37\3\2\2\2\35\33\3")
        buf.write("\2\2\2\35\36\3\2\2\2\36\5\3\2\2\2\37\35\3\2\2\2 !\7\f")
        buf.write("\2\2!\"\5\4\3\2\"#\7\r\2\2#\'\3\2\2\2$\'\7\t\2\2%\'\7")
        buf.write("\6\2\2& \3\2\2\2&$\3\2\2\2&%\3\2\2\2\'\7\3\2\2\2\6\20")
        buf.write("\33\35&")
        return buf.getvalue()


class seqParser ( Parser ):

    grammarFileName = "seq.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'last'", "'zero'", "'i'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'&'", "'('", "')'", "'*'", "'/'", "'+'", "'-'", "'^'", 
                     "'N'", "'S'", "'W'", "'E'", "'WE'", "'EW'", "'NS'", 
                     "'SN'" ]

    symbolicNames = [ "<INVALID>", "LAST", "ZERO", "I", "ELEM", "ELEM_val", 
                      "ELEM_idx", "NUMBER", "DIGIT", "OPIDX", "OPAR", "CPAR", 
                      "MULT", "DIV", "PLUS", "MINUS", "POW", "N", "S", "W", 
                      "E", "WE", "EW", "NS", "SN", "WS" ]

    RULE_sequence = 0
    RULE_expr = 1
    RULE_atom = 2

    ruleNames =  [ "sequence", "expr", "atom" ]

    EOF = Token.EOF
    LAST=1
    ZERO=2
    I=3
    ELEM=4
    ELEM_val=5
    ELEM_idx=6
    NUMBER=7
    DIGIT=8
    OPIDX=9
    OPAR=10
    CPAR=11
    MULT=12
    DIV=13
    PLUS=14
    MINUS=15
    POW=16
    N=17
    S=18
    W=19
    E=20
    WE=21
    EW=22
    NS=23
    SN=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dire = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.ExprContext)
            else:
                return self.getTypedRuleContext(seqParser.ExprContext,i)


        def N(self):
            return self.getToken(seqParser.N, 0)

        def S(self):
            return self.getToken(seqParser.S, 0)

        def W(self):
            return self.getToken(seqParser.W, 0)

        def E(self):
            return self.getToken(seqParser.E, 0)

        def WE(self):
            return self.getToken(seqParser.WE, 0)

        def EW(self):
            return self.getToken(seqParser.EW, 0)

        def NS(self):
            return self.getToken(seqParser.NS, 0)

        def SN(self):
            return self.getToken(seqParser.SN, 0)

        def getRuleIndex(self):
            return seqParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = seqParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr(0)
            self.state = 7
            localctx.dire = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.N) | (1 << seqParser.S) | (1 << seqParser.W) | (1 << seqParser.E) | (1 << seqParser.WE) | (1 << seqParser.EW) | (1 << seqParser.NS) | (1 << seqParser.SN))) != 0)):
                localctx.dire = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 8
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return seqParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(seqParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(seqParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinExpr" ):
                listener.enterMinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinExpr" ):
                listener.exitMinExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinExpr" ):
                return visitor.visitMinExpr(self)
            else:
                return visitor.visitChildren(self)


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


    class AtoExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(seqParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtoExpr" ):
                listener.enterAtoExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtoExpr" ):
                listener.exitAtoExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtoExpr" ):
                return visitor.visitAtoExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.ExprContext)
            else:
                return self.getTypedRuleContext(seqParser.ExprContext,i)

        def POW(self):
            return self.getToken(seqParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpr" ):
                listener.enterPowExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpr" ):
                listener.exitPowExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExpr" ):
                return visitor.visitPowExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = seqParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [seqParser.MINUS]:
                localctx = seqParser.MinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 11
                self.match(seqParser.MINUS)
                self.state = 12
                self.expr(4)
                pass
            elif token in [seqParser.ELEM, seqParser.NUMBER, seqParser.OPAR]:
                localctx = seqParser.AtoExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 25
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = seqParser.PowExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 17
                        self.match(seqParser.POW)
                        self.state = 18
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = seqParser.MulExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 20
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.MULT or _la==seqParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 21
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = seqParser.AddExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 23
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.PLUS or _la==seqParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 24
                        self.expr(3)
                        pass

             
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [seqParser.OPAR]:
                localctx = seqParser.ParExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(seqParser.OPAR)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(seqParser.CPAR)
                pass
            elif token in [seqParser.NUMBER]:
                localctx = seqParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(seqParser.NUMBER)
                pass
            elif token in [seqParser.ELEM]:
                localctx = seqParser.ElemAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
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
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




