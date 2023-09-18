# Solicita ao usuário para inserir uma string
string = input("Digite uma string para contar as vogais: ")

# Converte a string para letras minúsculas para considerar todas as vogais
string = string.lower()

# Inicializa um contador para as vogais
contador_vogais = 0

# Define as vogais
vogais = "aeiou"

# Itera pela string e conta as vogais
for caractere in string:
    if caractere in vogais:
        contador_vogais += 1

# Exibe a quantidade de vogais na string
print(f"A quantidade de vogais na string é: {contador_vogais}")
