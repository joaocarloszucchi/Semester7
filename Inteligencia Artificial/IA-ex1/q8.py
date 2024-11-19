"""
(Exerc. 8) O problema do Quebra-Cabeça de 8 consiste em movimentar as peças do quebra-cabeça horizontal ou 
verticalmente (para ocupar a posição vazia adjacente à peça) de modo que a conguração final seja alcançada: 
Por exemplo, expandindo o estado corrente acima, temos: 
Agora, usando uma função heurística, o algoritmo de busca deveria expandir o melhor entre esses dois estados 
sucessores. Mas como decidir qual deles é o melhor? Uma possibilidade  é verificar o quão longe cada peça encontra-se 
de sua posição na conguração  final e apontar como melhor estado aquele cuja soma das distâncias é mínima. Por 
exemplo, no estado s1, as peças 1, 5, 6, 7 e 8 já estão em suas posições finais. Para as peças 2, 3 e 4, a distância é 1. 
Portanto, h(s1) = 3. Analogamente, temos h(s2) = 5. Esses valores indicam que uma solução a partir do estado s1 pode 
6 
ser obtida com no mínimo mais três expansões, enquanto que uma solução a partir de s2 requer no mínimo mais cinco 
expansões. Então, o algoritmo de busca deve expandir o estado s1. 
a) Para esse problema, qual algoritmo seria mais apropriado: (i) o algoritmo de busca gulosa pela melhor escolha 
considerando que cada ação tem custo 1 ou (ii) o algoritmo de busca gulosa pela melhor escolha considerando as 
estimativas heurísticas calculadas?  
Apresentar o b) passo a passo o estado das listas de novos abertos e nodos fechados e c) desenhe a árvore de busca 
produzida pelos algoritmos citados em (i) e ii) para justificar a resposta apresentada. 
Considere que no Quebra-Cabeça de 8 cada ação tem custo 1. Usando a heurística da soma das distâncias, apresentar: 
d) o passo a passo o estado das listas de novos abertos e nodos fechados usados pelo  algoritmo A* 
e) desenhe a árvore de busca produzida pelo algoritmo A* quando o estado inicial do quebra-cabeça é [[1, 2, 3], [b, 6, 
4], [8, 7, 5]]. 
f) implementação dos algoritmos considerados neste exercício, onde deve ser entregue (i) print (em pdf) do passo a 
passo de execução dos algoritmos e das soluções do problema e (ii) código fonte das implementações: legível, identado, 
variáveis nomeadas de forma compreensível, comentado - padrão JavaDoc ou Doxigen, e orientado a objetos.  
"""

class State:
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    #this is one of the ugliest things I have ever done.
    #it returns the heuristic value of a number according to its index in the board
    h1 = {
        0: 0,
        1: 1,
        2: 2,
        3: 1,
        4: 2,
        5: 3,
        6: 2,
        7: 3,
        8: 4
    }
    h2 = {
        0: 1,
        1: 0,
        2: 1,
        3: 2,
        4: 1,
        5: 2,
        6: 3,
        7: 2,
        8: 3
    }
    h3 = {
        0: 2,
        1: 1,
        2: 0,
        3: 3,
        4: 2,
        5: 1,
        6: 4,
        7: 3,
        8: 2
    }
    h4 = {
        0: 3,
        1: 2,
        2: 1,
        3: 2,
        4: 1,
        5: 0,
        6: 3,
        7: 2,
        8: 1
    }
    h5 = {
        0: 4,
        1: 3,
        2: 2,
        3: 3,
        4: 2,
        5: 1,
        6: 2,
        7: 1,
        8: 0
    }
    h6 = {
        0: 3,
        1: 2,
        2: 3,
        3: 2,
        4: 1,
        5: 2,
        6: 1,
        7: 0,
        8: 1
    }
    h7 = {
        0: 2,
        1: 3,
        2: 4,
        3: 1,
        4: 2,
        5: 3,
        6: 0,
        7: 1,
        8: 2
    }
    h8 = {
        0: 1,
        1: 2,
        2: 3,
        3: 0,
        4: 1,
        5: 2,
        6: 1,
        7: 2,
        8: 3
    }

    def __init__(self, initial):
        self.board = initial
        self.cost = 0

    def __str__(self):
       return str(self.board) + ' ' + str(self.cost)

    def genPossibleTransitions(self):
        board = self.board
        pos = board.index(0)
        transitions = []

        if pos == 0:
            transitions.append(State(self.switch(board, pos, 1)))
            transitions.append(State(self.switch(board, pos, 3)))
        elif pos == 1:
            transitions.append(State(self.switch(board, pos, 0)))
            transitions.append(State(self.switch(board, pos, 2)))
            transitions.append(State(self.switch(board, pos, 4)))
        elif pos == 2:
            transitions.append(State(self.switch(board, pos, 1)))
            transitions.append(State(self.switch(board, pos, 5)))
        elif pos == 3:
            transitions.append(State(self.switch(board, pos, 0)))
            transitions.append(State(self.switch(board, pos, 4)))
            transitions.append(State(self.switch(board, pos, 6)))
        elif pos == 4:  # in the middle
            transitions.append(State(self.switch(board, pos, 5)))
            transitions.append(State(self.switch(board, pos, 3)))
            transitions.append(State(self.switch(board, pos, 1)))
            transitions.append(State(self.switch(board, pos, 7)))
        elif pos == 5:
            transitions.append(State(self.switch(board, pos, 2)))
            transitions.append(State(self.switch(board, pos, 4)))
            transitions.append(State(self.switch(board, pos, 8)))
        elif pos == 6:
            transitions.append(State(self.switch(board, pos, 3)))
            transitions.append(State(self.switch(board, pos, 7)))
        elif pos == 7:
            transitions.append(State(self.switch(board, pos, 4)))
            transitions.append(State(self.switch(board, pos, 6)))
            transitions.append(State(self.switch(board, pos, 8)))
        elif pos == 8:
            transitions.append(State(self.switch(board, pos, 5)))
            transitions.append(State(self.switch(board, pos, 7)))
        return transitions

    def switch(self, board, i, j):
        copy = board.copy()
        temp = copy[i]
        copy[i] = copy[j]
        copy[j] = temp
        return copy

    def evalHeuristic(self):
        board = self.board
        h1 = self.h1[board.index(1)]
        h2 = self.h2[board.index(2)]
        h3 = self.h3[board.index(3)]
        h4 = self.h4[board.index(4)]
        h5 = self.h5[board.index(5)]
        h6 = self.h6[board.index(6)]
        h7 = self.h7[board.index(7)]
        h8 = self.h8[board.index(8)]

        self.cost = h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8
        
    def addStep(self):
        self.cost += 1

class StateManager:
    def __init__(self, initial):
        self.queueStates = [] 
        self.closedStates = []
        self.states = []
        self.current = State(initial)
        self.goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.current.evalHeuristic()
        self.counter = 0

    def printStates(self):
        print("Printing States:")
        for state in self.states:
            print(f"Current: {state.current}, Cost: {state.current.cost}")

    def greedySearchH(self):
        print("\nStarting Greedy Search Heuristic")

        self.queueStates.append(self.current)
        self.closedStates.append(self.current.board)

        while self.queueStates:
            print("\nClosed states: ", self.closedStates)
            #print("Queue order: ", printList(self.queueStates))
            print("Current state and cost          | State number ", self.counter)
            print(str(self.current)  + '   | ')
            self.counter += 1

            if self.counter == 100000:
                return

            if self.isStateFinal():
                print("Solution found!")
                return True
            
            self.queueStates.pop(0)
            self.generateDestiniesH()
            self.current = self.queueStates[0]

        print("\nFinishing Greedy Search Heuristic\n")

    def greedySearchS(self):
        print("\nStarting Greedy Search S(step)")

        self.queueStates.append(self.current)
        self.closedStates.append(self.current.board)

        while self.queueStates:
            print("\nClosed states: ", self.closedStates)
            #print("Queue order: ", printList(self.queueStates))
            print("Current state and cost          | State number ", self.counter)
            print(str(self.current)  + '   | ')
            self.counter += 1

            if self.counter == 100000:
                return

            if self.isStateFinal():
                print("Solution found!")
                return True
            
            self.queueStates.pop(0)
            self.generateDestiniesS()
            self.current = self.queueStates[0]

        print("\nFinishing Greedy Search S(step)\n")

    def greedySearchA(self):
        print("\nStarting Greedy Search A*")

        self.queueStates.append(self.current)
        self.closedStates.append(self.current.board)

        while self.queueStates:
            print("\nClosed states: ", self.closedStates)
            #print("Queue order: ", printList(self.queueStates))
            print("Current state and cost          | State number ", self.counter)
            print(str(self.current)  + '   | ')
            self.counter += 1

            if self.counter == 100000:
                return

            if self.isStateFinal():
                print("Solution found!")
                return True
            
            self.queueStates.pop(0)
            self.generateDestiniesA()
            self.current = self.queueStates[0]

        print("\nFinishing Greedy Search Heuristic\n")

    def generateDestiniesH(self):
        """Generate the possible destinies from self.current using the Greedy Search Algorithm Heuristic"""
        transitions = self.current.genPossibleTransitions()
        
        for i in range(len(transitions)):
            if transitions[i].board not in self.closedStates:
                transitions[i].evalHeuristic()
                self.queueStates.append(transitions[i])
                self.closedStates.append(transitions[i].board)
                #print("\ncandidate: ", transitions[i])
        self.sortByCost()

    def generateDestiniesS(self):
        """Generate the possible destinies from self.current using the Greedy Search Algorithm S(+1 by step)"""
        transitions = self.current.genPossibleTransitions()
        
        for i in range(len(transitions)):
            if transitions[i].board not in self.closedStates:
                transitions[i].cost = transitions[i].cost + 1
                self.queueStates.append(transitions[i])
                self.closedStates.append(transitions[i].board)
                #print("\ncandidate: ", transitions[i])
        self.sortByCost()

    def generateDestiniesA(self):
        """Generate the possible destinies from self.current using the Greedy Search Algorithm A*"""
        transitions = self.current.genPossibleTransitions()
        
        for i in range(len(transitions)):
            if transitions[i].board not in self.closedStates:
                transitions[i].evalHeuristic()
                transitions[i].addStep()
                self.queueStates.append(transitions[i])
                self.closedStates.append(transitions[i].board)
                #print("\ncandidate: ", transitions[i])
        self.sortByCost()

    def isStateFinal(self):
        return self.current.board == self.goal
    
    def sortByCost(self):
        self.queueStates = sorted(self.queueStates, key = lambda state: state.cost)

if __name__ == '__main__':
    print("\n------Starting q8------")

    #controlH = StateManager([3, 2, 4, 0, 7, 8, 1, 5, 6]) IMPOSSIBLE
    controlH = StateManager([1, 3, 4, 8, 2, 0, 7, 6, 5])
    controlH.greedySearchH()

    controlS = StateManager([1, 3, 4, 8, 2, 0, 7, 6, 5])
    controlS.greedySearchS()

    controlA = StateManager([1, 3, 4, 8, 2, 0, 7, 6, 5])
    controlA.greedySearchA()

    print("\n------Finishing q8------")