def cria_fila():
    fila = []
    return fila

def tamanho(fila):
    tam = len(fila)
    return tam

def adiciona(fila, elemento):
    fila.append(elemento)
    return fila

def remove(fila):
    if fila == []:
        return None
    else:
        rmv = fila.pop(0)
        return rmv
  
def fila_prioritaria(lista):
    fila1 = cria_fila()
    fila2 = cria_fila()
    for i in range(tamanho(lista)): 
        if lista[0] >= 65:
            a = remove(lista)
            adiciona(fila1, a)
        elif lista[0] < 65:
            b = remove(lista)
            adiciona(fila2, b)
    
    fila = fila1 + fila2     
    return print(fila)


lista = [65, 30, 70, 18, 66]
fila_prioritaria(lista)
        