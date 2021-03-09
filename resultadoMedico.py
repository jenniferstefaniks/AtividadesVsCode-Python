
print(50*"-")
print(10*"*" + " RESULTADOS DE EXAME " + 10*"*")
print(50*"-")

def exame(resultado):
    
    if(resultado >= 7 ):
        return print("Parabéns, continue assim!")
    
    if(resultado >= 4 and resultado < 7):
        return print("Busque se cuidar mais e fazer um acompanhamento médico!")

    if(resultado < 4):
        return print("A coisa tá feia em.. Procure a Equipe médica urgente!")

        
    

paciente1 = int(input("Qual foi o resultado o exame médico: "))
exame(paciente1)
print(50*"-")

paciente2 = int(input("Qual foi o resultado o exame médico: "))
exame(paciente2)
print(50*"-")

paciente3 = int(input("Qual foi o resultado o exame médico: "))
exame(paciente3)
print(50*"-")