#Criando dicionário

Igredientes_bolo_cenoura = ['1/2 xícara de óleo', 
                            '3 cenouras', 
                            '4 ovos', 
                            '2 xícara de açucar', 
                            '2 xícara de Farinha', 
                            '1 colher de fermento']
ch_ig_bolo = [1, 2, 3, 4, 5, 6]

Igredientes_cobertura_chocolate = ['1 colher de manteiga', 
                                   '3 colheres de chocolate em pó', 
                                   '1 xícara de açucar', 
                                   '1 xícara de leite']

ch_ig_cobertura = [1, 2, 3, 4]

bolo = dict(zip(ch_ig_bolo, Igredientes_bolo_cenoura))
cobertura = dict(zip(ch_ig_cobertura, Igredientes_cobertura_chocolate))

print(120*'*')
print(bolo)
print(cobertura)
print('\n')
print('o total de igredientes para fazer o bolo de cenoura é: ', 
len(Igredientes_bolo_cenoura))
print('o total de igredientes para fazer a cobertura do bolo de cenoura é: ', 
len(Igredientes_cobertura_chocolate))

