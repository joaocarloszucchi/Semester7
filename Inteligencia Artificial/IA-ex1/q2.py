"""
(Exerc. 02) Problema dos Jarros consiste no seguinte: 
Há dois jarros com capacidades de 3 e 4 litros, respectivamente. Nenhum dos jarros contém qualquer medida ou escala, 
de modo que só se pode saber o conteúdo exato quando eles estão cheios. Sabendo-se que podemos encher ou esvaziar 
um jarro, bem como transferir água de um jarro para outro, encontre: 
a) uma sequência de passos que deixe o jarro de 4 litros com exatamente 2 litros de água. 
Para representar os estados desse problema, podemos usar um par [X, Y ], onde X ϵ {0, 1, 2, 3} representa o conteúdo do 
primeiro jarro e Y ϵ {0, 1, 2, 3, 4} representa o conteúdo do segundo jarro. 
As ações podem ser representadas pelos seguintes operadores: 
oper(enche1, [X, Y ], [3, Y ]) ← X < 3 
oper(enche2, [X, Y ], [X, 4])  ← Y < 4 
oper(esvazia1, [X, Y ], [0, Y ]) ←  X > 0 
oper(esvazia2, [X, Y ], [X, 0]) ←  Y > 0 
oper(despeja1em2, [X, Y ], [0, X + Y ]) ←  X > 0, Y < 4, X + Y ≤ 4 
oper(despeja1em2, [X, Y ], [X + Y – 4, 4])  ← X > 0; Y < 4, X + Y > 4 
oper(despeja2em1, [X, Y ], [X + Y, 0]) ← X < 3, Y > 0, X + Y ≤ 3 
oper(despeja2em1, [X, Y ], [3, X + Y – 3]) ←  X < 3, Y > 0, X + Y > 3 
O estado inicial é s0 = [0, 0] e o conjunto de estados meta é G = {[X, 2]}. Com base nessa especificação, apresentar: 
b) o passo a passo o estado das listas de novos abertos e nodos fechados usada pelo algoritmo de busca em largura 
c) desenho da árvore de busca criada pelo algoritmo de busca em largura ao procurar a solução do problema. 
c) Implementar algoritmos para solucionar as questões propostas. Entregar (i) print (em pdf) do passo a passo de 
execução dos algoritmos e das soluções do problema e (ii) código fonte das implementações: legível, identado, variáveis 
nomeadas de forma compreensível, comentado - padrão JavaDoc ou Doxigen, e orientado a objetos.
"""

class StateManager:
    bowl3 = None
    bowl4 = None
    queueStates = []
    visitedStates = []
    counter = 0

    def __init__(self, vol3, vol4):
        self.bowl3 = vol3
        self.bowl4 = vol4

    def breadthFirstSearch(self):
        """Finds a solution to the Bowls problem using the Breadth First Search"""
        state = (self.bowl3, self.bowl4)
        self.queueStates.append(state)

        while self.queueStates:
            print("\nClosed states: ", self.visitedStates)
            print("Queue order: ", self.queueStates)
            print("Bowl3 | Bowl4 | State number ", self.counter)
            print(str(self.bowl3) + '     | ' + str(self.bowl4))
            self.counter += 1
        
            if self.isStateFinal(state):
                print("Solution found!")
                return True
            
            self.visitedStates.append(state)
            self.generatePossibleTransitions(state)
            self.queueStates.pop(0)

            state = self.queueStates[0]
            self.bowl3 = state[0]
            self.bowl4 = state[1]

    def generatePossibleTransitions(self, state):
        """Generate the possible transitions"""
        bowl3 = state[0]
        bowl4 = state[1]
        candidates = []

        candidates.append((3, bowl4))# full bowl3
        candidates.append((bowl3, 4))# full bowl4
        candidates.append((0, bowl4))# empty bowl3
        candidates.append((bowl3, 0))# empty bowl4
        if bowl3 + bowl4 > 4:#throw bowl3 in bowl4
            remaining = bowl3 + bowl4 - 4
            candidates.append((remaining, 4))
        else:
            candidates.append((0, bowl3 + bowl4))

        if bowl4 + bowl3 > 3:#throw bowl4 in bowl3
            remaining = bowl4 + bowl3 - 3
            candidates.append((3, remaining))
        else:
            candidates.append((bowl4 + bowl3, 0))

        for i in range(len(candidates)):
            if self.isStatePossible(candidates[i]):
                print("candidate ", candidates[i], "from", state)
                self.queueStates.append(candidates[i])

    def isStatePossible(self, state):
        """Checks if the state is valid"""
        return not state in self.visitedStates

    def isStateFinal(self, state):
        return state[1] == 2


    
if __name__ == '__main__':
    control = StateManager(0, 0)
    print("\n------Starting q2------")
    control.breadthFirstSearch()
    print("\n------Finishing q2------")