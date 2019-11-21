from .pessoa import Pessoa
import datetime

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
    
    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        self.compras[-1]
