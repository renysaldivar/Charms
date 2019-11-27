# Module that handles quadruples

def printQuadruples(quadruples):
    for quad in quadruples:
        quad.printQuad()

# Function to convert the operands and result in the quadruples from names to memory addresses for execution
def convertQuadruples(quadruples, functionDirectory, constantTable, varTable):
    currentFunctionIndex = 0
    functionDirectoryList = list(functionDirectory.dictionary)

    for quad in quadruples:
        key = functionDirectoryList[currentFunctionIndex]
        currentFunction = functionDirectory.dictionary[key]

        if quad.operator != 'ERA' and quad.operator != 'GOSUB' and quad.operator != 'goto':
            leftOperand = quad.leftOperand
            rightOperand = quad.rightOperand
            result = quad.result
            parameterTable = currentFunction.parameterTable.parameters
            constants = constantTable.constants
            variables = varTable.vars
            tempVariableTable = currentFunction.tempVariableTable.tempVariables

            # Left operand
            if leftOperand in parameterTable:
                quad.leftOperand = parameterTable[leftOperand].parameterAddress
            elif leftOperand in constants:
                quad.leftOperand = constants[leftOperand].constantAddress
            elif leftOperand in variables:
                quad.leftOperand = variables[leftOperand].varAddress
            elif leftOperand in tempVariableTable:
                quad.leftOperand = tempVariableTable[leftOperand].tempVariableAddress

            # Right operand
            if rightOperand in parameterTable:
                quad.rightOperand = parameterTable[rightOperand].parameterAddress
            elif rightOperand in constants:
                quad.rightOperand = constants[rightOperand].constantAddress
            elif rightOperand in variables:
                quad.rightOperand = variables[rightOperand].varAddress
            elif rightOperand in tempVariableTable:
                quad.rightOperand = tempVariableTable[rightOperand].tempVariableAddress

            # Result
            if quad.operator != 'gotoF':
                if result in parameterTable:
                    quad.result = parameterTable[result].parameterAddress
                elif result in constants:
                    quad.result = constants[result].constantAddress
                elif result in variables:
                    quad.result = variables[result].varAddress
                elif result in tempVariableTable:
                    quad.result = tempVariableTable[result].tempVariableAddress

        if quad.operator == 'ENDPROC' or quad.operator == 'END':
            currentFunctionIndex += 1