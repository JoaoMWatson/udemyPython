from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='useless_guy',
    passwd='killmeplzA1#@'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de dados {i}: {database[0]}')