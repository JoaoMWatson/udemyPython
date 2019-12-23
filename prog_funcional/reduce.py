from functools import reduce

pessoas = [
    {'nome': 'João', 'idade':11},
    {'nome': 'Maria', 'idade':18},
    {'nome': 'Arthur', 'idade':26},
    {'nome': 'Mariana', 'idade':6},
    {'nome': 'May', 'idade':19},
    {'nome': 'Gabriela', 'idade':17},
]

so_idade = map(lambda p: p['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idade)
soma_idade_menores = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idade_menores)
