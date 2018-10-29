# Generated from Quark.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from collections import namedtuple


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u00ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\7$\u00c4\n$\f")
        buf.write("$\16$\u00c7\13$\3%\3%\7%\u00cb\n%\f%\16%\u00ce\13%\3&")
        buf.write("\6&\u00d1\n&\r&\16&\u00d2\3\'\6\'\u00d6\n\'\r\'\16\'\u00d7")
        buf.write("\3\'\3\'\6\'\u00dc\n\'\r\'\16\'\u00dd\3(\3(\7(\u00e2\n")
        buf.write("(\f(\16(\u00e5\13(\3(\3(\3)\6)\u00ea\n)\r)\16)\u00eb\3")
        buf.write(")\3)\3\u00e3\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*\3\2\t\3\2c|\6\2\62;C\\aac|\3\2C\\")
        buf.write("\3\2\62;\3\2\60\60\3\2$$\5\2\13\f\16\17\"\"\2\u00f5\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\3S\3\2\2")
        buf.write("\2\5W\3\2\2\2\7Y\3\2\2\2\t[\3\2\2\2\13^\3\2\2\2\r`\3\2")
        buf.write("\2\2\17b\3\2\2\2\21l\3\2\2\2\23n\3\2\2\2\25p\3\2\2\2\27")
        buf.write("t\3\2\2\2\31v\3\2\2\2\33{\3\2\2\2\35\u0081\3\2\2\2\37")
        buf.write("\u0088\3\2\2\2!\u008c\3\2\2\2#\u008e\3\2\2\2%\u0090\3")
        buf.write("\2\2\2\'\u0095\3\2\2\2)\u0098\3\2\2\2+\u009a\3\2\2\2-")
        buf.write("\u009f\3\2\2\2/\u00a5\3\2\2\2\61\u00a7\3\2\2\2\63\u00a9")
        buf.write("\3\2\2\2\65\u00ab\3\2\2\2\67\u00ae\3\2\2\29\u00b1\3\2")
        buf.write("\2\2;\u00b4\3\2\2\2=\u00b6\3\2\2\2?\u00b8\3\2\2\2A\u00ba")
        buf.write("\3\2\2\2C\u00bc\3\2\2\2E\u00be\3\2\2\2G\u00c1\3\2\2\2")
        buf.write("I\u00c8\3\2\2\2K\u00d0\3\2\2\2M\u00d5\3\2\2\2O\u00df\3")
        buf.write("\2\2\2Q\u00e9\3\2\2\2ST\7f\2\2TU\7g\2\2UV\7h\2\2V\4\3")
        buf.write("\2\2\2WX\7*\2\2X\6\3\2\2\2YZ\7+\2\2Z\b\3\2\2\2[\\\7/\2")
        buf.write("\2\\]\7@\2\2]\n\3\2\2\2^_\7}\2\2_\f\3\2\2\2`a\7\177\2")
        buf.write("\2a\16\3\2\2\2bc\7f\2\2cd\7g\2\2de\7h\2\2ef\7c\2\2fg\7")
        buf.write("w\2\2gh\7n\2\2hi\7v\2\2ij\7\"\2\2jk\7}\2\2k\20\3\2\2\2")
        buf.write("lm\7<\2\2m\22\3\2\2\2no\7.\2\2o\24\3\2\2\2pq\7K\2\2qr")
        buf.write("\7p\2\2rs\7v\2\2s\26\3\2\2\2tu\7A\2\2u\30\3\2\2\2vw\7")
        buf.write("D\2\2wx\7q\2\2xy\7q\2\2yz\7n\2\2z\32\3\2\2\2{|\7H\2\2")
        buf.write("|}\7n\2\2}~\7q\2\2~\177\7c\2\2\177\u0080\7v\2\2\u0080")
        buf.write("\34\3\2\2\2\u0081\u0082\7U\2\2\u0082\u0083\7v\2\2\u0083")
        buf.write("\u0084\7t\2\2\u0084\u0085\7k\2\2\u0085\u0086\7p\2\2\u0086")
        buf.write("\u0087\7i\2\2\u0087\36\3\2\2\2\u0088\u0089\7p\2\2\u0089")
        buf.write("\u008a\7q\2\2\u008a\u008b\7p\2\2\u008b \3\2\2\2\u008c")
        buf.write("\u008d\7]\2\2\u008d\"\3\2\2\2\u008e\u008f\7_\2\2\u008f")
        buf.write("$\3\2\2\2\u0090\u0091\7v\2\2\u0091\u0092\7{\2\2\u0092")
        buf.write("\u0093\7r\2\2\u0093\u0094\7g\2\2\u0094&\3\2\2\2\u0095")
        buf.write("\u0096\7>\2\2\u0096\u0097\7/\2\2\u0097(\3\2\2\2\u0098")
        buf.write("\u0099\7~\2\2\u0099*\3\2\2\2\u009a\u009b\7V\2\2\u009b")
        buf.write("\u009c\7t\2\2\u009c\u009d\7w\2\2\u009d\u009e\7g\2\2\u009e")
        buf.write(",\3\2\2\2\u009f\u00a0\7H\2\2\u00a0\u00a1\7c\2\2\u00a1")
        buf.write("\u00a2\7n\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4")
        buf.write(".\3\2\2\2\u00a5\u00a6\7@\2\2\u00a6\60\3\2\2\2\u00a7\u00a8")
        buf.write("\7>\2\2\u00a8\62\3\2\2\2\u00a9\u00aa\7?\2\2\u00aa\64\3")
        buf.write("\2\2\2\u00ab\u00ac\7@\2\2\u00ac\u00ad\7?\2\2\u00ad\66")
        buf.write("\3\2\2\2\u00ae\u00af\7>\2\2\u00af\u00b0\7?\2\2\u00b08")
        buf.write("\3\2\2\2\u00b1\u00b2\7#\2\2\u00b2\u00b3\7?\2\2\u00b3:")
        buf.write("\3\2\2\2\u00b4\u00b5\7-\2\2\u00b5<\3\2\2\2\u00b6\u00b7")
        buf.write("\7/\2\2\u00b7>\3\2\2\2\u00b8\u00b9\7,\2\2\u00b9@\3\2\2")
        buf.write("\2\u00ba\u00bb\7\61\2\2\u00bbB\3\2\2\2\u00bc\u00bd\7\'")
        buf.write("\2\2\u00bdD\3\2\2\2\u00be\u00bf\7]\2\2\u00bf\u00c0\7_")
        buf.write("\2\2\u00c0F\3\2\2\2\u00c1\u00c5\t\2\2\2\u00c2\u00c4\t")
        buf.write("\3\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6H\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c8\u00cc\t\4\2\2\u00c9\u00cb\t\3\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cdJ\3\2\2\2\u00ce\u00cc\3\2\2")
        buf.write("\2\u00cf\u00d1\t\5\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("L\3\2\2\2\u00d4\u00d6\t\5\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9\u00db\t\6\2\2\u00da\u00dc\t")
        buf.write("\5\2\2\u00db\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00deN\3\2\2\2\u00df\u00e3")
        buf.write("\t\7\2\2\u00e0\u00e2\13\2\2\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e5\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2")
        buf.write("\u00e4\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7\t")
        buf.write("\7\2\2\u00e7P\3\2\2\2\u00e8\u00ea\t\b\2\2\u00e9\u00e8")
        buf.write("\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\b)\2\2")
        buf.write("\u00eeR\3\2\2\2\n\2\u00c5\u00cc\u00d2\u00d7\u00dd\u00e3")
        buf.write("\u00eb\3\b\2\2")
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
    ID = 35
    TYPE_ID = 36
    CONST_I = 37
    CONST_F = 38
    STRING = 39
    SPACE = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'('", "')'", "'->'", "'{'", "'}'", "'default {'", 
            "':'", "','", "'Int'", "'?'", "'Bool'", "'Float'", "'String'", 
            "'non'", "'['", "']'", "'type'", "'<-'", "'|'", "'True'", "'False'", 
            "'>'", "'<'", "'='", "'>='", "'<='", "'!='", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'[]'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "TYPE_ID", "CONST_I", "CONST_F", "STRING", "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "ID", "TYPE_ID", "CONST_I", "CONST_F", 
                  "STRING", "SPACE" ]

    grammarFileName = "Quark.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


