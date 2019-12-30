from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='useless_guy',
    passwd='killmeplzA1#@'
)

cursor = conexao.cursor()
# CREATE DATABASE IF NOT EXISTS agenda -> Alternativa
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')
