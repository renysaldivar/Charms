# Generated from CharmsParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CharmsParser import CharmsParser
else:
    from CharmsParser import CharmsParser

# This class defines a complete listener for a parse tree produced by CharmsParser.
class CharmsParserListener(ParseTreeListener):

    # Enter a parse tree produced by CharmsParser#program.
    def enterProgram(self, ctx:CharmsParser.ProgramContext):
        pass

    # Exit a parse tree produced by CharmsParser#program.
    def exitProgram(self, ctx:CharmsParser.ProgramContext):
        pass


    # Enter a parse tree produced by CharmsParser#p.
    def enterP(self, ctx:CharmsParser.PContext):
        pass

    # Exit a parse tree produced by CharmsParser#p.
    def exitP(self, ctx:CharmsParser.PContext):
        pass


    # Enter a parse tree produced by CharmsParser#p1.
    def enterP1(self, ctx:CharmsParser.P1Context):
        pass

    # Exit a parse tree produced by CharmsParser#p1.
    def exitP1(self, ctx:CharmsParser.P1Context):
        pass


    # Enter a parse tree produced by CharmsParser#p_vars.
    def enterP_vars(self, ctx:CharmsParser.P_varsContext):
        pass

    # Exit a parse tree produced by CharmsParser#p_vars.
    def exitP_vars(self, ctx:CharmsParser.P_varsContext):
        pass


    # Enter a parse tree produced by CharmsParser#v.
    def enterV(self, ctx:CharmsParser.VContext):
        pass

    # Exit a parse tree produced by CharmsParser#v.
    def exitV(self, ctx:CharmsParser.VContext):
        pass


    # Enter a parse tree produced by CharmsParser#v1.
    def enterV1(self, ctx:CharmsParser.V1Context):
        pass

    # Exit a parse tree produced by CharmsParser#v1.
    def exitV1(self, ctx:CharmsParser.V1Context):
        pass


    # Enter a parse tree produced by CharmsParser#v2.
    def enterV2(self, ctx:CharmsParser.V2Context):
        pass

    # Exit a parse tree produced by CharmsParser#v2.
    def exitV2(self, ctx:CharmsParser.V2Context):
        pass


    # Enter a parse tree produced by CharmsParser#function.
    def enterFunction(self, ctx:CharmsParser.FunctionContext):
        pass

    # Exit a parse tree produced by CharmsParser#function.
    def exitFunction(self, ctx:CharmsParser.FunctionContext):
        pass


    # Enter a parse tree produced by CharmsParser#f.
    def enterF(self, ctx:CharmsParser.FContext):
        pass

    # Exit a parse tree produced by CharmsParser#f.
    def exitF(self, ctx:CharmsParser.FContext):
        pass


    # Enter a parse tree produced by CharmsParser#f1.
    def enterF1(self, ctx:CharmsParser.F1Context):
        pass

    # Exit a parse tree produced by CharmsParser#f1.
    def exitF1(self, ctx:CharmsParser.F1Context):
        pass


    # Enter a parse tree produced by CharmsParser#f2.
    def enterF2(self, ctx:CharmsParser.F2Context):
        pass

    # Exit a parse tree produced by CharmsParser#f2.
    def exitF2(self, ctx:CharmsParser.F2Context):
        pass


    # Enter a parse tree produced by CharmsParser#section.
    def enterSection(self, ctx:CharmsParser.SectionContext):
        pass

    # Exit a parse tree produced by CharmsParser#section.
    def exitSection(self, ctx:CharmsParser.SectionContext):
        pass


    # Enter a parse tree produced by CharmsParser#type_id.
    def enterType_id(self, ctx:CharmsParser.Type_idContext):
        pass

    # Exit a parse tree produced by CharmsParser#type_id.
    def exitType_id(self, ctx:CharmsParser.Type_idContext):
        pass


    # Enter a parse tree produced by CharmsParser#assignment.
    def enterAssignment(self, ctx:CharmsParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CharmsParser#assignment.
    def exitAssignment(self, ctx:CharmsParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CharmsParser#expression.
    def enterExpression(self, ctx:CharmsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CharmsParser#expression.
    def exitExpression(self, ctx:CharmsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CharmsParser#e.
    def enterE(self, ctx:CharmsParser.EContext):
        pass

    # Exit a parse tree produced by CharmsParser#e.
    def exitE(self, ctx:CharmsParser.EContext):
        pass


    # Enter a parse tree produced by CharmsParser#exp.
    def enterExp(self, ctx:CharmsParser.ExpContext):
        pass

    # Exit a parse tree produced by CharmsParser#exp.
    def exitExp(self, ctx:CharmsParser.ExpContext):
        pass


    # Enter a parse tree produced by CharmsParser#e1.
    def enterE1(self, ctx:CharmsParser.E1Context):
        pass

    # Exit a parse tree produced by CharmsParser#e1.
    def exitE1(self, ctx:CharmsParser.E1Context):
        pass


    # Enter a parse tree produced by CharmsParser#factor.
    def enterFactor(self, ctx:CharmsParser.FactorContext):
        pass

    # Exit a parse tree produced by CharmsParser#factor.
    def exitFactor(self, ctx:CharmsParser.FactorContext):
        pass


    # Enter a parse tree produced by CharmsParser#fa.
    def enterFa(self, ctx:CharmsParser.FaContext):
        pass

    # Exit a parse tree produced by CharmsParser#fa.
    def exitFa(self, ctx:CharmsParser.FaContext):
        pass


    # Enter a parse tree produced by CharmsParser#term.
    def enterTerm(self, ctx:CharmsParser.TermContext):
        pass

    # Exit a parse tree produced by CharmsParser#term.
    def exitTerm(self, ctx:CharmsParser.TermContext):
        pass


    # Enter a parse tree produced by CharmsParser#t.
    def enterT(self, ctx:CharmsParser.TContext):
        pass

    # Exit a parse tree produced by CharmsParser#t.
    def exitT(self, ctx:CharmsParser.TContext):
        pass


    # Enter a parse tree produced by CharmsParser#condition.
    def enterCondition(self, ctx:CharmsParser.ConditionContext):
        pass

    # Exit a parse tree produced by CharmsParser#condition.
    def exitCondition(self, ctx:CharmsParser.ConditionContext):
        pass


    # Enter a parse tree produced by CharmsParser#c.
    def enterC(self, ctx:CharmsParser.CContext):
        pass

    # Exit a parse tree produced by CharmsParser#c.
    def exitC(self, ctx:CharmsParser.CContext):
        pass


    # Enter a parse tree produced by CharmsParser#loop.
    def enterLoop(self, ctx:CharmsParser.LoopContext):
        pass

    # Exit a parse tree produced by CharmsParser#loop.
    def exitLoop(self, ctx:CharmsParser.LoopContext):
        pass


    # Enter a parse tree produced by CharmsParser#read.
    def enterRead(self, ctx:CharmsParser.ReadContext):
        pass

    # Exit a parse tree produced by CharmsParser#read.
    def exitRead(self, ctx:CharmsParser.ReadContext):
        pass


    # Enter a parse tree produced by CharmsParser#write.
    def enterWrite(self, ctx:CharmsParser.WriteContext):
        pass

    # Exit a parse tree produced by CharmsParser#write.
    def exitWrite(self, ctx:CharmsParser.WriteContext):
        pass


    # Enter a parse tree produced by CharmsParser#w.
    def enterW(self, ctx:CharmsParser.WContext):
        pass

    # Exit a parse tree produced by CharmsParser#w.
    def exitW(self, ctx:CharmsParser.WContext):
        pass


    # Enter a parse tree produced by CharmsParser#w2.
    def enterW2(self, ctx:CharmsParser.W2Context):
        pass

    # Exit a parse tree produced by CharmsParser#w2.
    def exitW2(self, ctx:CharmsParser.W2Context):
        pass


    # Enter a parse tree produced by CharmsParser#var_cte.
    def enterVar_cte(self, ctx:CharmsParser.Var_cteContext):
        pass

    # Exit a parse tree produced by CharmsParser#var_cte.
    def exitVar_cte(self, ctx:CharmsParser.Var_cteContext):
        pass


    # Enter a parse tree produced by CharmsParser#func_call.
    def enterFunc_call(self, ctx:CharmsParser.Func_callContext):
        pass

    # Exit a parse tree produced by CharmsParser#func_call.
    def exitFunc_call(self, ctx:CharmsParser.Func_callContext):
        pass


    # Enter a parse tree produced by CharmsParser#fc.
    def enterFc(self, ctx:CharmsParser.FcContext):
        pass

    # Exit a parse tree produced by CharmsParser#fc.
    def exitFc(self, ctx:CharmsParser.FcContext):
        pass


