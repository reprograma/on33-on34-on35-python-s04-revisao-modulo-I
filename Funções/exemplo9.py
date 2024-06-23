# Define a função para cadastrar produtos em uma lista (dicionário)
def cadastra_produto(lista_de_produtos):
    # Solicita ao usuário o nome do produto e armazena na variável nome_prod
    nome_prod = input("Digite o nome do produto: ")
    # Solicita ao usuário o valor do produto, converte para float e armazena na variável valor
    valor = float(input("Digite o valor do produto: "))
    # Adiciona o produto e seu valor ao dicionário lista_de_produtos
    lista_de_produtos[nome_prod] = valor

# Define a função para dividir os valores dos produtos pelo número de pessoas
def divisão_valores(lista_de_produto, num_pessoas):
    # Inicializa a variável valor_div para acumular a soma dos valores divididos
    valor_div = 0
    # Itera sobre cada item e valor no dicionário lista_de_produto
    for item, valor in lista_de_produto.items():
        # Divide o valor do item pelo número de pessoas e acumula em valor_div
        valor_div += valor / num_pessoas
    # Retorna o valor total dividido pelo número de pessoas
    return valor_div

# Cria um dicionário vazio para armazenar as compras conjuntas
compras_conjuntas = dict()

# Chama a função cadastra_produto duas vezes para adicionar dois produtos às compras conjuntas
cadastra_produto(compras_conjuntas)
cadastra_produto(compras_conjuntas)

# Exibe os produtos cadastrados nas compras conjuntas
print("Compras conjuntas:", compras_conjuntas)

# Chama a função divisão_valores para dividir o total das compras conjuntas por 5 pessoas
valor_por_pessoa = divisão_valores(compras_conjuntas, 2)

# Exibe o valor que cada pessoa deve pagar
print("Valor por pessoa nas compras conjuntas:", valor_por_pessoa)