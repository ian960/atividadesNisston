def remover_duplicatas(vetor):
    # Cria um conjunto para armazenar elementos únicos
    elementos_unicos = set()
    
    # Cria um novo vetor para armazenar os elementos sem duplicatas
    vetor_sem_duplicatas = []
    
    for elemento in vetor:
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            vetor_sem_duplicatas.append(elemento)
    
    return vetor_sem_duplicatas

# Exemplo de uso:
vetor = [1, 2, 2, 3, 4, 4, 5, 5, 5]

resultado = remover_duplicatas(vetor)

print("Vetor sem duplicatas:", resultado)
