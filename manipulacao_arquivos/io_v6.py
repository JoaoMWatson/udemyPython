with open('manipulacao_arquivos\pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('O arquivo foi fechado')

if saida.closed:
    print('O arquivo foi fechado')
