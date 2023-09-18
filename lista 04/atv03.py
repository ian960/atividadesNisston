def encontrar_maximo(vetor):
    if not vetor:
        return None  # Retorna None se o vetor estiver vazio

    maximo = vetor[0]  # Inicializa o máximo com o primeiro elemento

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento

    return maximo

def encontrar_minimo(vetor):
    if not vetor:
        return None  # Retorna None se o vetor estiver vazio

    minimo = vetor[0]  # Inicializa o mínimo com o primeiro elemento

    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento

    return minimo

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]

maximo = encontrar_maximo(vetor)
minimo = encontrar_minimo(vetor)

print("Elemento máximo:", maximo)
print("Elemento mínimo:", minimo)
