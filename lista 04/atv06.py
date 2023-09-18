def ordenar_decrescente(vetor):
    return sorted(vetor, reverse=True)

def contar_pares_impares(vetor):
    pares = 0
    impares = 0
    
    for numero in vetor:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]

vetor_ordenado = ordenar_decrescente(vetor)
print("Vetor ordenado em ordem decrescente:", vetor_ordenado)

pares, impares = contar_pares_impares(vetor_ordenado)
print("Número de pares:", pares)
print("Número de ímpares:", impares)
