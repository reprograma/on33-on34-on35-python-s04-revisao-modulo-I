'''

Lista de 5 itens de compra.
Se o valor for maior que 10, a gente divide ele entre eu e minha esposa.
Caso contrário, eu vou pagar.

CRIANDO COM ITERAÇÃO

'''

valores_meus = 0
valores_esposa = 0

lista_5_itens_valores = [5, 12, 8, 15, 3]

# Calcula o valor da lista de compras
for preco in lista_5_itens_valores:
  if(preco) > 10:
    valores_meus += preco/2
    valores_esposa += preco/2
  else:
    valores_meus += preco

# cálculo de quem usou VR
# input de compras do mês
# ...
print('VALORES MEUS: '+str(valores_meus)+'\nVALORES ESPOSA: '+str(valores_esposa))