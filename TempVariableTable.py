# Class that stores the variable table structure, composed of several temp variables
from TempVariable import TempVariable

class TempVariableTable:
    def __init__(self, tempVariables):
        self.tempVariables = {}

    # Checks if temporal variable name has already been used.
	# If not, creates a new tempVariable and inserts it into the table.
    def insertTempVariable(self, tempVariableId, tempVariableType, tempVariableAddress):
        if tempVariableId in self.tempVariables:
            raise Exception("{} already exists in the directory".format(varId))
        else:
            tv = TempVariable(tempVariableType, tempVariableAddress)
            self.tempVariables[tempVariableId] = tv

    def printTable(self):
        for tempVariable in self.tempVariables:
            print(tempVariable, self.tempVariables[tempVariable].tempVariableType, self.tempVariables[tempVariable].tempVariableAddress)