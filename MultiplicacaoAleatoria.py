
import random

titulo = "MULTIPLICAÇÃO DE NUMEROS ALEATÓRIOS"
print(100*"-")
print(titulo.center(100, "*"))
print(100*"-")

def aleatorio(num1, num2):
    return (num1 * num2)

multiplicando = int(input("""
Por favor, insira um numero entre 1 a 50 para multiplicarmos: """))

if(multiplicando >= 1 and multiplicando <= 50):
    multiplicador = int(input("""
Por favor, insira um numero entre 1 a 50 para ser o multiplicador: """))

    print(f"\n{multiplicando} x {multiplicador} = {aleatorio(multiplicando, multiplicador)}")
    print(100*"-")
else:
    print(100*"-")
    print("\nJá falei que tem que ser um numero entre 1 e 50!!!\n")
    print(100*"-")






''' OUTRA OPÇÃO 
multiplicando = random.randint(1, 50)
multiplicador = random.randint(1, 50)
print(f"{multiplicando} x {multiplicador} = {aleatorio(multiplicando, multiplicador)}")
'''
