from mysql.connector import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Luka', '4678-4412'),
    ('xDxD', '1010-3231'),
    ('Soph', '7764-1113'),
    ('May', '1121-5643'),
    ('Breo', '2341-4083'),
    ('Jeej', '1111-2222'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'{cursor.rowcount} registros incluidos')
