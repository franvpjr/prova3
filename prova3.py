produtos = {}

for i in range(5):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))

    produtos[nome] = preco

valortotal = sum((produtos.values()))

print(f'A sua compra foi {dict(produtos)}, com o valor total de  {valortotal}')