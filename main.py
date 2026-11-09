gastos = []


def adicionar_gastos(descriçao, valor, categoria):
    gasto = {
        "descriçao": descriçao,
        "valor": valor,
        "categoria": categoria
    }
    gastos.append(gasto)


adicionar_gastos("Aluguel", 1200, "Moradia")
adicionar_gastos("Supermercado", 300, "Alimentação")
print(gastos)
