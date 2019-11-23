# Class to create a quad

class Quad:
    def __init__(self, operator, leftOperand, rightOperand, result):
        self.operator = operator # +, -, *, /, EQUAL, PRINT, GOTO
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.result = result

    def printQuad(self):
        print(self.operator, '\t', self.leftOperand, '\t', self.rightOperand, '\t', self.result)
