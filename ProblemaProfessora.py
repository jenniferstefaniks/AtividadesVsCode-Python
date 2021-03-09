'''  Uma professora deseja desenvolver um sistema para automatizar
seu trabalho. Ela precisa criar uma solução onde seus alunos
consigam inserir suas notas (seja a média geral de todas as
matérias ou a média de uma única disciplina), receber a média, e
saber sua situação (aprovação, reprovação ou recuperação) '''

def mediaGeral(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5 / 5

def mediaIndividual(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 / 3

print(80*'-')
titulo = "SISTEMA PARA CALCULO DE MÉDIA"
print(titulo.center(80, '*'))
print(80*'-')

resposta = int(input('''
Olá, o que gostaria de calcular no momento?:  
[1] MÉDIA GERAL
[2] MÉDIA INDIVIDUAL
Insira a opção que deseja (1 ou 2): '''))
print(80*'-')

if resposta == 1:
    print('''
Por favor insira as notas dos 5 alunos: 
''')
    nota1 = float(input('nota do 1º aluno: '))
    nota2 = float(input('nota do 2º aluno: '))
    nota3 = float(input('nota do 3º aluno: '))
    nota4 = float(input('nota do 4º aluno: '))
    nota5 = float(input('nota do 5º aluno: '))
    print(80*'-')

    mediaTurma = mediaGeral(nota1, nota2, nota3, nota4, nota5)   
    print(f'A média geral da classe é: {mediaTurma:.2f}')
    
    if mediaTurma >= 7:
        print(80*'-')
        mensagem = "TURMA APROVADA COM SUCESSO!"
        print(mensagem.center(80, " "))
        print(80*'-')
    elif mediaTurma >= 5 and mediaTurma < 7:
        print(80*'-')
        mensagem = "TURMA EM RECUPERAÇÃO!"
        print(mensagem.center(80, " "))
        print(80*'-')
    else:
        print(80*'-')
        mensagem = "TURMA REPROVADA!"
        print(mensagem.center(80, " "))
        print(80*'-') 
    #------------------------------------------------------------------
elif resposta == 2:
    print('''
 Por favor as 3 notas do aluno: 
 ''')
    nota_1 = float(input('1º nota: '))
    nota_2 = float(input('2º nota: '))
    nota_3 = float(input('3º nota: '))
    print(80*'-')

    resultado = float(mediaIndividual(nota_1, nota_2, nota_3))
    print(f'A média do aluno é: {resultado:.2f}')

    if resultado >= 7:
        print(80*'-')
        mensagem = "ALUNO(A) APROVADO(A) COM SUCESSO!"
        print(mensagem.center(80, " "))
        print(80*'-')
    elif resultado >= 5 and mediaTurma < 7:
        print(80*'-')
        mensagem = "ALUNO(A) EM RECUPERAÇÃO!"
        print(mensagem.center(80, " "))
        print(80*'-')
    else:
        print(80*'-')
        mensagem = "ALUNO(A) REPROVADO(A)!"
        print(mensagem.center(80, " "))
        print(80*'-')
else:
    print("Opção invalida! Insira somente 1 ou 2!")