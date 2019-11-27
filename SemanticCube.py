def isLessOrGreaterThan(operator):
    return operator == '>' or operator == '<'

def isEqualOrNotEqual(operator):
    return operator == '==' or operator == '!='

def arithmeticOperators(operator, type1, type2):
    if type1 == 'int' and type2 == 'int':
        return 'int'
    raise Exception("Type Error")

def relationalOperators(operator, type1, type2):
    if (isLessOrGreaterThan(operator) and type1 == 'int' and type2 == 'int') or (isEqualOrNotEqual(operator) and type1 == type2):
        return 'bool'
    raise Exception("Type Error")

def logicalOperators(operator, type1, type2):
    if type1 == 'bool' and type2 == 'bool':
        return 'bool'
    raise Exception("Type Error")

def assignmentOperator(operator, type1, type2):
    if type1 == type2:
        return 'true'
    raise Exception("Type Error")

def validOperation(operator, type1, type2):
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        return arithmeticOperators(operator, type1, type2)
    if operator == '<' or operator == '>' or operator == '==' or operator == '!=':
        return relationalOperators(operator, type1, type2)
    if operator == '&&' or operator == '||':
        return logicalOperators(operator, type1, type2)
    if operator == '=':
        return assignmentOperator(operator, type1, type2)
    raise Exception("{} does not exist".format(operator))
