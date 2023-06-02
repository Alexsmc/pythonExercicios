import json

# Função para carregar os dados das contas do arquivo JSON
def carregar_dados():
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return {}

# Função para salvar os dados das contas no arquivo JSON
def salvar_dados(dados):
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo)

# Função para exibir o menu de contas e retornar a conta selecionada
def exibir_menu_contas(contas):
    print("Selecione uma conta:")
    for i, conta in enumerate(contas):
        print(f"{i+1}. {conta}")
    while True:
        try:
            opcao = int(input("Digite o número da conta desejada: "))
            if 1 <= opcao <= len(contas):
                return list(contas.keys())[opcao-1]
            else:
                print("Opção inválida. Digite um número válido.")
        except ValueError:
            print("Opção inválida. Digite um número válido.")

# Função para registrar uma movimentação no histórico
def registrar_movimentacao(movimentacao):
    with open("historico.txt", "a") as arquivo:
        arquivo.write(movimentacao + "\n")

# Função para exibir o histórico de movimentações
def exibir_historico():
    with open("historico.txt", "r") as arquivo:
        historico = arquivo.readlines()

    print("Histórico de movimentações:")
    for movimentacao in historico:
        print(movimentacao.strip())

# Função para fazer um depósito em uma conta específica
def fazer_deposito_conta(contas):
    nome_conta = exibir_menu_contas(contas)
    while True:
        try:
            valor = float(input("Digite o valor a ser depositado na conta " + nome_conta + ": "))
            break
        except ValueError:
            print("Valor inválido. Digite um número válido.")

    saldo = contas[nome_conta]
    saldo += valor
    contas[nome_conta] = saldo

    registrar_movimentacao(f"Depósito de {valor} na conta {nome_conta}")
    print("Depósito realizado com sucesso!")

# Função para fazer um saque em uma conta específica
def fazer_saque_conta(contas):
    nome_conta = exibir_menu_contas(contas)
    while True:
        try:
            valor = float(input("Digite o valor a ser sacado da conta " + nome_conta + ": "))
            break
        except ValueError:
            print("Valor inválido. Digite um número válido.")

    saldo = contas[nome_conta]
    if valor > saldo:
        print("Saldo insuficiente na conta", nome_conta + ". Não é possível realizar o saque.")
    else:
        saldo -= valor
        contas[nome_conta] = saldo
        registrar_movimentacao(f"Saque de {valor} na conta {nome_conta}")
        print("Saque realizado com sucesso!")

# Função para fazer uma transferência entre contas
def fazer_transferencia(contas):
    origem = exibir_menu_contas(contas)
    destino = exibir_menu_contas(contas)
    while True:
        try:
            valor = float(input("Digite o valor a ser transferido da conta " + origem + " para a conta " + destino + ": "))
            break
        except ValueError:
            print("Valor inválido. Digite um número válido.")

    saldo_origem = contas[origem]
    saldo_destino = contas[destino]

    if valor <= saldo_origem:
        saldo_origem -= valor
        saldo_destino += valor
        contas[origem] = saldo_origem
        contas[destino] = saldo_destino

        registrar_movimentacao(f"Transferência de {valor} da conta {origem} para a conta {destino}")
        print("Transferência realizada com sucesso!")
    else:
        print("Saldo insuficiente na conta de origem. Transferência não realizada.")

# Função para editar o nome de uma conta
def editar_nome_conta(contas):
    nome_conta = exibir_menu_contas(contas)
    novo_nome = input("Digite o novo nome para a conta " + nome_conta + ": ")
    contas[novo_nome] = contas.pop(nome_conta)
    print("Nome da conta atualizado com sucesso!")

# Função para mostrar o saldo total entre as contas
def mostrar_saldo_total(contas):
    total = sum(contas.values())

    print("Saldo total entre as contas:")
    for conta, saldo in contas.items():
        print(conta + ": " + str(saldo))

    print("Saldo total: " + str(total))

# Função para adicionar uma nova conta
def adicionar_conta(contas):
    nome_conta = input("Digite o nome da nova conta: ")
    while True:
        try:
            saldo_inicial = float(input("Digite o saldo inicial da conta " + nome_conta + ": "))
            break
        except ValueError:
            print("Valor inválido. Digite um número válido.")

    contas[nome_conta] = saldo_inicial
    print("Conta", nome_conta, "adicionada com sucesso!")

# Função para excluir uma conta
def excluir_conta(contas):
    nome_conta = exibir_menu_contas(contas)
    if contas[nome_conta] == 0:
        del contas[nome_conta]
        print("Conta", nome_conta, "excluída com sucesso!")
    else:
        print("A conta não pode ser excluída pois possui saldo.")

# Função para exibir o submenu de operações com contas
def exibir_submenu_contas(contas):
    while True:
        print("\n=== SUBMENU DE CONTAS ===")
        print("1. Fazer um depósito em uma conta")
        print("2. Fazer um saque de uma conta")
        print("3. Fazer uma transferência entre contas")
        print("4. Editar nome de uma conta")
        print("5. Voltar ao menu principal")

        opcao = input("Digite o número correspondente à opção desejada: ")

        if opcao == "1":
            fazer_deposito_conta(contas)
        elif opcao == "2":
            fazer_saque_conta(contas)
        elif opcao == "3":
            fazer_transferencia(contas)
        elif opcao == "4":
            editar_nome_conta(contas)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

# Função para exibir o menu principal e realizar as operações
def exibir_menu_principal():
    dados = carregar_dados()
    contas = dados.get("contas", {})

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Operações com contas")
        print("2. Exibir histórico de movimentações")
        print("3. Mostrar saldo total")
        print("4. Fechar o programa")

        opcao = input("Digite o número correspondente à opção desejada: ")

        if opcao == "1":
            exibir_submenu_contas(contas)
        elif opcao == "2":
            exibir_historico()
        elif opcao == "3":
            mostrar_saldo_total(contas)
        elif opcao == "4":
            salvar_dados({"contas": contas})
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")

# Iniciar o programa
exibir_menu_principal()
