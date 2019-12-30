from mysql.connector import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
args = (
    ('Trabalho', ),
    ('Casa', )
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