qtdAcerto = 0

print(65 * '-')
print('''
***** Questionário a Respeito da Astrônoma Vera Cooper Rubin *****
''')
print(65 * '-')

print('''
1º Pergunta: Qual era o apelido de vera rubin? 
  I) Rainha da Galaxia
 II) Senhora das estrelas
III) Queen Of Galaxy''')

prgt1 = input('''
Quais das alternativas está correta? (Escolha duas alternativas)
A) I e II
B) I e III
C) II e III
_''')

if(prgt1 == 'b'):
    print("Resposta Correta!")
    qtdAcerto+=1

print(65 * '-')

print('''
2º Pergunta: Escolha as duas verdades sobre Vera Rubin...
  I) Vera rubin nunca recebeu prêmio nobel.
 II) Somente 3 mulheres receberam o prêmio.
III) Vera foi a unica a receber o prêmio.''')

prgt2 = input('''
Quais das alternativas está correta? (Escolha duas alternativas)
A) I e II
B) I e III
C) II e III
_''')

if(prgt2 == 'a'):
    print("Resposta Correta!")
    qtdAcerto+=1

print(65 * '-')

print('''
3º Pergunta: Vera Robin fez... 
  I) Mestrado na Univesidade de Cornell.
 II) Pós em astronomia na universidade Galaxys.
III) Doutorado na Universidade de Georgetown.''')

prgt3 = input('''
Quais das alternativas está correta? (Escolha duas alternativas)
A) I e II
B) I e III
C) II e III

_''')

print(65 * '-')

if(prgt3 == 'b'):
    print("Resposta Correta!")
    qtdAcerto+=1

if(qtdAcerto == 3):
    print('''
    PARABÉNS, VOCÊ ACERTOU TODAS AS PERGUNTAS!
''')

if(qtdAcerto == 2):
    print('''
    PARABÉNS, VOCÊ ACERTOU A MAIORIA DAS PERGUNTAS!
    ''')

if(qtdAcerto == 1):
    print('''
    VOCÊ ACERTOU SOMENTE UMA DAS PERGUNTAS! 
    ''')

if(qtdAcerto == 0):
    print('''
    QUE PENA, VOCÊ ERROU TODAS AS QUESTÕES!
    ''')
print(65 * '-')