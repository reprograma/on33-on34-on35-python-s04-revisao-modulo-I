'''

Lista de 5 itens de compra.
Se o valor for maior que 10, a gente divide ele entre eu e minha esposa.
Caso contrário, eu vou pagar.

CRIANDO COM ITERAÇÃO E FUNÇÕES

'''
def calcular_valores(lista_precos):
    #Calcula e imprime os valores a serem pagos por mim e minha esposa, dividindo os preços maiores que 10.
    # lista_precos: Uma lista de preços dos itens.
    valores_meus = 0
    valores_esposa = 0
    for preco in lista_precos:
        if preco > 10:
            valores_meus += preco / 2
            valores_esposa += preco / 2
        else:
            valores_meus += preco
    print(f"VALORES MEUS: {valores_meus}\nVALORES ESPOSA: {valores_esposa}")

# Lista de 5 itens e seus valores da FEIRA
feira = [5, 12, 8, 15, 3]
calcular_valores(feira)

# Lista de itens de vegetariana
compra_vegetariana = [23, 56, 12, 4, 6]
calcular_valores(compra_vegetariana)