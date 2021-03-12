def RetirandoRepetidos(seq):

    lista = []
    for i in seq:
        if i not in lista:
            lista.append(i) 

    return print(lista)

seq = [1, 2, 2, 3, 3, 4]
RetirandoRepetidos(seq)
