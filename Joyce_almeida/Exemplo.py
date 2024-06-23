# crie uma função onde o usuario coloque o peso e voce informa o IMC

def calcula_imc():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura ** 2)
    return (f"Seu IMC é: {imc:.2f}")

resultado = calcula_imc()
print(resultado)
