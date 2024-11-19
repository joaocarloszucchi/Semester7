'''
Dada a gramática G = ({E,E’,T,T’,F}, {+,-,*,/, num}, P, E), onde P contém as
produções:
E à T E’
E’ à + T E’ | - T E’ | ε
T à F T’
T’ à * F T’ | / F T’ | ε
F à (E) | num

de grosso modo, reconhece expressões artiméticas com numeros de apenas 1 digito
também suporta parênteses para indicar precedência de operadores
'''


def extractTokens(program):
    tokens = []
    token = ''
    program = program + ' '
    for i in program:
        if i != ' ':
            token = token + i
        elif i == ' ' and len(token) > 0:
            tokens.append(token)
            token = ''
    print(tokens)
    return tokens 

def checkParenthesis(tokens):
    #used to check if every open parenthesis has a corresponding closing one
    opened = 0
    closed = 0
    toRemove = []

    for token in tokens:
        if token == '(':
            if closed > opened:
                #para prevenir casos como " )( "
                return False
            opened += 1
            toRemove.append(token)
        elif token == ')':
            closed += 1
            toRemove.append(token)

    for token in toRemove:
        tokens.remove(token)

    return opened == closed

def checkOperators(tokens):
    #used to check if between 2 numbers there is a operation. To avoid things like " + * 5 6 "
    last = ""
    for token in tokens:
        if ord(token) > 47 and ord(token) < 58:
            if last == 'NUM':
                return False
            last = 'NUM'
        else:
            if last == 'OP':
                return False
            last = 'OP'
    return True

def checkTokens(tokens):
    return checkParenthesis(tokens) and checkOperators(tokens)


tokens = extractTokens("+ 5 * ( ( 7 + 5 ) - 7 ) / 4")
result = checkTokens(tokens)
print(result)