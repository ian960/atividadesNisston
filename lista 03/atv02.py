def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

# Solicita ao usuário para inserir um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

resultado = calcular_fatorial(numero)

if isinstance(resultado, int):
    print(f"O fatorial de {numero} é {resultado}.")
else:
    print(resultado)
