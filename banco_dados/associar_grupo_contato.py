from mysql.connector import ProgrammingError
from db import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    'Rogeria':'Casa',
    'Caa':'Trabalho',
    'Bia':'Casa',
    'Gui':'Trabalho',
    'Jaja':'Casa',
    'Luka':'Trabalho',
    'xDxD':'Casa',
    'Soph':'Trabalho',
    'May':'Casa',
    'Breo':'Trabalho',
    'Jeej':'Casa',
    'Lucas':'Trabalho'
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo, ))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print('Contatos associados')