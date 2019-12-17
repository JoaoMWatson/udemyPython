class Animal:
    @property
    def capacidade(self):
        return ('dormir', 'comer', 'beber')

class Homem(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('amar', 'falar', 'estudar')

class Aranha(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('fazer teia', 'andar pelas paredes')

class HomemAranha(Homem, Aranha):
    @property
    def capacidade(self):
        return super().capacidade + ('bater em bandidos', 'atirar teias entre predios')

if __name__ == "__main__":
    john = Homem()
    print(f'John: {john.capacidade}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidade}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidade}')
