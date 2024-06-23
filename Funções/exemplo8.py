'''

Lista de 5 itens de compra.
Se o valor for maior que 10, a gente divide ele entre eu e minha esposa.
Caso contrário, eu vou pagar.

CRIANDO COM ITERAÇÃO E FUNÇÕES E DICIONARIO

'''

def calcular_valores(lista_precos):
    # lista_precos: Uma lista de preços dos itens.
    # return: Um dicionário com os valores_meus e valores_esposa.

    valores_meus = 0
    valores_esposa = 0

    for preco in lista_precos:
        if preco > 10:
            valores_meus += preco / 2
            valores_esposa += preco / 2
        else:
            valores_meus += preco

    return {'meus': valores_meus, 'esposa': valores_esposa}

# Lista de 5 itens e seus valores
lista_5_itens_valores = [5, 12, 8, 15, 3]

# Chama a função e armazena o resultado
resultado = calcular_valores(lista_5_itens_valores)

# Imprime os resultados usando f-strings
print(f"VALORES MEUS: {resultado['meus']}\nVALORES ESPOSA: {resultado['esposa']}")