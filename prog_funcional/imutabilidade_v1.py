# from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Listar todos os meses do ano com 31 dias
# 1. (filter)pegar todos os indices de todos os meses com 31 dias
# 2. (map) transformar os indices em nome
# 3. (reduce) juntar tudo para imprimir

meses_31 = filter(lambda mes: mdays[mes] > 30, range(1, 13))
meses_nome = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                        meses_nome, 'Meses com 31 dias: ')
print(juntar_meses)

print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] > 30, 
                range(1, 13)
            )
        ),
        'Meses com 31 dias: '
    )
)