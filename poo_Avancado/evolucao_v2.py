class Humano:
    # atributo de classe
    especie = 'Homo Erectus'

    def __init__(self, nome):
        self.nome = nome

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
        """ 
        "cls" == classe como paramentro e chama a partir dela ou seja:
            HomoSapiens.is_evoluido()
                return HomoSapiens.especie == cls.especies()[-1]
                (True)
        """


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == "__main__":
    jose = HomoSapiens('jose')
    grokn = Neanderthal('jorge')
    aaaaka = Humano('Aaaaka')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da classe): {", ".join(Humano.especies())}')
    print(f'Evolução (a partir da classe): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
    print(f'Humano é evoluido? {Humano.is_evoluido()}')
    print(f'Aaaaka é evoluido? {aaaaka.is_evoluido()}')
