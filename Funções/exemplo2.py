# Definição da função para calcular o Índice de Massa Corporal (IMC)
def calcular_imc(peso, altura):
    # Calcula o IMC usando a fórmula peso dividido pela altura ao quadrado
    imc = peso / (altura ** 2)
    # Retorna o valor do IMC calculado
    return imc
# Peso do usuário em quilogramas
peso_usuario = 70  
# Altura do usuário em metros
altura_usuario = 1.75  
# Chamada da função calcular_imc com os valores de peso e altura do usuário
imc_usuario = calcular_imc(peso_usuario, altura_usuario)

# Exibe o IMC do usuário formatado com duas casas decimais
print(f"Seu IMC é: {imc_usuario:.2f}")