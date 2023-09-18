def terceiro_maior(vetor):
    # Converte o vetor em um conjunto para remover duplicatas
    conjunto_sem_duplicatas = set(vetor)
    
    # Converte o conjunto de volta para uma lista e ordena em ordem decrescente
    lista_ordenada = sorted(list(conjunto_sem_duplicatas), reverse=True)
    
    # Verifica se há pelo menos três elementos na lista
    if len(lista_ordenada) >= 3:
        return lista_ordenada[2]  # O terceiro maior número está na posição 2
    else:
        return "Não há terceiro maior número no vetor."

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11, 25]

resultado = terceiro_maior(vetor)

print("Terceiro maior número:", resultado)
