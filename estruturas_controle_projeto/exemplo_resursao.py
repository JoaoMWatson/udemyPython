# Existe limite para a recursividade!!
def imprimir(maximo, atual):
    if atual >= maximo: # Condição de parada
        return
    print(atual)
    imprimir(maximo, atual + 1)
    # Outra maneira de se fazer

    # if atual < maximo:
    #     print(atual)
    #     imprimir(maximo, atual + 1)

imprimir(10, 1)
