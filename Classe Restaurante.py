class Restaurante:
    def __init__(self, cardapio, dia_semana):
        self.cardapio = cardapio
        self.dia_semana = dia_semana


class Mc(Restaurante):
    def __init__(self, nome, pagamento, cardapio, dia_semana):
        super().__init__(self.cardapio, self.dia_semana)
        self.nome = nome
        self.pagamento = pagamento
        
        
class Bk(Restaurante):
    def __init__(self, nome, pagamento, cardapio, dia_semana):
        super().__init__(self.cardapio, self.dia_semana)
        self.nome = nome
        self.pagamento = pagamento


class Habibs(Restaurante):
    def __init__(self, nome, pagamento, cardapio, dia_semana):
        super().__init__(self.cardapio, self.dia_semana)
        self.nome = nome
        self.pagamento = pagamento
    

