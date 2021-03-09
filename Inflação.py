kg_tomate_1ano = float(input("Qual foi o preço do tomate a 1 ano atrás?: "))
kg_tomate_hj = float(input("Qual é o preço do tomate hoje?: "))

diferenca = kg_tomate_hj - kg_tomate_1ano
inflacao =  int((diferenca / kg_tomate_1ano) * 100)

print(f"O valor da inflação é de {inflacao}%")