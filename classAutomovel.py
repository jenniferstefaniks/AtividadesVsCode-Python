
class Automovel:
    def __init__(self, tipo, marca, modelo, ano, quilometragem_rodada, cor):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem_rodada = quilometragem_rodada 
        self.cor = cor
    
    def exibirInfo(self):
        print(f'''
        Tipo:    {self.tipo}
        Marca:   {self.marca}
        Modelo:  {self.modelo}
        Ano:     {self.ano}
        Km:      {self.quilometragem_rodada}
        Cor:     {self.cor}''')
        print('-'*40)

carro = Automovel('Carro', 'Fiat', 'Uno', '2000', 1000, 'Vermelho')
carro.exibirInfo()

moto = Automovel('Moto', 'Honda', 'Fan 160', '2022', 0, 'Preta')
moto.exibirInfo()

