def criar_pilha():
    fila = []
    return fila

def tamanho(fila):
    tam = print(len(fila))
    return tam

def adiciona(fila, elemento):
    fila.append(elemento)
    return fila

def remove(fila):
    if fila == []:
        return None
    else: 
        remv = fila.pop(0)
        return print(remv)

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

fila = []
#criar_pilha()
tamanho(fila)
adiciona(fila, 9)
remove(fila)

