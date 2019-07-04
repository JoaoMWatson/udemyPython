# Leitura com o bloco with

with open('manipulacao_arquivos\pessoas.csv') as arquivo:

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo foi fechado')
