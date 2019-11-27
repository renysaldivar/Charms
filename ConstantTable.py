# Class that stores the constant table structure, composed of several constants

from Constant import Constant

class ConstantTable:
    def __init__(self, constants):
        self.constants = {}

    # Checks if constant already exists.
	# If not, creates a new function and inserts it into the table.
    def insertConstant(self, constantValue, constantType, constantAddress):
        if constantValue in self.constants:
            raise Exception("{} already exists in the directory".format(constantValue))
        else:
            c = Constant(constantType, constantAddress)
            self.constants[constantValue] = c

    def printTable(self):
        for constant in self.constants:
            print(constant, self.constants[constant].constantType, self.constants[constant].constantAddress)
