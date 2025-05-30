def is_consistent(assignment, tarefa, pessoa, tarefas_acopladas):
    """
    Realiza a verificaçáo se uma atribuição é consistentes com as outras ja existentes e com as restrições definidas
    """
    # Restrição 1: Exclusividade de Pessoa
    # Uma pessoa não pode ser atribuída a mais de uma tarefa.
    if pessoa in assignment.values():
        return False

    # Restrição 2: Habilidade (Beto não faz café)
    if tarefa == "Fazer Café" and pessoa == "Beto":
        return False

    # Restrição 3: Preferência/Custo (Ana não lava louça)
    if tarefa == "Lavar Louça" and pessoa == "Ana":
        return False

    # Restrição 4: Acoplamento (Lavar louça e limpar chão só por Ana ou Carlos)
    if tarefa in tarefas_acopladas and pessoa not in ["Ana", "Carlos"]:
        return False

    # Se nenhuma restrição foi violada, a atribuição é consistente
    return True

def solve_csp(tarefas, pessoas, tarefas_acopladas, assignment={}):
    """
    Função de solver recursivo que utiliza backtracking para encontrar uma solução.
    """
    
    # Caso Base: Se todas as tarefas foram atribuídas, encontra-se uma solução.
    if len(assignment) == len(tarefas):
        return assignment

    # Seleciona a próxima tarefa não atribuída
    # Pega a primeira tarefa da lista que ainda não está no dicionário 'assignment'
    tarefa_atual = [t for t in tarefas if t not in assignment][0]

    # Itera sobre o domínio de possíveis valores (pessoas) para a tarefa atual
    for pessoa in pessoas:
        # Verifica se a atribuição é consistente com as regras
        if is_consistent(assignment, tarefa_atual, pessoa, tarefas_acopladas):
            
            # 1. Tenta a atribuição
            assignment[tarefa_atual] = pessoa
            
            # 2. Chama a recursão para o próximo nível da árvore de busca
            result = solve_csp(tarefas, pessoas, tarefas_acopladas, assignment)
            
            # Se a chamada recursiva encontrou uma solução completa, propaga o resultado
            if result is not None:
                return result
            
            # 3. Backtrack: Se a chamada não levou a uma solução, desfaz a atribuição
            del assignment[tarefa_atual]
            
    return None


if __name__ == "__main__":
    # Variáveis do CSP (representadas pelas tarefas)
    tarefas = ["Fazer Café", "Lavar Louça", "Limpar Chão"]
    
    # Domínio do CSP (representado pelas pessoas)
    pessoas = ["Ana", "Beto", "Carlos"]
    
    # Parâmetro para a Restrição 4
    tarefas_acopladas = ["Lavar Louça", "Limpar Chão"]

    print("Iniciando a resolução do Problema de Alocação de Tarefas...")
    
    solucao = solve_csp(tarefas, pessoas, tarefas_acopladas)
    
    print("\n--- Resultado ---")
    if solucao:
        print("Solução encontrada!")
        for tarefa, pessoa in solucao.items():
            print(f"- {tarefa}: {pessoa}")
    else:
        print("Nenhuma solução encontrada que satisfaça todas as restrições.")