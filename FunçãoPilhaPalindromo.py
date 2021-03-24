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
        rmv = pilha.pop()
        return rmv
  
def Palindromo(texto):
    pilha = cria_pilha()
    if texto == "":
        return print(True)
    else:
        lista = list(texto)
        for i in range(tamanho(lista)):
            a = remove(lista)
            adiciona(pilha, a)
    
    string = "".join(pilha)
    if texto == string:
        print(string)
        return print(True)
    else:
        print(string)
        return print(False)
    

Palindromo("a")