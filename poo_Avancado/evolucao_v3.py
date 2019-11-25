class Humano:
    # atributo de classe
    especie = 'Homo Erectus'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError("Idade deve ser positivo")
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self  # Retorna o proprio objeto

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == "__main__":
    jose = HomoSapiens('Jose')
    jose.set_idade(40)
    print(f'Nome {jose.nome} Idade: {jose.get_idade()}')

    # Não ira passar para o tratamento do get, possivel de passar valores negativos
    jose._idade = -40
    print(f'Nome {jose.nome} Idade: {jose.get_idade()}')

    grokn = Neanderthal('Grokn')
    grokn.set_idade(-40)
    print(f'Nome {grokn.nome} Idade: {grokn.get_idade()}')
