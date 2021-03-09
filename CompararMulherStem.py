
titulo = "DIFERENÇA ENTRE VOCÊ E VERA COOPER RUBIN"
print(100*"-")
print(titulo.center(100, "*"))
print(100*"-")

#--------------------------------------------------------

def idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

ano_atuals = 2021

#--------------------------------------------------------
print("\nME CONTE UM POUCO SOBRE VERA COOPER...\n")
ano_nascimento_vera = int(input("Qual ano que Vera Cooper Rubin nasceu: "))
estado = input("Qual Estado ela reside: ")
pais = input("Qual Pais ela mora: ")


print("\n AGORA ME CONTE MAIS SOBRE VOCÊ...\n")
ano_meu_nascimento = int(input("Qual ano você nasceu: "))
meu_estado = input("Qual estado você mora: ")
meu_pais = input("Qual pais Você reside: ")

#--------------------------------------------------------

if(meu_estado == 'Pensilvânia' and meu_pais == 'Estados Unidos'):
    print("Vocês residem no mesmo estado!")
else:
    mensagem = "Vocês moram em paises e estados diferentes!"

#--------------------------------------------------------
titulo = "COMPARAÇÕES SOBRE VOCÊS"
print(100*"-")
print(titulo.center(100, "*"))
print(100*"-")
print("")
print(mensagem)
print(f"\nidade de vera: {idade(ano_atuals, ano_nascimento_vera)}\n")
print(f"sua idade: {idade(ano_atuals, ano_meu_nascimento)}\n")
print("Vocês duas tem", idade(ano_atuals, ano_nascimento_vera) - idade(ano_atuals, ano_meu_nascimento), "anos de diferença!\n")
print(100*"-")
#--------------------------------------------------------