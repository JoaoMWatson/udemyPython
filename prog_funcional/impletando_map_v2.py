#!/usr/bin/python3.6
# Implementacao simplificada do map


def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)

if __name__ == "__main__":
    resultado = mapear(lambda x: x** 2, [2, 3, 4])
    print(set(resultado))
