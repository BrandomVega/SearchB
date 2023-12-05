import random

def f(solution):
    # Función objetivo: Puedes definir tu propia función para evaluar la calidad de la solución
    return sum(solution)

def swap(solution, j, k):
    # Operador de intercambio
    solution[j], solution[k] = solution[k], solution[j]
    return solution

def reverse_edge(solution, m1, m2):
    # Operador de reversión de borde
    solution[m1:m2 + 1] = reversed(solution[m1:m2 + 1])
    return solution

def hill_climbing(X):
    # Algoritmo de Hill Climbing
    while True:
        X_original = X.copy()  # Copia de la solución actual
        
        # Generar vecindario y evaluar las soluciones
        for j in range(j1, j1 + N // 3):
            for k in range(N):
                X1 = swap(X.copy(), j, k)
                if f(X1) < f(X):
                    X = X1

                m1, m2 = min(j, k), max(j, k)
                X1_reverse_edge = reverse_edge(X.copy(), m1, m2)
                if f(X1_reverse_edge) < f(X):
                    X = X1_reverse_edge

        # Comprobar si se ha producido una mejora en la iteración
        if X == X_original:
            break

    return X

if __name__ == "__main__":
    N = 8  # Número de ciudades en el TSP
    j1 = random.randint(1, 2 * N // 3)  # Punto de inicio aleatorio

    # Solución inicial aleatoria
    initial_solution = list(range(1, N + 1))
    random.shuffle(initial_solution)

    # Ejecutar Hill Climbing
    final_solution = hill_climbing(initial_solution)

    print("Solución inicial:", initial_solution)
    print("Solución mejorada:", final_solution)
    print("Valor de la función objetivo:", f(final_solution))
