from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append("(Concluida)")
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append(('Vencida'))
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao}' + ' '.join(status)


def main():
    casa = Projeto("Tarefas de casa")
    casa.add("Passar roupa")
    casa.add("lavar prato")
    print(casa)

    casa.procurar('lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(f'\n{casa}')

    mercado = Projeto("\nComprar do mercado")
    mercado.add("frutas secas")
    mercado.add("Tomates", datetime.now() + timedelta(days=3, minutes=1))
    mercado.add("Carne")
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')


if __name__ == "__main__":
    main()
