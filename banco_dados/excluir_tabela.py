# droyp table emails
from mysql.connector import ProgrammingError
from db import nova_conexao

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute("DROP TABLE emails")
    except ProgrammingError as e:
        print(f'Error ao dropar: {e.msg}')
