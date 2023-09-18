# Solicita ao usuário para inserir um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Inicializa a variável para armazenar a soma dos dígitos
    soma = 0

    # Converte o número em uma string para iterar através dos dígitos
    numero_str = str(numero)

    # Itera através dos dígitos e calcula a soma
    for digito in numero_str:
        soma += int(digito)

    # Exibe a soma dos dígitos
    print(f"A soma dos dígitos de {numero} é {soma}.")
