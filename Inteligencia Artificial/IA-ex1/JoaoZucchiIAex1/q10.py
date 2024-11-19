"""
(Exerc. 10) Consider o seguinte problema. 
7 
Dados 5 palitos cada jogador pode retirar 1, 2 ou 3 por turno. Perde o jogador que retira o último palito. A pergunta é: 
será que max pode ganhar o jogo? 
Usando a seguinte função de utilidade: F(S) = +1 se MAX ganhar, -1 se MIN ganhar, desenhar a árvore de busca.  
a) Apresentar os valores de min e max propagados na árvore de busca construída 
b) Adotando a poda alfa-beta, nos sentidos i) da esquerda para a direita e ii) da direita para a esquerda, indicar quais 
arestas/subárvores serão podadas. 
c) Implementar algoritmos para solucionar as questões propostas. Entregar (i) print (em pdf) do passo a passo de 
execução dos algoritmos e das soluções do problema e (ii) código fonte das implementações: legível, identado, variáveis 
nomeadas de forma compreensível, comentado - padrão JavaDoc ou Doxigen, e orientado a objetos.
"""

class Node():
    def __init__(self, operation, value, functionValue = 0):
        self.operation = operation
        self.value = value
        self.functionValue = functionValue
        self.children = []

class StateManager():
    opposite = {'MAX':'MIN', 'MIN':'MAX'}
    root = None

    def __init__(self, number):
        self.number = number
        self.genTree()

    def genTree(self):
        self.root = Node('MAX', self.number)
        self.genTreeRec(self.root)
        self.evalFunctionValues(self.root)

    def genTreeRec(self, father):
        children = self.genChildrenIndex(father.value)
        for i in range(len(children)):
            father.children.append(Node(self.opposite[father.operation], children[i], self.genFunctionValue(self.opposite[father.operation], children[i])))

            self.genTreeRec(father.children[-1])

    def genChildrenIndex(self, value):
        if value == 0:
            return []
        elif value == 1:
            return [0]
        elif value == 2:
            return [1, 0]
        else:
            return [value - 1, value - 2, value - 3]
        
    def genFunctionValue(self, operation, value):
        if value != 0:
            return 0
        if operation == 'MAX':
            return 1
        elif operation == 'MIN':
            return -1

    def evalFunctionValues(self, node=None):
        if node is None:
            node = self.root
        if node.value != 0:
            for child in node.children:
                self.evalFunctionValues(child)
            if node.operation == 'MAX':
                node.functionValue = max(child.functionValue for child in node.children)
            elif node.operation == 'MIN':
                node.functionValue = min(child.functionValue for child in node.children)

    def alphaBetaPruningLR(self, node, alpha, beta, isMaximizingPlayer, level = 0):
        """Performs Alpha-Beta Pruning from left to right"""
        if len(node.children) == 0:
            print('  ' * level + str(node.value) + ' ' + node.operation + ' ' + str(node.functionValue))
            return node.functionValue

        print('  ' * level + str(node.value) + ' ' + node.operation + ' ' + str(node.functionValue))
        if isMaximizingPlayer:
            maxEval = float('-inf')
            for child in node.children:
                eval = self.alphaBetaPruningLR(child, alpha, beta, False, level + 1)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    print('  ' * (level + 1) + '(PRUNING HERE)')
                    break
            return maxEval
        else:
            minEval = float('inf')
            for child in node.children:
                eval = self.alphaBetaPruningLR(child, alpha, beta, True, level + 1)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    print('  ' * (level + 1) + '(PRUNING HERE)')
                    break
            return minEval

    def alphaBetaPruningRL(self, node, alpha, beta, isMaximizingPlayer, level = 0):
        """Performs Alpha-Beta Pruning from left to right"""
        if len(node.children) == 0:
            print('  ' * level + str(node.value) + ' ' + node.operation + ' ' + str(node.functionValue))
            return node.functionValue

        print('  ' * level + str(node.value) + ' ' + node.operation + ' ' + str(node.functionValue))
        if isMaximizingPlayer:
            maxEval = float('-inf')
            for child in reversed(node.children):
                eval = self.alphaBetaPruningRL(child, alpha, beta, False, level + 1)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    print('  ' * (level + 1) + '(PRUNING HERE)')
                    break
            return maxEval
        else:
            minEval = float('inf')
            for child in reversed(node.children):
                eval = self.alphaBetaPruningRL(child, alpha, beta, True, level + 1)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    print('  ' * (level + 1) + '(PRUNING HERE)')
                    break
            return minEval

    def printTree(self, node=None, level=0):
        if node is None:
            node = self.root
        print('  ' * level + str(node.value) + ' ' + node.operation + ' ' + str(node.functionValue))
        for child in node.children:
            self.printTree(child, level+1)


if __name__ == '__main__':
    print("\n------Starting q10------")

    control = StateManager(5)
    control.printTree()

    print("\n------Alpha Beta Pruning LR:------\n")
    control.alphaBetaPruningLR(control.root, float('-inf'), float('inf'), True)

    print("\n------Alpha Beta Pruning RL:------\n")
    control.alphaBetaPruningRL(control.root, float('-inf'), float('inf'), True)

    print("\n------Finishing q10------")