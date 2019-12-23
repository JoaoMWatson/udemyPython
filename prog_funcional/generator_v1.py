def cores_arco_iris():
    yield 'vermelho'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'laranja'
    yield 'violeta'

if __name__ == "__main__":
    generator = cores_arco_iris()
    print(type(generator))
    
    while True:
        try:
            print(next(generator))
        except StopIteration:
            break
