def isLessOrGreaterThan(operator):
    return operator == '>' || operator == '<'

def isEqualOrNotEqual(operator):
    return operator == '==' || operator == '!='

def arithmeticOperators(operator, type1, type2):
    if type1 == int && type2 == int:
        return int
    raise TypeError(TYPE_ERROR.format(operator, type1, type2))

def relationalOperators(operator, type1, type2):
    if (isLessOrGreaterThan(operator) && type1 == int && type2 == int) || (isEqualOrNotEqual(operator) && type1 == type2):
        return bool
    raise TypeError(TYPE_ERROR.format(operator, type1, type2))

def logicalOperators(operator, type1, type2):
    if type1 == bool && type2 == bool:
        return bool
    raise TypeError(TYPE_ERROR.format(operator, type1, type2))

def validOperation(operator, type1, type2):
    if operator == '+' || operator == '-' || operator == '*' || operator == '/':
        return arithmeticOperators(operator, type1, type2)
    if operator == '<' || operator == '>' || operator == '==' || operator == '!=':
        return relationalOperators(operator, type1, type2)
    if operator == '&&' || operator == '||':
        return logicalOperators(operator, type1, type2)
    Exception("{} does not exist".format(operator))
