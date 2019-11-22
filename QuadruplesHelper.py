def printQuadruples(quadruples):
    for quad in quadruples:
        quad.printQuad()

def convertQuadruples(quadruples, functionDirectory, constantTable, varTable):
    for quad in quadruples:
        if quad.operator != 'ERA' and quad.operator != 'GOSUB':
            leftOperand = quad.leftOperand
            rightOperand = quad.rightOperand
            variables = varTable.vars
            constants = constantTable.constants
            functions = functionDirectory.dictionary

            # Left operand
            if leftOperand in variables:
                quad.leftOperand = variables[leftOperand].varAddress
            elif leftOperand in constants:
                quad.leftOperand = constants[leftOperand].constantAddress

            # Right operand
            if rightOperand in variables:
                quad.rightOperand = variables[rightOperand].varAddress
            elif rightOperand in constants:
                quad.rightOperand = constants[rightOperand].constantAddress