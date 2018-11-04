# Generated from Quark.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from collections import namedtuple
from arithmetic_cube import check_operation_type
import pprint
pp = pprint.PrettyPrinter(indent=4)


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2+")
        buf.write("\u00f5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\7%\u00ca\n%\f%\16%\u00cd\13%\3&\3&\7&\u00d1\n")
        buf.write("&\f&\16&\u00d4\13&\3\'\6\'\u00d7\n\'\r\'\16\'\u00d8\3")
        buf.write("(\6(\u00dc\n(\r(\16(\u00dd\3(\3(\6(\u00e2\n(\r(\16(\u00e3")
        buf.write("\3)\3)\7)\u00e8\n)\f)\16)\u00eb\13)\3)\3)\3*\6*\u00f0")
        buf.write("\n*\r*\16*\u00f1\3*\3*\3\u00e9\2+\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+\3\2\t\3\2c|\6\2")
        buf.write("\62;C\\aac|\3\2C\\\3\2\62;\3\2\60\60\3\2$$\5\2\13\f\16")
        buf.write("\17\"\"\2\u00fb\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\3U\3\2\2\2\5Y\3\2\2\2\7[\3\2\2\2\t")
        buf.write("]\3\2\2\2\13`\3\2\2\2\rb\3\2\2\2\17d\3\2\2\2\21n\3\2\2")
        buf.write("\2\23p\3\2\2\2\25r\3\2\2\2\27v\3\2\2\2\31x\3\2\2\2\33")
        buf.write("}\3\2\2\2\35\u0083\3\2\2\2\37\u008a\3\2\2\2!\u008e\3\2")
        buf.write("\2\2#\u0092\3\2\2\2%\u0094\3\2\2\2\'\u0096\3\2\2\2)\u009b")
        buf.write("\3\2\2\2+\u009e\3\2\2\2-\u00a0\3\2\2\2/\u00a5\3\2\2\2")
        buf.write("\61\u00ab\3\2\2\2\63\u00ad\3\2\2\2\65\u00af\3\2\2\2\67")
        buf.write("\u00b1\3\2\2\29\u00b4\3\2\2\2;\u00b7\3\2\2\2=\u00ba\3")
        buf.write("\2\2\2?\u00bc\3\2\2\2A\u00be\3\2\2\2C\u00c0\3\2\2\2E\u00c2")
        buf.write("\3\2\2\2G\u00c4\3\2\2\2I\u00c7\3\2\2\2K\u00ce\3\2\2\2")
        buf.write("M\u00d6\3\2\2\2O\u00db\3\2\2\2Q\u00e5\3\2\2\2S\u00ef\3")
        buf.write("\2\2\2UV\7f\2\2VW\7g\2\2WX\7h\2\2X\4\3\2\2\2YZ\7*\2\2")
        buf.write("Z\6\3\2\2\2[\\\7+\2\2\\\b\3\2\2\2]^\7/\2\2^_\7@\2\2_\n")
        buf.write("\3\2\2\2`a\7}\2\2a\f\3\2\2\2bc\7\177\2\2c\16\3\2\2\2d")
        buf.write("e\7f\2\2ef\7g\2\2fg\7h\2\2gh\7c\2\2hi\7w\2\2ij\7n\2\2")
        buf.write("jk\7v\2\2kl\7\"\2\2lm\7}\2\2m\20\3\2\2\2no\7<\2\2o\22")
        buf.write("\3\2\2\2pq\7.\2\2q\24\3\2\2\2rs\7K\2\2st\7p\2\2tu\7v\2")
        buf.write("\2u\26\3\2\2\2vw\7A\2\2w\30\3\2\2\2xy\7D\2\2yz\7q\2\2")
        buf.write("z{\7q\2\2{|\7n\2\2|\32\3\2\2\2}~\7H\2\2~\177\7n\2\2\177")
        buf.write("\u0080\7q\2\2\u0080\u0081\7c\2\2\u0081\u0082\7v\2\2\u0082")
        buf.write("\34\3\2\2\2\u0083\u0084\7U\2\2\u0084\u0085\7v\2\2\u0085")
        buf.write("\u0086\7t\2\2\u0086\u0087\7k\2\2\u0087\u0088\7p\2\2\u0088")
        buf.write("\u0089\7i\2\2\u0089\36\3\2\2\2\u008a\u008b\7p\2\2\u008b")
        buf.write("\u008c\7q\2\2\u008c\u008d\7p\2\2\u008d \3\2\2\2\u008e")
        buf.write("\u008f\7C\2\2\u008f\u0090\7p\2\2\u0090\u0091\7{\2\2\u0091")
        buf.write("\"\3\2\2\2\u0092\u0093\7]\2\2\u0093$\3\2\2\2\u0094\u0095")
        buf.write("\7_\2\2\u0095&\3\2\2\2\u0096\u0097\7v\2\2\u0097\u0098")
        buf.write("\7{\2\2\u0098\u0099\7r\2\2\u0099\u009a\7g\2\2\u009a(\3")
        buf.write("\2\2\2\u009b\u009c\7>\2\2\u009c\u009d\7/\2\2\u009d*\3")
        buf.write("\2\2\2\u009e\u009f\7~\2\2\u009f,\3\2\2\2\u00a0\u00a1\7")
        buf.write("V\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4.\3\2\2\2\u00a5\u00a6\7H\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\60\3\2\2\2\u00ab\u00ac\7@\2\2\u00ac\62\3")
        buf.write("\2\2\2\u00ad\u00ae\7>\2\2\u00ae\64\3\2\2\2\u00af\u00b0")
        buf.write("\7?\2\2\u00b0\66\3\2\2\2\u00b1\u00b2\7@\2\2\u00b2\u00b3")
        buf.write("\7?\2\2\u00b38\3\2\2\2\u00b4\u00b5\7>\2\2\u00b5\u00b6")
        buf.write("\7?\2\2\u00b6:\3\2\2\2\u00b7\u00b8\7#\2\2\u00b8\u00b9")
        buf.write("\7?\2\2\u00b9<\3\2\2\2\u00ba\u00bb\7-\2\2\u00bb>\3\2\2")
        buf.write("\2\u00bc\u00bd\7/\2\2\u00bd@\3\2\2\2\u00be\u00bf\7,\2")
        buf.write("\2\u00bfB\3\2\2\2\u00c0\u00c1\7\61\2\2\u00c1D\3\2\2\2")
        buf.write("\u00c2\u00c3\7\'\2\2\u00c3F\3\2\2\2\u00c4\u00c5\7]\2\2")
        buf.write("\u00c5\u00c6\7_\2\2\u00c6H\3\2\2\2\u00c7\u00cb\t\2\2\2")
        buf.write("\u00c8\u00ca\t\3\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cd\3")
        buf.write("\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00ccJ")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d2\t\4\2\2\u00cf")
        buf.write("\u00d1\t\3\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3L\3\2\2")
        buf.write("\2\u00d4\u00d2\3\2\2\2\u00d5\u00d7\t\5\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9N\3\2\2\2\u00da\u00dc\t\5\2\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\t")
        buf.write("\6\2\2\u00e0\u00e2\t\5\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("P\3\2\2\2\u00e5\u00e9\t\7\2\2\u00e6\u00e8\13\2\2\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e9\3")
        buf.write("\2\2\2\u00ec\u00ed\t\7\2\2\u00edR\3\2\2\2\u00ee\u00f0")
        buf.write("\t\b\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2")
        buf.write("\u00f3\u00f4\b*\2\2\u00f4T\3\2\2\2\n\2\u00cb\u00d2\u00d8")
        buf.write("\u00dd\u00e3\u00e9\u00f1\3\b\2\2")
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
    ID = 36
    TYPE_ID = 37
    CONST_I = 38
    CONST_F = 39
    STRING = 40
    SPACE = 41

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'('", "')'", "'->'", "'{'", "'}'", "'default {'", 
            "':'", "','", "'Int'", "'?'", "'Bool'", "'Float'", "'String'", 
            "'non'", "'Any'", "'['", "']'", "'type'", "'<-'", "'|'", "'True'", 
            "'False'", "'>'", "'<'", "'='", "'>='", "'<='", "'!='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'[]'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "TYPE_ID", "CONST_I", "CONST_F", "STRING", "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "ID", "TYPE_ID", "CONST_I", 
                  "CONST_F", "STRING", "SPACE" ]

    grammarFileName = "Quark.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


