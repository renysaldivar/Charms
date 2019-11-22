from TempVariable import TempVariable

class TempVariableTable:
    def __init__(self, tempVariables):
        self.tempVariables = {}

    def insertTempVariable(self, tempVariableId, tempVariableType, tempVariableAddress):
        if tempVariableId in self.tempVariables:
            Exception("{} already exists in the directory".format(varId))
        else:
            tv = TempVariable(tempVariableType, tempVariableAddress)
            self.tempVariables[tempVariableId] = tv

    def printTable(self):
        for tempVariable in self.tempVariables:
            print(tempVariable, self.tempVariables[tempVariable].tempVariableType, self.tempVariables[tempVariable].tempVariableAddress)