class Pessoas:
    def __init__(self, nome, cpf, rg, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rg = rg

    def Info(self):
        print(f'''
        Informações da pessoa:
        Nome:      {self.nome}
        cpf:       {str(self.cpf)}
        Rg:        {str(self.rg)}
        telefone:  {str(self.telefone)}
        ''')

class Pessoa_Entregadora(Pessoas):
    def __init__(self, nome, cpf, rg, telefone, emprego):
        super().__init__(nome, cpf, rg, telefone)
        self.emprego = emprego

    def falar(self):
        print(f'Olá, sou uma pessoa e sou {self.emprego}')

class Pessoa_cliente(Pessoas):
    def __init__(self, nome, cpf, rg, telefone, emprego):
       super().__init__(nome, cpf, rg, telefone)
       self.emprego = emprego

    def falar(self):
        print(f'Olá, sou uma pessoa e sou {self.emprego}')

class Pessoa_dona_Restaurante(Pessoas):
    def __init__(self, nome, cpf, rg, telefone, emprego):
       super().__init__(nome, cpf, rg, telefone)
       self.emprego = emprego

    def falar(self):
        print(f'Olá, sou uma pessoa e sou {self.emprego}')


entregador = Pessoa_Entregadora('Luiz', 451216695, 552418124, 1845454529, 'entregador')
entregador.Info()
entregador.falar()

cliente = Pessoa_cliente('jose', 4561215455, 85424521, 1842554236, 'Cliente')
cliente.Info()
cliente.falar()

dono_restaurante = Pessoa_dona_Restaurante('Bernadete', 7898456421, 5281425856, 1842542526, 'Dona do Restaurante')
dono_restaurante.Info()
dono_restaurante.falar()