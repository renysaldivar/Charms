def isLessOrGreaterThan(operator):
    return operator == '>' or operator == '<'

def isEqualOrNotEqual(operator):
    return operator == '==' or operator == '!='

def arithmeticOperators(operator, type1, type2):
    if type1 == 'int' and type2 == 'int':
        return 'int'
    raise TypeError(TYPE_ERROR.format(operator, type1, type2))

def relationalOperators(operator, type1, type2):
    if (isLessOrGreaterThan(operator) and type1 == 'int' and type2 == 'int') or (isEqualOrNotEqual(operator) and type1 == type2):
        return 'bool'
    raise TypeError(TYPE_ERROR.format(operator, type1, type2))

def logicalOperators(operator, type1, type2):
    if type1 == 'bool' and type2 == 'bool':
        return 'bool'
    raise TypeError(TYPE_ERROR.format(operator, type1, type2))

def validOperation(operator, type1, type2):
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        return arithmeticOperators(operator, type1, type2)
    if operator == '<' or operator == '>' or operator == '==' or operator == '!=':
        return relationalOperators(operator, type1, type2)
    if operator == '&&' or operator == '||':
        return logicalOperators(operator, type1, type2)
    Exception("{} does not exist".format(operator))
