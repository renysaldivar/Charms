# Class to store information about a constant

class Constant:
    def __init__(self, constantType, constantAddress):
        self.constantType = constantType # int, bool
        self.constantAddress = constantAddress # memory address

    def updateAddress(self, newAddress):
        self.constantAddress = newAddress
