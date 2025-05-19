import math

# Grafo representado como um dicionário.
# Cada nó possui uma lista de tuplas (vizinho, custo)
graph = {
    'A': [('B', 1), ('C', 4), ('D', 5)],
    'B': [('E', 3), ('F', 5)],
    'C': [],
    'D': [('G', 2)],
    'E': [],
    'F': [],
    'G': []
}

# Heurística para cada nó (estimativa da distância até o objetivo 'G')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 5,
    'F': 3,
    'G': 0
}

def rbfs(node, goal, f_limit, g=0):
    print(f"Visitando {node} com f_limit = {f_limit}")

    # Verifica se chegamos no objetivo
    if node == goal:
        return [node], 0

    successors = []

    # Gera os sucessores do nó atual
    for child, cost in graph[node]:
        g_child = g + cost 
        f = g_child + heuristic[child]  # f(n) = g(n) + h(n)
        successors.append([child, g_child, f])

    if not successors:
        return None, math.inf

    # Ordena os sucessores com base no valor de f(n)
    successors.sort(key=lambda x: x[2])

    while True:
        best = successors[0]  # Escolhe o melhor nó (menor f)

        # Se o melhor f(n) for maior que o limite, volta para o pai com esse valor
        if best[2] > f_limit:
            return None, best[2]

        # Define o segundo melhor f(n), ou infinito se não houver
        alternative = successors[1][2] if len(successors) > 1 else math.inf

        # Chamada recursiva para o melhor sucessor, com novo f_limit
        result, new_f = rbfs(best[0], goal, min(f_limit, alternative), best[1])

        # Atualiza o valor f(n) com o valor retornado pela recursão
        best[2] = new_f
        successors[0] = best 

        successors.sort(key=lambda x: x[2])

        if result is not None:
            return [node] + result, new_f

# Executa o algoritmo partindo de 'A' até 'G' com f_limit inicial infinito
path, _ = rbfs('A', 'G', math.inf)

# Exibe o caminho encontrado
print("\nCaminho encontrado:", path)
