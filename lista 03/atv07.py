def calcular_imc(peso, altura):
    # Verifica se o peso e a altura são valores válidos
    if peso <= 0 or altura <= 0:
        return "Peso e altura devem ser valores positivos."
    
    # Calcula o IMC usando a fórmula: IMC = peso / (altura ** 2)
    imc = peso / (altura ** 2)
    
    return imc

# Solicita ao usuário para inserir o peso (em kg) e a altura (em metros)
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC chamando a função e exibe o resultado
imc = calcular_imc(peso, altura)

if isinstance(imc, float):
    print(f"Seu IMC é: {imc:.2f}")
else:
    print(imc)
