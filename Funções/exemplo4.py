'''

Lista de 5 itens de compra.
Se o valor for maior que 10, a gente divide ele entre eu e minha esposa.
Caso contrário, eu vou pagar.

'''

# Lista de 5 itens e seus valores
lista_5_itens_valores = [5, 12, 8, 15, 3]

# Inicializa as variáveis para armazenar os valores
valores_meus = 0
valores_esposa = 0

# Processa o primeiro item (índice 0)
if lista_5_itens_valores[0] > 10:
    valores_meus += lista_5_itens_valores[0] / 2
    valores_esposa += lista_5_itens_valores[0] / 2
else:
    valores_meus += lista_5_itens_valores[0]

# Processa o segundo item (índice 1)
if lista_5_itens_valores[1] > 10:
    valores_meus += lista_5_itens_valores[1] / 2
    valores_esposa += lista_5_itens_valores[1] / 2
else:
    valores_meus += lista_5_itens_valores[1]

# Processa o terceiro item (índice 2)
if lista_5_itens_valores[2] > 10:
    valores_meus += lista_5_itens_valores[2] / 2
    valores_esposa += lista_5_itens_valores[2] / 2
else:
    valores_meus += lista_5_itens_valores[2]

# Processa o quarto item (índice 3)
if lista_5_itens_valores[3] > 10:
    valores_meus += lista_5_itens_valores[3] / 2
    valores_esposa += lista_5_itens_valores[3] / 2
else:
    valores_meus += lista_5_itens_valores[3]

# Processa o quinto item (índice 4)
if lista_5_itens_valores[4] > 10:
    valores_meus += lista_5_itens_valores[4] / 2
    valores_esposa += lista_5_itens_valores[4] / 2
else:
    valores_meus += lista_5_itens_valores[4]

# Imprime os resultados
print('VALORES MEUS: ' + str(valores_meus) + '\nVALORES ESPOSA: ' + str(valores_esposa))