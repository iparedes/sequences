# Generated from /Users/nacho/ownCloud/Python-projects/sequences/seq.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\6\2\35\n\2\r\2\16\2\36\3\3\3\3\3\4\3\4\3\4\7\4&\n\4\f")
        buf.write("\4\16\4)\13\4\3\5\5\5,\n\5\3\5\3\5\3\5\3\5\5\5\62\n\5")
        buf.write("\3\5\6\5\65\n\5\r\5\16\5\66\3\6\3\6\3\6\5\6<\n\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write("L\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nW\n\n\f\n")
        buf.write("\16\nZ\13\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13b\n\13\3")
        buf.write("\13\2\3\22\f\2\4\6\b\n\f\16\20\22\24\2\6\3\2\32!\3\2\21")
        buf.write("\22\3\2\23\24\3\2\3\7\2g\2\26\3\2\2\2\4 \3\2\2\2\6\"\3")
        buf.write("\2\2\2\b+\3\2\2\2\n8\3\2\2\2\f=\3\2\2\2\16?\3\2\2\2\20")
        buf.write("A\3\2\2\2\22K\3\2\2\2\24a\3\2\2\2\26\27\7\17\2\2\27\30")
        buf.write("\5\4\3\2\30\34\7\20\2\2\31\32\5\6\4\2\32\33\7\30\2\2\33")
        buf.write("\35\3\2\2\2\34\31\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2")
        buf.write("\36\37\3\2\2\2\37\3\3\2\2\2 !\5\22\n\2!\5\3\2\2\2\"\'")
        buf.write("\5\b\5\2#$\7\31\2\2$&\5\b\5\2%#\3\2\2\2&)\3\2\2\2\'%\3")
        buf.write("\2\2\2\'(\3\2\2\2(\7\3\2\2\2)\'\3\2\2\2*,\5\f\7\2+*\3")
        buf.write("\2\2\2+,\3\2\2\2,\61\3\2\2\2-.\7\r\2\2./\5\20\t\2/\60")
        buf.write("\7\16\2\2\60\62\3\2\2\2\61-\3\2\2\2\61\62\3\2\2\2\62\64")
        buf.write("\3\2\2\2\63\65\5\n\6\2\64\63\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\67\t\3\2\2\28;\t\2\2\29:\7\27")
        buf.write("\2\2:<\5\16\b\2;9\3\2\2\2;<\3\2\2\2<\13\3\2\2\2=>\5\22")
        buf.write("\n\2>\r\3\2\2\2?@\5\22\n\2@\17\3\2\2\2AB\5\22\n\2B\21")
        buf.write("\3\2\2\2CD\b\n\1\2DE\7\24\2\2EL\5\22\n\bFG\7\26\2\2GL")
        buf.write("\5\22\n\7HL\5\24\13\2IJ\7\n\2\2JL\5\24\13\2KC\3\2\2\2")
        buf.write("KF\3\2\2\2KH\3\2\2\2KI\3\2\2\2LX\3\2\2\2MN\f\t\2\2NO\7")
        buf.write("\25\2\2OW\5\22\n\tPQ\f\6\2\2QR\t\3\2\2RW\5\22\n\7ST\f")
        buf.write("\5\2\2TU\t\4\2\2UW\5\22\n\6VM\3\2\2\2VP\3\2\2\2VS\3\2")
        buf.write("\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\23\3\2\2\2ZX\3\2\2")
        buf.write("\2[\\\7\13\2\2\\]\5\22\n\2]^\7\f\2\2^b\3\2\2\2_b\7\b\2")
        buf.write("\2`b\t\5\2\2a[\3\2\2\2a_\3\2\2\2a`\3\2\2\2b\25\3\2\2\2")
        buf.write("\f\36\'+\61\66;KVXa")
        return buf.getvalue()


class seqParser ( Parser ):

    grammarFileName = "seq.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'i'", "'z'", "'t'", "'l'", "'j'", "<INVALID>", 
                     "<INVALID>", "'&'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'*'", "'/'", "'+'", "'-'", "'^'", "'#'", "':'", 
                     "';'", "','", "'N'", "'S'", "'W'", "'E'", "'WE'", "'EW'", 
                     "'NS'", "'SN'" ]

    symbolicNames = [ "<INVALID>", "LAST", "ZERO", "STEP", "LAYER", "ILAYER", 
                      "NUMBER", "DIGIT", "OPIDX", "OPAR", "CPAR", "OBRA", 
                      "CBRA", "OCUR", "CCUR", "MULT", "DIV", "PLUS", "MINUS", 
                      "POW", "SUM", "COLON", "SEMI", "COMMA", "N", "S", 
                      "W", "E", "WE", "EW", "NS", "SN", "WS" ]

    RULE_sequence = 0
    RULE_gen = 1
    RULE_layer = 2
    RULE_step = 3
    RULE_dirs = 4
    RULE_repet = 5
    RULE_offset = 6
    RULE_base = 7
    RULE_expr = 8
    RULE_atom = 9

    ruleNames =  [ "sequence", "gen", "layer", "step", "dirs", "repet", 
                   "offset", "base", "expr", "atom" ]

    EOF = Token.EOF
    LAST=1
    ZERO=2
    STEP=3
    LAYER=4
    ILAYER=5
    NUMBER=6
    DIGIT=7
    OPIDX=8
    OPAR=9
    CPAR=10
    OBRA=11
    CBRA=12
    OCUR=13
    CCUR=14
    MULT=15
    DIV=16
    PLUS=17
    MINUS=18
    POW=19
    SUM=20
    COLON=21
    SEMI=22
    COMMA=23
    N=24
    S=25
    W=26
    E=27
    WE=28
    EW=29
    NS=30
    SN=31
    WS=32

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

        def layer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.LayerContext)
            else:
                return self.getTypedRuleContext(seqParser.LayerContext,i)


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
            self.state = 20
            self.match(seqParser.OCUR)
            self.state = 21
            self.gen()
            self.state = 22
            self.match(seqParser.CCUR)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.layer()
                self.state = 24
                self.match(seqParser.SEMI)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.LAST) | (1 << seqParser.ZERO) | (1 << seqParser.STEP) | (1 << seqParser.LAYER) | (1 << seqParser.ILAYER) | (1 << seqParser.NUMBER) | (1 << seqParser.OPIDX) | (1 << seqParser.OPAR) | (1 << seqParser.OBRA) | (1 << seqParser.MINUS) | (1 << seqParser.SUM) | (1 << seqParser.N) | (1 << seqParser.S) | (1 << seqParser.W) | (1 << seqParser.E) | (1 << seqParser.WE) | (1 << seqParser.EW) | (1 << seqParser.NS) | (1 << seqParser.SN))) != 0)):
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
            self.state = 30
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LayerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def step(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(seqParser.StepContext)
            else:
                return self.getTypedRuleContext(seqParser.StepContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(seqParser.COMMA)
            else:
                return self.getToken(seqParser.COMMA, i)

        def getRuleIndex(self):
            return seqParser.RULE_layer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayer" ):
                listener.enterLayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayer" ):
                listener.exitLayer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLayer" ):
                return visitor.visitLayer(self)
            else:
                return visitor.visitChildren(self)




    def layer(self):

        localctx = seqParser.LayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_layer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.step()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==seqParser.COMMA:
                self.state = 33
                self.match(seqParser.COMMA)
                self.state = 34
                self.step()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 6, self.RULE_step)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.LAST) | (1 << seqParser.ZERO) | (1 << seqParser.STEP) | (1 << seqParser.LAYER) | (1 << seqParser.ILAYER) | (1 << seqParser.NUMBER) | (1 << seqParser.OPIDX) | (1 << seqParser.OPAR) | (1 << seqParser.MINUS) | (1 << seqParser.SUM))) != 0):
                self.state = 40
                self.repet()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==seqParser.OBRA:
                self.state = 43
                self.match(seqParser.OBRA)
                self.state = 44
                self.base()
                self.state = 45
                self.match(seqParser.CBRA)


            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.dirs()
                self.state = 52 
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
        self.enterRule(localctx, 8, self.RULE_dirs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            localctx.dire = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.N) | (1 << seqParser.S) | (1 << seqParser.W) | (1 << seqParser.E) | (1 << seqParser.WE) | (1 << seqParser.EW) | (1 << seqParser.NS) | (1 << seqParser.SN))) != 0)):
                localctx.dire = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==seqParser.COLON:
                self.state = 55
                self.match(seqParser.COLON)
                self.state = 56
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
        self.enterRule(localctx, 10, self.RULE_repet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
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
        self.enterRule(localctx, 12, self.RULE_offset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
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
        self.enterRule(localctx, 14, self.RULE_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
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


    class SumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a seqParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUM(self):
            return self.getToken(seqParser.SUM, 0)
        def expr(self):
            return self.getTypedRuleContext(seqParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumExpr" ):
                listener.enterSumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumExpr" ):
                listener.exitSumExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumExpr" ):
                return visitor.visitSumExpr(self)
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [seqParser.MINUS]:
                localctx = seqParser.MinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 66
                self.match(seqParser.MINUS)
                self.state = 67
                self.expr(6)
                pass
            elif token in [seqParser.SUM]:
                localctx = seqParser.SumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(seqParser.SUM)
                self.state = 69
                self.expr(5)
                pass
            elif token in [seqParser.LAST, seqParser.ZERO, seqParser.STEP, seqParser.LAYER, seqParser.ILAYER, seqParser.NUMBER, seqParser.OPAR]:
                localctx = seqParser.AtoExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.atom()
                pass
            elif token in [seqParser.OPIDX]:
                localctx = seqParser.AtoIdxContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(seqParser.OPIDX)
                self.state = 72
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = seqParser.PowExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 76
                        self.match(seqParser.POW)
                        self.state = 77
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = seqParser.MulExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.MULT or _la==seqParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = seqParser.AddExprContext(self, seqParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==seqParser.PLUS or _la==seqParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        self.expr(4)
                        pass

             
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        def LAYER(self):
            return self.getToken(seqParser.LAYER, 0)
        def ILAYER(self):
            return self.getToken(seqParser.ILAYER, 0)

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
        self.enterRule(localctx, 18, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [seqParser.OPAR]:
                localctx = seqParser.ParExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(seqParser.OPAR)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(seqParser.CPAR)
                pass
            elif token in [seqParser.NUMBER]:
                localctx = seqParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(seqParser.NUMBER)
                pass
            elif token in [seqParser.LAST, seqParser.ZERO, seqParser.STEP, seqParser.LAYER, seqParser.ILAYER]:
                localctx = seqParser.ElemAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                localctx.elem = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << seqParser.LAST) | (1 << seqParser.ZERO) | (1 << seqParser.STEP) | (1 << seqParser.LAYER) | (1 << seqParser.ILAYER))) != 0)):
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
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




