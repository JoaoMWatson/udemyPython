# Le o arquivo inteiro e aloca na memoria do pc
arquivo = open('manipulacao_arquivos\pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
