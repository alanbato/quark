# Generated from Quark.g4 by ANTLR 4.7.1
# encoding: utf-8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("\u0127\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\7\2B\n\2\f\2\16\2E\13\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4Z\n\4\3\5\3\5\3\5\5\5_\n\5\3\6\3\6\3\6\3\6\5\6")
        buf.write("e\n\6\3\6\3\6\5\6i\n\6\3\6\3\6\5\6m\n\6\3\6\3\6\5\6q\n")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6z\n\6\3\7\3\7\5\7~\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u008a\n")
        buf.write("\t\f\t\16\t\u008d\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u009f\n")
        buf.write("\13\3\13\3\13\3\13\3\13\7\13\u00a5\n\13\f\13\16\13\u00a8")
        buf.write("\13\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00b8\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\5\16\u00c5\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00d7\n\17\3\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00de\n\20\3\21\5\21\u00e1\n\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00f3\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00fb\n\22\3\23\3\23\7\23\u00ff\n\23\f\23\16\23\u0102")
        buf.write("\13\23\3\24\3\24\5\24\u0106\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u011f\n")
        buf.write("\30\3\31\3\31\3\31\3\31\5\31\u0125\n\31\3\31\2\3\24\32")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2")
        buf.write("\3\4\2\30\31&&\2\u013d\2\62\3\2\2\2\4L\3\2\2\2\6Y\3\2")
        buf.write("\2\2\b^\3\2\2\2\ny\3\2\2\2\f}\3\2\2\2\16\177\3\2\2\2\20")
        buf.write("\u0085\3\2\2\2\22\u0091\3\2\2\2\24\u009e\3\2\2\2\26\u00a9")
        buf.write("\3\2\2\2\30\u00b7\3\2\2\2\32\u00c4\3\2\2\2\34\u00d6\3")
        buf.write("\2\2\2\36\u00dd\3\2\2\2 \u00f2\3\2\2\2\"\u00fa\3\2\2\2")
        buf.write("$\u00fc\3\2\2\2&\u0105\3\2\2\2(\u0107\3\2\2\2*\u010e\3")
        buf.write("\2\2\2,\u0114\3\2\2\2.\u011e\3\2\2\2\60\u0124\3\2\2\2")
        buf.write("\62\63\7\3\2\2\63\64\7&\2\2\64\65\b\2\1\2\65\66\7\4\2")
        buf.write("\2\66\67\5\4\3\2\678\7\5\2\289\7\6\2\29:\5\n\6\2:;\b\2")
        buf.write("\1\2;C\7\7\2\2<=\5\22\n\2=>\7\7\2\2>?\5$\23\2?@\7\b\2")
        buf.write("\2@B\3\2\2\2A<\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D")
        buf.write("F\3\2\2\2EC\3\2\2\2FG\7\t\2\2GH\5$\23\2HI\7\b\2\2IJ\7")
        buf.write("\b\2\2JK\b\2\1\2K\3\3\2\2\2LM\7&\2\2MN\7\n\2\2NO\5\n\6")
        buf.write("\2OP\b\3\1\2PQ\5\6\4\2Q\5\3\2\2\2RS\7\13\2\2ST\7&\2\2")
        buf.write("TU\7\n\2\2UV\5\n\6\2VW\b\4\1\2WZ\3\2\2\2XZ\3\2\2\2YR\3")
        buf.write("\2\2\2YX\3\2\2\2Z\7\3\2\2\2[\\\7\13\2\2\\_\5\n\6\2]_\3")
        buf.write("\2\2\2^[\3\2\2\2^]\3\2\2\2_\t\3\2\2\2`a\7\'\2\2az\b\6")
        buf.write("\1\2bd\7\f\2\2ce\7\r\2\2dc\3\2\2\2de\3\2\2\2ez\3\2\2\2")
        buf.write("fh\7\16\2\2gi\7\r\2\2hg\3\2\2\2hi\3\2\2\2iz\3\2\2\2jl")
        buf.write("\7\17\2\2km\7\r\2\2lk\3\2\2\2lm\3\2\2\2mz\3\2\2\2np\7")
        buf.write("\20\2\2oq\7\r\2\2po\3\2\2\2pq\3\2\2\2qz\3\2\2\2rz\7\21")
        buf.write("\2\2sz\7\22\2\2tu\7\23\2\2uv\5\n\6\2vw\5\b\5\2wx\7\24")
        buf.write("\2\2xz\3\2\2\2y`\3\2\2\2yb\3\2\2\2yf\3\2\2\2yj\3\2\2\2")
        buf.write("yn\3\2\2\2yr\3\2\2\2ys\3\2\2\2yt\3\2\2\2z\13\3\2\2\2{")
        buf.write("~\5\n\6\2|~\5\20\t\2}{\3\2\2\2}|\3\2\2\2~\r\3\2\2\2\177")
        buf.write("\u0080\7\25\2\2\u0080\u0081\7\'\2\2\u0081\u0082\7\26\2")
        buf.write("\2\u0082\u0083\5\f\7\2\u0083\u0084\b\b\1\2\u0084\17\3")
        buf.write("\2\2\2\u0085\u0086\7\4\2\2\u0086\u008b\5\n\6\2\u0087\u0088")
        buf.write("\7\27\2\2\u0088\u008a\5\n\6\2\u0089\u0087\3\2\2\2\u008a")
        buf.write("\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\7")
        buf.write("\5\2\2\u008f\u0090\b\t\1\2\u0090\21\3\2\2\2\u0091\u0092")
        buf.write("\7\4\2\2\u0092\u0093\5\24\13\2\u0093\u0094\5\36\20\2\u0094")
        buf.write("\u0095\7\5\2\2\u0095\23\3\2\2\2\u0096\u0097\b\13\1\2\u0097")
        buf.write("\u009f\5(\25\2\u0098\u009f\5\26\f\2\u0099\u009a\5\32\16")
        buf.write("\2\u009a\u009b\5\24\13\6\u009b\u009f\3\2\2\2\u009c\u009f")
        buf.write("\5\32\16\2\u009d\u009f\7\21\2\2\u009e\u0096\3\2\2\2\u009e")
        buf.write("\u0098\3\2\2\2\u009e\u0099\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009d\3\2\2\2\u009f\u00a6\3\2\2\2\u00a0\u00a1\f")
        buf.write("\4\2\2\u00a1\u00a2\5\30\r\2\u00a2\u00a3\5\24\13\5\u00a3")
        buf.write("\u00a5\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a5\u00a8\3\2\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\25\3\2")
        buf.write("\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa\t\2\2\2\u00aa\27")
        buf.write("\3\2\2\2\u00ab\u00ac\7\32\2\2\u00ac\u00b8\b\r\1\2\u00ad")
        buf.write("\u00ae\7\33\2\2\u00ae\u00b8\b\r\1\2\u00af\u00b0\7\34\2")
        buf.write("\2\u00b0\u00b8\b\r\1\2\u00b1\u00b2\7\35\2\2\u00b2\u00b8")
        buf.write("\b\r\1\2\u00b3\u00b4\7\36\2\2\u00b4\u00b8\b\r\1\2\u00b5")
        buf.write("\u00b6\7\37\2\2\u00b6\u00b8\b\r\1\2\u00b7\u00ab\3\2\2")
        buf.write("\2\u00b7\u00ad\3\2\2\2\u00b7\u00af\3\2\2\2\u00b7\u00b1")
        buf.write("\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write("\31\3\2\2\2\u00b9\u00c5\5\34\17\2\u00ba\u00bb\7 \2\2\u00bb")
        buf.write("\u00bc\b\16\1\2\u00bc\u00bd\5\34\17\2\u00bd\u00be\b\16")
        buf.write("\1\2\u00be\u00c5\3\2\2\2\u00bf\u00c0\7!\2\2\u00c0\u00c1")
        buf.write("\b\16\1\2\u00c1\u00c2\5\34\17\2\u00c2\u00c3\b\16\1\2\u00c3")
        buf.write("\u00c5\3\2\2\2\u00c4\u00b9\3\2\2\2\u00c4\u00ba\3\2\2\2")
        buf.write("\u00c4\u00bf\3\2\2\2\u00c5\33\3\2\2\2\u00c6\u00d7\5 \21")
        buf.write("\2\u00c7\u00c8\7\"\2\2\u00c8\u00c9\b\17\1\2\u00c9\u00ca")
        buf.write("\5 \21\2\u00ca\u00cb\b\17\1\2\u00cb\u00d7\3\2\2\2\u00cc")
        buf.write("\u00cd\7#\2\2\u00cd\u00ce\b\17\1\2\u00ce\u00cf\5 \21\2")
        buf.write("\u00cf\u00d0\b\17\1\2\u00d0\u00d7\3\2\2\2\u00d1\u00d2")
        buf.write("\7$\2\2\u00d2\u00d3\b\17\1\2\u00d3\u00d4\5 \21\2\u00d4")
        buf.write("\u00d5\b\17\1\2\u00d5\u00d7\3\2\2\2\u00d6\u00c6\3\2\2")
        buf.write("\2\u00d6\u00c7\3\2\2\2\u00d6\u00cc\3\2\2\2\u00d6\u00d1")
        buf.write("\3\2\2\2\u00d7\35\3\2\2\2\u00d8\u00d9\7\13\2\2\u00d9\u00da")
        buf.write("\5\24\13\2\u00da\u00db\5\36\20\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00de\3\2\2\2\u00dd\u00d8\3\2\2\2\u00dd\u00dc\3\2\2\2")
        buf.write("\u00de\37\3\2\2\2\u00df\u00e1\7!\2\2\u00e0\u00df\3\2\2")
        buf.write("\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00f3")
        buf.write("\5\"\22\2\u00e3\u00e4\7\4\2\2\u00e4\u00e5\b\21\1\2\u00e5")
        buf.write("\u00e6\5\24\13\2\u00e6\u00e7\7\5\2\2\u00e7\u00e8\b\21")
        buf.write("\1\2\u00e8\u00f3\3\2\2\2\u00e9\u00f3\7\21\2\2\u00ea\u00eb")
        buf.write("\7*\2\2\u00eb\u00f3\b\21\1\2\u00ec\u00ed\7\23\2\2\u00ed")
        buf.write("\u00ee\5\24\13\2\u00ee\u00ef\5\36\20\2\u00ef\u00f0\7\24")
        buf.write("\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00f3\7%\2\2\u00f2\u00e0")
        buf.write("\3\2\2\2\u00f2\u00e3\3\2\2\2\u00f2\u00e9\3\2\2\2\u00f2")
        buf.write("\u00ea\3\2\2\2\u00f2\u00ec\3\2\2\2\u00f2\u00f1\3\2\2\2")
        buf.write("\u00f3!\3\2\2\2\u00f4\u00f5\7&\2\2\u00f5\u00fb\b\22\1")
        buf.write("\2\u00f6\u00f7\7(\2\2\u00f7\u00fb\b\22\1\2\u00f8\u00f9")
        buf.write("\7)\2\2\u00f9\u00fb\b\22\1\2\u00fa\u00f4\3\2\2\2\u00fa")
        buf.write("\u00f6\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb#\3\2\2\2\u00fc")
        buf.write("\u0100\5&\24\2\u00fd\u00ff\5&\24\2\u00fe\u00fd\3\2\2\2")
        buf.write("\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3")
        buf.write("\2\2\2\u0101%\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0106")
        buf.write("\5*\26\2\u0104\u0106\5\24\13\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\'\3\2\2\2\u0107\u0108\7&\2\2\u0108")
        buf.write("\u0109\b\25\1\2\u0109\u010a\7\4\2\2\u010a\u010b\5\24\13")
        buf.write("\2\u010b\u010c\5\36\20\2\u010c\u010d\7\5\2\2\u010d)\3")
        buf.write("\2\2\2\u010e\u010f\5\n\6\2\u010f\u0110\7&\2\2\u0110\u0111")
        buf.write("\7\26\2\2\u0111\u0112\5\24\13\2\u0112\u0113\b\26\1\2\u0113")
        buf.write("+\3\2\2\2\u0114\u0115\5.\30\2\u0115\u0116\5\60\31\2\u0116")
        buf.write("\u0117\b\27\1\2\u0117\u0118\7\2\2\3\u0118-\3\2\2\2\u0119")
        buf.write("\u011f\5\2\2\2\u011a\u011f\5(\25\2\u011b\u011f\5*\26\2")
        buf.write("\u011c\u011f\5\24\13\2\u011d\u011f\5\16\b\2\u011e\u0119")
        buf.write("\3\2\2\2\u011e\u011a\3\2\2\2\u011e\u011b\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f/\3\2\2\2\u0120")
        buf.write("\u0121\5.\30\2\u0121\u0122\5\60\31\2\u0122\u0125\3\2\2")
        buf.write("\2\u0123\u0125\3\2\2\2\u0124\u0120\3\2\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125\61\3\2\2\2\31CY^dhlpy}\u008b\u009e\u00a6")
        buf.write("\u00b7\u00c4\u00d6\u00dd\u00e0\u00f2\u00fa\u0100\u0105")
        buf.write("\u011e\u0124")
        return buf.getvalue()


class QuarkParser ( Parser ):

    grammarFileName = "Quark.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'('", "')'", "'->'", "'{'", 
                     "'}'", "'default {'", "':'", "','", "'Int'", "'?'", 
                     "'Bool'", "'Float'", "'String'", "'non'", "'Any'", 
                     "'['", "']'", "'type'", "'<-'", "'|'", "'True'", "'False'", 
                     "'>'", "'<'", "'='", "'>='", "'<='", "'!='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'[]'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "TYPE_ID", "CONST_I", "CONST_F", "STRING", "SPACE" ]

    RULE_function = 0
    RULE_params = 1
    RULE_moreparams = 2
    RULE_moreTypes = 3
    RULE_typeRule = 4
    RULE_typevalue = 5
    RULE_typedef = 6
    RULE_typeset = 7
    RULE_cond = 8
    RULE_expression = 9
    RULE_boolRule = 10
    RULE_comparator = 11
    RULE_exp = 12
    RULE_term = 13
    RULE_more_expressions = 14
    RULE_factor = 15
    RULE_varconst = 16
    RULE_block = 17
    RULE_statement = 18
    RULE_func_call = 19
    RULE_assignment = 20
    RULE_main = 21
    RULE_things = 22
    RULE_morethings = 23

    ruleNames =  [ "function", "params", "moreparams", "moreTypes", "typeRule", 
                   "typevalue", "typedef", "typeset", "cond", "expression", 
                   "boolRule", "comparator", "exp", "term", "more_expressions", 
                   "factor", "varconst", "block", "statement", "func_call", 
                   "assignment", "main", "things", "morethings" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    ID=36
    TYPE_ID=37
    CONST_I=38
    CONST_F=39
    STRING=40
    SPACE=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    FuncRecord = namedtuple('FuncRecord', ['type', 'vars'])
    VarRecord = namedtuple('VarRecord', ['type', 'dir', 'dim'])
    func_directory = {
      "global": FuncRecord('non', {}), 
      "append": FuncRecord('[Any]', {}),
      "print": FuncRecord('none', {}),
      "upper": FuncRecord('String', {}),
      "head": FuncRecord('Any', {}),
      "tail": FuncRecord('[Any]', {})
    }
    type_directory = {}
    current_function = "global"
    PilaO = []
    PTypes = []
    POper = []
    quadruples = []
    temp = 0
    # Memory = namedtuple('Memory', ['number', 'value'])
    # memory = Memory()


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._typeRule = None # TypeRuleContext

        def ID(self):
            return self.getToken(QuarkParser.ID, 0)

        def params(self):
            return self.getTypedRuleContext(QuarkParser.ParamsContext,0)


        def typeRule(self):
            return self.getTypedRuleContext(QuarkParser.TypeRuleContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.BlockContext)
            else:
                return self.getTypedRuleContext(QuarkParser.BlockContext,i)


        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.CondContext)
            else:
                return self.getTypedRuleContext(QuarkParser.CondContext,i)


        def getRuleIndex(self):
            return QuarkParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = QuarkParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(QuarkParser.T__0)
            self.state = 49
            localctx._ID = self.match(QuarkParser.ID)

            ident = (None if localctx._ID is None else localctx._ID.text)
            self.current_function = ident
            if ident in self.func_directory:
              raise Exception("Function {} already defined".format(ident))
            else:
              self.func_directory[ident] = self.FuncRecord(None, {})

            self.state = 51
            self.match(QuarkParser.T__1)
            self.state = 52
            self.params()
            self.state = 53
            self.match(QuarkParser.T__2)
            self.state = 54
            self.match(QuarkParser.T__3)
            self.state = 55
            localctx._typeRule = self.typeRule()

            ident = (None if localctx._ID is None else localctx._ID.text)
            ret_type = (None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop)))
            self.func_directory[ident] = self.func_directory[ident]._replace(type=ret_type)

            self.state = 57
            self.match(QuarkParser.T__4)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__1:
                self.state = 58
                self.cond()
                self.state = 59
                self.match(QuarkParser.T__4)
                self.state = 60
                self.block()
                self.state = 61
                self.match(QuarkParser.T__5)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(QuarkParser.T__6)
            self.state = 69
            self.block()
            self.state = 70
            self.match(QuarkParser.T__5)
            self.state = 71
            self.match(QuarkParser.T__5)
            self.current_function = "global"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._typeRule = None # TypeRuleContext

        def ID(self):
            return self.getToken(QuarkParser.ID, 0)

        def typeRule(self):
            return self.getTypedRuleContext(QuarkParser.TypeRuleContext,0)


        def moreparams(self):
            return self.getTypedRuleContext(QuarkParser.MoreparamsContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = QuarkParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            localctx._ID = self.match(QuarkParser.ID)
            self.state = 75
            self.match(QuarkParser.T__7)
            self.state = 76
            localctx._typeRule = self.typeRule()
            self.func_directory[self.current_function].vars[(None if localctx._ID is None else localctx._ID.text)] = self.VarRecord((None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))), 0, None)
                
            self.state = 78
            self.moreparams()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MoreparamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._typeRule = None # TypeRuleContext

        def ID(self):
            return self.getToken(QuarkParser.ID, 0)

        def typeRule(self):
            return self.getTypedRuleContext(QuarkParser.TypeRuleContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_moreparams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreparams" ):
                listener.enterMoreparams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreparams" ):
                listener.exitMoreparams(self)




    def moreparams(self):

        localctx = QuarkParser.MoreparamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_moreparams)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(QuarkParser.T__8)
                self.state = 81
                localctx._ID = self.match(QuarkParser.ID)
                self.state = 82
                self.match(QuarkParser.T__7)
                self.state = 83
                localctx._typeRule = self.typeRule()
                self.func_directory[self.current_function].vars[(None if localctx._ID is None else localctx._ID.text)] = self.VarRecord((None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))), 0, None)
                    
                pass
            elif token in [QuarkParser.T__2]:
                self.enterOuterAlt(localctx, 2)

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

    class MoreTypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeRule(self):
            return self.getTypedRuleContext(QuarkParser.TypeRuleContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_moreTypes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreTypes" ):
                listener.enterMoreTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreTypes" ):
                listener.exitMoreTypes(self)




    def moreTypes(self):

        localctx = QuarkParser.MoreTypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_moreTypes)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(QuarkParser.T__8)
                self.state = 90
                self.typeRule()
                pass
            elif token in [QuarkParser.T__17]:
                self.enterOuterAlt(localctx, 2)

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

    class TypeRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuarkParser.RULE_typeRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class ListOfTypeContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeRule(self):
            return self.getTypedRuleContext(QuarkParser.TypeRuleContext,0)

        def moreTypes(self):
            return self.getTypedRuleContext(QuarkParser.MoreTypesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListOfType" ):
                listener.enterListOfType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListOfType" ):
                listener.exitListOfType(self)


    class StringContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class BooleanContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)


    class UserTypeContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self._TYPE_ID = None # Token
            self.copyFrom(ctx)

        def TYPE_ID(self):
            return self.getToken(QuarkParser.TYPE_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUserType" ):
                listener.enterUserType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUserType" ):
                listener.exitUserType(self)


    class NoneContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNone" ):
                listener.enterNone(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNone" ):
                listener.exitNone(self)


    class AnyContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny" ):
                listener.enterAny(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny" ):
                listener.exitAny(self)


    class IntContext(TypeRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TypeRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def typeRule(self):

        localctx = QuarkParser.TypeRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeRule)
        self._la = 0 # Token type
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.TYPE_ID]:
                localctx = QuarkParser.UserTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                localctx._TYPE_ID = self.match(QuarkParser.TYPE_ID)

                if (None if localctx._TYPE_ID is None else localctx._TYPE_ID.text) not in self.type_directory:
                  raise Exception("Undefined type {}".format((None if localctx._TYPE_ID is None else localctx._TYPE_ID.text)))
                  
                pass
            elif token in [QuarkParser.T__9]:
                localctx = QuarkParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(QuarkParser.T__9)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 97
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__11]:
                localctx = QuarkParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.match(QuarkParser.T__11)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 101
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__12]:
                localctx = QuarkParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(QuarkParser.T__12)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 105
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__13]:
                localctx = QuarkParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.match(QuarkParser.T__13)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 109
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__14]:
                localctx = QuarkParser.NoneContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 112
                self.match(QuarkParser.T__14)
                pass
            elif token in [QuarkParser.T__15]:
                localctx = QuarkParser.AnyContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 113
                self.match(QuarkParser.T__15)
                pass
            elif token in [QuarkParser.T__16]:
                localctx = QuarkParser.ListOfTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 114
                self.match(QuarkParser.T__16)
                self.state = 115
                self.typeRule()
                self.state = 116
                self.moreTypes()
                self.state = 117
                self.match(QuarkParser.T__17)
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

    class TypevalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeRule(self):
            return self.getTypedRuleContext(QuarkParser.TypeRuleContext,0)


        def typeset(self):
            return self.getTypedRuleContext(QuarkParser.TypesetContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_typevalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypevalue" ):
                listener.enterTypevalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypevalue" ):
                listener.exitTypevalue(self)




    def typevalue(self):

        localctx = QuarkParser.TypevalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typevalue)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__9, QuarkParser.T__11, QuarkParser.T__12, QuarkParser.T__13, QuarkParser.T__14, QuarkParser.T__15, QuarkParser.T__16, QuarkParser.TYPE_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.typeRule()
                pass
            elif token in [QuarkParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.typeset()
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

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._TYPE_ID = None # Token
            self._typevalue = None # TypevalueContext

        def TYPE_ID(self):
            return self.getToken(QuarkParser.TYPE_ID, 0)

        def typevalue(self):
            return self.getTypedRuleContext(QuarkParser.TypevalueContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_typedef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedef" ):
                listener.enterTypedef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedef" ):
                listener.exitTypedef(self)




    def typedef(self):

        localctx = QuarkParser.TypedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(QuarkParser.T__18)
            self.state = 126
            localctx._TYPE_ID = self.match(QuarkParser.TYPE_ID)
            self.state = 127
            self.match(QuarkParser.T__19)
            self.state = 128
            localctx._typevalue = self.typevalue()

            # TODO: This typevalue.text should be replaced by either the aliased type or a list of known types.
            self.type_directory[(None if localctx._TYPE_ID is None else localctx._TYPE_ID.text)] = (None if localctx._typevalue is None else self._input.getText((localctx._typevalue.start,localctx._typevalue.stop)))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypesetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.TypeRuleContext)
            else:
                return self.getTypedRuleContext(QuarkParser.TypeRuleContext,i)


        def getRuleIndex(self):
            return QuarkParser.RULE_typeset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeset" ):
                listener.enterTypeset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeset" ):
                listener.exitTypeset(self)




    def typeset(self):

        localctx = QuarkParser.TypesetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(QuarkParser.T__1)
            self.state = 132
            self.typeRule()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__20:
                self.state = 133
                self.match(QuarkParser.T__20)
                self.state = 134
                self.typeRule()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(QuarkParser.T__2)
            #TODO: This should return the list of defined types
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def more_expressions(self):
            return self.getTypedRuleContext(QuarkParser.More_expressionsContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = QuarkParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(QuarkParser.T__1)
            self.state = 144
            self.expression(0)
            self.state = 145
            self.more_expressions()
            self.state = 146
            self.match(QuarkParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(QuarkParser.Func_callContext,0)


        def boolRule(self):
            return self.getTypedRuleContext(QuarkParser.BoolRuleContext,0)


        def exp(self):
            return self.getTypedRuleContext(QuarkParser.ExpContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuarkParser.ExpressionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(QuarkParser.ComparatorContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = QuarkParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 149
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 150
                self.boolRule()
                pass

            elif la_ == 3:
                self.state = 151
                self.exp()
                self.state = 152
                self.expression(4)
                pass

            elif la_ == 4:
                self.state = 154
                self.exp()
                pass

            elif la_ == 5:
                self.state = 155
                self.match(QuarkParser.T__14)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QuarkParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 158
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 159
                    self.comparator()
                    self.state = 160
                    self.expression(3) 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BoolRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(QuarkParser.ID, 0)

        def getRuleIndex(self):
            return QuarkParser.RULE_boolRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolRule" ):
                listener.enterBoolRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolRule" ):
                listener.exitBoolRule(self)




    def boolRule(self):

        localctx = QuarkParser.BoolRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_boolRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__21) | (1 << QuarkParser.T__22) | (1 << QuarkParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuarkParser.RULE_comparator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GreaterEqualContext(ComparatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ComparatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEqual" ):
                listener.enterGreaterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEqual" ):
                listener.exitGreaterEqual(self)


    class LesserContext(ComparatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ComparatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesser" ):
                listener.enterLesser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesser" ):
                listener.exitLesser(self)


    class NotEqualContext(ComparatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ComparatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqual" ):
                listener.enterNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqual" ):
                listener.exitNotEqual(self)


    class EqualContext(ComparatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ComparatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)


    class GreaterContext(ComparatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ComparatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater" ):
                listener.enterGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater" ):
                listener.exitGreater(self)


    class LesserEqualContext(ComparatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ComparatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesserEqual" ):
                listener.enterLesserEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesserEqual" ):
                listener.exitLesserEqual(self)



    def comparator(self):

        localctx = QuarkParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comparator)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__23]:
                localctx = QuarkParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(QuarkParser.T__23)
                self.POper.append('>')
                pass
            elif token in [QuarkParser.T__24]:
                localctx = QuarkParser.LesserContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(QuarkParser.T__24)
                self.POper.append('<')
                pass
            elif token in [QuarkParser.T__25]:
                localctx = QuarkParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(QuarkParser.T__25)
                self.POper.append('=')
                pass
            elif token in [QuarkParser.T__26]:
                localctx = QuarkParser.GreaterEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.match(QuarkParser.T__26)
                self.POper.append('>=')
                pass
            elif token in [QuarkParser.T__27]:
                localctx = QuarkParser.LesserEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 177
                self.match(QuarkParser.T__27)
                self.POper.append('<=')
                pass
            elif token in [QuarkParser.T__28]:
                localctx = QuarkParser.NotEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.match(QuarkParser.T__28)
                self.POper.append('!=')
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

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuarkParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubstractionContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstraction" ):
                listener.enterSubstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstraction" ):
                listener.exitSubstraction(self)


    class AdditionContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)


    class JustTermContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJustTerm" ):
                listener.enterJustTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJustTerm" ):
                listener.exitJustTerm(self)



    def exp(self):

        localctx = QuarkParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = QuarkParser.JustTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.term()
                pass

            elif la_ == 2:
                localctx = QuarkParser.AdditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(QuarkParser.T__29)
                self.POper.append('+')
                self.state = 186
                self.term()

                if self.POper[-1] == "+":
                  right_operand, right_type = self.PilaO.pop()
                  left_operand, left_type = self.PilaO.pop()
                  operator = self.POper.pop()
                  self.temp = self.temp + 1
                  return_type = check_operation_type(operator, left_type, right_type)
                  self.quadruples.append((operator, left_operand, right_operand, self.temp))
                  self.PilaO.append(self.temp)

                pass

            elif la_ == 3:
                localctx = QuarkParser.SubstractionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.match(QuarkParser.T__30)
                self.POper.append('-')
                self.state = 191
                self.term()

                if self.POper[-1] == "-":
                  right_operand, right_type = self.PilaO.pop()
                  left_operand, left_type = self.PilaO.pop()
                  operator = self.POper.pop()
                  self.temp = self.temp + 1
                  return_type = check_operation_type(operator, left_type, right_type)
                  self.quadruples.append((operator, left_operand, right_operand, self.temp))
                  self.PilaO.append(self.temp)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuarkParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiplicationContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(QuarkParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)


    class ModuloContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(QuarkParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo" ):
                listener.enterModulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo" ):
                listener.exitModulo(self)


    class DivisionContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(QuarkParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)


    class JustFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(QuarkParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJustFactor" ):
                listener.enterJustFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJustFactor" ):
                listener.exitJustFactor(self)



    def term(self):

        localctx = QuarkParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_term)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__1, QuarkParser.T__14, QuarkParser.T__16, QuarkParser.T__30, QuarkParser.T__34, QuarkParser.ID, QuarkParser.CONST_I, QuarkParser.CONST_F, QuarkParser.STRING]:
                localctx = QuarkParser.JustFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.factor()
                pass
            elif token in [QuarkParser.T__31]:
                localctx = QuarkParser.MultiplicationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(QuarkParser.T__31)
                self.POper.append('*')
                self.state = 199
                self.factor()

                if self.POper[-1] == "*":
                  right_operand, right_type = self.PilaO.pop()
                  left_operand, left_type = self.PilaO.pop()
                  operator = self.POper.pop()
                  self.temp = self.temp + 1
                  return_type = check_operation_type(operator, left_type, right_type)
                  self.quadruples.append((operator, left_operand, right_operand, self.temp))
                  self.PilaO.append(self.temp)

                pass
            elif token in [QuarkParser.T__32]:
                localctx = QuarkParser.DivisionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.match(QuarkParser.T__32)
                self.POper.append('/')
                self.state = 204
                self.factor()

                if self.POper[-1] == "/":
                  right_operand, right_type = self.PilaO.pop()
                  left_operand, left_type = self.PilaO.pop()
                  operator = self.POper.pop()
                  self.temp = self.temp + 1
                  return_type = check_operation_type(operator, left_type, right_type)
                  self.quadruples.append((operator, left_operand, right_operand, self.temp))
                  self.PilaO.append(self.temp)

                pass
            elif token in [QuarkParser.T__33]:
                localctx = QuarkParser.ModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.match(QuarkParser.T__33)
                self.POper.append('%')
                self.state = 209
                self.factor()

                if self.POper[-1] == "%":
                  right_operand, right_type = self.PilaO.pop()
                  left_operand, left_type = self.PilaO.pop()
                  operator = self.POper.pop()
                  return_type = check_operation_type(operator, left_type, right_type)
                  self.temp = self.temp + 1
                  self.quadruples.append((operator, left_operand, right_operand, self.temp))
                  self.PilaO.append(self.temp)

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

    class More_expressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def more_expressions(self):
            return self.getTypedRuleContext(QuarkParser.More_expressionsContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_more_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore_expressions" ):
                listener.enterMore_expressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore_expressions" ):
                listener.exitMore_expressions(self)




    def more_expressions(self):

        localctx = QuarkParser.More_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_more_expressions)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(QuarkParser.T__8)
                self.state = 215
                self.expression(0)
                self.state = 216
                self.more_expressions()
                pass
            elif token in [QuarkParser.T__2, QuarkParser.T__17]:
                self.enterOuterAlt(localctx, 2)

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

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STRING = None # Token

        def varconst(self):
            return self.getTypedRuleContext(QuarkParser.VarconstContext,0)


        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(QuarkParser.STRING, 0)

        def more_expressions(self):
            return self.getTypedRuleContext(QuarkParser.More_expressionsContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = QuarkParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__30, QuarkParser.ID, QuarkParser.CONST_I, QuarkParser.CONST_F]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__30:
                    self.state = 221
                    self.match(QuarkParser.T__30)


                self.state = 224
                self.varconst()
                pass
            elif token in [QuarkParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(QuarkParser.T__1)
                self.POper.append('(')
                self.state = 227
                self.expression(0)
                self.state = 228
                self.match(QuarkParser.T__2)
                self.POper.append(')')
                pass
            elif token in [QuarkParser.T__14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.match(QuarkParser.T__14)
                pass
            elif token in [QuarkParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                localctx._STRING = self.match(QuarkParser.STRING)
                self.POper.append((None if localctx._STRING is None else localctx._STRING.text)); self.PTypes.append("String")
                pass
            elif token in [QuarkParser.T__16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.match(QuarkParser.T__16)
                self.state = 235
                self.expression(0)
                self.state = 236
                self.more_expressions()
                self.state = 237
                self.match(QuarkParser.T__17)
                pass
            elif token in [QuarkParser.T__34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 239
                self.match(QuarkParser.T__34)
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

    class VarconstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._CONST_I = None # Token
            self._CONST_F = None # Token

        def ID(self):
            return self.getToken(QuarkParser.ID, 0)

        def CONST_I(self):
            return self.getToken(QuarkParser.CONST_I, 0)

        def CONST_F(self):
            return self.getToken(QuarkParser.CONST_F, 0)

        def getRuleIndex(self):
            return QuarkParser.RULE_varconst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarconst" ):
                listener.enterVarconst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarconst" ):
                listener.exitVarconst(self)




    def varconst(self):

        localctx = QuarkParser.VarconstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_varconst)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                localctx._ID = self.match(QuarkParser.ID)

                if (None if localctx._ID is None else localctx._ID.text) not in self.func_directory[self.current_function].vars:
                  raise Exception("ID {} is not defined".format((None if localctx._ID is None else localctx._ID.text)))
                self.PilaO.append(((None if localctx._ID is None else localctx._ID.text), self.func_directory[self.current_function].vars[(None if localctx._ID is None else localctx._ID.text)].type))

                pass
            elif token in [QuarkParser.CONST_I]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                localctx._CONST_I = self.match(QuarkParser.CONST_I)
                self.PilaO.append(((None if localctx._CONST_I is None else localctx._CONST_I.text), "Int"))
                pass
            elif token in [QuarkParser.CONST_F]:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                localctx._CONST_F = self.match(QuarkParser.CONST_F)
                self.PilaO.append(((None if localctx._CONST_F is None else localctx._CONST_F.text), "Float"))
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

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.StatementContext)
            else:
                return self.getTypedRuleContext(QuarkParser.StatementContext,i)


        def getRuleIndex(self):
            return QuarkParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = QuarkParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.statement()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__1) | (1 << QuarkParser.T__9) | (1 << QuarkParser.T__11) | (1 << QuarkParser.T__12) | (1 << QuarkParser.T__13) | (1 << QuarkParser.T__14) | (1 << QuarkParser.T__15) | (1 << QuarkParser.T__16) | (1 << QuarkParser.T__21) | (1 << QuarkParser.T__22) | (1 << QuarkParser.T__29) | (1 << QuarkParser.T__30) | (1 << QuarkParser.T__31) | (1 << QuarkParser.T__32) | (1 << QuarkParser.T__33) | (1 << QuarkParser.T__34) | (1 << QuarkParser.ID) | (1 << QuarkParser.TYPE_ID) | (1 << QuarkParser.CONST_I) | (1 << QuarkParser.CONST_F) | (1 << QuarkParser.STRING))) != 0):
                self.state = 251
                self.statement()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(QuarkParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = QuarkParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(QuarkParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def more_expressions(self):
            return self.getTypedRuleContext(QuarkParser.More_expressionsContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




    def func_call(self):

        localctx = QuarkParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            localctx._ID = self.match(QuarkParser.ID)

            if (None if localctx._ID is None else localctx._ID.text) not in self.func_directory:
              raise Exception("Function {} does not exist".format((None if localctx._ID is None else localctx._ID.text)))

            self.state = 263
            self.match(QuarkParser.T__1)
            self.state = 264
            self.expression(0)
            self.state = 265
            self.more_expressions()
            self.state = 266
            self.match(QuarkParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._typeRule = None # TypeRuleContext
            self._ID = None # Token

        def typeRule(self):
            return self.getTypedRuleContext(QuarkParser.TypeRuleContext,0)


        def ID(self):
            return self.getToken(QuarkParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = QuarkParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            localctx._typeRule = self.typeRule()
            self.state = 269
            localctx._ID = self.match(QuarkParser.ID)
            self.state = 270
            self.match(QuarkParser.T__19)
            self.state = 271
            self.expression(0)

            if (None if localctx._ID is None else localctx._ID.text) not in self.func_directory[self.current_function]:
              self.func_directory[self.current_function].vars[(None if localctx._ID is None else localctx._ID.text)] = self.VarRecord((None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))), 0, None)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def things(self):
            return self.getTypedRuleContext(QuarkParser.ThingsContext,0)


        def morethings(self):
            return self.getTypedRuleContext(QuarkParser.MorethingsContext,0)


        def EOF(self):
            return self.getToken(QuarkParser.EOF, 0)

        def getRuleIndex(self):
            return QuarkParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = QuarkParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.things()
            self.state = 275
            self.morethings()
            pp.pprint(self.func_directory); pp.pprint(self.quadruples)
            self.state = 277
            self.match(QuarkParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ThingsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(QuarkParser.FunctionContext,0)


        def func_call(self):
            return self.getTypedRuleContext(QuarkParser.Func_callContext,0)


        def assignment(self):
            return self.getTypedRuleContext(QuarkParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def typedef(self):
            return self.getTypedRuleContext(QuarkParser.TypedefContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_things

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThings" ):
                listener.enterThings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThings" ):
                listener.exitThings(self)




    def things(self):

        localctx = QuarkParser.ThingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_things)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.typedef()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MorethingsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def things(self):
            return self.getTypedRuleContext(QuarkParser.ThingsContext,0)


        def morethings(self):
            return self.getTypedRuleContext(QuarkParser.MorethingsContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_morethings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMorethings" ):
                listener.enterMorethings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMorethings" ):
                listener.exitMorethings(self)




    def morethings(self):

        localctx = QuarkParser.MorethingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_morethings)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__0, QuarkParser.T__1, QuarkParser.T__9, QuarkParser.T__11, QuarkParser.T__12, QuarkParser.T__13, QuarkParser.T__14, QuarkParser.T__15, QuarkParser.T__16, QuarkParser.T__18, QuarkParser.T__21, QuarkParser.T__22, QuarkParser.T__29, QuarkParser.T__30, QuarkParser.T__31, QuarkParser.T__32, QuarkParser.T__33, QuarkParser.T__34, QuarkParser.ID, QuarkParser.TYPE_ID, QuarkParser.CONST_I, QuarkParser.CONST_F, QuarkParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.things()
                self.state = 287
                self.morethings()
                pass
            elif token in [QuarkParser.EOF]:
                self.enterOuterAlt(localctx, 2)

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
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




