import json

gastos = []


def salvar_gastos():
    with open("gastos.json", "w") as f:
        json.dump(gastos, f)


def carregar_gastos():
    try:
        with open("gastos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


gastos = carregar_gastos()


def adicionar_gastos(descriçao, valor, categoria):
    gasto = {
        "descriçao": descriçao,
        "valor": valor,
        "categoria": categoria
    }
    gastos.append(gasto)


while True:
    print("""Escolha umas das opções abaixo:
    Opção 1- Adicionar Gastos
    Opção 2- Listar Gastos
    Opção 3- Sair
    Opção 4- Resumo por Categoria
    """)
    escolha = input("Escolha a Opção com o Numero: ")
    if escolha == "1":
        descriçao = input("Coloque a descrição do Gasto Aqui: ").lower()
        valor = float(input("Digite o Valor do Gasto Aqui: "))
        categoria = input("Coloque a categoria do Gasto Aqui: ").lower()
        adicionar_gastos(descriçao, valor, categoria)
        salvar_gastos()  

    if escolha == "2":
        if not gastos:
            print("Nenhum gasto registrado ainda.")
        else:

            for gasto in gastos:
                print(
                    f"Descrição: {gasto['descriçao']}, Valor: {gasto['valor']:.2f}, Categoria: {gasto['categoria']}")
    if escolha == "4":
        if not gastos:
            print("Nenhum gasto registrado ainda.")
        else:
            print("Resumo dos Gastos por Categoria:")
            resumo = {}
            for gasto in gastos:
                categoria = gasto["categoria"]
                valor = gasto["valor"]
                if categoria in resumo:
                    resumo[categoria] += valor
                else:
                    resumo[categoria] = valor
            for categoria, total in resumo.items():
                print(f"{categoria}: {total:.2f}")
        
    if escolha == "3":
        break




