from mysql.connector import ProgrammingError
from db import nova_conexao

sql = 'SELECT * FROM contatos' # LIMIT %s OFFSET %s

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} Telefone: {contato[1]}')
