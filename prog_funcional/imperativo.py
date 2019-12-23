from calendar import mdays, month_name

# Listar todos os meses do ano com 31 dias
print('Meses com 31 dias: ')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')
