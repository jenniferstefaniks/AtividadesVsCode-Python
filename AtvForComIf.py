print("Verificando se é PAR ou ÍMPAR!")

final = int(input("Verificar de 1 até: "))

for cont in range(1, final+1):
    if cont % 2 == 0:
        print(cont, "é Par!")
    else:
        print(cont, "é Ímpar")
print("Fim!")