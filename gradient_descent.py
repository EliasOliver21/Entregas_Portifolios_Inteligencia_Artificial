
#Frunção gradiente com os seguintes parâmetros: A derivada da função expecífica (x - 3)^2 + 4, o ponto de início de x, a taxa de aprendizado(saltos para avançar e se aproximar do ponto mínimo) e a quantidade de iterações 
def gradient_descent(derivative_func, start, learning_rate, n_iterations):
    x = start  # Ponto inicial
    for i in range(n_iterations):
        grad = derivative_func(x)  # Calcula o gradiente (derivada)
        x = x - learning_rate * grad  # Atualiza x na direção oposta ao gradiente
        print(f"Iteração {i + 1}: x = {x:.4f}, f(x) = {(x - 3)**2 + 4:.4f}")
    return x

# Derivada da função f(x) = (x - 3)^2 + 4 → f'(x) = 2*(x - 3)
def derivative(x):
    return 2 * (x - 3)

# Executar
min_x = gradient_descent(derivative, start=0.0, learning_rate=0.1, n_iterations=50)
print(f"\nValor mínimo aproximado: x = {min_x:.4f}")
