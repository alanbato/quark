# Generated from Quark.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from compiler import Compiler
c = Compiler()
quadruples = None
func_directory = None
type_directory = None
constants = None


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2-")
        buf.write("\u00fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\7\'\u00d3\n\'\f\'\16\'\u00d6")
        buf.write("\13\'\3(\3(\7(\u00da\n(\f(\16(\u00dd\13(\3)\6)\u00e0\n")
        buf.write(")\r)\16)\u00e1\3*\6*\u00e5\n*\r*\16*\u00e6\3*\3*\6*\u00eb")
        buf.write("\n*\r*\16*\u00ec\3+\3+\7+\u00f1\n+\f+\16+\u00f4\13+\3")
        buf.write("+\3+\3,\6,\u00f9\n,\r,\16,\u00fa\3,\3,\3\u00f2\2-\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-\3\2\t\3\2c|\6\2\62;C\\aac|\3\2C\\\3\2\62;\3\2\60")
        buf.write("\60\3\2$$\5\2\13\f\16\17\"\"\2\u0104\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\3Y\3\2\2\2\5]\3\2\2\2\7_\3\2\2\2\ta\3\2\2\2\13")
        buf.write("d\3\2\2\2\rf\3\2\2\2\17h\3\2\2\2\21r\3\2\2\2\23t\3\2\2")
        buf.write("\2\25v\3\2\2\2\27z\3\2\2\2\31|\3\2\2\2\33\u0081\3\2\2")
        buf.write("\2\35\u0087\3\2\2\2\37\u008e\3\2\2\2!\u0092\3\2\2\2#\u0096")
        buf.write("\3\2\2\2%\u0098\3\2\2\2\'\u009a\3\2\2\2)\u009f\3\2\2\2")
        buf.write("+\u00a2\3\2\2\2-\u00a4\3\2\2\2/\u00a6\3\2\2\2\61\u00a8")
        buf.write("\3\2\2\2\63\u00aa\3\2\2\2\65\u00ad\3\2\2\2\67\u00b0\3")
        buf.write("\2\2\29\u00b3\3\2\2\2;\u00b5\3\2\2\2=\u00b7\3\2\2\2?\u00b9")
        buf.write("\3\2\2\2A\u00bb\3\2\2\2C\u00bd\3\2\2\2E\u00c0\3\2\2\2")
        buf.write("G\u00c5\3\2\2\2I\u00cb\3\2\2\2K\u00ce\3\2\2\2M\u00d0\3")
        buf.write("\2\2\2O\u00d7\3\2\2\2Q\u00df\3\2\2\2S\u00e4\3\2\2\2U\u00ee")
        buf.write("\3\2\2\2W\u00f8\3\2\2\2YZ\7f\2\2Z[\7g\2\2[\\\7h\2\2\\")
        buf.write("\4\3\2\2\2]^\7*\2\2^\6\3\2\2\2_`\7+\2\2`\b\3\2\2\2ab\7")
        buf.write("/\2\2bc\7@\2\2c\n\3\2\2\2de\7}\2\2e\f\3\2\2\2fg\7\177")
        buf.write("\2\2g\16\3\2\2\2hi\7f\2\2ij\7g\2\2jk\7h\2\2kl\7c\2\2l")
        buf.write("m\7w\2\2mn\7n\2\2no\7v\2\2op\7\"\2\2pq\7}\2\2q\20\3\2")
        buf.write("\2\2rs\7<\2\2s\22\3\2\2\2tu\7.\2\2u\24\3\2\2\2vw\7K\2")
        buf.write("\2wx\7p\2\2xy\7v\2\2y\26\3\2\2\2z{\7A\2\2{\30\3\2\2\2")
        buf.write("|}\7D\2\2}~\7q\2\2~\177\7q\2\2\177\u0080\7n\2\2\u0080")
        buf.write("\32\3\2\2\2\u0081\u0082\7H\2\2\u0082\u0083\7n\2\2\u0083")
        buf.write("\u0084\7q\2\2\u0084\u0085\7c\2\2\u0085\u0086\7v\2\2\u0086")
        buf.write("\34\3\2\2\2\u0087\u0088\7U\2\2\u0088\u0089\7v\2\2\u0089")
        buf.write("\u008a\7t\2\2\u008a\u008b\7k\2\2\u008b\u008c\7p\2\2\u008c")
        buf.write("\u008d\7i\2\2\u008d\36\3\2\2\2\u008e\u008f\7p\2\2\u008f")
        buf.write("\u0090\7q\2\2\u0090\u0091\7p\2\2\u0091 \3\2\2\2\u0092")
        buf.write("\u0093\7C\2\2\u0093\u0094\7p\2\2\u0094\u0095\7{\2\2\u0095")
        buf.write("\"\3\2\2\2\u0096\u0097\7]\2\2\u0097$\3\2\2\2\u0098\u0099")
        buf.write("\7_\2\2\u0099&\3\2\2\2\u009a\u009b\7v\2\2\u009b\u009c")
        buf.write("\7{\2\2\u009c\u009d\7r\2\2\u009d\u009e\7g\2\2\u009e(\3")
        buf.write("\2\2\2\u009f\u00a0\7>\2\2\u00a0\u00a1\7/\2\2\u00a1*\3")
        buf.write("\2\2\2\u00a2\u00a3\7~\2\2\u00a3,\3\2\2\2\u00a4\u00a5\7")
        buf.write("@\2\2\u00a5.\3\2\2\2\u00a6\u00a7\7>\2\2\u00a7\60\3\2\2")
        buf.write("\2\u00a8\u00a9\7?\2\2\u00a9\62\3\2\2\2\u00aa\u00ab\7@")
        buf.write("\2\2\u00ab\u00ac\7?\2\2\u00ac\64\3\2\2\2\u00ad\u00ae\7")
        buf.write(">\2\2\u00ae\u00af\7?\2\2\u00af\66\3\2\2\2\u00b0\u00b1")
        buf.write("\7#\2\2\u00b1\u00b2\7?\2\2\u00b28\3\2\2\2\u00b3\u00b4")
        buf.write("\7-\2\2\u00b4:\3\2\2\2\u00b5\u00b6\7/\2\2\u00b6<\3\2\2")
        buf.write("\2\u00b7\u00b8\7,\2\2\u00b8>\3\2\2\2\u00b9\u00ba\7\61")
        buf.write("\2\2\u00ba@\3\2\2\2\u00bb\u00bc\7\'\2\2\u00bcB\3\2\2\2")
        buf.write("\u00bd\u00be\7*\2\2\u00be\u00bf\7/\2\2\u00bfD\3\2\2\2")
        buf.write("\u00c0\u00c1\7V\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7w")
        buf.write("\2\2\u00c3\u00c4\7g\2\2\u00c4F\3\2\2\2\u00c5\u00c6\7H")
        buf.write("\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9")
        buf.write("\7u\2\2\u00c9\u00ca\7g\2\2\u00caH\3\2\2\2\u00cb\u00cc")
        buf.write("\7]\2\2\u00cc\u00cd\7_\2\2\u00cdJ\3\2\2\2\u00ce\u00cf")
        buf.write("\7=\2\2\u00cfL\3\2\2\2\u00d0\u00d4\t\2\2\2\u00d1\u00d3")
        buf.write("\t\3\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5N\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d7\u00db\t\4\2\2\u00d8\u00da\t\3\2\2")
        buf.write("\u00d9\u00d8\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00db\u00dc\3\2\2\2\u00dcP\3\2\2\2\u00dd\u00db")
        buf.write("\3\2\2\2\u00de\u00e0\t\5\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2")
        buf.write("\u00e2R\3\2\2\2\u00e3\u00e5\t\5\2\2\u00e4\u00e3\3\2\2")
        buf.write("\2\u00e5\u00e6\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\t\6\2\2\u00e9")
        buf.write("\u00eb\t\5\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00edT\3\2\2")
        buf.write("\2\u00ee\u00f2\t\7\2\2\u00ef\u00f1\13\2\2\2\u00f0\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f5\u00f6\t\7\2\2\u00f6V\3\2\2\2\u00f7\u00f9\t\b\2")
        buf.write("\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fd\b,\2\2\u00fdX\3\2\2\2\n\2\u00d4\u00db\u00e1\u00e6")
        buf.write("\u00ec\u00f2\u00fa\3\b\2\2")
        return buf.getvalue()


class QuarkLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    ID = 38
    TYPE_ID = 39
    CONST_I = 40
    CONST_F = 41
    STRING = 42
    SPACE = 43

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'('", "')'", "'->'", "'{'", "'}'", "'default {'", 
            "':'", "','", "'Int'", "'?'", "'Bool'", "'Float'", "'String'", 
            "'non'", "'Any'", "'['", "']'", "'type'", "'<-'", "'|'", "'>'", 
            "'<'", "'='", "'>='", "'<='", "'!='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'(-'", "'True'", "'False'", "'[]'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "TYPE_ID", "CONST_I", "CONST_F", "STRING", "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "ID", "TYPE_ID", 
                  "CONST_I", "CONST_F", "STRING", "SPACE" ]

    grammarFileName = "Quark.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


