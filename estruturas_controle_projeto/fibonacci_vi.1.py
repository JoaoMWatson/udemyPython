def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end='')
    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    limite = int(input('de um limite: '))
    fibonacci(limite)