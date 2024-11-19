"""
(Exerc. 9) Conside a seguinte árvore de busca. 
a) Apresentar os valores de min e max propagados na árvore de busca 
b) Adotando a poda alfa-beta, nos sentidos i) da esquerda para a direita e ii) da direita para a esquerda, indicar quais 
arestas/subárvores serão podadas. 
c) Implementar algoritmos para solucionar as questões propostas. Entregar (i) print (em pdf) do passo a passo de 
execução dos algoritmos e das soluções do problema e (ii) código fonte das implementações: legível, identado, variáveis 
nomeadas de forma compreensível, comentado - padrão JavaDoc ou Doxigen, e orientado a objetos.
"""

class Node():
    def __init__(self, operation, value = None):
        self.operation = operation
        self.value = value
        self.children = []

class StateManager():
    opposite = {'MAX':'MIN', 'MIN':'MAX'}
    root = None

    def __init__(self):
        self.genTree()

    def genTree(self):
        values = [20, 33, -45, 31, 24, 25, -10, 20, 40, -25, 18, -42, 24, -19, 36, -41]
        self.root = self.createNode('MAX', 0, values)

    def createNode(self, operation, depth, values):
        node = Node(operation)
        if depth == 4:
            node.value = values.pop(0)
        else:
            node.children.append(self.createNode(self.opposite[operation], depth + 1, values))
            node.children.append(self.createNode(self.opposite[operation], depth + 1, values))
        return node
        
    def evalFunctionValues(self, node):
        if node is None:
            return

        for child in node.children:
            self.evalFunctionValues(child)

        if node.children:
            if node.operation == 'MAX':
                node.value = max(child.value for child in node.children)
            elif node.operation == 'MIN':
                node.value = min(child.value for child in node.children)

    def alphaBetaPruningLR(self, node, alpha, beta, maximizingPlayer, level = 0):
        """Performs Alpha-Beta Pruning from left to right"""
        if len(node.children) == 0:
            print('  ' * level + str(node.value) + ' ' + node.operation )
            return node.value

        print('  ' * level + str(node.value) + ' ' + node.operation )
        if maximizingPlayer:
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

    def alphaBetaPruningRL(self, node, alpha, beta, maximizingPlayer, level = 0):
        """Performs Alpha-Beta Pruning from right to left"""
        if len(node.children) == 0:
            print('  ' * level + str(node.value) + ' ' + node.operation )
            return node.value

        print('  ' * level + str(node.value) + ' ' + node.operation )
        if maximizingPlayer:
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
        print('  ' * level + str(node.value) + ' ' + node.operation)
        for child in node.children:
            self.printTree(child, level+1)


if __name__ == '__main__':
    print("\n------Starting q9------")

    control = StateManager()
    control.evalFunctionValues(control.root)
    control.printTree()
    
    print("\n------Alpha Beta Pruning LR:------\n")
    control.alphaBetaPruningLR(control.root, float('-inf'), float('inf'), True)

    print("\n------Alpha Beta Pruning RL:------\n")
    control.alphaBetaPruningRL(control.root, float('-inf'), float('inf'), True)

    print("\n------Finishing q9------")