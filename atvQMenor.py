#Retorna o numero menor da lista

def encontre_n_menor(numbers):
    for i in numbers:
        if i == min(numbers):
            menor = i
    return menor


num = (34, 15, 88, 2, 1)

print(num)
print('o menor da lista é: ', encontre_n_menor(num))