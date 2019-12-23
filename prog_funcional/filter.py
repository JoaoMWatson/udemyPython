pessoas = [
    {'nome': 'João', 'idade':11},
    {'nome': 'Maria', 'idade':18},
    {'nome': 'Arthur', 'idade':26},
    {'nome': 'Mariana', 'idade':6},
    {'nome': 'May', 'idade':19},
    {'nome': 'Gabriela', 'idade':17},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nome_grandeV1 = filter(lambda p: p['nome'] if len(p['nome']) > 6 else None, pessoas)
nome_grandeV2 = filter(lambda p: len(p['nome'])  > 6, pessoas)
print('Versão 1: ', list(nome_grandeV1))
print('Versão 2: ', list(nome_grandeV2))
