opcaoInvalida = 0
valorIngresso = 0

nome = input("Qual é o seu nome?: ")
idade = int(input("Qual sua idade?: "))
estudante = input("Você é estudante de Python?: ")

if(idade < 18 ):
    print("Desculpe, mas somente maiores de 18 anos podem ter acesso ao Clube de festa...")
    print("Faltam ", 18 - idade, " ano(s), para que você consiga acesso.")
else:
    
    print(60 * "-")
 
    ingresso = input('''
    Olá " + nome + ", Você gostaria de adquirir qual Ingresso?:
    A) Entrada padrão = R$35,00
    B) Entrada VIP = R$60,00
    Escolha A ou B: ''')
    print(60 * "-")
    
    if(ingresso == 'A'):
        valorIngresso = 35.00
    elif(ingresso == 'B'): 
        valorIngresso = 60.00
    else:
        print("Opção inválida. Tente novamente!")
        opcaoInvalida = 1

    if(estudante == "Sim"):
        desconto = float(valorIngresso * 50.00 / 100.00)
        print("Você tem um desconto de 50 por cento no valor do ingresso por ser estudante de Python."
        print("Valor com desconto: ", desconto, " Reais")
    elif (opcaoInvalida == 0):
        print("Obrigada por adquirir nosso ingresso! Boa diversão!")
