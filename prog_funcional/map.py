lista_1 = [1, 2, 3]

dobro = map(lambda x: x * 2, lista_1)
print('Dobro: ', list(dobro))

lista_2 = [
    {'nome': 'João', 'idade':32},
    {'nome': 'Maria', 'idade':32},
    {'nome': 'Jose', 'idade':26},
]

so_nomes = map(lambda p: p['nome'], lista_2)
print('So nomes: ', list(so_nomes))

so_idade = map(lambda p: p['idade'], lista_2)
a = list(so_idade)
print('Idades: ', a)
print(f'Soma das idades: {sum(a)}')

desafio = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos', lista_2)
print(list(desafio))