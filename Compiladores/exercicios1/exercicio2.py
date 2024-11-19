
def extractTokens(program):
    tokens = []
    token = ''
    
    for i in program:
        if i != ' ':
            token = token + i
        elif i == ' ' and len(token) > 0:
            tokens.append(token)
            token = ''
    print(tokens)
    return tokens 

def numberOrReal(token):
    for i in token:
        if i == '.':
            return 'NUMR'
    return 'NUMI'

def checkTokens(tokens):
    mathOperators = {'+': 'SUM', '-': 'SUB', '*': 'MULT', '/': 'DIV'}
    reservedWords = {'for': 'FL', 'while': 'WL', 'if': 'IF', 'else': 'EL'}
    delimiters = {'(': 'OP', ')': 'CP', '[': 'OB', ']': 'CB', '{': 'OCB', '}': 'CCB'}
    booleans = {'>': 'BT', '<': 'ST', '==' : 'EQ', '!=': 'DF'}


    tokenTuple = []
    
    for token in tokens:
        if token[0] == "'" and token[-1] == "'":
            #STRINGS
            tokenTuple.append((token, 'STR'))
        elif token in mathOperators:
            #MATH OPERATORS
            tokenTuple.append((token, mathOperators[token]))
        elif token in reservedWords:
            #RESERVED WORDS
            tokenTuple.append((token, reservedWords[token]))
        elif token in delimiters:
            #DELIMITERS
            tokenTuple.append((token, delimiters[token]))
        elif token in booleans:
            #BOOLEAN OPERATORS
            tokenTuple.append((token, booleans[token]))
        elif ord(token[0]) > 47 and ord(token[0]) < 58:
            #NUMBERS
            tokenTuple.append((token, numberOrReal(token)))
        elif len(token) > 1 and (token[0] == '+' or token[0] == '-'):
            #SIGNED NUMBERS
            if ord(token[1]) > 47 and ord(token[1]) < 58:
                tokenTuple.append((token, numberOrReal(token)))
        elif (ord(token[0]) > 64 and ord(token[0]) < 91) or (ord(token[0]) > 96 and ord(token[0]) < 123) or (ord(token[0]) == 95):
            #VARIABLES (A-Z) or (a-z) or (_)
            tokenTuple.append((token, 'VAR'))

    return tokenTuple
tokens = extractTokens("if ( x > 27 ) y + 7 else z + -0.73")
result = checkTokens(tokens)
print(result)
