#Usando Try Finally

# Codigo arriscado!!!!!!!
try:
    arquivo = open('manipulacao_arquivos\pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

# Garantir que o arquivo sera fechado!!
# Sempre vai ser executado, com erro ou não.
finally:
    print('finally')
    arquivo.close()

# Checa se o arquivo foi fechado
if arquivo.closed:
    print('O arquivo foi fechado')