
valor = 9
cont = 1

def tabuada():
    resultado = valor * cont
    print(valor, " X ", cont, " = ", resultado)

while cont <= 10:
    tabuada()
    cont = cont + 1 
print("Fim!")
