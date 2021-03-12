def positive_sum(arr):
    soma = 0
    
    for i in arr:
      if i > 0:
        soma = soma + i
        
    return print(soma)

lista = (1,-2,3,4,5)
positive_sum(lista)