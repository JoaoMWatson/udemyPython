from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

# Organiza
print(sorted(valores))
print(valores)

# Mutabilidade
# valores.sort()
# print(valores)

# Menor valor
print(min(valores))

# Maior Valor
print(max(valores))

# Soma
print(sum(valores))

# Soma com reduce
print(reduce(add, valores))


# Reverte itens
print(reversed(valores))
print(list(reversed(valores)))

# Forma mutavel de reversão
valores.reverse()
print(valores)