# Generated from Quark.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QuarkParser import QuarkParser
else:
    from QuarkParser import QuarkParser

from compiler import Compiler
c = Compiler()
quadruples = None
func_directory = None
type_directory = None
constants = None


# This class defines a complete listener for a parse tree produced by QuarkParser.
class QuarkListener(ParseTreeListener):

    # Enter a parse tree produced by QuarkParser#function.
    def enterFunction(self, ctx:QuarkParser.FunctionContext):
        pass

    # Exit a parse tree produced by QuarkParser#function.
    def exitFunction(self, ctx:QuarkParser.FunctionContext):
        pass


    # Enter a parse tree produced by QuarkParser#params.
    def enterParams(self, ctx:QuarkParser.ParamsContext):
        pass

    # Exit a parse tree produced by QuarkParser#params.
    def exitParams(self, ctx:QuarkParser.ParamsContext):
        pass


    # Enter a parse tree produced by QuarkParser#moreparams.
    def enterMoreparams(self, ctx:QuarkParser.MoreparamsContext):
        pass

    # Exit a parse tree produced by QuarkParser#moreparams.
    def exitMoreparams(self, ctx:QuarkParser.MoreparamsContext):
        pass


    # Enter a parse tree produced by QuarkParser#moreTypes.
    def enterMoreTypes(self, ctx:QuarkParser.MoreTypesContext):
        pass

    # Exit a parse tree produced by QuarkParser#moreTypes.
    def exitMoreTypes(self, ctx:QuarkParser.MoreTypesContext):
        pass


    # Enter a parse tree produced by QuarkParser#UserType.
    def enterUserType(self, ctx:QuarkParser.UserTypeContext):
        pass

    # Exit a parse tree produced by QuarkParser#UserType.
    def exitUserType(self, ctx:QuarkParser.UserTypeContext):
        pass


    # Enter a parse tree produced by QuarkParser#Int.
    def enterInt(self, ctx:QuarkParser.IntContext):
        pass

    # Exit a parse tree produced by QuarkParser#Int.
    def exitInt(self, ctx:QuarkParser.IntContext):
        pass


    # Enter a parse tree produced by QuarkParser#Boolean.
    def enterBoolean(self, ctx:QuarkParser.BooleanContext):
        pass

    # Exit a parse tree produced by QuarkParser#Boolean.
    def exitBoolean(self, ctx:QuarkParser.BooleanContext):
        pass


    # Enter a parse tree produced by QuarkParser#Float.
    def enterFloat(self, ctx:QuarkParser.FloatContext):
        pass

    # Exit a parse tree produced by QuarkParser#Float.
    def exitFloat(self, ctx:QuarkParser.FloatContext):
        pass


    # Enter a parse tree produced by QuarkParser#String.
    def enterString(self, ctx:QuarkParser.StringContext):
        pass

    # Exit a parse tree produced by QuarkParser#String.
    def exitString(self, ctx:QuarkParser.StringContext):
        pass


    # Enter a parse tree produced by QuarkParser#None.
    def enterNone(self, ctx:QuarkParser.NoneContext):
        pass

    # Exit a parse tree produced by QuarkParser#None.
    def exitNone(self, ctx:QuarkParser.NoneContext):
        pass


    # Enter a parse tree produced by QuarkParser#Any.
    def enterAny(self, ctx:QuarkParser.AnyContext):
        pass

    # Exit a parse tree produced by QuarkParser#Any.
    def exitAny(self, ctx:QuarkParser.AnyContext):
        pass


    # Enter a parse tree produced by QuarkParser#ListOfType.
    def enterListOfType(self, ctx:QuarkParser.ListOfTypeContext):
        pass

    # Exit a parse tree produced by QuarkParser#ListOfType.
    def exitListOfType(self, ctx:QuarkParser.ListOfTypeContext):
        pass


    # Enter a parse tree produced by QuarkParser#typevalue.
    def enterTypevalue(self, ctx:QuarkParser.TypevalueContext):
        pass

    # Exit a parse tree produced by QuarkParser#typevalue.
    def exitTypevalue(self, ctx:QuarkParser.TypevalueContext):
        pass


    # Enter a parse tree produced by QuarkParser#typedef.
    def enterTypedef(self, ctx:QuarkParser.TypedefContext):
        pass

    # Exit a parse tree produced by QuarkParser#typedef.
    def exitTypedef(self, ctx:QuarkParser.TypedefContext):
        pass


    # Enter a parse tree produced by QuarkParser#typeset.
    def enterTypeset(self, ctx:QuarkParser.TypesetContext):
        pass

    # Exit a parse tree produced by QuarkParser#typeset.
    def exitTypeset(self, ctx:QuarkParser.TypesetContext):
        pass


    # Enter a parse tree produced by QuarkParser#cond.
    def enterCond(self, ctx:QuarkParser.CondContext):
        pass

    # Exit a parse tree produced by QuarkParser#cond.
    def exitCond(self, ctx:QuarkParser.CondContext):
        pass


    # Enter a parse tree produced by QuarkParser#expression.
    def enterExpression(self, ctx:QuarkParser.ExpressionContext):
        pass

    # Exit a parse tree produced by QuarkParser#expression.
    def exitExpression(self, ctx:QuarkParser.ExpressionContext):
        pass


    # Enter a parse tree produced by QuarkParser#comp.
    def enterComp(self, ctx:QuarkParser.CompContext):
        pass

    # Exit a parse tree produced by QuarkParser#comp.
    def exitComp(self, ctx:QuarkParser.CompContext):
        pass


    # Enter a parse tree produced by QuarkParser#exp.
    def enterExp(self, ctx:QuarkParser.ExpContext):
        pass

    # Exit a parse tree produced by QuarkParser#exp.
    def exitExp(self, ctx:QuarkParser.ExpContext):
        pass


    # Enter a parse tree produced by QuarkParser#term.
    def enterTerm(self, ctx:QuarkParser.TermContext):
        pass

    # Exit a parse tree produced by QuarkParser#term.
    def exitTerm(self, ctx:QuarkParser.TermContext):
        pass


    # Enter a parse tree produced by QuarkParser#more_expressions.
    def enterMore_expressions(self, ctx:QuarkParser.More_expressionsContext):
        pass

    # Exit a parse tree produced by QuarkParser#more_expressions.
    def exitMore_expressions(self, ctx:QuarkParser.More_expressionsContext):
        pass


    # Enter a parse tree produced by QuarkParser#Positive.
    def enterPositive(self, ctx:QuarkParser.PositiveContext):
        pass

    # Exit a parse tree produced by QuarkParser#Positive.
    def exitPositive(self, ctx:QuarkParser.PositiveContext):
        pass


    # Enter a parse tree produced by QuarkParser#Negative.
    def enterNegative(self, ctx:QuarkParser.NegativeContext):
        pass

    # Exit a parse tree produced by QuarkParser#Negative.
    def exitNegative(self, ctx:QuarkParser.NegativeContext):
        pass


    # Enter a parse tree produced by QuarkParser#Parens.
    def enterParens(self, ctx:QuarkParser.ParensContext):
        pass

    # Exit a parse tree produced by QuarkParser#Parens.
    def exitParens(self, ctx:QuarkParser.ParensContext):
        pass


    # Enter a parse tree produced by QuarkParser#True.
    def enterTrue(self, ctx:QuarkParser.TrueContext):
        pass

    # Exit a parse tree produced by QuarkParser#True.
    def exitTrue(self, ctx:QuarkParser.TrueContext):
        pass


    # Enter a parse tree produced by QuarkParser#False.
    def enterFalse(self, ctx:QuarkParser.FalseContext):
        pass

    # Exit a parse tree produced by QuarkParser#False.
    def exitFalse(self, ctx:QuarkParser.FalseContext):
        pass


    # Enter a parse tree produced by QuarkParser#StringLiteral.
    def enterStringLiteral(self, ctx:QuarkParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by QuarkParser#StringLiteral.
    def exitStringLiteral(self, ctx:QuarkParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by QuarkParser#List.
    def enterList(self, ctx:QuarkParser.ListContext):
        pass

    # Exit a parse tree produced by QuarkParser#List.
    def exitList(self, ctx:QuarkParser.ListContext):
        pass


    # Enter a parse tree produced by QuarkParser#EmptyList.
    def enterEmptyList(self, ctx:QuarkParser.EmptyListContext):
        pass

    # Exit a parse tree produced by QuarkParser#EmptyList.
    def exitEmptyList(self, ctx:QuarkParser.EmptyListContext):
        pass


    # Enter a parse tree produced by QuarkParser#varconst.
    def enterVarconst(self, ctx:QuarkParser.VarconstContext):
        pass

    # Exit a parse tree produced by QuarkParser#varconst.
    def exitVarconst(self, ctx:QuarkParser.VarconstContext):
        pass


    # Enter a parse tree produced by QuarkParser#block.
    def enterBlock(self, ctx:QuarkParser.BlockContext):
        pass

    # Exit a parse tree produced by QuarkParser#block.
    def exitBlock(self, ctx:QuarkParser.BlockContext):
        pass


    # Enter a parse tree produced by QuarkParser#statement.
    def enterStatement(self, ctx:QuarkParser.StatementContext):
        pass

    # Exit a parse tree produced by QuarkParser#statement.
    def exitStatement(self, ctx:QuarkParser.StatementContext):
        pass


    # Enter a parse tree produced by QuarkParser#func_call.
    def enterFunc_call(self, ctx:QuarkParser.Func_callContext):
        pass

    # Exit a parse tree produced by QuarkParser#func_call.
    def exitFunc_call(self, ctx:QuarkParser.Func_callContext):
        pass


    # Enter a parse tree produced by QuarkParser#assignment.
    def enterAssignment(self, ctx:QuarkParser.AssignmentContext):
        pass

    # Exit a parse tree produced by QuarkParser#assignment.
    def exitAssignment(self, ctx:QuarkParser.AssignmentContext):
        pass


    # Enter a parse tree produced by QuarkParser#main.
    def enterMain(self, ctx:QuarkParser.MainContext):
        pass

    # Exit a parse tree produced by QuarkParser#main.
    def exitMain(self, ctx:QuarkParser.MainContext):
        pass


    # Enter a parse tree produced by QuarkParser#things.
    def enterThings(self, ctx:QuarkParser.ThingsContext):
        pass

    # Exit a parse tree produced by QuarkParser#things.
    def exitThings(self, ctx:QuarkParser.ThingsContext):
        pass


    # Enter a parse tree produced by QuarkParser#morethings.
    def enterMorethings(self, ctx:QuarkParser.MorethingsContext):
        pass

    # Exit a parse tree produced by QuarkParser#morethings.
    def exitMorethings(self, ctx:QuarkParser.MorethingsContext):
        pass


