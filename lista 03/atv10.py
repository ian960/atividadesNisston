def gerar_sequencia_fibonacci(numero_de_termos):
    # Inicializa os primeiros dois termos da sequência
    termo1, termo2 = 0, 1

    # Verifica se o número de termos é menor ou igual a 0
    if numero_de_termos <= 0:
        return "O número de termos deve ser maior que zero."
    # Se o número de termos for 1, retorna apenas o primeiro termo
    elif numero_de_termos == 1:
        return [termo1]
    # Caso contrário, gera a sequência até o número de termos especificado
    else:
        sequencia = [termo1, termo2]
        for _ in range(2, numero_de_termos):
            proximo_termo = termo1 + termo2
            sequencia.append(proximo_termo)
            termo1, termo2 = termo2, proximo_termo
        return sequencia

# Solicita ao usuário para inserir o número de termos desejados
numero_de_termos = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))

# Gera a sequência de Fibonacci com base no número de termos inserido
resultado = gerar_sequencia_fibonacci(numero_de_termos)

# Exibe a sequência de Fibonacci
if isinstance(resultado, list):
    print(f"A sequência de Fibonacci com {numero_de_termos} termos é: {resultado}")
else:
    print(resultado)
