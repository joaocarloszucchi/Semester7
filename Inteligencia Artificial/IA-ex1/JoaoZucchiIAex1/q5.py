"""
(Exerc. 5) Considere o mapa de vôos da Figura 1, representado pelos operadores a seguir: 
voo(a, b, 1), voo(a, c, 9), voo(a, d, 4), voo(b, c, 7), voo(b, e, 6), voo(b, f, 1), voo(c, f, 7), voo(d, f, 4), 
voo(d, g, 5), voo(e, h, 9), voo(f, h, 4), voo(g, h, 1) 
Sejam A o conjunto de ações acima: 
(a) Apresentar o b) passo a passo o estado das listas de novos abertos e nodos fechados e c) desenhe a árvore de busca 
produzida pelo algoritmo de busca gulosa pela melhor escolha para s0 = a e G = [h]. Neste exercício, o algoritmo deve 
usar os valores de custos g(n) (ver Figura 1) apresentados na descrição do problema. 
(b) Mostrar que, usando os operadores na ordem declarada acima, os algoritmos de busca em largura e em 
profundidade podem encontrar soluções de custo superior àquele encontrada pelo algoritmo de busca gulosa pela 
melhor escolha, quando s0 = a e G = [h]. 
c) Implementar algoritmos para solucionar as questões propostas. Entregar (i) print (em pdf) do passo a passo de 
execução dos algoritmos e das soluções do problema e (ii) código fonte das implementações: legível, identado, variáveis 
nomeadas de forma compreensível, comentado - padrão JavaDoc ou Doxigen, e orientado a objetos. 
"""

class State:
    def __init__(self, source, destiny, cost):
        self.source = source
        self.destiny = destiny
        self.cost = cost

    def getOpposite(self):
        return State(self.destiny, self.source, self.cost)

class StateManager:
    states = []

    def __init__(self, initial, final):
        self.queueCities = [] 
        self.closedCities = []

        self.addStates()
        self.current = initial
        self.goal = final
        self.cost = 0
        self.counter = 0

    def addStates(self):
        self.states.append(State('A', 'B', 1))
        self.states.append(State('A', 'C', 9))
        self.states.append(State('A', 'D', 4))
        self.states.append(State('B', 'C', 7))
        self.states.append(State('B', 'E', 6))
        self.states.append(State('B', 'F', 1))
        self.states.append(State('C', 'F', 7))
        self.states.append(State('D', 'F', 4))
        self.states.append(State('D', 'G', 5))
        self.states.append(State('G', 'H', 9))
        self.states.append(State('F', 'H', 4))
        self.states.append(State('G', 'H', 1))

        length = len(self.states)
        for i in range(length):
            self.states.append(self.states[i].getOpposite())

    def greedySearch(self):
        print("\nStarting Greedy Search\n")

        self.queueCities.append(self.current)
        self.closedCities.append(self.current)

        while self.queueCities:
            print("\nClosed states: ", self.closedCities)
            print("Queue order: ", self.queueCities)
            print("Current city | State number ", self.counter)
            print(str(self.current) + '            | ')
            self.counter += 1

            if self.isStateFinal():
                print("Solution found!")
                return True
            
            self.generateDestiniesG()
            self.current = self.queueCities[0][0]
            self.cost = self.queueCities[0][1]

        print("\nFinishing Greedy Search\n")

    def generateDestiniesG(self):
        """Generate the possible destinies from self.current using the Greedy Search Algorithm"""
        for i in range(len(self.states)):
            if self.states[i].source == self.current and self.states[i].destiny not in self.closedCities:
                self.queueCities.append((self.states[i].destiny, self.evalCost(self.states[i])))
                self.closedCities.append(self.states[i].destiny)
                print("candidate ", self.states[i].destiny, ' from ', self.current)
        self.queueCities.pop(0)
        self.sortByCost()

    def sortByCost(self):
        """sorts the self.queueStates for lowest cost"""
        self.queueCities = sorted(self.queueCities, key = lambda city: city[1])

    def evalCost(self, state):
        """Evalues the cost of the state by the following formula: (Total current cost) + (Transition cost)"""
        return self.cost + state.cost

    def isStateFinal(self):
        return self.current == self.goal

if __name__ == '__main__':
    print("\n------Starting q5------")

    controlB = StateManager('A', 'H')
    controlB.greedySearch()

    print("\n------Finishing q5------")