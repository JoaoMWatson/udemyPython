class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self # Retorna o proprio objeto

if __name__ == "__main__":
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()
    
    # Metodos sem return retornam None

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')
