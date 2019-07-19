def fibonacchi(sequencia=[0, 1]):
    # Uso de mutaveis como valor padrão = armadilha
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacchi()
    print(inicio, id(inicio))
    print(fibonacchi(inicio))
    restart = fibonacchi()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
