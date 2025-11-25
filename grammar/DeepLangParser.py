# Generated from grammar/DeepLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


# deeplang ANTLR grammar - generated

def serializedATN():
    return [
        4,1,50,375,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,2,1,2,3,2,80,
        8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,90,8,4,1,5,1,5,1,5,1,5,1,
        6,1,6,3,6,98,8,6,1,7,1,7,1,7,1,7,5,7,104,8,7,10,7,12,7,107,9,7,1,
        8,1,8,1,8,3,8,112,8,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,
        10,123,8,10,1,11,1,11,1,11,1,11,3,11,129,8,11,1,11,1,11,1,11,3,11,
        134,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,5,12,145,8,
        12,10,12,12,12,148,9,12,1,13,1,13,1,13,3,13,153,8,13,1,13,1,13,3,
        13,157,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,5,14,174,8,14,10,14,12,14,177,9,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,3,14,186,8,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,212,8,17,10,17,12,17,215,9,
        17,1,17,3,17,218,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,
        19,1,19,1,19,5,19,231,8,19,10,19,12,19,234,9,19,1,20,1,20,1,20,5,
        20,239,8,20,10,20,12,20,242,9,20,1,21,1,21,1,21,3,21,247,8,21,1,
        22,1,22,1,22,5,22,252,8,22,10,22,12,22,255,9,22,1,23,1,23,1,23,5,
        23,260,8,23,10,23,12,23,263,9,23,1,24,1,24,1,24,5,24,268,8,24,10,
        24,12,24,271,9,24,1,25,1,25,1,25,3,25,276,8,25,1,26,1,26,1,26,3,
        26,281,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,3,27,298,8,27,1,28,1,28,1,28,3,28,303,8,28,
        1,28,1,28,1,29,1,29,1,29,5,29,310,8,29,10,29,12,29,313,9,29,1,29,
        3,29,316,8,29,1,30,1,30,1,30,1,30,1,30,5,30,323,8,30,10,30,12,30,
        326,9,30,1,30,1,30,1,31,1,31,1,31,1,31,5,31,334,8,31,10,31,12,31,
        337,9,31,3,31,339,8,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,5,32,348,
        8,32,10,32,12,32,351,9,32,1,32,1,32,1,32,1,32,1,32,1,32,5,32,359,
        8,32,10,32,12,32,362,9,32,1,32,1,32,5,32,366,8,32,10,32,12,32,369,
        9,32,1,32,1,32,1,33,1,33,1,33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,0,3,3,0,10,10,15,15,32,37,1,0,26,27,2,0,28,30,39,39,390,0,68,
        1,0,0,0,2,74,1,0,0,0,4,79,1,0,0,0,6,81,1,0,0,0,8,89,1,0,0,0,10,91,
        1,0,0,0,12,95,1,0,0,0,14,99,1,0,0,0,16,108,1,0,0,0,18,115,1,0,0,
        0,20,122,1,0,0,0,22,124,1,0,0,0,24,141,1,0,0,0,26,149,1,0,0,0,28,
        158,1,0,0,0,30,187,1,0,0,0,32,195,1,0,0,0,34,205,1,0,0,0,36,225,
        1,0,0,0,38,227,1,0,0,0,40,235,1,0,0,0,42,246,1,0,0,0,44,248,1,0,
        0,0,46,256,1,0,0,0,48,264,1,0,0,0,50,275,1,0,0,0,52,277,1,0,0,0,
        54,297,1,0,0,0,56,299,1,0,0,0,58,306,1,0,0,0,60,317,1,0,0,0,62,329,
        1,0,0,0,64,342,1,0,0,0,66,372,1,0,0,0,68,69,3,2,1,0,69,70,5,0,0,
        1,70,1,1,0,0,0,71,73,3,4,2,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,
        0,0,0,74,75,1,0,0,0,75,3,1,0,0,0,76,74,1,0,0,0,77,80,3,6,3,0,78,
        80,3,20,10,0,79,77,1,0,0,0,79,78,1,0,0,0,80,5,1,0,0,0,81,82,3,8,
        4,0,82,83,5,25,0,0,83,7,1,0,0,0,84,90,3,10,5,0,85,90,3,12,6,0,86,
        90,3,14,7,0,87,90,3,16,8,0,88,90,3,18,9,0,89,84,1,0,0,0,89,85,1,
        0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,9,1,0,0,0,91,
        92,5,22,0,0,92,93,5,31,0,0,93,94,3,36,18,0,94,11,1,0,0,0,95,97,5,
        1,0,0,96,98,3,36,18,0,97,96,1,0,0,0,97,98,1,0,0,0,98,13,1,0,0,0,
        99,100,5,2,0,0,100,105,5,22,0,0,101,102,5,41,0,0,102,104,5,22,0,
        0,103,101,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,
        0,106,15,1,0,0,0,107,105,1,0,0,0,108,109,5,3,0,0,109,111,5,43,0,
        0,110,112,3,36,18,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,1,0,
        0,0,113,114,5,44,0,0,114,17,1,0,0,0,115,116,3,36,18,0,116,19,1,0,
        0,0,117,123,3,22,11,0,118,123,3,28,14,0,119,123,3,30,15,0,120,123,
        3,32,16,0,121,123,3,34,17,0,122,117,1,0,0,0,122,118,1,0,0,0,122,
        119,1,0,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,21,1,0,0,0,124,125,
        5,4,0,0,125,126,5,22,0,0,126,128,5,43,0,0,127,129,3,24,12,0,128,
        127,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,133,5,44,0,0,131,
        132,5,40,0,0,132,134,3,66,33,0,133,131,1,0,0,0,133,134,1,0,0,0,134,
        135,1,0,0,0,135,136,5,42,0,0,136,137,5,25,0,0,137,138,5,49,0,0,138,
        139,3,2,1,0,139,140,5,50,0,0,140,23,1,0,0,0,141,146,3,26,13,0,142,
        143,5,41,0,0,143,145,3,26,13,0,144,142,1,0,0,0,145,148,1,0,0,0,146,
        144,1,0,0,0,146,147,1,0,0,0,147,25,1,0,0,0,148,146,1,0,0,0,149,152,
        5,22,0,0,150,151,5,42,0,0,151,153,3,66,33,0,152,150,1,0,0,0,152,
        153,1,0,0,0,153,156,1,0,0,0,154,155,5,31,0,0,155,157,3,36,18,0,156,
        154,1,0,0,0,156,157,1,0,0,0,157,27,1,0,0,0,158,159,5,5,0,0,159,160,
        3,36,18,0,160,161,5,42,0,0,161,162,5,25,0,0,162,163,5,49,0,0,163,
        164,3,2,1,0,164,175,5,50,0,0,165,166,5,6,0,0,166,167,3,36,18,0,167,
        168,5,42,0,0,168,169,5,25,0,0,169,170,5,49,0,0,170,171,3,2,1,0,171,
        172,5,50,0,0,172,174,1,0,0,0,173,165,1,0,0,0,174,177,1,0,0,0,175,
        173,1,0,0,0,175,176,1,0,0,0,176,185,1,0,0,0,177,175,1,0,0,0,178,
        179,5,7,0,0,179,180,5,42,0,0,180,181,5,25,0,0,181,182,5,49,0,0,182,
        183,3,2,1,0,183,184,5,50,0,0,184,186,1,0,0,0,185,178,1,0,0,0,185,
        186,1,0,0,0,186,29,1,0,0,0,187,188,5,8,0,0,188,189,3,36,18,0,189,
        190,5,42,0,0,190,191,5,25,0,0,191,192,5,49,0,0,192,193,3,2,1,0,193,
        194,5,50,0,0,194,31,1,0,0,0,195,196,5,9,0,0,196,197,5,22,0,0,197,
        198,5,10,0,0,198,199,3,36,18,0,199,200,5,42,0,0,200,201,5,25,0,0,
        201,202,5,49,0,0,202,203,3,2,1,0,203,204,5,50,0,0,204,33,1,0,0,0,
        205,206,5,11,0,0,206,217,5,22,0,0,207,208,5,43,0,0,208,213,5,22,
        0,0,209,210,5,41,0,0,210,212,5,22,0,0,211,209,1,0,0,0,212,215,1,
        0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,213,1,
        0,0,0,216,218,5,44,0,0,217,207,1,0,0,0,217,218,1,0,0,0,218,219,1,
        0,0,0,219,220,5,42,0,0,220,221,5,25,0,0,221,222,5,49,0,0,222,223,
        3,2,1,0,223,224,5,50,0,0,224,35,1,0,0,0,225,226,3,38,19,0,226,37,
        1,0,0,0,227,232,3,40,20,0,228,229,5,12,0,0,229,231,3,40,20,0,230,
        228,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,
        39,1,0,0,0,234,232,1,0,0,0,235,240,3,42,21,0,236,237,5,13,0,0,237,
        239,3,42,21,0,238,236,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,
        241,1,0,0,0,241,41,1,0,0,0,242,240,1,0,0,0,243,244,5,14,0,0,244,
        247,3,42,21,0,245,247,3,44,22,0,246,243,1,0,0,0,246,245,1,0,0,0,
        247,43,1,0,0,0,248,253,3,46,23,0,249,250,7,0,0,0,250,252,3,46,23,
        0,251,249,1,0,0,0,252,255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,
        0,254,45,1,0,0,0,255,253,1,0,0,0,256,261,3,48,24,0,257,258,7,1,0,
        0,258,260,3,48,24,0,259,257,1,0,0,0,260,263,1,0,0,0,261,259,1,0,
        0,0,261,262,1,0,0,0,262,47,1,0,0,0,263,261,1,0,0,0,264,269,3,50,
        25,0,265,266,7,2,0,0,266,268,3,50,25,0,267,265,1,0,0,0,268,271,1,
        0,0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,49,1,0,0,0,271,269,1,0,
        0,0,272,273,7,1,0,0,273,276,3,50,25,0,274,276,3,52,26,0,275,272,
        1,0,0,0,275,274,1,0,0,0,276,51,1,0,0,0,277,280,3,54,27,0,278,279,
        5,38,0,0,279,281,3,50,25,0,280,278,1,0,0,0,280,281,1,0,0,0,281,53,
        1,0,0,0,282,298,5,22,0,0,283,298,5,19,0,0,284,298,5,20,0,0,285,298,
        5,21,0,0,286,298,5,16,0,0,287,298,5,17,0,0,288,298,5,18,0,0,289,
        290,5,43,0,0,290,291,3,36,18,0,291,292,5,44,0,0,292,298,1,0,0,0,
        293,298,3,62,31,0,294,298,3,64,32,0,295,298,3,56,28,0,296,298,3,
        60,30,0,297,282,1,0,0,0,297,283,1,0,0,0,297,284,1,0,0,0,297,285,
        1,0,0,0,297,286,1,0,0,0,297,287,1,0,0,0,297,288,1,0,0,0,297,289,
        1,0,0,0,297,293,1,0,0,0,297,294,1,0,0,0,297,295,1,0,0,0,297,296,
        1,0,0,0,298,55,1,0,0,0,299,300,5,22,0,0,300,302,5,43,0,0,301,303,
        3,58,29,0,302,301,1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,
        5,44,0,0,305,57,1,0,0,0,306,311,3,36,18,0,307,308,5,41,0,0,308,310,
        3,36,18,0,309,307,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,
        1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,314,316,5,41,0,0,315,314,
        1,0,0,0,315,316,1,0,0,0,316,59,1,0,0,0,317,318,5,22,0,0,318,319,
        5,45,0,0,319,324,3,36,18,0,320,321,5,41,0,0,321,323,3,36,18,0,322,
        320,1,0,0,0,323,326,1,0,0,0,324,322,1,0,0,0,324,325,1,0,0,0,325,
        327,1,0,0,0,326,324,1,0,0,0,327,328,5,46,0,0,328,61,1,0,0,0,329,
        338,5,45,0,0,330,335,3,36,18,0,331,332,5,41,0,0,332,334,3,36,18,
        0,333,331,1,0,0,0,334,337,1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,
        0,336,339,1,0,0,0,337,335,1,0,0,0,338,330,1,0,0,0,338,339,1,0,0,
        0,339,340,1,0,0,0,340,341,5,46,0,0,341,63,1,0,0,0,342,343,5,45,0,
        0,343,344,5,45,0,0,344,349,3,36,18,0,345,346,5,41,0,0,346,348,3,
        36,18,0,347,345,1,0,0,0,348,351,1,0,0,0,349,347,1,0,0,0,349,350,
        1,0,0,0,350,352,1,0,0,0,351,349,1,0,0,0,352,367,5,46,0,0,353,354,
        5,41,0,0,354,355,5,45,0,0,355,360,3,36,18,0,356,357,5,41,0,0,357,
        359,3,36,18,0,358,356,1,0,0,0,359,362,1,0,0,0,360,358,1,0,0,0,360,
        361,1,0,0,0,361,363,1,0,0,0,362,360,1,0,0,0,363,364,5,46,0,0,364,
        366,1,0,0,0,365,353,1,0,0,0,366,369,1,0,0,0,367,365,1,0,0,0,367,
        368,1,0,0,0,368,370,1,0,0,0,369,367,1,0,0,0,370,371,5,46,0,0,371,
        65,1,0,0,0,372,373,5,22,0,0,373,67,1,0,0,0,34,74,79,89,97,105,111,
        122,128,133,146,152,156,175,185,213,217,232,240,246,253,261,269,
        275,280,297,302,311,315,324,335,338,349,360,367
    ]

class DeepLangParser ( Parser ):

    grammarFileName = "DeepLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'import'", "'print'", "'def'", 
                     "'if'", "'elif'", "'else'", "'while'", "'for'", "'in'", 
                     "'class'", "'or'", "'and'", "'not'", "'is'", "'None'", 
                     "'True'", "'False'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'**'", "'//'", "'->'", 
                     "','", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TK_INT", "TK_FLOAT", 
                      "TK_STRING", "ID", "COMMENT", "WS", "NEWLINE", "PLUS", 
                      "MINUS", "STAR", "SLASH", "PERC", "EQ", "EQEQ", "NEQ", 
                      "LT", "LE", "GT", "GE", "POW", "FLOORDIV", "ARROW", 
                      "COMMA", "COLON", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                      "LBRACE", "RBRACE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_stmtList = 1
    RULE_stmt = 2
    RULE_simple_stmt = 3
    RULE_small_stmt = 4
    RULE_assign_stmt = 5
    RULE_return_stmt = 6
    RULE_import_stmt = 7
    RULE_print_stmt = 8
    RULE_expr_stmt = 9
    RULE_compound_stmt = 10
    RULE_funcdef = 11
    RULE_paramList = 12
    RULE_param = 13
    RULE_if_stmt = 14
    RULE_while_stmt = 15
    RULE_for_stmt = 16
    RULE_classdef = 17
    RULE_expr = 18
    RULE_orExpr = 19
    RULE_andExpr = 20
    RULE_notExpr = 21
    RULE_comparison = 22
    RULE_arithExpr = 23
    RULE_term = 24
    RULE_factor = 25
    RULE_power = 26
    RULE_atom = 27
    RULE_callExpr = 28
    RULE_argList = 29
    RULE_indexing = 30
    RULE_listLiteral = 31
    RULE_matrixLiteral = 32
    RULE_type = 33

    ruleNames =  [ "program", "stmtList", "stmt", "simple_stmt", "small_stmt", 
                   "assign_stmt", "return_stmt", "import_stmt", "print_stmt", 
                   "expr_stmt", "compound_stmt", "funcdef", "paramList", 
                   "param", "if_stmt", "while_stmt", "for_stmt", "classdef", 
                   "expr", "orExpr", "andExpr", "notExpr", "comparison", 
                   "arithExpr", "term", "factor", "power", "atom", "callExpr", 
                   "argList", "indexing", "listLiteral", "matrixLiteral", 
                   "type" ]

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
    TK_INT=19
    TK_FLOAT=20
    TK_STRING=21
    ID=22
    COMMENT=23
    WS=24
    NEWLINE=25
    PLUS=26
    MINUS=27
    STAR=28
    SLASH=29
    PERC=30
    EQ=31
    EQEQ=32
    NEQ=33
    LT=34
    LE=35
    GT=36
    GE=37
    POW=38
    FLOORDIV=39
    ARROW=40
    COMMA=41
    COLON=42
    LPAREN=43
    RPAREN=44
    LBRACK=45
    RBRACK=46
    LBRACE=47
    RBRACE=48
    INDENT=49
    DEDENT=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtList(self):
            return self.getTypedRuleContext(DeepLangParser.StmtListContext,0)


        def EOF(self):
            return self.getToken(DeepLangParser.EOF, 0)

        def getRuleIndex(self):
            return DeepLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DeepLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.stmtList()
            self.state = 69
            self.match(DeepLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.StmtContext,i)


        def getRuleIndex(self):
            return DeepLangParser.RULE_stmtList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtList" ):
                listener.enterStmtList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtList" ):
                listener.exitStmtList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = DeepLangParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 43980674779966) != 0):
                self.state = 71
                self.stmt()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Simple_stmtContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = DeepLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 14, 16, 17, 18, 19, 20, 21, 22, 26, 27, 43, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.simple_stmt()
                pass
            elif token in [4, 5, 8, 9, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.compound_stmt()
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


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def small_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Small_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(DeepLangParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DeepLangParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmt" ):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmt(self):

        localctx = DeepLangParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.small_stmt()
            self.state = 82
            self.match(DeepLangParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Small_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Assign_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Return_stmtContext,0)


        def import_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Import_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Print_stmtContext,0)


        def expr_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.Expr_stmtContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_small_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmall_stmt" ):
                listener.enterSmall_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmall_stmt" ):
                listener.exitSmall_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmall_stmt" ):
                return visitor.visitSmall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def small_stmt(self):

        localctx = DeepLangParser.Small_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_small_stmt)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.return_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.import_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.print_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.expr_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def EQ(self):
            return self.getToken(DeepLangParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = DeepLangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(DeepLangParser.ID)
            self.state = 92
            self.match(DeepLangParser.EQ)
            self.state = 93
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = DeepLangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(DeepLangParser.T__0)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 43980674777088) != 0):
                self.state = 96
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.ID)
            else:
                return self.getToken(DeepLangParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COMMA)
            else:
                return self.getToken(DeepLangParser.COMMA, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_import_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_stmt" ):
                listener.enterImport_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_stmt" ):
                listener.exitImport_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_stmt" ):
                return visitor.visitImport_stmt(self)
            else:
                return visitor.visitChildren(self)




    def import_stmt(self):

        localctx = DeepLangParser.Import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_import_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(DeepLangParser.T__1)
            self.state = 100
            self.match(DeepLangParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 101
                self.match(DeepLangParser.COMMA)
                self.state = 102
                self.match(DeepLangParser.ID)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(DeepLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DeepLangParser.RPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = DeepLangParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(DeepLangParser.T__2)
            self.state = 109
            self.match(DeepLangParser.LPAREN)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 43980674777088) != 0):
                self.state = 110
                self.expr()


            self.state = 113
            self.match(DeepLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_expr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_stmt" ):
                listener.enterExpr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_stmt" ):
                listener.exitExpr_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_stmt" ):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expr_stmt(self):

        localctx = DeepLangParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdef(self):
            return self.getTypedRuleContext(DeepLangParser.FuncdefContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(DeepLangParser.For_stmtContext,0)


        def classdef(self):
            return self.getTypedRuleContext(DeepLangParser.ClassdefContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_compound_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_stmt" ):
                listener.enterCompound_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_stmt" ):
                listener.exitCompound_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_stmt" ):
                return visitor.visitCompound_stmt(self)
            else:
                return visitor.visitChildren(self)




    def compound_stmt(self):

        localctx = DeepLangParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compound_stmt)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.funcdef()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.if_stmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.while_stmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.for_stmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.classdef()
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


    class FuncdefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeepLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DeepLangParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(DeepLangParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(DeepLangParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(DeepLangParser.INDENT, 0)

        def stmtList(self):
            return self.getTypedRuleContext(DeepLangParser.StmtListContext,0)


        def DEDENT(self):
            return self.getToken(DeepLangParser.DEDENT, 0)

        def paramList(self):
            return self.getTypedRuleContext(DeepLangParser.ParamListContext,0)


        def ARROW(self):
            return self.getToken(DeepLangParser.ARROW, 0)

        def type_(self):
            return self.getTypedRuleContext(DeepLangParser.TypeContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_funcdef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdef" ):
                listener.enterFuncdef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdef" ):
                listener.exitFuncdef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdef" ):
                return visitor.visitFuncdef(self)
            else:
                return visitor.visitChildren(self)




    def funcdef(self):

        localctx = DeepLangParser.FuncdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(DeepLangParser.T__3)
            self.state = 125
            self.match(DeepLangParser.ID)
            self.state = 126
            self.match(DeepLangParser.LPAREN)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 127
                self.paramList()


            self.state = 130
            self.match(DeepLangParser.RPAREN)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 131
                self.match(DeepLangParser.ARROW)
                self.state = 132
                self.type_()


            self.state = 135
            self.match(DeepLangParser.COLON)
            self.state = 136
            self.match(DeepLangParser.NEWLINE)
            self.state = 137
            self.match(DeepLangParser.INDENT)
            self.state = 138
            self.stmtList()
            self.state = 139
            self.match(DeepLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COMMA)
            else:
                return self.getToken(DeepLangParser.COMMA, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = DeepLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.param()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 142
                self.match(DeepLangParser.COMMA)
                self.state = 143
                self.param()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def COLON(self):
            return self.getToken(DeepLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(DeepLangParser.TypeContext,0)


        def EQ(self):
            return self.getToken(DeepLangParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = DeepLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(DeepLangParser.ID)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 150
                self.match(DeepLangParser.COLON)
                self.state = 151
                self.type_()


            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 154
                self.match(DeepLangParser.EQ)
                self.state = 155
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.ExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COLON)
            else:
                return self.getToken(DeepLangParser.COLON, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.NEWLINE)
            else:
                return self.getToken(DeepLangParser.NEWLINE, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.INDENT)
            else:
                return self.getToken(DeepLangParser.INDENT, i)

        def stmtList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.StmtListContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.StmtListContext,i)


        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.DEDENT)
            else:
                return self.getToken(DeepLangParser.DEDENT, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = DeepLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(DeepLangParser.T__4)
            self.state = 159
            self.expr()
            self.state = 160
            self.match(DeepLangParser.COLON)
            self.state = 161
            self.match(DeepLangParser.NEWLINE)
            self.state = 162
            self.match(DeepLangParser.INDENT)
            self.state = 163
            self.stmtList()
            self.state = 164
            self.match(DeepLangParser.DEDENT)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 165
                self.match(DeepLangParser.T__5)
                self.state = 166
                self.expr()
                self.state = 167
                self.match(DeepLangParser.COLON)
                self.state = 168
                self.match(DeepLangParser.NEWLINE)
                self.state = 169
                self.match(DeepLangParser.INDENT)
                self.state = 170
                self.stmtList()
                self.state = 171
                self.match(DeepLangParser.DEDENT)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 178
                self.match(DeepLangParser.T__6)
                self.state = 179
                self.match(DeepLangParser.COLON)
                self.state = 180
                self.match(DeepLangParser.NEWLINE)
                self.state = 181
                self.match(DeepLangParser.INDENT)
                self.state = 182
                self.stmtList()
                self.state = 183
                self.match(DeepLangParser.DEDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(DeepLangParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(DeepLangParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(DeepLangParser.INDENT, 0)

        def stmtList(self):
            return self.getTypedRuleContext(DeepLangParser.StmtListContext,0)


        def DEDENT(self):
            return self.getToken(DeepLangParser.DEDENT, 0)

        def getRuleIndex(self):
            return DeepLangParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = DeepLangParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(DeepLangParser.T__7)
            self.state = 188
            self.expr()
            self.state = 189
            self.match(DeepLangParser.COLON)
            self.state = 190
            self.match(DeepLangParser.NEWLINE)
            self.state = 191
            self.match(DeepLangParser.INDENT)
            self.state = 192
            self.stmtList()
            self.state = 193
            self.match(DeepLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)

        def COLON(self):
            return self.getToken(DeepLangParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(DeepLangParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(DeepLangParser.INDENT, 0)

        def stmtList(self):
            return self.getTypedRuleContext(DeepLangParser.StmtListContext,0)


        def DEDENT(self):
            return self.getToken(DeepLangParser.DEDENT, 0)

        def getRuleIndex(self):
            return DeepLangParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = DeepLangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(DeepLangParser.T__8)
            self.state = 196
            self.match(DeepLangParser.ID)
            self.state = 197
            self.match(DeepLangParser.T__9)
            self.state = 198
            self.expr()
            self.state = 199
            self.match(DeepLangParser.COLON)
            self.state = 200
            self.match(DeepLangParser.NEWLINE)
            self.state = 201
            self.match(DeepLangParser.INDENT)
            self.state = 202
            self.stmtList()
            self.state = 203
            self.match(DeepLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.ID)
            else:
                return self.getToken(DeepLangParser.ID, i)

        def COLON(self):
            return self.getToken(DeepLangParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(DeepLangParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(DeepLangParser.INDENT, 0)

        def stmtList(self):
            return self.getTypedRuleContext(DeepLangParser.StmtListContext,0)


        def DEDENT(self):
            return self.getToken(DeepLangParser.DEDENT, 0)

        def LPAREN(self):
            return self.getToken(DeepLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DeepLangParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COMMA)
            else:
                return self.getToken(DeepLangParser.COMMA, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_classdef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassdef" ):
                listener.enterClassdef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassdef" ):
                listener.exitClassdef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdef" ):
                return visitor.visitClassdef(self)
            else:
                return visitor.visitChildren(self)




    def classdef(self):

        localctx = DeepLangParser.ClassdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_classdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(DeepLangParser.T__10)
            self.state = 206
            self.match(DeepLangParser.ID)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 207
                self.match(DeepLangParser.LPAREN)
                self.state = 208
                self.match(DeepLangParser.ID)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 209
                    self.match(DeepLangParser.COMMA)
                    self.state = 210
                    self.match(DeepLangParser.ID)
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 216
                self.match(DeepLangParser.RPAREN)


            self.state = 219
            self.match(DeepLangParser.COLON)
            self.state = 220
            self.match(DeepLangParser.NEWLINE)
            self.state = 221
            self.match(DeepLangParser.INDENT)
            self.state = 222
            self.stmtList()
            self.state = 223
            self.match(DeepLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpr(self):
            return self.getTypedRuleContext(DeepLangParser.OrExprContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = DeepLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.orExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.AndExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.AndExprContext,i)


        def getRuleIndex(self):
            return DeepLangParser.RULE_orExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = DeepLangParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.andExpr()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 228
                self.match(DeepLangParser.T__11)
                self.state = 229
                self.andExpr()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.NotExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.NotExprContext,i)


        def getRuleIndex(self):
            return DeepLangParser.RULE_andExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = DeepLangParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.notExpr()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 236
                self.match(DeepLangParser.T__12)
                self.state = 237
                self.notExpr()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpr(self):
            return self.getTypedRuleContext(DeepLangParser.NotExprContext,0)


        def comparison(self):
            return self.getTypedRuleContext(DeepLangParser.ComparisonContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_notExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)




    def notExpr(self):

        localctx = DeepLangParser.NotExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_notExpr)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(DeepLangParser.T__13)
                self.state = 244
                self.notExpr()
                pass
            elif token in [16, 17, 18, 19, 20, 21, 22, 26, 27, 43, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.comparison()
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


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.ArithExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.ArithExprContext,i)


        def EQEQ(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.EQEQ)
            else:
                return self.getToken(DeepLangParser.EQEQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.NEQ)
            else:
                return self.getToken(DeepLangParser.NEQ, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.LT)
            else:
                return self.getToken(DeepLangParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.LE)
            else:
                return self.getToken(DeepLangParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.GT)
            else:
                return self.getToken(DeepLangParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.GE)
            else:
                return self.getToken(DeepLangParser.GE, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = DeepLangParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.arithExpr()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 270582973440) != 0):
                self.state = 249
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270582973440) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.arithExpr()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.TermContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.PLUS)
            else:
                return self.getToken(DeepLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.MINUS)
            else:
                return self.getToken(DeepLangParser.MINUS, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_arithExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithExpr" ):
                listener.enterArithExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithExpr" ):
                listener.exitArithExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr" ):
                return visitor.visitArithExpr(self)
            else:
                return visitor.visitChildren(self)




    def arithExpr(self):

        localctx = DeepLangParser.ArithExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arithExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.term()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 258
                self.term()
                self.state = 263
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.FactorContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.FactorContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.STAR)
            else:
                return self.getToken(DeepLangParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.SLASH)
            else:
                return self.getToken(DeepLangParser.SLASH, i)

        def PERC(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.PERC)
            else:
                return self.getToken(DeepLangParser.PERC, i)

        def FLOORDIV(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.FLOORDIV)
            else:
                return self.getToken(DeepLangParser.FLOORDIV, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = DeepLangParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.factor()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 551634862080) != 0):
                self.state = 265
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 551634862080) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self.factor()
                self.state = 271
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(DeepLangParser.FactorContext,0)


        def PLUS(self):
            return self.getToken(DeepLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(DeepLangParser.MINUS, 0)

        def power(self):
            return self.getTypedRuleContext(DeepLangParser.PowerContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = DeepLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 273
                self.factor()
                pass
            elif token in [16, 17, 18, 19, 20, 21, 22, 43, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.power()
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


    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(DeepLangParser.AtomContext,0)


        def POW(self):
            return self.getToken(DeepLangParser.POW, 0)

        def factor(self):
            return self.getTypedRuleContext(DeepLangParser.FactorContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_power

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)




    def power(self):

        localctx = DeepLangParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_power)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.atom()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 278
                self.match(DeepLangParser.POW)
                self.state = 279
                self.factor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def TK_INT(self):
            return self.getToken(DeepLangParser.TK_INT, 0)

        def TK_FLOAT(self):
            return self.getToken(DeepLangParser.TK_FLOAT, 0)

        def TK_STRING(self):
            return self.getToken(DeepLangParser.TK_STRING, 0)

        def LPAREN(self):
            return self.getToken(DeepLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(DeepLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(DeepLangParser.RPAREN, 0)

        def listLiteral(self):
            return self.getTypedRuleContext(DeepLangParser.ListLiteralContext,0)


        def matrixLiteral(self):
            return self.getTypedRuleContext(DeepLangParser.MatrixLiteralContext,0)


        def callExpr(self):
            return self.getTypedRuleContext(DeepLangParser.CallExprContext,0)


        def indexing(self):
            return self.getTypedRuleContext(DeepLangParser.IndexingContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = DeepLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atom)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(DeepLangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(DeepLangParser.TK_INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.match(DeepLangParser.TK_FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 285
                self.match(DeepLangParser.TK_STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 286
                self.match(DeepLangParser.T__15)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 287
                self.match(DeepLangParser.T__16)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.match(DeepLangParser.T__17)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 289
                self.match(DeepLangParser.LPAREN)
                self.state = 290
                self.expr()
                self.state = 291
                self.match(DeepLangParser.RPAREN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 293
                self.listLiteral()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 294
                self.matrixLiteral()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 295
                self.callExpr()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 296
                self.indexing()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeepLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DeepLangParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(DeepLangParser.ArgListContext,0)


        def getRuleIndex(self):
            return DeepLangParser.RULE_callExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpr" ):
                listener.enterCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpr" ):
                listener.exitCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)




    def callExpr(self):

        localctx = DeepLangParser.CallExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_callExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(DeepLangParser.ID)
            self.state = 300
            self.match(DeepLangParser.LPAREN)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 43980674777088) != 0):
                self.state = 301
                self.argList()


            self.state = 304
            self.match(DeepLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COMMA)
            else:
                return self.getToken(DeepLangParser.COMMA, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = DeepLangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr()
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 307
                    self.match(DeepLangParser.COMMA)
                    self.state = 308
                    self.expr() 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 314
                self.match(DeepLangParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def LBRACK(self):
            return self.getToken(DeepLangParser.LBRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.ExprContext,i)


        def RBRACK(self):
            return self.getToken(DeepLangParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COMMA)
            else:
                return self.getToken(DeepLangParser.COMMA, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_indexing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexing" ):
                listener.enterIndexing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexing" ):
                listener.exitIndexing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexing" ):
                return visitor.visitIndexing(self)
            else:
                return visitor.visitChildren(self)




    def indexing(self):

        localctx = DeepLangParser.IndexingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_indexing)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(DeepLangParser.ID)
            self.state = 318
            self.match(DeepLangParser.LBRACK)
            self.state = 319
            self.expr()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 320
                self.match(DeepLangParser.COMMA)
                self.state = 321
                self.expr()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 327
            self.match(DeepLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(DeepLangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(DeepLangParser.RBRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COMMA)
            else:
                return self.getToken(DeepLangParser.COMMA, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)




    def listLiteral(self):

        localctx = DeepLangParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(DeepLangParser.LBRACK)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 43980674777088) != 0):
                self.state = 330
                self.expr()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 331
                    self.match(DeepLangParser.COMMA)
                    self.state = 332
                    self.expr()
                    self.state = 337
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 340
            self.match(DeepLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.LBRACK)
            else:
                return self.getToken(DeepLangParser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.RBRACK)
            else:
                return self.getToken(DeepLangParser.RBRACK, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(DeepLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLangParser.COMMA)
            else:
                return self.getToken(DeepLangParser.COMMA, i)

        def getRuleIndex(self):
            return DeepLangParser.RULE_matrixLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixLiteral" ):
                listener.enterMatrixLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixLiteral" ):
                listener.exitMatrixLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixLiteral" ):
                return visitor.visitMatrixLiteral(self)
            else:
                return visitor.visitChildren(self)




    def matrixLiteral(self):

        localctx = DeepLangParser.MatrixLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_matrixLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(DeepLangParser.LBRACK)

            self.state = 343
            self.match(DeepLangParser.LBRACK)
            self.state = 344
            self.expr()
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 345
                self.match(DeepLangParser.COMMA)
                self.state = 346
                self.expr()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 352
            self.match(DeepLangParser.RBRACK)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 353
                self.match(DeepLangParser.COMMA)
                self.state = 354
                self.match(DeepLangParser.LBRACK)
                self.state = 355
                self.expr()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 356
                    self.match(DeepLangParser.COMMA)
                    self.state = 357
                    self.expr()
                    self.state = 362
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 363
                self.match(DeepLangParser.RBRACK)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370
            self.match(DeepLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLangParser.ID, 0)

        def getRuleIndex(self):
            return DeepLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = DeepLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(DeepLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





