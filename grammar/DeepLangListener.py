# Generated from grammar/DeepLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DeepLangParser import DeepLangParser
else:
    from DeepLangParser import DeepLangParser

# deeplang ANTLR grammar - generated


# This class defines a complete listener for a parse tree produced by DeepLangParser.
class DeepLangListener(ParseTreeListener):

    # Enter a parse tree produced by DeepLangParser#program.
    def enterProgram(self, ctx:DeepLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by DeepLangParser#program.
    def exitProgram(self, ctx:DeepLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by DeepLangParser#stmtList.
    def enterStmtList(self, ctx:DeepLangParser.StmtListContext):
        pass

    # Exit a parse tree produced by DeepLangParser#stmtList.
    def exitStmtList(self, ctx:DeepLangParser.StmtListContext):
        pass


    # Enter a parse tree produced by DeepLangParser#stmt.
    def enterStmt(self, ctx:DeepLangParser.StmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#stmt.
    def exitStmt(self, ctx:DeepLangParser.StmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#simple_stmt.
    def enterSimple_stmt(self, ctx:DeepLangParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#simple_stmt.
    def exitSimple_stmt(self, ctx:DeepLangParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#small_stmt.
    def enterSmall_stmt(self, ctx:DeepLangParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#small_stmt.
    def exitSmall_stmt(self, ctx:DeepLangParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#assign_stmt.
    def enterAssign_stmt(self, ctx:DeepLangParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#assign_stmt.
    def exitAssign_stmt(self, ctx:DeepLangParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#return_stmt.
    def enterReturn_stmt(self, ctx:DeepLangParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#return_stmt.
    def exitReturn_stmt(self, ctx:DeepLangParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#import_stmt.
    def enterImport_stmt(self, ctx:DeepLangParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#import_stmt.
    def exitImport_stmt(self, ctx:DeepLangParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#print_stmt.
    def enterPrint_stmt(self, ctx:DeepLangParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#print_stmt.
    def exitPrint_stmt(self, ctx:DeepLangParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#expr_stmt.
    def enterExpr_stmt(self, ctx:DeepLangParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#expr_stmt.
    def exitExpr_stmt(self, ctx:DeepLangParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#compound_stmt.
    def enterCompound_stmt(self, ctx:DeepLangParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#compound_stmt.
    def exitCompound_stmt(self, ctx:DeepLangParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#funcdef.
    def enterFuncdef(self, ctx:DeepLangParser.FuncdefContext):
        pass

    # Exit a parse tree produced by DeepLangParser#funcdef.
    def exitFuncdef(self, ctx:DeepLangParser.FuncdefContext):
        pass


    # Enter a parse tree produced by DeepLangParser#paramList.
    def enterParamList(self, ctx:DeepLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by DeepLangParser#paramList.
    def exitParamList(self, ctx:DeepLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by DeepLangParser#param.
    def enterParam(self, ctx:DeepLangParser.ParamContext):
        pass

    # Exit a parse tree produced by DeepLangParser#param.
    def exitParam(self, ctx:DeepLangParser.ParamContext):
        pass


    # Enter a parse tree produced by DeepLangParser#if_stmt.
    def enterIf_stmt(self, ctx:DeepLangParser.If_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#if_stmt.
    def exitIf_stmt(self, ctx:DeepLangParser.If_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#while_stmt.
    def enterWhile_stmt(self, ctx:DeepLangParser.While_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#while_stmt.
    def exitWhile_stmt(self, ctx:DeepLangParser.While_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#for_stmt.
    def enterFor_stmt(self, ctx:DeepLangParser.For_stmtContext):
        pass

    # Exit a parse tree produced by DeepLangParser#for_stmt.
    def exitFor_stmt(self, ctx:DeepLangParser.For_stmtContext):
        pass


    # Enter a parse tree produced by DeepLangParser#classdef.
    def enterClassdef(self, ctx:DeepLangParser.ClassdefContext):
        pass

    # Exit a parse tree produced by DeepLangParser#classdef.
    def exitClassdef(self, ctx:DeepLangParser.ClassdefContext):
        pass


    # Enter a parse tree produced by DeepLangParser#expr.
    def enterExpr(self, ctx:DeepLangParser.ExprContext):
        pass

    # Exit a parse tree produced by DeepLangParser#expr.
    def exitExpr(self, ctx:DeepLangParser.ExprContext):
        pass


    # Enter a parse tree produced by DeepLangParser#orExpr.
    def enterOrExpr(self, ctx:DeepLangParser.OrExprContext):
        pass

    # Exit a parse tree produced by DeepLangParser#orExpr.
    def exitOrExpr(self, ctx:DeepLangParser.OrExprContext):
        pass


    # Enter a parse tree produced by DeepLangParser#andExpr.
    def enterAndExpr(self, ctx:DeepLangParser.AndExprContext):
        pass

    # Exit a parse tree produced by DeepLangParser#andExpr.
    def exitAndExpr(self, ctx:DeepLangParser.AndExprContext):
        pass


    # Enter a parse tree produced by DeepLangParser#notExpr.
    def enterNotExpr(self, ctx:DeepLangParser.NotExprContext):
        pass

    # Exit a parse tree produced by DeepLangParser#notExpr.
    def exitNotExpr(self, ctx:DeepLangParser.NotExprContext):
        pass


    # Enter a parse tree produced by DeepLangParser#comparison.
    def enterComparison(self, ctx:DeepLangParser.ComparisonContext):
        pass

    # Exit a parse tree produced by DeepLangParser#comparison.
    def exitComparison(self, ctx:DeepLangParser.ComparisonContext):
        pass


    # Enter a parse tree produced by DeepLangParser#arithExpr.
    def enterArithExpr(self, ctx:DeepLangParser.ArithExprContext):
        pass

    # Exit a parse tree produced by DeepLangParser#arithExpr.
    def exitArithExpr(self, ctx:DeepLangParser.ArithExprContext):
        pass


    # Enter a parse tree produced by DeepLangParser#term.
    def enterTerm(self, ctx:DeepLangParser.TermContext):
        pass

    # Exit a parse tree produced by DeepLangParser#term.
    def exitTerm(self, ctx:DeepLangParser.TermContext):
        pass


    # Enter a parse tree produced by DeepLangParser#factor.
    def enterFactor(self, ctx:DeepLangParser.FactorContext):
        pass

    # Exit a parse tree produced by DeepLangParser#factor.
    def exitFactor(self, ctx:DeepLangParser.FactorContext):
        pass


    # Enter a parse tree produced by DeepLangParser#power.
    def enterPower(self, ctx:DeepLangParser.PowerContext):
        pass

    # Exit a parse tree produced by DeepLangParser#power.
    def exitPower(self, ctx:DeepLangParser.PowerContext):
        pass


    # Enter a parse tree produced by DeepLangParser#atom.
    def enterAtom(self, ctx:DeepLangParser.AtomContext):
        pass

    # Exit a parse tree produced by DeepLangParser#atom.
    def exitAtom(self, ctx:DeepLangParser.AtomContext):
        pass


    # Enter a parse tree produced by DeepLangParser#callExpr.
    def enterCallExpr(self, ctx:DeepLangParser.CallExprContext):
        pass

    # Exit a parse tree produced by DeepLangParser#callExpr.
    def exitCallExpr(self, ctx:DeepLangParser.CallExprContext):
        pass


    # Enter a parse tree produced by DeepLangParser#argList.
    def enterArgList(self, ctx:DeepLangParser.ArgListContext):
        pass

    # Exit a parse tree produced by DeepLangParser#argList.
    def exitArgList(self, ctx:DeepLangParser.ArgListContext):
        pass


    # Enter a parse tree produced by DeepLangParser#indexing.
    def enterIndexing(self, ctx:DeepLangParser.IndexingContext):
        pass

    # Exit a parse tree produced by DeepLangParser#indexing.
    def exitIndexing(self, ctx:DeepLangParser.IndexingContext):
        pass


    # Enter a parse tree produced by DeepLangParser#listLiteral.
    def enterListLiteral(self, ctx:DeepLangParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by DeepLangParser#listLiteral.
    def exitListLiteral(self, ctx:DeepLangParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by DeepLangParser#matrixLiteral.
    def enterMatrixLiteral(self, ctx:DeepLangParser.MatrixLiteralContext):
        pass

    # Exit a parse tree produced by DeepLangParser#matrixLiteral.
    def exitMatrixLiteral(self, ctx:DeepLangParser.MatrixLiteralContext):
        pass


    # Enter a parse tree produced by DeepLangParser#type.
    def enterType(self, ctx:DeepLangParser.TypeContext):
        pass

    # Exit a parse tree produced by DeepLangParser#type.
    def exitType(self, ctx:DeepLangParser.TypeContext):
        pass



del DeepLangParser