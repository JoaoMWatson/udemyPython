from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='useless_guy',
    passwd='killmeplzA1#@'
)

print(conexao)
