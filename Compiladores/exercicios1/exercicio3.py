'''
construir função q valide os tokens da gramatica

P={ S → aSc | bXc | aA | bB
X → bXc | bB
A → aA | bB | ε
B → bB | ε }

de grosso modo, eh um a+b+c* sendo que c < a + b
'''

def validateToken(token):
    a = 0
    b = 0
    c = 0

    if len(token) == 0:
        # ε n está no alfabeto
        return False

    for i in token:
        if i == 'a':
            if b + c != 0:
                #evite situações em que um b ou c foi lido antes de um a
                return False
            a += 1
        elif i == 'b':
            if c != 0:
                #evite situações em que um c foi lido antes de um b
                return False
            b += 1
        elif i == 'c':
            c += 1
        else:
            #caractere n está no alfabeto
            return False

    if c >= a + b or (a == 0 and b == 0):
        return False
    return True

r = validateToken("abbcc")

if r:
    print("deu bom")
else:
    print("deu ruim")