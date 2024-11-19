"""
(Exerc. 7) Para o Problema das Rotas especificado no Exercício 6, apresentar: 
a) o passo a passo o estado das listas de novos abertos e nodos fechados usados pelo algoritmo A* para s0 = a e G = [k] 
b) desenhe a árvore de busca produzida quando o algoritmo A* é chamado com s0 = a e G = [k].  
Neste exercício, o algoritmo deve usar os valores de custo g(n) e heurísticos h(n) apresentados anteriormente. 
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
    heuristic = {
        'A': 15,
        'B': 7,
        'C': 6,
        'D': 14,
        'E': 15,
        'F': 7,
        'G': 8,
        'H': 5,
        'I': 5,
        'J': 3,
        'K': 0,
        'L': 4
        }

    def __init__(self, initial, final):
        self.queueCities = [] 
        self.closedCities = []

        self.addStates()
        self.current = initial
        self.goal = final
        self.cost = 0
        self.counter = 0

    def addStates(self):
        self.states.append(State('A','B',7))
        self.states.append(State('A','D',3))
        self.states.append(State('A','C',9))
        self.states.append(State('B','F',3))
        self.states.append(State('B','I',4))
        self.states.append(State('C','J',5))
        self.states.append(State('D','E',1))
        self.states.append(State('F','G',2))
        self.states.append(State('G','H',3))
        self.states.append(State('J','L',6))
        self.states.append(State('I','K',5))
        self.states.append(State('L','K',4))

        length = len(self.states)
        for i in range(length):
            self.states.append(self.states[i].getOpposite())

    def printStates(self):
        print("Printing States:")
        for state in self.states:
            print(f"Source: {state.source}, Destiny: {state.destiny}, Cost: {state.cost}")

    def greedySearch(self):
        print("Starting Greedy Search\n")

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
            self.cost = self.queueCities[0][1] - self.heuristic[self.current]

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
        """Evalues the cost of the state by the following formula: (Total current cost) + (Transition cost) + (Heuristic cost)"""
        return self.cost + state.cost + self.heuristic[state.destiny]

    def isStateFinal(self):
        return self.current == self.goal

if __name__ == '__main__':
    print("\n------Starting q7------")

    controlB = StateManager('A', 'K')
    controlB.greedySearch()

    print("\n------Finishing q7------")