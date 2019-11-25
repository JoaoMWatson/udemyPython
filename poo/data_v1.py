# => Classe represente tipo de dado personalizado
class Data:  # => Camel case
    #   to_string(self)
    #   __str__ metodo interno para objeto => string
    def __str__(self):  # => Todo metodo dentro de uma classe começa com self
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()  # => Criação de objetos
# Python é uma ligunagem de tipo dinamico,
# ou seja, é possivel criar atributos de classe diretament no objeto
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 9
d2.ano = 2001
print(d1)
