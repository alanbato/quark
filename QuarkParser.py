# Generated from Quark.g4 by ANTLR 4.7.1
# encoding: utf-8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\u0144\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write("?\n\2\f\2\16\2B\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4X\n")
        buf.write("\4\3\5\3\5\3\5\5\5]\n\5\3\6\3\6\3\6\3\6\5\6c\n\6\3\6\3")
        buf.write("\6\5\6g\n\6\3\6\3\6\5\6k\n\6\3\6\3\6\5\6o\n\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6x\n\6\3\7\3\7\5\7|\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u0088\n\t\f\t\16")
        buf.write("\t\u008b\13\t\3\t\3\t\3\n\3\n\3\n\3\n\7\n\u0093\n\n\f")
        buf.write("\n\16\n\u0096\13\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u009f\n\13\f\13\16\13\u00a2\13\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b1\n\f\3\f\3\f")
        buf.write("\3\f\7\f\u00b6\n\f\f\f\16\f\u00b9\13\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00c0\n\r\3\r\3\r\3\r\7\r\u00c5\n\r\f\r\16\r")
        buf.write("\u00c8\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00d1")
        buf.write("\n\16\3\16\3\16\3\16\7\16\u00d6\n\16\f\16\16\16\u00d9")
        buf.write("\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u00f3\n\17\f\17\16\17\u00f6")
        buf.write("\13\17\3\17\3\17\3\17\3\17\3\17\5\17\u00fd\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\5\20\u0106\n\20\3\21\3\21")
        buf.write("\7\21\u010a\n\21\f\21\16\21\u010d\13\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u0115\n\22\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u011b\n\23\3\23\3\23\7\23\u011f\n\23\f\23\16\23\u0122")
        buf.write("\13\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u013c\n\26\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u0142\n\27\3\27\2\2\30\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,\2\2\2\u015e\2.\3\2\2\2\4J\3\2")
        buf.write("\2\2\6W\3\2\2\2\b\\\3\2\2\2\nw\3\2\2\2\f{\3\2\2\2\16}")
        buf.write("\3\2\2\2\20\u0083\3\2\2\2\22\u008e\3\2\2\2\24\u009a\3")
        buf.write("\2\2\2\26\u00a3\3\2\2\2\30\u00ba\3\2\2\2\32\u00c9\3\2")
        buf.write("\2\2\34\u00fc\3\2\2\2\36\u0105\3\2\2\2 \u0107\3\2\2\2")
        buf.write("\"\u0114\3\2\2\2$\u0116\3\2\2\2&\u0126\3\2\2\2(\u012c")
        buf.write("\3\2\2\2*\u013b\3\2\2\2,\u0141\3\2\2\2./\7\3\2\2/\60\7")
        buf.write("(\2\2\60\61\b\2\1\2\61\62\7\4\2\2\62\63\5\4\3\2\63\64")
        buf.write("\7\5\2\2\64\65\7\6\2\2\65\66\5\n\6\2\66\67\b\2\1\2\67")
        buf.write("@\7\7\2\289\5\22\n\29:\7\7\2\2:;\5 \21\2;<\7\b\2\2<=\b")
        buf.write("\2\1\2=?\3\2\2\2>8\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2")
        buf.write("\2AC\3\2\2\2B@\3\2\2\2CD\7\t\2\2DE\5 \21\2EF\7\b\2\2F")
        buf.write("G\b\2\1\2GH\7\b\2\2HI\b\2\1\2I\3\3\2\2\2JK\7(\2\2KL\7")
        buf.write("\n\2\2LM\5\n\6\2MN\b\3\1\2NO\5\6\4\2O\5\3\2\2\2PQ\7\13")
        buf.write("\2\2QR\7(\2\2RS\7\n\2\2ST\5\n\6\2TU\b\4\1\2UX\3\2\2\2")
        buf.write("VX\3\2\2\2WP\3\2\2\2WV\3\2\2\2X\7\3\2\2\2YZ\7\13\2\2Z")
        buf.write("]\5\n\6\2[]\3\2\2\2\\Y\3\2\2\2\\[\3\2\2\2]\t\3\2\2\2^")
        buf.write("_\7)\2\2_x\b\6\1\2`b\7\f\2\2ac\7\r\2\2ba\3\2\2\2bc\3\2")
        buf.write("\2\2cx\3\2\2\2df\7\16\2\2eg\7\r\2\2fe\3\2\2\2fg\3\2\2")
        buf.write("\2gx\3\2\2\2hj\7\17\2\2ik\7\r\2\2ji\3\2\2\2jk\3\2\2\2")
        buf.write("kx\3\2\2\2ln\7\20\2\2mo\7\r\2\2nm\3\2\2\2no\3\2\2\2ox")
        buf.write("\3\2\2\2px\7\21\2\2qx\7\22\2\2rs\7\23\2\2st\5\n\6\2tu")
        buf.write("\5\b\5\2uv\7\24\2\2vx\3\2\2\2w^\3\2\2\2w`\3\2\2\2wd\3")
        buf.write("\2\2\2wh\3\2\2\2wl\3\2\2\2wp\3\2\2\2wq\3\2\2\2wr\3\2\2")
        buf.write("\2x\13\3\2\2\2y|\5\n\6\2z|\5\20\t\2{y\3\2\2\2{z\3\2\2")
        buf.write("\2|\r\3\2\2\2}~\7\25\2\2~\177\7)\2\2\177\u0080\7\26\2")
        buf.write("\2\u0080\u0081\5\f\7\2\u0081\u0082\b\b\1\2\u0082\17\3")
        buf.write("\2\2\2\u0083\u0084\7\4\2\2\u0084\u0089\5\n\6\2\u0085\u0086")
        buf.write("\7\27\2\2\u0086\u0088\5\n\6\2\u0087\u0085\3\2\2\2\u0088")
        buf.write("\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\7")
        buf.write("\5\2\2\u008d\21\3\2\2\2\u008e\u008f\7\4\2\2\u008f\u0094")
        buf.write("\5\24\13\2\u0090\u0091\7\13\2\2\u0091\u0093\5\24\13\2")
        buf.write("\u0092\u0090\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3")
        buf.write("\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0097\u0098\7\5\2\2\u0098\u0099\b\n\1\2\u0099")
        buf.write("\23\3\2\2\2\u009a\u00a0\5\26\f\2\u009b\u009c\5\26\f\2")
        buf.write("\u009c\u009d\5\30\r\2\u009d\u009f\3\2\2\2\u009e\u009b")
        buf.write("\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\25\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3")
        buf.write("\u00b7\5\30\r\2\u00a4\u00a5\7\30\2\2\u00a5\u00b1\b\f\1")
        buf.write("\2\u00a6\u00a7\7\31\2\2\u00a7\u00b1\b\f\1\2\u00a8\u00a9")
        buf.write("\7\32\2\2\u00a9\u00b1\b\f\1\2\u00aa\u00ab\7\33\2\2\u00ab")
        buf.write("\u00b1\b\f\1\2\u00ac\u00ad\7\34\2\2\u00ad\u00b1\b\f\1")
        buf.write("\2\u00ae\u00af\7\35\2\2\u00af\u00b1\b\f\1\2\u00b0\u00a4")
        buf.write("\3\2\2\2\u00b0\u00a6\3\2\2\2\u00b0\u00a8\3\2\2\2\u00b0")
        buf.write("\u00aa\3\2\2\2\u00b0\u00ac\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b3\5\30\r\2\u00b3\u00b4")
        buf.write("\b\f\1\2\u00b4\u00b6\3\2\2\2\u00b5\u00b0\3\2\2\2\u00b6")
        buf.write("\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\27\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00c6\5\32")
        buf.write("\16\2\u00bb\u00bc\7\36\2\2\u00bc\u00c0\b\r\1\2\u00bd\u00be")
        buf.write("\7\37\2\2\u00be\u00c0\b\r\1\2\u00bf\u00bb\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\5\32\16")
        buf.write("\2\u00c2\u00c3\b\r\1\2\u00c3\u00c5\3\2\2\2\u00c4\u00bf")
        buf.write("\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\31\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9")
        buf.write("\u00d7\5\34\17\2\u00ca\u00cb\7 \2\2\u00cb\u00d1\b\16\1")
        buf.write("\2\u00cc\u00cd\7!\2\2\u00cd\u00d1\b\16\1\2\u00ce\u00cf")
        buf.write("\7\"\2\2\u00cf\u00d1\b\16\1\2\u00d0\u00ca\3\2\2\2\u00d0")
        buf.write("\u00cc\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d3\5\34\17\2\u00d3\u00d4\b\16\1\2\u00d4\u00d6")
        buf.write("\3\2\2\2\u00d5\u00d0\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\33\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00da\u00fd\5\36\20\2\u00db\u00dc\7#\2")
        buf.write("\2\u00dc\u00dd\b\17\1\2\u00dd\u00de\5\36\20\2\u00de\u00df")
        buf.write("\7\5\2\2\u00df\u00fd\3\2\2\2\u00e0\u00e1\7\4\2\2\u00e1")
        buf.write("\u00e2\b\17\1\2\u00e2\u00e3\5\24\13\2\u00e3\u00e4\7\5")
        buf.write("\2\2\u00e4\u00e5\b\17\1\2\u00e5\u00fd\3\2\2\2\u00e6\u00e7")
        buf.write("\7$\2\2\u00e7\u00fd\b\17\1\2\u00e8\u00e9\7%\2\2\u00e9")
        buf.write("\u00fd\b\17\1\2\u00ea\u00eb\7\21\2\2\u00eb\u00fd\b\17")
        buf.write("\1\2\u00ec\u00ed\7,\2\2\u00ed\u00fd\b\17\1\2\u00ee\u00ef")
        buf.write("\7\23\2\2\u00ef\u00f4\5\24\13\2\u00f0\u00f1\7\13\2\2\u00f1")
        buf.write("\u00f3\5\24\13\2\u00f2\u00f0\3\2\2\2\u00f3\u00f6\3\2\2")
        buf.write("\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\7\24\2\2\u00f8")
        buf.write("\u00f9\b\17\1\2\u00f9\u00fd\3\2\2\2\u00fa\u00fb\7&\2\2")
        buf.write("\u00fb\u00fd\b\17\1\2\u00fc\u00da\3\2\2\2\u00fc\u00db")
        buf.write("\3\2\2\2\u00fc\u00e0\3\2\2\2\u00fc\u00e6\3\2\2\2\u00fc")
        buf.write("\u00e8\3\2\2\2\u00fc\u00ea\3\2\2\2\u00fc\u00ec\3\2\2\2")
        buf.write("\u00fc\u00ee\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\35\3\2")
        buf.write("\2\2\u00fe\u0106\5$\23\2\u00ff\u0100\7(\2\2\u0100\u0106")
        buf.write("\b\20\1\2\u0101\u0102\7*\2\2\u0102\u0106\b\20\1\2\u0103")
        buf.write("\u0104\7+\2\2\u0104\u0106\b\20\1\2\u0105\u00fe\3\2\2\2")
        buf.write("\u0105\u00ff\3\2\2\2\u0105\u0101\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0106\37\3\2\2\2\u0107\u010b\5\"\22\2\u0108\u010a")
        buf.write("\5\"\22\2\u0109\u0108\3\2\2\2\u010a\u010d\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c!\3\2\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010e\u010f\5&\24\2\u010f\u0110\7\'\2\2")
        buf.write("\u0110\u0115\3\2\2\2\u0111\u0112\5\24\13\2\u0112\u0113")
        buf.write("\7\'\2\2\u0113\u0115\3\2\2\2\u0114\u010e\3\2\2\2\u0114")
        buf.write("\u0111\3\2\2\2\u0115#\3\2\2\2\u0116\u0117\7(\2\2\u0117")
        buf.write("\u0118\b\23\1\2\u0118\u011a\7\4\2\2\u0119\u011b\5\24\13")
        buf.write("\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u0120")
        buf.write("\3\2\2\2\u011c\u011d\7\13\2\2\u011d\u011f\5\24\13\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0123\u0124\7\5\2\2\u0124\u0125\b\23\1\2\u0125")
        buf.write("%\3\2\2\2\u0126\u0127\5\n\6\2\u0127\u0128\7(\2\2\u0128")
        buf.write("\u0129\7\26\2\2\u0129\u012a\5\24\13\2\u012a\u012b\b\24")
        buf.write("\1\2\u012b\'\3\2\2\2\u012c\u012d\5*\26\2\u012d\u012e\5")
        buf.write(",\27\2\u012e\u012f\b\25\1\2\u012f\u0130\7\2\2\3\u0130")
        buf.write(")\3\2\2\2\u0131\u013c\5\2\2\2\u0132\u0133\5&\24\2\u0133")
        buf.write("\u0134\7\'\2\2\u0134\u013c\3\2\2\2\u0135\u0136\5\24\13")
        buf.write("\2\u0136\u0137\7\'\2\2\u0137\u013c\3\2\2\2\u0138\u0139")
        buf.write("\5\16\b\2\u0139\u013a\7\'\2\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u0131\3\2\2\2\u013b\u0132\3\2\2\2\u013b\u0135\3\2\2\2")
        buf.write("\u013b\u0138\3\2\2\2\u013c+\3\2\2\2\u013d\u013e\5*\26")
        buf.write("\2\u013e\u013f\5,\27\2\u013f\u0142\3\2\2\2\u0140\u0142")
        buf.write("\3\2\2\2\u0141\u013d\3\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("-\3\2\2\2\35@W\\bfjnw{\u0089\u0094\u00a0\u00b0\u00b7\u00bf")
        buf.write("\u00c6\u00d0\u00d7\u00f4\u00fc\u0105\u010b\u0114\u011a")
        buf.write("\u0120\u013b\u0141")
        return buf.getvalue()


class QuarkParser ( Parser ):

    grammarFileName = "Quark.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'('", "')'", "'->'", "'{'", 
                     "'}'", "'default {'", "':'", "','", "'Int'", "'?'", 
                     "'Bool'", "'Float'", "'String'", "'non'", "'Any'", 
                     "'['", "']'", "'type'", "'<-'", "'|'", "'>'", "'<'", 
                     "'='", "'>='", "'<='", "'!='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'(-'", "'True'", "'False'", "'[]'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "TYPE_ID", "CONST_I", 
                      "CONST_F", "STRING", "SPACE" ]

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
    RULE_comp = 10
    RULE_exp = 11
    RULE_term = 12
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
                   "comp", "exp", "term", "factor", "varconst", "block", 
                   "statement", "func_call", "assignment", "main", "things", 
                   "morethings" ]

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
    T__36=37
    ID=38
    TYPE_ID=39
    CONST_I=40
    CONST_F=41
    STRING=42
    SPACE=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



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
            c.define_function((None if localctx._ID is None else localctx._ID.text))
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

            c.set_function_return_type((None if localctx._ID is None else localctx._ID.text), (None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))))

            self.state = 53
            self.match(QuarkParser.T__4)
            self.state = 62
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
                c.process_function_clause()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(QuarkParser.T__6)
            self.state = 66
            self.block()
            self.state = 67
            self.match(QuarkParser.T__5)
            c.process_default_clause()
            		
            self.state = 69
            self.match(QuarkParser.T__5)
            c.process_function_end()
            		
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
            self.state = 72
            localctx._ID = self.match(QuarkParser.ID)
            self.state = 73
            self.match(QuarkParser.T__7)
            self.state = 74
            localctx._typeRule = self.typeRule()
            c.process_param((None if localctx._ID is None else localctx._ID.text), (None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))))
            self.state = 76
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
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(QuarkParser.T__8)
                self.state = 79
                localctx._ID = self.match(QuarkParser.ID)
                self.state = 80
                self.match(QuarkParser.T__7)
                self.state = 81
                localctx._typeRule = self.typeRule()
                c.process_param((None if localctx._ID is None else localctx._ID.text), (None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))))
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(QuarkParser.T__8)
                self.state = 88
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
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.TYPE_ID]:
                localctx = QuarkParser.UserTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                localctx._TYPE_ID = self.match(QuarkParser.TYPE_ID)
                c.check_user_def_type((None if localctx._TYPE_ID is None else localctx._TYPE_ID.text))
                pass
            elif token in [QuarkParser.T__9]:
                localctx = QuarkParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(QuarkParser.T__9)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 95
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__11]:
                localctx = QuarkParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.match(QuarkParser.T__11)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 99
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__12]:
                localctx = QuarkParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(QuarkParser.T__12)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 103
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__13]:
                localctx = QuarkParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.match(QuarkParser.T__13)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuarkParser.T__10:
                    self.state = 107
                    self.match(QuarkParser.T__10)


                pass
            elif token in [QuarkParser.T__14]:
                localctx = QuarkParser.NoneContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 110
                self.match(QuarkParser.T__14)
                pass
            elif token in [QuarkParser.T__15]:
                localctx = QuarkParser.AnyContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.match(QuarkParser.T__15)
                pass
            elif token in [QuarkParser.T__16]:
                localctx = QuarkParser.ListOfTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 112
                self.match(QuarkParser.T__16)
                self.state = 113
                self.typeRule()
                self.state = 114
                self.moreTypes()
                self.state = 115
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__9, QuarkParser.T__11, QuarkParser.T__12, QuarkParser.T__13, QuarkParser.T__14, QuarkParser.T__15, QuarkParser.T__16, QuarkParser.TYPE_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.typeRule()
                pass
            elif token in [QuarkParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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
            self.state = 123
            self.match(QuarkParser.T__18)
            self.state = 124
            localctx._TYPE_ID = self.match(QuarkParser.TYPE_ID)
            self.state = 125
            self.match(QuarkParser.T__19)
            self.state = 126
            self.typevalue()
            c.define_type((None if localctx._TYPE_ID is None else localctx._TYPE_ID.text))
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
            self.state = 129
            self.match(QuarkParser.T__1)
            self.state = 130
            self.typeRule()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__20:
                self.state = 131
                self.match(QuarkParser.T__20)
                self.state = 132
                self.typeRule()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(QuarkParser.T__2)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuarkParser.ExpressionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(QuarkParser.T__1)
            self.state = 141
            self.expression()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__8:
                self.state = 142
                self.match(QuarkParser.T__8)
                self.state = 143
                self.expression()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(QuarkParser.T__2)
            c.condition()
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

        def comp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.CompContext)
            else:
                return self.getTypedRuleContext(QuarkParser.CompContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.ExpContext)
            else:
                return self.getTypedRuleContext(QuarkParser.ExpContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.comp()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__1) | (1 << QuarkParser.T__14) | (1 << QuarkParser.T__16) | (1 << QuarkParser.T__32) | (1 << QuarkParser.T__33) | (1 << QuarkParser.T__34) | (1 << QuarkParser.T__35) | (1 << QuarkParser.ID) | (1 << QuarkParser.CONST_I) | (1 << QuarkParser.CONST_F) | (1 << QuarkParser.STRING))) != 0):
                self.state = 153
                self.comp()
                self.state = 154
                self.exp()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.ExpContext)
            else:
                return self.getTypedRuleContext(QuarkParser.ExpContext,i)


        def getRuleIndex(self):
            return QuarkParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = QuarkParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.exp()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__21) | (1 << QuarkParser.T__22) | (1 << QuarkParser.T__23) | (1 << QuarkParser.T__24) | (1 << QuarkParser.T__25) | (1 << QuarkParser.T__26))) != 0):
                self.state = 174
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [QuarkParser.T__21]:
                    self.state = 162
                    self.match(QuarkParser.T__21)
                    c.add_operator('>')
                    pass
                elif token in [QuarkParser.T__22]:
                    self.state = 164
                    self.match(QuarkParser.T__22)
                    c.add_operator('<')
                    pass
                elif token in [QuarkParser.T__23]:
                    self.state = 166
                    self.match(QuarkParser.T__23)
                    c.add_operator('=')
                    pass
                elif token in [QuarkParser.T__24]:
                    self.state = 168
                    self.match(QuarkParser.T__24)
                    c.add_operator('>=')
                    pass
                elif token in [QuarkParser.T__25]:
                    self.state = 170
                    self.match(QuarkParser.T__25)
                    c.add_operator('<=')
                    pass
                elif token in [QuarkParser.T__26]:
                    self.state = 172
                    self.match(QuarkParser.T__26)
                    c.add_operator('!=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 176
                self.exp()
                c.handle_math_operation(">", "<", "=", ">=", "<=", "!=")
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.TermContext)
            else:
                return self.getTypedRuleContext(QuarkParser.TermContext,i)


        def getRuleIndex(self):
            return QuarkParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = QuarkParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.term()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__27 or _la==QuarkParser.T__28:
                self.state = 189
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [QuarkParser.T__27]:
                    self.state = 185
                    self.match(QuarkParser.T__27)
                    c.add_operator('+')
                    pass
                elif token in [QuarkParser.T__28]:
                    self.state = 187
                    self.match(QuarkParser.T__28)
                    c.add_operator('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 191
                self.term()
                c.handle_math_operation("+", "-")
                			
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.FactorContext)
            else:
                return self.getTypedRuleContext(QuarkParser.FactorContext,i)


        def getRuleIndex(self):
            return QuarkParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = QuarkParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.factor()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__29) | (1 << QuarkParser.T__30) | (1 << QuarkParser.T__31))) != 0):
                self.state = 206
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [QuarkParser.T__29]:
                    self.state = 200
                    self.match(QuarkParser.T__29)
                    c.add_operator('*')
                    pass
                elif token in [QuarkParser.T__30]:
                    self.state = 202
                    self.match(QuarkParser.T__30)
                    c.add_operator('/')
                    pass
                elif token in [QuarkParser.T__31]:
                    self.state = 204
                    self.match(QuarkParser.T__31)
                    c.add_operator('%')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 208
                self.factor()
                c.handle_math_operation("*", "/", "%")
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def getRuleIndex(self):
            return QuarkParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyListContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyList" ):
                listener.enterEmptyList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyList" ):
                listener.exitEmptyList(self)


    class NegativeContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varconst(self):
            return self.getTypedRuleContext(QuarkParser.VarconstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative" ):
                listener.enterNegative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative" ):
                listener.exitNegative(self)


    class StringLiteralContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self._STRING = None # Token
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(QuarkParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)


    class PositiveContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varconst(self):
            return self.getTypedRuleContext(QuarkParser.VarconstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositive" ):
                listener.enterPositive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositive" ):
                listener.exitPositive(self)


    class ParensContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(QuarkParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class TrueContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)


    class ListContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuarkParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)


    class FalseContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuarkParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)



    def factor(self):

        localctx = QuarkParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.ID, QuarkParser.CONST_I, QuarkParser.CONST_F]:
                localctx = QuarkParser.PositiveContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.varconst()
                pass
            elif token in [QuarkParser.T__32]:
                localctx = QuarkParser.NegativeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(QuarkParser.T__32)
                c.set_negative()
                self.state = 219
                self.varconst()
                self.state = 220
                self.match(QuarkParser.T__2)
                pass
            elif token in [QuarkParser.T__1]:
                localctx = QuarkParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(QuarkParser.T__1)
                c.start_parens()
                self.state = 224
                self.expression()
                self.state = 225
                self.match(QuarkParser.T__2)
                c.end_parens()
                pass
            elif token in [QuarkParser.T__33]:
                localctx = QuarkParser.TrueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.match(QuarkParser.T__33)
                c.add_literal('True', "Bool")
                pass
            elif token in [QuarkParser.T__34]:
                localctx = QuarkParser.FalseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.match(QuarkParser.T__34)
                c.add_literal('False', "Bool")
                pass
            elif token in [QuarkParser.T__14]:
                localctx = QuarkParser.FalseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 232
                self.match(QuarkParser.T__14)
                c.add_literal('non', "non")
                pass
            elif token in [QuarkParser.STRING]:
                localctx = QuarkParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 234
                localctx._STRING = self.match(QuarkParser.STRING)
                c.get_math_literal((None if localctx._STRING is None else localctx._STRING.text), "String")
                pass
            elif token in [QuarkParser.T__16]:
                localctx = QuarkParser.ListContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 236
                self.match(QuarkParser.T__16)
                self.state = 237
                self.expression()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==QuarkParser.T__8:
                    self.state = 238
                    self.match(QuarkParser.T__8)
                    self.state = 239
                    self.expression()
                    self.state = 244
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 245
                self.match(QuarkParser.T__17)
                #TODO Handle Lists
                pass
            elif token in [QuarkParser.T__35]:
                localctx = QuarkParser.EmptyListContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 248
                self.match(QuarkParser.T__35)
                c.add_literal('[]', "[Any]")
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

        def func_call(self):
            return self.getTypedRuleContext(QuarkParser.Func_callContext,0)


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
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                localctx._ID = self.match(QuarkParser.ID)
                c.get_variable((None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                localctx._CONST_I = self.match(QuarkParser.CONST_I)
                c.get_math_literal((None if localctx._CONST_I is None else localctx._CONST_I.text), "Int")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                localctx._CONST_F = self.match(QuarkParser.CONST_F)
                c.get_math_literal((None if localctx._CONST_F is None else localctx._CONST_F.text), "Float")
                pass


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
            self.state = 261
            self.statement()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__1) | (1 << QuarkParser.T__9) | (1 << QuarkParser.T__11) | (1 << QuarkParser.T__12) | (1 << QuarkParser.T__13) | (1 << QuarkParser.T__14) | (1 << QuarkParser.T__15) | (1 << QuarkParser.T__16) | (1 << QuarkParser.T__32) | (1 << QuarkParser.T__33) | (1 << QuarkParser.T__34) | (1 << QuarkParser.T__35) | (1 << QuarkParser.ID) | (1 << QuarkParser.TYPE_ID) | (1 << QuarkParser.CONST_I) | (1 << QuarkParser.CONST_F) | (1 << QuarkParser.STRING))) != 0):
                self.state = 262
                self.statement()
                self.state = 267
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
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.assignment()
                self.state = 269
                self.match(QuarkParser.T__36)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.expression()
                self.state = 272
                self.match(QuarkParser.T__36)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuarkParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuarkParser.ExpressionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            localctx._ID = self.match(QuarkParser.ID)
            c.check_function((None if localctx._ID is None else localctx._ID.text))
            self.state = 278
            self.match(QuarkParser.T__1)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuarkParser.T__1) | (1 << QuarkParser.T__14) | (1 << QuarkParser.T__16) | (1 << QuarkParser.T__32) | (1 << QuarkParser.T__33) | (1 << QuarkParser.T__34) | (1 << QuarkParser.T__35) | (1 << QuarkParser.ID) | (1 << QuarkParser.CONST_I) | (1 << QuarkParser.CONST_F) | (1 << QuarkParser.STRING))) != 0):
                self.state = 279
                self.expression()


            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuarkParser.T__8:
                self.state = 282
                self.match(QuarkParser.T__8)
                self.state = 283
                self.expression()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
            self.match(QuarkParser.T__2)
            c.call_function((None if localctx._ID is None else localctx._ID.text))
            			
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
            self.state = 292
            localctx._typeRule = self.typeRule()
            self.state = 293
            localctx._ID = self.match(QuarkParser.ID)
            self.state = 294
            self.match(QuarkParser.T__19)
            self.state = 295
            self.expression()
            c.handle_assignment((None if localctx._ID is None else localctx._ID.text), (None if localctx._typeRule is None else self._input.getText((localctx._typeRule.start,localctx._typeRule.stop))))
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
            self.state = 298
            self.things()
            self.state = 299
            self.morethings()
            c.print_state(); c.save_state(self)
            self.state = 301
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
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.assignment()
                self.state = 305
                self.match(QuarkParser.T__36)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.expression()
                self.state = 308
                self.match(QuarkParser.T__36)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.typedef()
                self.state = 311
                self.match(QuarkParser.T__36)
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
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuarkParser.T__0, QuarkParser.T__1, QuarkParser.T__9, QuarkParser.T__11, QuarkParser.T__12, QuarkParser.T__13, QuarkParser.T__14, QuarkParser.T__15, QuarkParser.T__16, QuarkParser.T__18, QuarkParser.T__32, QuarkParser.T__33, QuarkParser.T__34, QuarkParser.T__35, QuarkParser.ID, QuarkParser.TYPE_ID, QuarkParser.CONST_I, QuarkParser.CONST_F, QuarkParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.things()
                self.state = 316
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





