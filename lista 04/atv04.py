def segundo_menor(vetor):
    if len(vetor) < 2:
        return "O vetor deve conter pelo menos dois números."

    menor = float('inf')  # Inicializa o menor com um valor infinito
    segundo_menor = float('inf')  # Inicializa o segundo menor com um valor infinito

    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    if segundo_menor == float('inf'):
        return "Não há segundo menor número no vetor."
    else:
        return segundo_menor

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]

resultado = segundo_menor(vetor)

print("Segundo menor número:", resultado)
