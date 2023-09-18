def ordenar_vetor(vetor, crescente=True):
    """
    Ordena um vetor de inteiros em ordem crescente ou decrescente.
    
    Args:
        vetor (list): O vetor de inteiros a ser ordenado.
        crescente (bool): True para ordenação crescente, False para ordenação decrescente.
    
    Returns:
        list: O vetor ordenado.
    """
    # Utiliza a função sorted para ordenar o vetor com base na chave reversa, se necessário
    if crescente:
        return sorted(vetor)
    else:
        return sorted(vetor, reverse=True)

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]

# Ordena em ordem crescente
vetor_crescente = ordenar_vetor(vetor, crescente=True)
print("Vetor ordenado em ordem crescente:", vetor_crescente)

# Ordena em ordem decrescente
vetor_decrescente = ordenar_vetor(vetor, crescente=False)
print("Vetor ordenado em ordem decrescente:", vetor_decrescente)
