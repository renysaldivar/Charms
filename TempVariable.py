# Class to store information about a temp variable

class TempVariable:
    def __init__(self, tempVariableType, tempVariableAddress):
        self.tempVariableType = tempVariableType # int, char, bool
        self.tempVariableAddress = tempVariableAddress # memory address

    def updateAddress(self, newAddress):
        self.tempVariableAddress = newAddress
