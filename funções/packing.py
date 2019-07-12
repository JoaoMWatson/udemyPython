def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


print(soma_2(2, 3))
print(soma_3(2, 3, 5))

# Packing
print(soma_n(1))
print(soma_n(1, 1, 2, 4, 5, 6, 7, 8, 1))

# UnPacking
tupla_nums = (1, 2, 3)
print(soma_n(*tupla_nums))
lista_nums = [1, 2, 3]
print(soma_n(*lista_nums))
