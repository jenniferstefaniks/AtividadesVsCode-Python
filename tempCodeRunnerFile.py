def fila_prioridade(lista):
    lista1 = []
    for i in lista:
        if i >= 65:
            lista.append(i)
        else:
            lista1.append(i)
    
    print(lista)
    print(lista1)


lista = [18, 23, 65, 89]
fila_prioridade(lista)