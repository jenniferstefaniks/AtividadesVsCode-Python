
class Automovel:
    def __init__(self, tipo, marca, modelo, ano, quilometragem_rodada, cor):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem_rodada = quilometragem_rodada 
        self.cor = cor

    def informações(self):
        print(f'''
        Tipo:    {self.tipo} 
        Marca:   {self.marca}
        Modelo:  {self.modelo}
        Ano:     {str(self.ano)}
        Km:      {str(self.quilometragem_rodada)}
        Cor:     {self.cor}
        {print('-'*30)}
        ''')

class Carro(Automovel):
    def __init__(self):
        self.tipo = 'Carro'
        self.marca = 'Fiat'
        self.modelo = 'Uno'
        self.ano = 2000
        self.quilometragem_rodada = 8000
        self.cor = 'Azul'
        super().__init__(self.tipo, self.marca, self.modelo, self.ano, self.quilometragem_rodada, self.cor)


class Moto(Automovel):
    def __init__(self):
        self.tipo = 'Moto'
        self.marca = 'Honda'
        self.modelo = 'Fan 160'
        self.ano = 2021
        self.quilometragem_rodada = 0
        self.cor = 'Branca'
        super().__init__(self.tipo, self.marca, self.modelo, self.ano, self.quilometragem_rodada, self.cor)

veiculo1 = Carro()
veiculo1.informações()
veiculo2 = Moto()
veiculo2.informações()