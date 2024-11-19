"""
(Exerc. 4) Considere os seguintes operadores que descrevem os vôos existentes entre cidades de um país: 
oper(1, a, b), oper(2, a, b), oper(3, a, d), oper(4, b, e), oper(5, b, f), oper(6, c, g), oper(7, c, h),  
oper(8, c, i), oper(9, d, j), oper(10, e, k), oper(11, e, l), oper(12, g, m), oper(13,  j, n), oper(14, j, o), 
oper(15, k, f), oper(16, l, h), oper(17, m, d), oper(18, o, a), oper(19, n, b) 
Por exemplo, o operador oper(1, a, b) indica que o vôo 1 parte da cidade A e chega na cidade B. Com base nesses 
operadores, e supondo que eles sejam usados na ordem em que eles foram declarados, apresentar: 
a) o passo a passo o estado das listas de novos abertos e nodos fechados usados pelo algoritmo de busca em largura e 
algoritmo de busca em profundidade que levem da cidade A até a cidade J 
b) desenhe a árvore de busca criada pelo algoritmo de busca em largura e algoritmo de busca em profundidade ao 
procurar uma sequência de vôos que levem da cidade A até a cidade J. 
c) Implementar algoritmos para solucionar as questões propostas. Entregar (i) print (em pdf) do passo a passo de 
execução dos algoritmos e das soluções do problema e (ii) código fonte das implementações: legível, identado, variáveis 
nomeadas de forma compreensível, comentado - padrão JavaDoc ou Doxigen, e orientado a objetos. 
"""

class State:
    def __init__(self, number, source, destiny):
        self.number = number
        self.source = source
        self.destiny = destiny

class StateManager:
    states = []

    def __init__(self, initial, final):
        self.queueCities = [] 
        self.closedCities = []

        self.addStates()
        self.current = initial
        self.goal = final
        self.counter = 0

    def addStates(self):
        self.states.append(State(1, 'A', 'B'))
        self.states.append(State(2, 'A', 'B'))
        self.states.append(State(3, 'A', 'D'))
        self.states.append(State(4, 'B', 'E'))
        self.states.append(State(5, 'B', 'F'))
        self.states.append(State(6, 'C', 'G'))
        self.states.append(State(7, 'C', 'H'))
        self.states.append(State(8, 'C', 'I'))
        self.states.append(State(9, 'D', 'J'))
        self.states.append(State(10, 'E', 'K'))
        self.states.append(State(11, 'E', 'L'))
        self.states.append(State(12, 'G', 'M'))
        self.states.append(State(13, 'J', 'N'))
        self.states.append(State(14, 'J', 'O'))
        self.states.append(State(15, 'K', 'F'))
        self.states.append(State(16, 'L', 'H'))
        self.states.append(State(17, 'M', 'D'))
        self.states.append(State(18, 'O', 'A'))
        self.states.append(State(19, 'N', 'B'))

    def breadthFirstSearch(self):#largura
        print("\nStarting Breadth First Search\n")
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
            
            self.generateDestiniesB()
            self.queueCities.pop(0)
            self.current = self.queueCities[0]

        print("\nFinishing Breadth First Search\n")

    def depthFirstSearch(self):#profundidade
        print("\nStarting Depth First Search\n")
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
            
            self.generateDestiniesD()
            self.queueCities.pop(0)
            self.current = self.queueCities[0]

        print("\nFinishing Depth First Search\n")

    def generateDestiniesB(self):
        """Generate the possible destinies from self.current using the Breadth First Search Algorithm"""
        for i in range(len(self.states)):
            if self.states[i].source == self.current and self.states[i].destiny not in self.closedCities:
                self.queueCities.append(self.states[i].destiny)
                self.closedCities.append(self.states[i].destiny)
                print("candidate ", self.states[i].destiny, ' from ', self.current)

    def generateDestiniesD(self):
        """Generate the possible destinies from self.current using the Depth First Search Algorithm"""
        j = 1
        for i in range(len(self.states)):
            if self.states[i].source == self.current and self.states[i].destiny not in self.closedCities:
                self.queueCities.insert(j, self.states[i].destiny)
                self.closedCities.append(self.states[i].destiny)
                j += 1
                print("candidate ", self.states[i].destiny, ' from ', self.current)

    def isStateFinal(self):
        return self.current == self.goal
    
if __name__ == '__main__':
    print("\n------Starting q4------")

    controlB = StateManager('A', 'J')
    controlB.breadthFirstSearch()

    controlD = StateManager('A', 'J')
    controlD.depthFirstSearch()

    print("\n------Finishing q4------")


    
    