# Usa streaming de dados, le por demanda
arquivo = open('manipulacao_arquivo\pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

arquivo.close()
