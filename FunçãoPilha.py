def criar_pilha():
    pilha = []
    return pilha

def tamanho(pilha):
    tam = print(len(pilha) + 1)
    return tam

def adiciona(pilha, elemento):
    pilha.append(elemento)
    return pilha

def remove(pilha):
    if pilha == []:
        return None
    else: 
        remv = pilha.pop()
        return print(remv)

def insere_par_remove_impar(lista):
    
    for i in lista:
        if (i % 2) == 0:
            pilha.append(i)

    return print(pilha)

def palindromo(s):
    c = s
    inverse = s[::-1]
    if inverse == c:
        return print(True)
    else:
        return print(False)

s = 'aAbA'
palindromo(s)
            



pilha = []
lista = [1, 2, 3, 4, 6, 8]

#criar_pilha()
tamanho(pilha)
adiciona(pilha, 9)
remove(pilha)
insere_par_remove_impar(lista)

