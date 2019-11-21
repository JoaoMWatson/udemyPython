maiorDeIdade = 18

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = self.nome
        self.idade = int(idade)

    def __str__(self):
        return f'Nome: {self.nome}, idade: {self.idade} anos'
        

    def isAdult(self):
        return self.idade >= maiorDeIdade
