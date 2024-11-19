"""
(Exerc. 01) Implementar um algoritmo de busca em largura e usar a implementação desenvolvida para resolver o 
problema dos Missionários e Canibais (descrito na aula). Apresentar:  
a) print (em pdf) do passo a passo de execução do algoritmo e da solução do problema (plano para levar todos para o 
outro lado do rio) para 3 Missionários e 3 Canibais (veja exemplo deste print apresentado em aula) e  
b) código fonte da implementação: legível, identado, variáveis nomeadas de forma compreensível, comentado - padrão 
JavaDoc ou Doxigen, parametrizado para: N missionários, N canibais, N operadores válidos, e orientado a objetos.

Estado <M, C, PosiçãoDoBarco> 
M: número de missionários na margem esquerda do rio 
C: número de canibais na margem esquerda do rio 
PosiçãoDoBarco: posição do barco (MargemEsq, MargemDir) 
1 barco pode carregar 2 
Missionários nunca devem estar em menor número que canibais 
Obs.: Somente embarcam e desembarcam do barco os missionários e os 
canibais que desejarem fazer isso 
"""

class StateManager:
    M = None
    C = None
    Pos = None
    queueStates = []
    visitedStates = []
    opposite = {'L':'R', 'R':'L'}
    counter = 0

    def __init__(self, nM, nC, initPos):
        self.M = nM
        self.C = nC
        self.Pos = initPos

    def breadthFirstSearch(self):
        """Finds a solution to the Missionary problem using the Breadth First Search"""
        state = (self.M, self.C, self.Pos)
        self.queueStates.append(state)

        while self.queueStates:
            print("\nM | C | Pos | State number ", self.counter)
            print(str(self.M) + ' | ' + str(self.C) + ' | ' + self.Pos)
            self.counter += 1
        
            if self.isStateFinal(state):
                print("Solution found!")
                return True
            
            self.visitedStates.append(state)
            self.generatePossibleTransitions(state)
            self.queueStates.pop(0)

            state = self.queueStates[0]
            self.M = state[0]
            self.C = state[1]
            self.Pos = state[2]
        
    def generatePossibleTransitions(self, state):
        """Generate the possible transitions"""
        m = state[0]
        c = state[1]
        pos = state[2]
        candidates = []

        if pos == 'L':
            candidates.append((m - 1, c, self.opposite[pos]))# moving 1 missionary to the other side
            candidates.append((m - 2, c, self.opposite[pos]))# moving 2 missionaries to the other side
            candidates.append((m, c - 1, self.opposite[pos]))# moving 1 canibal to the other side
            candidates.append((m, c - 2, self.opposite[pos]))# moving 2 canibals to the other side
            candidates.append((m - 1, c - 1, self.opposite[pos]))# moving 1 missionary and 1 canibal to the other side
        elif pos == 'R':
            candidates.append((m + 1, c, self.opposite[pos]))# moving 1 missionary to the other side
            candidates.append((m + 2, c, self.opposite[pos]))# moving 2 missionaries to the other side
            candidates.append((m, c + 1, self.opposite[pos]))# moving 1 canibal to the other side
            candidates.append((m, c + 2, self.opposite[pos]))# moving 2 canibals to the other side
            candidates.append((m + 1, c + 1, self.opposite[pos]))# moving 1 missionary and 1 canibal to the other side

        for i in range(len(candidates)):
            if self.isStatePossible(candidates[i]):
                print("candidate ", candidates[i], "from", state)
                self.queueStates.append(candidates[i])
    
    def isStatePossible(self, state):
        """Checks if the state is valid"""
        m = state[0]
        c = state[1]
        pos = state[2]

        if state in self.visitedStates:
            return False

        if m > 3 or m < 0:
            return False
        elif c > 3 or c < 0:
            return False
        
        if pos == 'R':
            if c > m:
                return False
        elif pos == 'L':
            if c < m:
                return False
        return True

    def isStateFinal(self, state):
        return state[0] == 0 and state[1] == 0 and state[2] == 'R'

if __name__ == '__main__':
    control = StateManager(3, 3, 'L')
    print("\n------Starting q1------")
    control.breadthFirstSearch()
    print("\n------Finishing q1------")