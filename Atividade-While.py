# Tabuada

valor = int(input("Qual tabuada você gostaria de ver? "))
cont = 1

while cont <= 10:
    resultado = valor * cont
    print(valor, " X ", cont, " = ", resultado)
    cont = cont + 1 
print("Fim!")
