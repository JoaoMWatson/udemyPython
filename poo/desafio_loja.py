from datetime import datetime
from Loja import Cliente, Vendedor, Compra


def main():
    juracy = Cliente('Juracy Filho', 44)
    leo = Vendedor('Leonardo Leitão', 36, 1000)
    compra1 = Compra(leo, datetime.now(), 512)
    compra2 = Compra(leo, datetime(2018, 6, 4), 256)
    juracy.registrar_compra(compra1)
    juracy.registrar_compra(compra2)

    print(f'Cliente: {juracy}', '(adulto)' if juracy.isAdult() else '')
    print(f'Vendedor: {leo}')
    print(f'Total: {juracy.total_compra()} em {len(juracy.compras)} compras')
    print(f'Ultima Compra: {juracy.get_data_ultima_compra()}')


if __name__ == "__main__":
    main()