
temperatura = float(input('Qual é a sua temperatura?: '))

if temperatura > 37:
    print('\033[31m'+'Sinto muito, você está com febre, melhor tomar um antitérmico.'+'\033[0;0m')
else:
    print('\033[32m'+'Você não está com febre, volte para casa!.'+'\033[0;0m')
