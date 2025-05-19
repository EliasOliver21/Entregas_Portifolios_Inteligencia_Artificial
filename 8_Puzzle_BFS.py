from collections import deque
import copy

# Função para encontrar posição do zero
def initial_number(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Função para gerar estados vizinhos
def get_neighbors(state):
    x, y = initial_number(state)
    neighbors = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Direções possíveis: cima, baixo, esq, dir

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# Função para checar se é o estado desejado
def is_goal(state):
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    return state == goal

# Transformar lista em tupla imutável para usar como chave
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# BFS
def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(state_to_tuple(start))

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = state_to_tuple(neighbor)
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [current_state]))

    return None

# Estado inicial
start_state = [
    [8, 7, 6],
    [5, 4, 3],
    [2, 1, 0]
]

# Executar busca
solution = bfs(start_state)

# Exibir solução
if solution:
    print("Solução encontrada em", len(solution) - 1, "movimentos:")
    for step in solution:
        for row in step:
            print(row)
        print("------")
else:
    print("Nenhuma solução encontrada.")
