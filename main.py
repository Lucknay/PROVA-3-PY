total = 0

lista_preco = []
for  i in range (5):
    produtocliente = input('Digite o produto ')
    precoCliente = float(input('Digite o preço '))

    produto1 = {
    "Nome": produtocliente,
    "Preço": precoCliente
    }   
    total += precoCliente 

    lista_preco.append(produto1)


for produto_da_vez in lista_preco:
    print(f"""
    Contato: {produto_da_vez['Nome']}
    Preço: {produto_da_vez['Preço']}

    """)

print(f"Preço total: {total}")
