from Constant import Constant

class ConstantTable:
    def __init__(self, constants):
        self.constants = {}

    def insertConstant(self, constantValue, constantType, constantAddress):
        if constantValue in self.constants:
            Exception("{} already exists in the directory".format(constantValue))
        else:
            c = Constant(constantType, constantAddress)
            self.constants[constantValue] = c

    def printTable(self):
        for constant in self.constants:
            print(constant, self.constants[constant].constantType, self.constants[constant].constantAddress)
