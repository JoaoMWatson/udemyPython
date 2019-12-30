from db import nova_conexao
from mysql.connector import ProgrammingError

sql = "UPDATE contatos SET nome = %s WHERE id= %s"
args = ()

with nova_conexao() as conexao:
    try:
        codigo = input("Id Contato: ")
        nome = input("Nome para atualização: ")
        args = (nome, codigo)

        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) alterados')