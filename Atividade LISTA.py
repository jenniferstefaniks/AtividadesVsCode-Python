# Atividade LISTA

#Criação da lista
cantores = ["Gabriela", "Roberto Carlos", "Isadora Pompeu", "Fernandinho"]

print(cantores)
#Adicionar item a lista
cantores.append("Fernandinho")
print(cantores)

# REMOVE() - Remove também, porem precisa passar o item da lista 
cantores.remove("Gabriela")

# Retira um item da lista
# sem índice de posição remove o ultimo
cantores.pop(0)
print(cantores)



#Adicionar item e a localização
cantores.insert(0, "Cassiane")
print(cantores)

# mostra somente do 0 até o 3 da lista
print(cantores[0:3])

#Pula em 2 em 2
print(cantores[::2]) 


numeros = [1, 10, 9, 4, 2, 8, 5, 0]
# Ordena a lista em dornem crescente
numeros.sort()
print(numeros)
# Ordena a lista em ordem decrescente
numeros.reverse()
print(numeros)

print(cantores.count("Fernandinho"))

print(len(cantores))
print(len(numeros))

