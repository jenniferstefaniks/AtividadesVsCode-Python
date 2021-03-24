def cria_pilha():
    pilha = []
    return pilha

def tamanho(pilha):
    tam = len(pilha)
    return tam

def adiciona(pilha, elemento):
    pilha.append(elemento)
    return pilha

def remove(pilha):
    if pilha == []:
        return None
    else:
        rmv = pilha.pop(0)
        return rmv
    
def insere_par_remove_impar(lista):
    pilha = cria_pilha()
    for i in lista:
        if i % 2 == 0:
            adiciona(pilha, i)
        else:
            remove(pilha)

    print(pilha)
            
lista = [1, 2, 3]
insere_par_remove_impar(lista)
            