# Generated from Quark.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from Compiler import Compiler
c = Compiler()
quadruples = None
func_directory = None
type_directory = None
constants = None


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,")
        buf.write("\u00f9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3&\3&\7&\u00ce\n&\f&\16&\u00d1\13&\3\'\3\'\7\'")
        buf.write("\u00d5\n\'\f\'\16\'\u00d8\13\'\3(\6(\u00db\n(\r(\16(\u00dc")
        buf.write("\3)\6)\u00e0\n)\r)\16)\u00e1\3)\3)\6)\u00e6\n)\r)\16)")
        buf.write("\u00e7\3*\3*\7*\u00ec\n*\f*\16*\u00ef\13*\3*\3*\3+\6+")
        buf.write("\u00f4\n+\r+\16+\u00f5\3+\3+\3\u00ed\2,\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,\3\2\t\3")
        buf.write("\2c|\6\2\62;C\\aac|\3\2C\\\3\2\62;\3\2\60\60\3\2$$\5\2")
        buf.write("\13\f\16\17\"\"\2\u00ff\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\3W\3\2\2\2\5[\3")
        buf.write("\2\2\2\7]\3\2\2\2\t_\3\2\2\2\13b\3\2\2\2\rd\3\2\2\2\17")
        buf.write("f\3\2\2\2\21p\3\2\2\2\23r\3\2\2\2\25t\3\2\2\2\27x\3\2")
        buf.write("\2\2\31z\3\2\2\2\33\177\3\2\2\2\35\u0085\3\2\2\2\37\u008c")
        buf.write("\3\2\2\2!\u0090\3\2\2\2#\u0094\3\2\2\2%\u0096\3\2\2\2")
        buf.write("\'\u0098\3\2\2\2)\u009d\3\2\2\2+\u00a0\3\2\2\2-\u00a2")
        buf.write("\3\2\2\2/\u00a4\3\2\2\2\61\u00a6\3\2\2\2\63\u00a8\3\2")
        buf.write("\2\2\65\u00ab\3\2\2\2\67\u00ae\3\2\2\29\u00b1\3\2\2\2")
        buf.write(";\u00b3\3\2\2\2=\u00b5\3\2\2\2?\u00b7\3\2\2\2A\u00b9\3")
        buf.write("\2\2\2C\u00bb\3\2\2\2E\u00be\3\2\2\2G\u00c3\3\2\2\2I\u00c9")
        buf.write("\3\2\2\2K\u00cb\3\2\2\2M\u00d2\3\2\2\2O\u00da\3\2\2\2")
        buf.write("Q\u00df\3\2\2\2S\u00e9\3\2\2\2U\u00f3\3\2\2\2WX\7f\2\2")
        buf.write("XY\7g\2\2YZ\7h\2\2Z\4\3\2\2\2[\\\7*\2\2\\\6\3\2\2\2]^")
        buf.write("\7+\2\2^\b\3\2\2\2_`\7/\2\2`a\7@\2\2a\n\3\2\2\2bc\7}\2")
        buf.write("\2c\f\3\2\2\2de\7\177\2\2e\16\3\2\2\2fg\7f\2\2gh\7g\2")
        buf.write("\2hi\7h\2\2ij\7c\2\2jk\7w\2\2kl\7n\2\2lm\7v\2\2mn\7\"")
        buf.write("\2\2no\7}\2\2o\20\3\2\2\2pq\7<\2\2q\22\3\2\2\2rs\7.\2")
        buf.write("\2s\24\3\2\2\2tu\7K\2\2uv\7p\2\2vw\7v\2\2w\26\3\2\2\2")
        buf.write("xy\7A\2\2y\30\3\2\2\2z{\7D\2\2{|\7q\2\2|}\7q\2\2}~\7n")
        buf.write("\2\2~\32\3\2\2\2\177\u0080\7H\2\2\u0080\u0081\7n\2\2\u0081")
        buf.write("\u0082\7q\2\2\u0082\u0083\7c\2\2\u0083\u0084\7v\2\2\u0084")
        buf.write("\34\3\2\2\2\u0085\u0086\7U\2\2\u0086\u0087\7v\2\2\u0087")
        buf.write("\u0088\7t\2\2\u0088\u0089\7k\2\2\u0089\u008a\7p\2\2\u008a")
        buf.write("\u008b\7i\2\2\u008b\36\3\2\2\2\u008c\u008d\7p\2\2\u008d")
        buf.write("\u008e\7q\2\2\u008e\u008f\7p\2\2\u008f \3\2\2\2\u0090")
        buf.write("\u0091\7C\2\2\u0091\u0092\7p\2\2\u0092\u0093\7{\2\2\u0093")
        buf.write("\"\3\2\2\2\u0094\u0095\7]\2\2\u0095$\3\2\2\2\u0096\u0097")
        buf.write("\7_\2\2\u0097&\3\2\2\2\u0098\u0099\7v\2\2\u0099\u009a")
        buf.write("\7{\2\2\u009a\u009b\7r\2\2\u009b\u009c\7g\2\2\u009c(\3")
        buf.write("\2\2\2\u009d\u009e\7>\2\2\u009e\u009f\7/\2\2\u009f*\3")
        buf.write("\2\2\2\u00a0\u00a1\7~\2\2\u00a1,\3\2\2\2\u00a2\u00a3\7")
        buf.write("@\2\2\u00a3.\3\2\2\2\u00a4\u00a5\7>\2\2\u00a5\60\3\2\2")
        buf.write("\2\u00a6\u00a7\7?\2\2\u00a7\62\3\2\2\2\u00a8\u00a9\7@")
        buf.write("\2\2\u00a9\u00aa\7?\2\2\u00aa\64\3\2\2\2\u00ab\u00ac\7")
        buf.write(">\2\2\u00ac\u00ad\7?\2\2\u00ad\66\3\2\2\2\u00ae\u00af")
        buf.write("\7#\2\2\u00af\u00b0\7?\2\2\u00b08\3\2\2\2\u00b1\u00b2")
        buf.write("\7-\2\2\u00b2:\3\2\2\2\u00b3\u00b4\7/\2\2\u00b4<\3\2\2")
        buf.write("\2\u00b5\u00b6\7,\2\2\u00b6>\3\2\2\2\u00b7\u00b8\7\61")
        buf.write("\2\2\u00b8@\3\2\2\2\u00b9\u00ba\7\'\2\2\u00baB\3\2\2\2")
        buf.write("\u00bb\u00bc\7*\2\2\u00bc\u00bd\7/\2\2\u00bdD\3\2\2\2")
        buf.write("\u00be\u00bf\7V\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7w")
        buf.write("\2\2\u00c1\u00c2\7g\2\2\u00c2F\3\2\2\2\u00c3\u00c4\7H")
        buf.write("\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7u\2\2\u00c7\u00c8\7g\2\2\u00c8H\3\2\2\2\u00c9\u00ca")
        buf.write("\7=\2\2\u00caJ\3\2\2\2\u00cb\u00cf\t\2\2\2\u00cc\u00ce")
        buf.write("\t\3\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0L\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d6\t\4\2\2\u00d3\u00d5\t\3\2\2")
        buf.write("\u00d4\u00d3\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d6\u00d7\3\2\2\2\u00d7N\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d9\u00db\t\5\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00ddP\3\2\2\2\u00de\u00e0\t\5\2\2\u00df\u00de\3\2\2")
        buf.write("\2\u00e0\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\t\6\2\2\u00e4")
        buf.write("\u00e6\t\5\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8R\3\2\2")
        buf.write("\2\u00e9\u00ed\t\7\2\2\u00ea\u00ec\13\2\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00f0\u00f1\t\7\2\2\u00f1T\3\2\2\2\u00f2\u00f4\t\b\2")
        buf.write("\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u00f8\b+\2\2\u00f8V\3\2\2\2\n\2\u00cf\u00d6\u00dc\u00e1")
        buf.write("\u00e7\u00ed\u00f5\3\b\2\2")
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
    ID = 37
    TYPE_ID = 38
    CONST_I = 39
    CONST_F = 40
    STRING = 41
    SPACE = 42

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'('", "')'", "'->'", "'{'", "'}'", "'default {'", 
            "':'", "','", "'Int'", "'?'", "'Bool'", "'Float'", "'String'", 
            "'non'", "'Any'", "'['", "']'", "'type'", "'<-'", "'|'", "'>'", 
            "'<'", "'='", "'>='", "'<='", "'!='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'(-'", "'True'", "'False'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "TYPE_ID", "CONST_I", "CONST_F", "STRING", "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "ID", "TYPE_ID", "CONST_I", 
                  "CONST_F", "STRING", "SPACE" ]

    grammarFileName = "Quark.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


