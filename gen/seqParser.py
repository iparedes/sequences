# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\6\2\33\n")
        buf.write("\2\r\2\16\2\34\3\3\3\3\3\4\5\4\"\n\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4(\n\4\3\4\6\4+\n\4\r\4\16\4,\3\5\3\5\3\5\5\5\62\n\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t@")
        buf.write("\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\tK\n\t\f\t")
        buf.write("\16\tN\13\t\3\n\3\n\3\n\3\n\3\n\3\n\5\nV\n\n\3\n\2\3\20")
        buf.write("\13\2\4\6\b\n\f\16\20\22\2\6\3\2\27\36\3\2\20\21\3\2\22")
        buf.write("\23\4\2\3\4\6\6\2Z\2\24\3\2\2\2\4\36\3\2\2\2\6!\3\2\2")
        buf.write("\2\b.\3\2\2\2\n\63\3\2\2\2\f\65\3\2\2\2\16\67\3\2\2\2")
        buf.write("\20?\3\2\2\2\22U\3\2\2\2\24\25\7\16\2\2\25\26\5\4\3\2")
        buf.write("\26\32\7\17\2\2\27\30\5\6\4\2\30\31\7\26\2\2\31\33\3\2")
        buf.write("\2\2\32\27\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3")
        buf.write("\2\2\2\35\3\3\2\2\2\36\37\5\20\t\2\37\5\3\2\2\2 \"\5\n")
        buf.write("\6\2! \3\2\2\2!\"\3\2\2\2\"\'\3\2\2\2#$\7\f\2\2$%\5\16")
        buf.write("\b\2%&\7\r\2\2&(\3\2\2\2\'#\3\2\2\2\'(\3\2\2\2(*\3\2\2")
        buf.write("\2)+\5\b\5\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-")
        buf.write("\7\3\2\2\2.\61\t\2\2\2/\60\7\25\2\2\60\62\5\f\7\2\61/")
        buf.write("\3\2\2\2\61\62\3\2\2\2\62\t\3\2\2\2\63\64\5\20\t\2\64")
        buf.write("\13\3\2\2\2\65\66\5\20\t\2\66\r\3\2\2\2\678\5\20\t\28")
        buf.write("\17\3\2\2\29:\b\t\1\2:;\7\23\2\2;@\5\20\t\7<@\5\22\n\2")
        buf.write("=>\7\t\2\2>@\5\22\n\2?9\3\2\2\2?<\3\2\2\2?=\3\2\2\2@L")
        buf.write("\3\2\2\2AB\f\b\2\2BC\7\24\2\2CK\5\20\t\bDE\f\6\2\2EF\t")
        buf.write("\3\2\2FK\5\20\t\7GH\f\5\2\2HI\t\4\2\2IK\5\20\t\6JA\3\2")
        buf.write("\2\2JD\3\2\2\2JG\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2")
        buf.write("M\21\3\2\2\2NL\3\2\2\2OP\7\n\2\2PQ\5\20\t\2QR\7\13\2\2")
        buf.write("RV\3\2\2\2SV\7\7\2\2TV\t\5\2\2UO\3\2\2\2US\3\2\2\2UT\3")
        buf.write("\2\2\2V\23\3\2\2\2\13\34!\',\61?JLU")
        return buf.getvalue()


class seqParser ( Parser ):

    grammarFileName = "seq.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'I'", "'Z'", "'L'", "'T'", "<INVALID>", 
                     "<INVALID>", "'&'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'*'", "'/'", "'+'", "'-'", "'^'", "':'", "';'", 
                     "'N'", "'S'", "'W'", "'E'", "'WE'", "'EW'", "'NS'", 
                     "'SN'" ]

    symbolicNames = [ "<INVALID>", "LAST", "ZERO", "LAYER", "STEP", "NUMBER", 
                      "DIGIT", "OPIDX", "OPAR", "CPAR", "OBRA", "CBRA", 
                      "OCUR", "CCUR", "MULT", "DIV", "PLUS", "MINUS", "POW", 
                      "COLON", "SEMI", "N", "S", "W", "E", "WE", "EW", "NS", 
                      "SN", "WS" ]

    RULE_sequence = 0
    RULE_gen = 1
    RULE_step = 2
    RULE_dirs = 3
    RULE_repet = 4
    RULE_offset = 5
    RULE_base = 6
    RULE_expr = 7
    RULE_atom = 8

    ruleNames =  [ "sequence", "gen", "step", "dirs", "repet", "offset", 
                   "base", "expr", "atom" ]

    EOF = Token.EOF
    LAST=1
    ZERO=2
    LAYER=3
    STEP=4
    NUMBER=5
    DIGIT=6
    OPIDX=7
    OPAR=8
    CPAR=9
    OBRA=10
    CBRA=11
    OCUR=12
    CCUR=13
    MULT=14
    DIV=15
    PLUS=16
    MINUS=17
    POW=18
    COLON=19
    SEMI=20
    N=21
    S=22
    W=23
    E=24
    WE=25
    EW=26
    NS=27
    SN=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCUR(self):
            return self.getToken(seqParser.OCUR, 0)

        def gen(self):
            return self.getTypedRuleContext(seqParser.GenContext,0)


        def CCUR(self):
            return self.getToken(seqParser.CCUR, 0)

        def step(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.StepContext)
            else:
                return self.getTypedRuleContext(seqParser.StepContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(seqParser.SEMI)
            else:
                return self.getToken(seqParser.SEMI, i)

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
            self.state = 18
            self.match(seqParser.OCUR)
            self.state = 19
            self.gen()
            self.state = 20
            self.match(seqParser.CCUR)
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.step()
                self.state = 22
                self.match(seqParser.SEMI)
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.LAST) | (1 << seqParser.ZERO) | (1 << seqParser.STEP) | (1 << seqParser.NUMBER) | (1 << seqParser.OPIDX) | (1 << seqParser.OPAR) | (1 << seqParser.OBRA) | (1 << seqParser.MINUS) | (1 << seqParser.N) | (1 << seqParser.S) | (1 << seqParser.W) | (1 << seqParser.E) | (1 << seqParser.WE) | (1 << seqParser.EW) | (1 << seqParser.NS) | (1 << seqParser.SN))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(seqParser.ExprContext,0)


        def getRuleIndex(self):
            return seqParser.RULE_gen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGen" ):
                listener.enterGen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGen" ):
                listener.exitGen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGen" ):
                return visitor.visitGen(self)
            else:
                return visitor.visitChildren(self)




    def gen(self):

        localctx = seqParser.GenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_gen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StepContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def repet(self):
            return self.getTypedRuleContext(seqParser.RepetContext,0)


        def OBRA(self):
            return self.getToken(seqParser.OBRA, 0)

        def base(self):
            return self.getTypedRuleContext(seqParser.BaseContext,0)


        def CBRA(self):
            return self.getToken(seqParser.CBRA, 0)

        def dirs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.DirsContext)
            else:
                return self.getTypedRuleContext(seqParser.DirsContext,i)


        def getRuleIndex(self):
            return seqParser.RULE_step

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStep" ):
                listener.enterStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStep" ):
                listener.exitStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStep" ):
                return visitor.visitStep(self)
            else:
                return visitor.visitChildren(self)




    def step(self):

        localctx = seqParser.StepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_step)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.LAST) | (1 << seqParser.ZERO) | (1 << seqParser.STEP) | (1 << seqParser.NUMBER) | (1 << seqParser.OPIDX) | (1 << seqParser.OPAR) | (1 << seqParser.MINUS))) != 0):
                self.state = 30
                self.repet()


            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==seqParser.OBRA:
                self.state = 33
                self.match(seqParser.OBRA)
                self.state = 34
                self.base()
                self.state = 35
                self.match(seqParser.CBRA)


            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.dirs()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.N) | (1 << seqParser.S) | (1 << seqParser.W) | (1 << seqParser.E) | (1 << seqParser.WE) | (1 << seqParser.EW) | (1 << seqParser.NS) | (1 << seqParser.SN))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dire = None # Token

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

        def COLON(self):
            return self.getToken(seqParser.COLON, 0)

        def offset(self):
            return self.getTypedRuleContext(seqParser.OffsetContext,0)


        def getRuleIndex(self):
            return seqParser.RULE_dirs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirs" ):
                listener.enterDirs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirs" ):
                listener.exitDirs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirs" ):
                return visitor.visitDirs(self)
            else:
                return visitor.visitChildren(self)




    def dirs(self):

        localctx = seqParser.DirsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dirs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            localctx.dire = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.N) | (1 << seqParser.S) | (1 << seqParser.W) | (1 << seqParser.E) | (1 << seqParser.WE) | (1 << seqParser.EW) | (1 << seqParser.NS) | (1 << seqParser.SN))) != 0)):
                localctx.dire = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==seqParser.COLON:
                self.state = 45
                self.match(seqParser.COLON)
                self.state = 46
                self.offset()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RepetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(seqParser.ExprContext,0)


        def getRuleIndex(self):
            return seqParser.RULE_repet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepet" ):
                listener.enterRepet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepet" ):
                listener.exitRepet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepet" ):
                return visitor.visitRepet(self)
            else:
                return visitor.visitChildren(self)




    def repet(self):

        localctx = seqParser.RepetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_repet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OffsetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(seqParser.ExprContext,0)


        def getRuleIndex(self):
            return seqParser.RULE_offset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOffset" ):
                listener.enterOffset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOffset" ):
                listener.exitOffset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOffset" ):
                return visitor.visitOffset(self)
            else:
                return visitor.visitChildren(self)




    def offset(self):

        localctx = seqParser.OffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_offset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(seqParser.ExprContext,0)


        def getRuleIndex(self):
            return seqParser.RULE_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase" ):
                listener.enterBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase" ):
                listener.exitBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase" ):
                return visitor.visitBase(self)
            else:
                return visitor.visitChildren(self)




    def base(self):

        localctx = seqParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
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


    class AtoIdxContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPIDX(self):
            return self.getToken(seqParser.OPIDX, 0)
        def atom(self):
            return self.getTypedRuleContext(seqParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtoIdx" ):
                listener.enterAtoIdx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtoIdx" ):
                listener.exitAtoIdx(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtoIdx" ):
                return visitor.visitAtoIdx(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = seqParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [seqParser.MINUS]:
                localctx = seqParser.MinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 56
                self.match(seqParser.MINUS)
                self.state = 57
                self.expr(5)
                pass
            elif token in [seqParser.LAST, seqParser.ZERO, seqParser.STEP, seqParser.NUMBER, seqParser.OPAR]:
                localctx = seqParser.AtoExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.atom()
                pass
            elif token in [seqParser.OPIDX]:
                localctx = seqParser.AtoIdxContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(seqParser.OPIDX)
                self.state = 60
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = seqParser.PowExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 64
                        self.match(seqParser.POW)
                        self.state = 65
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = seqParser.MulExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.MULT or _la==seqParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = seqParser.AddExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.PLUS or _la==seqParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expr(4)
                        pass

             
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
            self.elem = None # Token
            self.copyFrom(ctx)

        def LAST(self):
            return self.getToken(seqParser.LAST, 0)
        def ZERO(self):
            return self.getToken(seqParser.ZERO, 0)
        def STEP(self):
            return self.getToken(seqParser.STEP, 0)

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
        self.enterRule(localctx, 16, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [seqParser.OPAR]:
                localctx = seqParser.ParExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(seqParser.OPAR)
                self.state = 78
                self.expr(0)
                self.state = 79
                self.match(seqParser.CPAR)
                pass
            elif token in [seqParser.NUMBER]:
                localctx = seqParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(seqParser.NUMBER)
                pass
            elif token in [seqParser.LAST, seqParser.ZERO, seqParser.STEP]:
                localctx = seqParser.ElemAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                localctx.elem = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.LAST) | (1 << seqParser.ZERO) | (1 << seqParser.STEP))) != 0)):
                    localctx.elem = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




