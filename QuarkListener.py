# Generated from Quark.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QuarkParser import QuarkParser
else:
    from QuarkParser import QuarkParser

from collections import namedtuple
from arithmetic_cube import check_operation_type
import pprint
pp = pprint.PrettyPrinter()


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


    # Enter a parse tree produced by QuarkParser#JustTerm.
    def enterJustTerm(self, ctx:QuarkParser.JustTermContext):
        pass

    # Exit a parse tree produced by QuarkParser#JustTerm.
    def exitJustTerm(self, ctx:QuarkParser.JustTermContext):
        pass


    # Enter a parse tree produced by QuarkParser#Addition.
    def enterAddition(self, ctx:QuarkParser.AdditionContext):
        pass

    # Exit a parse tree produced by QuarkParser#Addition.
    def exitAddition(self, ctx:QuarkParser.AdditionContext):
        pass


    # Enter a parse tree produced by QuarkParser#Substraction.
    def enterSubstraction(self, ctx:QuarkParser.SubstractionContext):
        pass

    # Exit a parse tree produced by QuarkParser#Substraction.
    def exitSubstraction(self, ctx:QuarkParser.SubstractionContext):
        pass


    # Enter a parse tree produced by QuarkParser#Greater.
    def enterGreater(self, ctx:QuarkParser.GreaterContext):
        pass

    # Exit a parse tree produced by QuarkParser#Greater.
    def exitGreater(self, ctx:QuarkParser.GreaterContext):
        pass


    # Enter a parse tree produced by QuarkParser#Lesser.
    def enterLesser(self, ctx:QuarkParser.LesserContext):
        pass

    # Exit a parse tree produced by QuarkParser#Lesser.
    def exitLesser(self, ctx:QuarkParser.LesserContext):
        pass


    # Enter a parse tree produced by QuarkParser#Equal.
    def enterEqual(self, ctx:QuarkParser.EqualContext):
        pass

    # Exit a parse tree produced by QuarkParser#Equal.
    def exitEqual(self, ctx:QuarkParser.EqualContext):
        pass


    # Enter a parse tree produced by QuarkParser#GreaterEqual.
    def enterGreaterEqual(self, ctx:QuarkParser.GreaterEqualContext):
        pass

    # Exit a parse tree produced by QuarkParser#GreaterEqual.
    def exitGreaterEqual(self, ctx:QuarkParser.GreaterEqualContext):
        pass


    # Enter a parse tree produced by QuarkParser#LesserEqual.
    def enterLesserEqual(self, ctx:QuarkParser.LesserEqualContext):
        pass

    # Exit a parse tree produced by QuarkParser#LesserEqual.
    def exitLesserEqual(self, ctx:QuarkParser.LesserEqualContext):
        pass


    # Enter a parse tree produced by QuarkParser#NotEqual.
    def enterNotEqual(self, ctx:QuarkParser.NotEqualContext):
        pass

    # Exit a parse tree produced by QuarkParser#NotEqual.
    def exitNotEqual(self, ctx:QuarkParser.NotEqualContext):
        pass


    # Enter a parse tree produced by QuarkParser#JustFactor.
    def enterJustFactor(self, ctx:QuarkParser.JustFactorContext):
        pass

    # Exit a parse tree produced by QuarkParser#JustFactor.
    def exitJustFactor(self, ctx:QuarkParser.JustFactorContext):
        pass


    # Enter a parse tree produced by QuarkParser#Multiplication.
    def enterMultiplication(self, ctx:QuarkParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by QuarkParser#Multiplication.
    def exitMultiplication(self, ctx:QuarkParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by QuarkParser#Division.
    def enterDivision(self, ctx:QuarkParser.DivisionContext):
        pass

    # Exit a parse tree produced by QuarkParser#Division.
    def exitDivision(self, ctx:QuarkParser.DivisionContext):
        pass


    # Enter a parse tree produced by QuarkParser#Modulo.
    def enterModulo(self, ctx:QuarkParser.ModuloContext):
        pass

    # Exit a parse tree produced by QuarkParser#Modulo.
    def exitModulo(self, ctx:QuarkParser.ModuloContext):
        pass


    # Enter a parse tree produced by QuarkParser#more_expressions.
    def enterMore_expressions(self, ctx:QuarkParser.More_expressionsContext):
        pass

    # Exit a parse tree produced by QuarkParser#more_expressions.
    def exitMore_expressions(self, ctx:QuarkParser.More_expressionsContext):
        pass


    # Enter a parse tree produced by QuarkParser#factor.
    def enterFactor(self, ctx:QuarkParser.FactorContext):
        pass

    # Exit a parse tree produced by QuarkParser#factor.
    def exitFactor(self, ctx:QuarkParser.FactorContext):
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


