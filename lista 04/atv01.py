def ordenar_por_selecao(vetor):
    tamanho = len(vetor)

    for i in range(tamanho):
        # Encontra o índice do elemento mínimo no restante do vetor
        indice_minimo = i
        for j in range(i + 1, tamanho):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        
        # Troca o elemento mínimo com o elemento atual
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]
ordenar_por_selecao(vetor)
print("Vetor ordenado:", vetor)
