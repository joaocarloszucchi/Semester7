"""
(Exerc. 03) O Problema do Fazendeiro consiste no seguinte:
Um fazendeiro encontra-se na margem esquerda de um rio, levando consigo um lobo, uma ovelha e um repolho. O 
fazendeiro precisa atingir a outra margem do rio com toda a sua carga intacta, mas para isso dispõe somente de um 
pequeno bote com capacidade para levar apenas ele mesmo e mais uma de suas cargas. O fazendeiro poderia cruzar o 
rio quantas vezes fossem necessárias para trasportar seus pertences, mas o problema é que, na ausência do fazendeiro, 
o lobo pode comer a ovelha e essa, por sua vez, pode comer o repolho. Encontrar:
a) uma sequência de passos que resolva esse problema.
Para representar os estados desse problema, podemos usar uma estrutura da forma [F, L, O, R], cujas variáveis denotam, 
respectivamente, as posições do fazendeiro, do lobo, da ovelha e do repolho. Cada variável pode assumir os valores e ou 
d, dependendo da margem do rio onde o objeto se encontra. As ações podem ser representadas pelos seguintes 
operadores:
oper(vai, [e, L, O, R], [d, L, O, R]) ← L ≠ O; O ≠ R
oper(levaLobo, [e, e, O, R], [d, d, O, R]) ← O ≠ R
oper(levaOvelha, [e, L, e, R], [d, L, d, R])
oper(levaRepolho, [e, L, O, e], [d, L, O, d]) ← L ≠ O
oper(volta, [d, L, O, R], [e, L, O, R]) ← L ≠ O, O ≠ R
oper(trazLobo, [d, d, O, R], [e, e, O, R]) ← O ≠ R
oper(trazOvelha, [d, L, d, R], [e, L, e, R])
oper(trazRepolho, [d, L, O, d], [e, L, O, e]) ← L ≠ O
O estado inicial é s0 = [e; e; e; e] e o conjunto de estados meta é G = {[d, d, d, d]}. Com base nessa especificação, 
apresentar:
b) o passo a passo o estado das listas de novos abertos e nodos fechados usada pelo algoritmo de busca em 
profundidade
3
c) desenhe a árvore de busca criada pelo algoritmo de busca em profundidade ao procurar a solução do problema.
c) Implementar algoritmos para solucionar as questões propostas. Entregar (i) print (em pdf) do passo a passo de 
execução dos algoritmos e das soluções do problema e (ii) código fonte das implementações: legível, identado, variáveis 
nomeadas de forma compreensível, comentado - padrão JavaDoc ou Doxigen, e orientado a objetos.
"""

class StateManager:
    farmer = None
    wolf = None
    sheep = None
    cabbage = None
    visitedStates = []
    opposite = {'L':'R', 'R':'L'}
    counter = 0

    def __init__(self, fPos, wPos, sPos, cPos):
        self.farmer = fPos
        self.wolf = wPos
        self.sheep = sPos
        self.cabbage = cPos

    def depthFirstSearch(self):
        """Finds a solution to the Farmer problem using a Depth First Search"""
        state = (self.farmer, self.wolf, self.sheep, self.cabbage)
        print("\nClosed states: ", self.visitedStates)
        print("F | W | S | C | State number ", self.counter)
        print(self.farmer + ' | ' + self.wolf + ' | ' + self.sheep + ' | ' + self.cabbage)
        self.counter += 1

        if self.isStateFinal(state):
            print("Solution found!")
            return True
        
        self.visitedStates.append(state)

        possibleTransitions = self.generatePossibleTransitions(state)

        for i in range(len(possibleTransitions)):
            self.farmer = possibleTransitions[i][0]
            self.wolf = possibleTransitions[i][1]
            self.sheep = possibleTransitions[i][2]
            self.cabbage = possibleTransitions[i][3]
            self.printTransition(state, (self.farmer, self.wolf, self.sheep, self.cabbage))
            if self.depthFirstSearch():
                return True
        
        return False

    def generatePossibleTransitions(self, state):
        """Generate the possible transitions"""
        f = state[0]
        w = state[1]
        s = state[2]
        c = state[3]
        transitions = []
        candidates = []
        
        candidates.append((self.opposite[f], w, s, c))#farmer moving to the other side

        #if they are in the same side
        if f == w:#farmer taking the wolf to the other side
            candidates.append((self.opposite[f], self.opposite[w], s, c))
        if f == s:#farmer taking the sheep to the other side
            candidates.append((self.opposite[f], w, self.opposite[s], c))
        if f == c:#farmer taking the cabbage to the other side
            candidates.append((self.opposite[f], w, s, self.opposite[c]))

        for i in range(len(candidates)):
            if self.isStatePossible(candidates[i]):
                transitions.append(candidates[i])

        return transitions
    
    def isStatePossible(self, state):
        """checks if a state is possible"""
        f = state[0]
        w = state[1]
        s = state[2]
        c = state[3]

        #wolf and sheep together without the farmer
        if w == s and f != w:
            return False
        #sheep and cabbage together without the farmer
        elif s == c and f != s:
            return False
        #state already visited
        elif state in self.visitedStates:
            return False
        return True
    
    def isStateFinal(self, state):
        for i in range(4):
            if state[i] != 'R':
                return False
        return True

    @staticmethod
    def printTransition(state0, state1):
        if state0[1] != state1[1]:
            print("Moving wolf from " + state0[0] + " to " + state1[0] + '\n')
        elif state0[2] != state1[2]:
            print("Moving sheep from " + state0[0] + " to " + state1[0] + '\n') 
        elif state0[3] != state1[3]:
            print("Moving cabbage from " + state0[0] + " to " + state1[0] + '\n')
        else:
            print("Moving farmer from " + state0[0] + " to " + state1[0] + '\n')

if __name__ == '__main__':
    control = StateManager('L', 'L', 'L', 'L')
    print("\n------Starting q3------")
    control.depthFirstSearch()
    print("\n------Finishing q3------")