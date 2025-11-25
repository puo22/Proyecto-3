# Generated from grammar/DeepLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DeepLangParser import DeepLangParser
else:
    from DeepLangParser import DeepLangParser

# deeplang ANTLR grammar - generated


# This class defines a complete generic visitor for a parse tree produced by DeepLangParser.

class DeepLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DeepLangParser#program.
    def visitProgram(self, ctx:DeepLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#stmtList.
    def visitStmtList(self, ctx:DeepLangParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#stmt.
    def visitStmt(self, ctx:DeepLangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#simple_stmt.
    def visitSimple_stmt(self, ctx:DeepLangParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#small_stmt.
    def visitSmall_stmt(self, ctx:DeepLangParser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:DeepLangParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#return_stmt.
    def visitReturn_stmt(self, ctx:DeepLangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#import_stmt.
    def visitImport_stmt(self, ctx:DeepLangParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#print_stmt.
    def visitPrint_stmt(self, ctx:DeepLangParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#expr_stmt.
    def visitExpr_stmt(self, ctx:DeepLangParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#compound_stmt.
    def visitCompound_stmt(self, ctx:DeepLangParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#funcdef.
    def visitFuncdef(self, ctx:DeepLangParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#paramList.
    def visitParamList(self, ctx:DeepLangParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#param.
    def visitParam(self, ctx:DeepLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#if_stmt.
    def visitIf_stmt(self, ctx:DeepLangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#while_stmt.
    def visitWhile_stmt(self, ctx:DeepLangParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#for_stmt.
    def visitFor_stmt(self, ctx:DeepLangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#classdef.
    def visitClassdef(self, ctx:DeepLangParser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#expr.
    def visitExpr(self, ctx:DeepLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#orExpr.
    def visitOrExpr(self, ctx:DeepLangParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#andExpr.
    def visitAndExpr(self, ctx:DeepLangParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#notExpr.
    def visitNotExpr(self, ctx:DeepLangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#comparison.
    def visitComparison(self, ctx:DeepLangParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#arithExpr.
    def visitArithExpr(self, ctx:DeepLangParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#term.
    def visitTerm(self, ctx:DeepLangParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#factor.
    def visitFactor(self, ctx:DeepLangParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#power.
    def visitPower(self, ctx:DeepLangParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#atom.
    def visitAtom(self, ctx:DeepLangParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#callExpr.
    def visitCallExpr(self, ctx:DeepLangParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#argList.
    def visitArgList(self, ctx:DeepLangParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#indexing.
    def visitIndexing(self, ctx:DeepLangParser.IndexingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#listLiteral.
    def visitListLiteral(self, ctx:DeepLangParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#matrixLiteral.
    def visitMatrixLiteral(self, ctx:DeepLangParser.MatrixLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLangParser#type.
    def visitType(self, ctx:DeepLangParser.TypeContext):
        return self.visitChildren(ctx)



del DeepLangParser