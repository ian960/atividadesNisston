import string

def e_palindromo(frase):
    # Remove espaços e pontuação da frase e converte para letras minúsculas
    frase = frase.lower()
    frase = ''.join(frase.split())
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    
    # Verifica se a frase é igual à sua inversão
    return frase == frase[::-1]

# Solicita ao usuário para inserir uma palavra ou frase
entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if e_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo.")
else:
    print(f"'{entrada}' não é um palíndromo.")
