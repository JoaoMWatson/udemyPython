from db import nova_conexao
from mysql.connector import ProgrammingError

table_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50), 
        tel VARCHAR(40)
        );
"""

table_emails = """
    CREATE TABLE emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(table_contatos)
            cursor.execute(table_emails)
        except ProgrammingError as e:
            print(f'Error {e.msg}')
except ProgrammingError as e:
        print(f'Error Conexao: {e.msg}')
