def calcular_mediana(vetor):
    # Ordena o vetor em ordem crescente
    vetor_ordenado = sorted(vetor)
    
    # Calcula o índice do elemento do meio
    tamanho = len(vetor_ordenado)
    indice_do_meio = tamanho // 2
    
    # Verifica se o vetor tem um número ímpar de elementos
    if tamanho % 2 == 1:
        # Se for ímpar, retorna o elemento do meio
        mediana = vetor_ordenado[indice_do_meio]
    else:
        # Se for par, calcula a média dos dois elementos do meio
        elemento1 = vetor_ordenado[indice_do_meio - 1]
        elemento2 = vetor_ordenado[indice_do_meio]
        mediana = (elemento1 + elemento2) / 2
    
    return mediana

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]

resultado = calcular_mediana(vetor)

print("Mediana:", resultado)
