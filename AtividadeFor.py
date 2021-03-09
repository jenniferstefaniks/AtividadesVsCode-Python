

valor = int(input("Qual tabuada você gostaria de ver? "))
cont = 1

for cont in range(1, 11):
    resultado = valor * cont
    print(valor, " X ", cont, " = ", resultado)
    cont = cont + 1 
print("Fim!")