queue = []
#Coisas que eu gosto 
queue.append('Bolo de cenoura com chocolate')
queue.append('Chocolate ao leite ')
queue.append('Chocolate meio amargo')
queue.append('Café')
queue.append('Capuccino')
queue.append('Milkshake')


print('\n #Estarei comendo cada coisa desta fila ...')
print(queue)
print('\n Comendo...', queue[0])
queue.pop(0)

print('\n Comendo...', queue[0])
print(queue)
queue.pop(0)

print('\n Comendo...', queue[0])
print(queue)
queue.pop(0)

print('\n tomando...', queue[0])
print(queue)
queue.pop(0)

print('\n tomando...', queue[0])
print(queue)
queue.pop(0)


print('\nSobrou somente este para comer mais tarde... Pq não aguentei :(')
print(queue)