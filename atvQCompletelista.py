seq = [1,5,6,8,22]

def ordenacao(seq): 
    seq.sort()

    return print(seq)


def NumerosRepetidos(seq):
    lista = []
    for i in seq:
        if i not in lista:
            lista.append(i)
        else:
            lista = []
    return print(lista)

def InserindoZero(seq):
    lista = seq
    for i in lista:
        if lista.count(i) > 1:
            lista = [0]
    return print(lista)

def completandoLista(seq):
    lista = seq
    for i in range(0,max(seq)+1):
        lista.append(i)
    return print(lista)

#Inserindo 0, ordenando, e completando a lista
def complete_series(seq): 
    seq.sort()
    lista = seq
    for i in lista:
        if lista.count(i) > 1:
            lista = [0]
    if lista != [0]:
        lista = []
        for i in range(0,max(seq)+1):
            lista.append(i)
    return print(lista)

complete_series(seq)
#ordenacao(seq)
#NumerosRepetidos(seq)
#InserindoZero(seq)
#completandoLista(seq)