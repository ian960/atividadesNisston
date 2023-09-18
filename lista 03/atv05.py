def e_primo(numero):
    # Verifica se o número é menor ou igual a 1
    if numero <= 1:
        return False
    # 2 é um número primo
    if numero == 2:
        return True
    # Verifica se o número é divisível por algum número de 2 até a raiz quadrada do número + 1
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicita ao usuário para inserir um número inteiro para verificar se é primo
numero = int(input("Digite um número inteiro para verificar se é primo: "))

if e_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
