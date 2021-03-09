print(75*'-')

print('''
           ************ VAMOS AS COMPRAS! ************
Por favor, Insira o nome de 3 mercadorias e os seus respectivos preços!
''')

print(75*'-')

mercadoria1 = input("1ª mercadoria: ")
preco1 = float(input("Preço: "))
print(75*'-')
mercadoria2 = input("\n2ª mercadoria: ")
preco2 = float(input("preço: "))
print(75*'-')
mercadoria3 = input("\n3ª mercadoria: ")
preco3 = float(input("preço: "))
print(75*'-')

if (preco1 < preco2 and preco1 < preco3):
    print("A mercadoria " + mercadoria1 + " é a mais barata entre as três!")
if(preco2 < preco1 and preco2 < preco3):
    print("A mercadoria " + mercadoria2 + " é a mais barata entre as três!")
if (preco3 < preco1 and preco3 < preco2):
    print("A mercadoria " + mercadoria3 + " é a mais barata entre as três!")

print(75*'-')

