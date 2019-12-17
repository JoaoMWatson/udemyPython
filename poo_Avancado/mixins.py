class HtmlToString:
    def __str__(self):
        # Conversão para HTML
        html = super().__str__().replace('(', '<strong>(').replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + '(pet)' if self.pet else ''


class PessoaHTML(HtmlToString, Pessoa):
    pass


class AnimalHTML(HtmlToString, Animal):
    pass


if __name__ == "__main__":
    p1 = Pessoa('Joao')
    print(p1)
    p2 = PessoaHTML('Maya')
    print(p2)

    toto = AnimalHTML("Toto")
    print(toto)
