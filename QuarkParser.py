# Generated from Quark.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from collections import namedtuple
from arithmetic_cube import check_operation_type
import pprint
pp = pprint.PrettyPrinter()

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("\u0132\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2>\n")
        buf.write("\2\f\2\16\2A\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4V\n\4\3\5")
        buf.write("\3\5\3\5\5\5[\n\5\3\6\3\6\3\6\3\6\5\6a\n\6\3\6\3\6\5\6")
        buf.write("e\n\6\3\6\3\6\5\6i\n\6\3\6\3\6\5\6m\n\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6v\n\6\3\7\3\7\5\7z\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u0086\n\t\f\t\16\t\u0089")
        buf.write("\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u0099\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c4\n\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u00d6\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00dd\n")
        buf.write("\16\3\17\5\17\u00e0\n\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00f6\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00fe\n\20\3\21\3\21\7\21\u0102\n\21\f\21")
        buf.write("\16\21\u0105\13\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u010d\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u012a\n")
        buf.write("\26\3\27\3\27\3\27\3\27\5\27\u0130\n\27\3\27\2\2\30\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,\2\2\2\u014a")
        buf.write("\2.\3\2\2\2\4H\3\2\2\2\6U\3\2\2\2\bZ\3\2\2\2\nu\3\2\2")
        buf.write("\2\fy\3\2\2\2\16{\3\2\2\2\20\u0081\3\2\2\2\22\u008d\3")
        buf.write("\2\2\2\24\u0098\3\2\2\2\26\u00c3\3\2\2\2\30\u00d5\3\2")
        buf.write("\2\2\32\u00dc\3\2\2\2\34\u00f5\3\2\2\2\36\u00fd\3\2\2")
        buf.write("\2 \u00ff\3\2\2\2\"\u010c\3\2\2\2$\u010e\3\2\2\2&\u0115")
        buf.write("\3\2\2\2(\u011b\3\2\2\2*\u0129\3\2\2\2,\u012f\3\2\2\2")
        buf.write("./\7\3\2\2/\60\7\'\2\2\60\61\b\2\1\2\61\62\7\4\2\2\62")
        buf.write("\63\5\4\3\2\63\64\7\5\2\2\64\65\7\6\2\2\65\66\5\n\6\2")
        buf.write("\66\67\b\2\1\2\67?\7\7\2\289\5\22\n\29:\7\7\2\2:;\5 \21")
        buf.write("\2;<\7\b\2\2<>\3\2\2\2=8\3\2\2\2>A\3\2\2\2?=\3\2\2\2?")
        buf.write("@\3\2\2\2@B\3\2\2\2A?\3\2\2\2BC\7\t\2\2CD\5 \21\2DE\7")
        buf.write("\b\2\2EF\7\b\2\2FG\b\2\1\2G\3\3\2\2\2HI\7\'\2\2IJ\7\n")
        buf.write("\2\2JK\5\n\6\2KL\b\3\1\2LM\5\6\4\2M\5\3\2\2\2NO\7\13\2")
        buf.write("\2OP\7\'\2\2PQ\7\n\2\2QR\5\n\6\2RS\b\4\1\2SV\3\2\2\2T")
        buf.write("V\3\2\2\2UN\3\2\2\2UT\3\2\2\2V\7\3\2\2\2WX\7\13\2\2X[")
        buf.write("\5\n\6\2Y[\3\2\2\2ZW\3\2\2\2ZY\3\2\2\2[\t\3\2\2\2\\]\7")
        buf.write("(\2\2]v\b\6\1\2^`\7\f\2\2_a\7\r\2\2`_\3\2\2\2`a\3\2\2")
        buf.write("\2av\3\2\2\2bd\7\16\2\2ce\7\r\2\2dc\3\2\2\2de\3\2\2\2")
        buf.write("ev\3\2\2\2fh\7\17\2\2gi\7\r\2\2hg\3\2\2\2hi\3\2\2\2iv")
        buf.write("\3\2\2\2jl\7\20\2\2km\7\r\2\2lk\3\2\2\2lm\3\2\2\2mv\3")
        buf.write("\2\2\2nv\7\21\2\2ov\7\22\2\2pq\7\23\2\2qr\5\n\6\2rs\5")
        buf.write("\b\5\2st\7\24\2\2tv\3\2\2\2u\\\3\2\2\2u^\3\2\2\2ub\3\2")
        buf.write("\2\2uf\3\2\2\2uj\3\2\2\2un\3\2\2\2uo\3\2\2\2up\3\2\2\2")
        buf.write("v\13\3\2\2\2wz\5\n\6\2xz\5\20\t\2yw\3\2\2\2yx\3\2\2\2")
        buf.write("z\r\3\2\2\2{|\7\25\2\2|}\7(\2\2}~\7\26\2\2~\177\5\f\7")
        buf.write("\2\177\u0080\b\b\1\2\u0080\17\3\2\2\2\u0081\u0082\7\4")
        buf.write("\2\2\u0082\u0087\5\n\6\2\u0083\u0084\7\27\2\2\u0084\u0086")
        buf.write("\5\n\6\2\u0085\u0083\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008a\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u008a\u008b\7\5\2\2\u008b\u008c\b")
        buf.write("\t\1\2\u008c\21\3\2\2\2\u008d\u008e\7\4\2\2\u008e\u008f")
        buf.write("\5\24\13\2\u008f\u0090\5\32\16\2\u0090\u0091\7\5\2\2\u0091")
        buf.write("\23\3\2\2\2\u0092\u0099\5$\23\2\u0093\u0094\5\26\f\2\u0094")
        buf.write("\u0095\5\24\13\2\u0095\u0099\3\2\2\2\u0096\u0099\5\26")
        buf.write("\f\2\u0097\u0099\7\21\2\2\u0098\u0092\3\2\2\2\u0098\u0093")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\25\3\2\2\2\u009a\u00c4\5\30\r\2\u009b\u009c\7\30\2\2")
        buf.write("\u009c\u009d\b\f\1\2\u009d\u009e\5\30\r\2\u009e\u009f")
        buf.write("\b\f\1\2\u009f\u00c4\3\2\2\2\u00a0\u00a1\7\31\2\2\u00a1")
        buf.write("\u00a2\b\f\1\2\u00a2\u00a3\5\30\r\2\u00a3\u00a4\b\f\1")
        buf.write("\2\u00a4\u00c4\3\2\2\2\u00a5\u00a6\7\32\2\2\u00a6\u00a7")
        buf.write("\b\f\1\2\u00a7\u00a8\5\30\r\2\u00a8\u00a9\b\f\1\2\u00a9")
        buf.write("\u00c4\3\2\2\2\u00aa\u00ab\7\33\2\2\u00ab\u00ac\b\f\1")
        buf.write("\2\u00ac\u00ad\5\30\r\2\u00ad\u00ae\b\f\1\2\u00ae\u00c4")
        buf.write("\3\2\2\2\u00af\u00b0\7\34\2\2\u00b0\u00b1\b\f\1\2\u00b1")
        buf.write("\u00b2\5\30\r\2\u00b2\u00b3\b\f\1\2\u00b3\u00c4\3\2\2")
        buf.write("\2\u00b4\u00b5\7\35\2\2\u00b5\u00b6\b\f\1\2\u00b6\u00b7")
        buf.write("\5\30\r\2\u00b7\u00b8\b\f\1\2\u00b8\u00c4\3\2\2\2\u00b9")
        buf.write("\u00ba\7\36\2\2\u00ba\u00bb\b\f\1\2\u00bb\u00bc\5\30\r")
        buf.write("\2\u00bc\u00bd\b\f\1\2\u00bd\u00c4\3\2\2\2\u00be\u00bf")
        buf.write("\7\37\2\2\u00bf\u00c0\b\f\1\2\u00c0\u00c1\5\30\r\2\u00c1")
        buf.write("\u00c2\b\f\1\2\u00c2\u00c4\3\2\2\2\u00c3\u009a\3\2\2\2")
        buf.write("\u00c3\u009b\3\2\2\2\u00c3\u00a0\3\2\2\2\u00c3\u00a5\3")
        buf.write("\2\2\2\u00c3\u00aa\3\2\2\2\u00c3\u00af\3\2\2\2\u00c3\u00b4")
        buf.write("\3\2\2\2\u00c3\u00b9\3\2\2\2\u00c3\u00be\3\2\2\2\u00c4")
        buf.write("\27\3\2\2\2\u00c5\u00d6\5\34\17\2\u00c6\u00c7\7 \2\2\u00c7")
        buf.write("\u00c8\b\r\1\2\u00c8\u00c9\5\34\17\2\u00c9\u00ca\b\r\1")
        buf.write("\2\u00ca\u00d6\3\2\2\2\u00cb\u00cc\7!\2\2\u00cc\u00cd")
        buf.write("\b\r\1\2\u00cd\u00ce\5\34\17\2\u00ce\u00cf\b\r\1\2\u00cf")
        buf.write("\u00d6\3\2\2\2\u00d0\u00d1\7\"\2\2\u00d1\u00d2\b\r\1\2")
        buf.write("\u00d2\u00d3\5\34\17\2\u00d3\u00d4\b\r\1\2\u00d4\u00d6")
        buf.write("\3\2\2\2\u00d5\u00c5\3\2\2\2\u00d5\u00c6\3\2\2\2\u00d5")
        buf.write("\u00cb\3\2\2\2\u00d5\u00d0\3\2\2\2\u00d6\31\3\2\2\2\u00d7")
        buf.write("\u00d8\7\13\2\2\u00d8\u00d9\5\24\13\2\u00d9\u00da\5\32")
        buf.write("\16\2\u00da\u00dd\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00d7")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\33\3\2\2\2\u00de\u00e0")
        buf.write("\7\31\2\2\u00df\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00f6\5\36\20\2\u00e2\u00e3\7\4\2")
        buf.write("\2\u00e3\u00e4\b\17\1\2\u00e4\u00e5\5\24\13\2\u00e5\u00e6")
        buf.write("\7\5\2\2\u00e6\u00e7\b\17\1\2\u00e7\u00f6\3\2\2\2\u00e8")
        buf.write("\u00e9\7#\2\2\u00e9\u00f6\b\17\1\2\u00ea\u00eb\7$\2\2")
        buf.write("\u00eb\u00f6\b\17\1\2\u00ec\u00ed\7+\2\2\u00ed\u00f6\b")
        buf.write("\17\1\2\u00ee\u00ef\7\23\2\2\u00ef\u00f0\5\24\13\2\u00f0")
        buf.write("\u00f1\5\32\16\2\u00f1\u00f2\7\24\2\2\u00f2\u00f6\3\2")
        buf.write("\2\2\u00f3\u00f4\7%\2\2\u00f4\u00f6\b\17\1\2\u00f5\u00df")
        buf.write("\3\2\2\2\u00f5\u00e2\3\2\2\2\u00f5\u00e8\3\2\2\2\u00f5")
        buf.write("\u00ea\3\2\2\2\u00f5\u00ec\3\2\2\2\u00f5\u00ee\3\2\2\2")
        buf.write("\u00f5\u00f3\3\2\2\2\u00f6\35\3\2\2\2\u00f7\u00f8\7\'")
        buf.write("\2\2\u00f8\u00fe\b\20\1\2\u00f9\u00fa\7)\2\2\u00fa\u00fe")
        buf.write("\b\20\1\2\u00fb\u00fc\7*\2\2\u00fc\u00fe\b\20\1\2\u00fd")
        buf.write("\u00f7\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fe\37\3\2\2\2\u00ff\u0103\5\"\22\2\u0100\u0102\5\"")
        buf.write("\22\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104!\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0106\u0107\5&\24\2\u0107\u0108\7&\2\2\u0108")
        buf.write("\u010d\3\2\2\2\u0109\u010a\5\24\13\2\u010a\u010b\7&\2")
        buf.write("\2\u010b\u010d\3\2\2\2\u010c\u0106\3\2\2\2\u010c\u0109")
        buf.write("\3\2\2\2\u010d#\3\2\2\2\u010e\u010f\7\'\2\2\u010f\u0110")
        buf.write("\b\23\1\2\u0110\u0111\7\4\2\2\u0111\u0112\5\24\13\2\u0112")
        buf.write("\u0113\5\32\16\2\u0113\u0114\7\5\2\2\u0114%\3\2\2\2\u0115")
        buf.write("\u0116\5\n\6\2\u0116\u0117\7\'\2\2\u0117\u0118\7\26\2")
        buf.write("\2\u0118\u0119\5\24\13\2\u0119\u011a\b\24\1\2\u011a\'")
        buf.write("\3\2\2\2\u011b\u011c\5*\26\2\u011c\u011d\5,\27\2\u011d")
        buf.write("\u011e\b\25\1\2\u011e\u011f\7\2\2\3\u011f)\3\2\2\2\u0120")
        buf.write("\u012a\5\2\2\2\u0121\u0122\5$\23\2\u0122\u0123\7&\2\2")
        buf.write("\u0123\u012a\3\2\2\2\u0124\u012a\5&\24\2\u0125\u012a\5")
        buf.write("\24\13\2\u0126\u0127\5\16\b\2\u0127\u0128\7&\2\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0120\3\2\2\2\u0129\u0121\3\2\2\2")
        buf.write("\u0129\u0124\3\2\2\2\u0129\u0125\3\2\2\2\u0129\u0126\3")
        buf.write("\2\2\2\u012a+\3\2\2\2\u012b\u012c\5*\26\2\u012c\u012d")
        buf.write("\5,\27\2\u012d\u0130\3\2\2\2\u012e\u0130\3\2\2\2\u012f")
        buf.write("\u012b\3\2\2\2\u012f\u012e\3\2\2\2\u0130-\3\2\2\2\27?")
        buf.write("UZ`dhluy\u0087\u0098\u00c3\u00d5\u00dc\u00df\u00f5\u00fd")
        buf.write("\u0103\u010c\u0129\u012f")
        return buf.getvalue()


class QuarkParser ( Parser ):

    grammarFileName = "Quark.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'('", "')'", "'->'", "'{'", 
                     "'}'", "'default {'", "':'", "','", "'Int'", "'?'", 
                     "'Bool'", "'Float'", "'String'", "'non'", "'Any'", 
                     "'['", "']'", "'type'", "'<-'", "'|'", "'+'", "'-'", 
                     "'>'", "'<'", "'='", "'>='", "'<='", "'!='", "'*'", 
                     "'/'", "'%'", "'True'", "'False'", "'[]'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "TYPE_ID", "CONST_I", "CONST_F", 
                      "STRING", "SPACE" ]

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
    RULE_exp = 10
    RULE_term = 11
    RULE_more_expressions = 12
    RULE_factor = 13
    RULE_varconst = 14
    RULE_block = 15
    RULE_statement = 16
    RULE_func_call = 17
    RULE_assignment = 18
    RULE_main = 19
    RULE_things = 20
    RULE_morethings = 21

    ruleNames =  [ "function", "params", "moreparams", "moreTypes", "typeRule", 
                   "typevalue", "typedef", "typeset", "cond", "expression", 
                   "exp", "term", "more_expressions", "factor", "varconst", 
                   "block", "statement", "func_call", "assignment", "main", 
                   "things", "morethings" ]

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
    T__35=36
    ID=37
    TYPE_ID=38
    CONST_I=39
    CONST_F=40
    STRING=41
    SPACE=42

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
    POper = []
    quadruples = []
    temp = 0
    # Memory = namedtuple('Memory', ['number', 'value'])
    # memory = Memory()

    def handle_operation(self):
      right_operand, right_type = self.PilaO.pop()
      left_operand, left_type = self.PilaO.pop()
      operator = self.POper.pop()
      self.temp = self.temp + 1
      return_type = check_operation_type(operator, left_type, right_type)
      self.quadruples.append((operator, left_operand, right_operand, self.temp))
      self.PilaO.append((self.temp, return_type))


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
            self.state = 44
            self.match(QuarkParser.T__0)
            self.state = 45
            localctx._ID = self.match(QuarkParser.ID)

            ident = (None if localctx._ID is None else localctx._ID.text)
            self.current_function = ident
            if ident in self.func_directory:
              raise Exception("Function {} already defined".format(ident))
            else:
              self.func_directory[ident] = self.FuncRecord(None, {})

            self.state = 47
            self.match(QuarkParser.T__1)
            self.state = 48
            self.params()
            self.state = 49
            self.match(QuarkParser.T__2)
            self.state = 50
            self.match(QuarkParser.T__3)
            self.state = 51
            localctx._typeRule = self.typeRule()

            ident = (None if localctx._ID is None else localctx._ID.text)
            ret_type = (None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop)))
            self.func_directory[ident] = self.func_directory[ident]._replace(type=ret_type)

            self.state = 53
            self.match(QuarkParser.T__4)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__1:
                self.state = 54
                self.cond()
                self.state = 55
                self.match(QuarkParser.T__4)
                self.state = 56
                self.block()
                self.state = 57
                self.match(QuarkParser.T__5)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(QuarkParser.T__6)
            self.state = 65
            self.block()
            self.state = 66
            self.match(QuarkParser.T__5)
            self.state = 67
            self.match(QuarkParser.T__5)

            self.current_function = "global"
            self.PilaO = []
            self.POper = []

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
            self.state = 70
            localctx._ID = self.match(QuarkParser.ID)
            self.state = 71
            self.match(QuarkParser.T__7)
            self.state = 72
            localctx._typeRule = self.typeRule()
            self.func_directory[self.current_function].vars[(None if localctx._ID is None else localctx._ID.text)] = self.VarRecord((None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))), 0, None)
                
            self.state = 74
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(QuarkParser.T__8)
                self.state = 77
                localctx._ID = self.match(QuarkParser.ID)
                self.state = 78
                self.match(QuarkParser.T__7)
                self.state = 79
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
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(QuarkParser.T__8)
                self.state = 86
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
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.TYPE_ID]:
                localctx = QuarkParser.UserTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                localctx._TYPE_ID = self.match(QuarkParser.TYPE_ID)

                if (None if localctx._TYPE_ID is None else localctx._TYPE_ID.text) not in self.type_directory:
                  raise Exception("Undefined type {}".format((None if localctx._TYPE_ID is None else localctx._TYPE_ID.text)))
                  
                pass
            elif token in [QuarkParser.T__9]:
                localctx = QuarkParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(QuarkParser.T__9)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 93
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__11]:
                localctx = QuarkParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(QuarkParser.T__11)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 97
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__12]:
                localctx = QuarkParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self.match(QuarkParser.T__12)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 101
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__13]:
                localctx = QuarkParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.match(QuarkParser.T__13)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 105
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__14]:
                localctx = QuarkParser.NoneContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.match(QuarkParser.T__14)
                pass
            elif token in [QuarkParser.T__15]:
                localctx = QuarkParser.AnyContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 109
                self.match(QuarkParser.T__15)
                pass
            elif token in [QuarkParser.T__16]:
                localctx = QuarkParser.ListOfTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 110
                self.match(QuarkParser.T__16)
                self.state = 111
                self.typeRule()
                self.state = 112
                self.moreTypes()
                self.state = 113
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
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__9, QuarkParser.T__11, QuarkParser.T__12, QuarkParser.T__13, QuarkParser.T__14, QuarkParser.T__15, QuarkParser.T__16, QuarkParser.TYPE_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.typeRule()
                pass
            elif token in [QuarkParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
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
            self.state = 121
            self.match(QuarkParser.T__18)
            self.state = 122
            localctx._TYPE_ID = self.match(QuarkParser.TYPE_ID)
            self.state = 123
            self.match(QuarkParser.T__19)
            self.state = 124
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
            self.state = 127
            self.match(QuarkParser.T__1)
            self.state = 128
            self.typeRule()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__20:
                self.state = 129
                self.match(QuarkParser.T__20)
                self.state = 130
                self.typeRule()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
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
            self.state = 139
            self.match(QuarkParser.T__1)
            self.state = 140
            self.expression()
            self.state = 141
            self.more_expressions()
            self.state = 142
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


        def exp(self):
            return self.getTypedRuleContext(QuarkParser.ExpContext,0)


        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return QuarkParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = QuarkParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.exp()
                self.state = 146
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.exp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(QuarkParser.T__14)
                pass


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


    class GreaterEqualContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEqual" ):
                listener.enterGreaterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEqual" ):
                listener.exitGreaterEqual(self)


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


    class LesserContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesser" ):
                listener.enterLesser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesser" ):
                listener.exitLesser(self)


    class NotEqualContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqual" ):
                listener.enterNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqual" ):
                listener.exitNotEqual(self)


    class EqualContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)


    class GreaterContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater" ):
                listener.enterGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater" ):
                listener.exitGreater(self)


    class LesserEqualContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QuarkParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesserEqual" ):
                listener.enterLesserEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesserEqual" ):
                listener.exitLesserEqual(self)


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
        self.enterRule(localctx, 20, self.RULE_exp)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = QuarkParser.JustTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.term()
                pass

            elif la_ == 2:
                localctx = QuarkParser.AdditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(QuarkParser.T__21)
                self.POper.append('+')
                self.state = 155
                self.term()

                if self.POper[-1] == "+":
                  self.handle_operation()

                pass

            elif la_ == 3:
                localctx = QuarkParser.SubstractionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(QuarkParser.T__22)
                self.POper.append('-')
                self.state = 160
                self.term()

                if self.POper[-1] == "-":
                  self.handle_operation()

                pass

            elif la_ == 4:
                localctx = QuarkParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.match(QuarkParser.T__23)
                self.POper.append('>')
                self.state = 165
                self.term()

                if self.POper[-1] == ">":
                  self.handle_operation()

                pass

            elif la_ == 5:
                localctx = QuarkParser.LesserContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 168
                self.match(QuarkParser.T__24)
                self.POper.append('<')
                self.state = 170
                self.term()

                if self.POper[-1] == "<":
                  self.handle_operation()

                pass

            elif la_ == 6:
                localctx = QuarkParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 173
                self.match(QuarkParser.T__25)
                self.POper.append('=')
                self.state = 175
                self.term()

                if self.POper[-1] == "=":
                  self.handle_operation()

                pass

            elif la_ == 7:
                localctx = QuarkParser.GreaterEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 178
                self.match(QuarkParser.T__26)
                self.POper.append('>=')
                self.state = 180
                self.term()

                if self.POper[-1] == ">=":
                  self.handle_operation()

                pass

            elif la_ == 8:
                localctx = QuarkParser.LesserEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 183
                self.match(QuarkParser.T__27)
                self.POper.append('<=')
                self.state = 185
                self.term()

                if self.POper[-1] == "<=":
                  self.handle_operation()

                pass

            elif la_ == 9:
                localctx = QuarkParser.NotEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 188
                self.match(QuarkParser.T__28)
                self.POper.append('!=')
                self.state = 190
                self.term()

                if self.POper[-1] == "!=":
                  self.handle_operation()

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
        self.enterRule(localctx, 22, self.RULE_term)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__1, QuarkParser.T__16, QuarkParser.T__22, QuarkParser.T__32, QuarkParser.T__33, QuarkParser.T__34, QuarkParser.ID, QuarkParser.CONST_I, QuarkParser.CONST_F, QuarkParser.STRING]:
                localctx = QuarkParser.JustFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.factor()
                pass
            elif token in [QuarkParser.T__29]:
                localctx = QuarkParser.MultiplicationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(QuarkParser.T__29)
                self.POper.append('*')
                self.state = 198
                self.factor()

                if self.POper[-1] == "*":
                  self.handle_operation()

                pass
            elif token in [QuarkParser.T__30]:
                localctx = QuarkParser.DivisionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.match(QuarkParser.T__30)
                self.POper.append('/')
                self.state = 203
                self.factor()

                if self.POper[-1] == "/":
                  self.handle_operation()

                pass
            elif token in [QuarkParser.T__31]:
                localctx = QuarkParser.ModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 206
                self.match(QuarkParser.T__31)
                self.POper.append('%')
                self.state = 208
                self.factor()

                if self.POper[-1] == "%":
                  self.handle_operation()

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
        self.enterRule(localctx, 24, self.RULE_more_expressions)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(QuarkParser.T__8)
                self.state = 214
                self.expression()
                self.state = 215
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
        self.enterRule(localctx, 26, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__22, QuarkParser.ID, QuarkParser.CONST_I, QuarkParser.CONST_F]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__22:
                    self.state = 220
                    self.match(QuarkParser.T__22)


                self.state = 223
                self.varconst()
                pass
            elif token in [QuarkParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(QuarkParser.T__1)
                self.POper.append('(')
                self.state = 226
                self.expression()
                self.state = 227
                self.match(QuarkParser.T__2)

                if self.POper[-1] == '(':
                  self.POper.pop()
                else:
                  raise Exception("Parenthesis mismatch")

                pass
            elif token in [QuarkParser.T__32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(QuarkParser.T__32)
                self.PilaO.append(('True', "Bool"))
                pass
            elif token in [QuarkParser.T__33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.match(QuarkParser.T__33)
                self.PilaO.append(('False', "Bool"))
                pass
            elif token in [QuarkParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                localctx._STRING = self.match(QuarkParser.STRING)
                self.PilaO.append(((None if localctx._STRING is None else localctx._STRING.text), "String"))
                pass
            elif token in [QuarkParser.T__16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 236
                self.match(QuarkParser.T__16)
                self.state = 237
                self.expression()
                self.state = 238
                self.more_expressions()
                self.state = 239
                self.match(QuarkParser.T__17)
                pass
            elif token in [QuarkParser.T__34]:
                self.enterOuterAlt(localctx, 7)
                self.state = 241
                self.match(QuarkParser.T__34)
                self.PilaO.append(('[]', "[Any]"))
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
        self.enterRule(localctx, 28, self.RULE_varconst)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                localctx._ID = self.match(QuarkParser.ID)

                if (None if localctx._ID is None else localctx._ID.text) not in self.func_directory[self.current_function].vars:
                  raise Exception("ID {} is not defined".format((None if localctx._ID is None else localctx._ID.text)))
                self.PilaO.append(((None if localctx._ID is None else localctx._ID.text), self.func_directory[self.current_function].vars[(None if localctx._ID is None else localctx._ID.text)].type))

                pass
            elif token in [QuarkParser.CONST_I]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                localctx._CONST_I = self.match(QuarkParser.CONST_I)
                self.PilaO.append(((None if localctx._CONST_I is None else localctx._CONST_I.text), "Int"))
                pass
            elif token in [QuarkParser.CONST_F]:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
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
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.statement()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__1) | (1 << QuarkParser.T__9) | (1 << QuarkParser.T__11) | (1 << QuarkParser.T__12) | (1 << QuarkParser.T__13) | (1 << QuarkParser.T__14) | (1 << QuarkParser.T__15) | (1 << QuarkParser.T__16) | (1 << QuarkParser.T__21) | (1 << QuarkParser.T__22) | (1 << QuarkParser.T__23) | (1 << QuarkParser.T__24) | (1 << QuarkParser.T__25) | (1 << QuarkParser.T__26) | (1 << QuarkParser.T__27) | (1 << QuarkParser.T__28) | (1 << QuarkParser.T__29) | (1 << QuarkParser.T__30) | (1 << QuarkParser.T__31) | (1 << QuarkParser.T__32) | (1 << QuarkParser.T__33) | (1 << QuarkParser.T__34) | (1 << QuarkParser.ID) | (1 << QuarkParser.TYPE_ID) | (1 << QuarkParser.CONST_I) | (1 << QuarkParser.CONST_F) | (1 << QuarkParser.STRING))) != 0):
                self.state = 254
                self.statement()
                self.state = 259
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
        self.enterRule(localctx, 32, self.RULE_statement)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.assignment()
                self.state = 261
                self.match(QuarkParser.T__35)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.expression()
                self.state = 264
                self.match(QuarkParser.T__35)
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
        self.enterRule(localctx, 34, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            localctx._ID = self.match(QuarkParser.ID)

            if (None if localctx._ID is None else localctx._ID.text) not in self.func_directory:
              raise Exception("Function {} does not exist".format((None if localctx._ID is None else localctx._ID.text)))

            self.state = 270
            self.match(QuarkParser.T__1)
            self.state = 271
            self.expression()
            self.state = 272
            self.more_expressions()
            self.state = 273
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
        self.enterRule(localctx, 36, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            localctx._typeRule = self.typeRule()
            self.state = 276
            localctx._ID = self.match(QuarkParser.ID)
            self.state = 277
            self.match(QuarkParser.T__19)
            self.state = 278
            self.expression()

            if (None if localctx._ID is None else localctx._ID.text) not in self.func_directory[self.current_function]:
              self.func_directory[self.current_function].vars[(None if localctx._ID is None else localctx._ID.text)] = self.VarRecord((None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))), 0, None)
            else:
              raise Exception("Cannot declare type again")

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
        self.enterRule(localctx, 38, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.things()
            self.state = 282
            self.morethings()
            pp.pprint(self.func_directory); pp.pprint(self.quadruples)
            self.state = 284
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
        self.enterRule(localctx, 40, self.RULE_things)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.func_call()
                self.state = 288
                self.match(QuarkParser.T__35)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 292
                self.typedef()
                self.state = 293
                self.match(QuarkParser.T__35)
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
        self.enterRule(localctx, 42, self.RULE_morethings)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__0, QuarkParser.T__1, QuarkParser.T__9, QuarkParser.T__11, QuarkParser.T__12, QuarkParser.T__13, QuarkParser.T__14, QuarkParser.T__15, QuarkParser.T__16, QuarkParser.T__18, QuarkParser.T__21, QuarkParser.T__22, QuarkParser.T__23, QuarkParser.T__24, QuarkParser.T__25, QuarkParser.T__26, QuarkParser.T__27, QuarkParser.T__28, QuarkParser.T__29, QuarkParser.T__30, QuarkParser.T__31, QuarkParser.T__32, QuarkParser.T__33, QuarkParser.T__34, QuarkParser.ID, QuarkParser.TYPE_ID, QuarkParser.CONST_I, QuarkParser.CONST_F, QuarkParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.things()
                self.state = 298
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





