import random
import string

# Frase alvo
TARGET = "HappyBirthday"

# Tamanho da população
POP_SIZE = 100

# Taxa de mutação
MUTATION_RATE = 0.01

# Gera string aleatória do mesmo tamanho da frase-alvo
def random_individual():
    return ''.join(random.choice(string.printable[:95]) for _ in range(len(TARGET)))

# Avalia a similaridade com a frase alvo (quanto mais próximo, melhor)
def fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET) if a == b)

# Seleção: torneio entre 2 indivíduos
def selection(population):
    a, b = random.sample(population, 2)
    return a if fitness(a) > fitness(b) else b

# Crossover: combina caracteres dos pais
def crossover(parent1, parent2):
    child = ''
    for i in range(len(TARGET)):
        child += parent1[i] if random.random() < 0.5 else parent2[i]
    return child

# Mutação: altera um caractere aleatoriamente
def mutate(individual):
    mutated = ''
    for c in individual:
        if random.random() < MUTATION_RATE:
            mutated += random.choice(string.printable[:95])
        else:
            mutated += c
    return mutated

# Função Principal
def genetic_algorithm():
    population = [random_individual() for _ in range(POP_SIZE)]
    generation = 0

    while True:
        # Ordena por fitness
        population.sort(key=fitness, reverse=True)
        best = population[0]
        print(f"Geração {generation}: {best} (fitness: {fitness(best)})")

        if best == TARGET:
            print("\nFrase alvo atingida!")
            break

        # Elitismo: mantém o melhor indivíduo
        new_population = [best]

        # Geração de novos indivíduos
        while len(new_population) < POP_SIZE:
            p1 = selection(population)
            p2 = selection(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population
        generation += 1

# Executar
genetic_algorithm()
