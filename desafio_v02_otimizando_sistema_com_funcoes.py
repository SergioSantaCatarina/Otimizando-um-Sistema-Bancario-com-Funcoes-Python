
import datetime
import time

def obter_operacao():
    menu = f"""
    🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷
    Data : {datetime.date.today()}        hora : {datetime.datetime.now().time().strftime("%H:%M:%S")}
    ====== Escolha uma das opções abaixo ===

                [d] Depositar
                [s] Sacar
                [e] Extrato
                [u] Cliente/Usuario
                [lu] Listar Clientes/Usuarios
                [c] Conta Bancária
                [lc] Listar Contas Bancárias
                [q] Sair

                => """

    return (input(menu).strip().lower())

def depositar(saldo, valor, extrato,/):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (saldo + valor), (extrato + f"\nEm {data_hora}, Deposito de ... R$ {valor:.2f}")

def sacar(*,saldo,valor,extrato,limite_saque,numero_saques,limite_saques):
    saldo_insuficiente = valor > saldo
    limite_excedido = valor > limite_saque
    limite_saques_excedido = (numero_saques + 1) > limite_saques
    if saldo_insuficiente:
        print(f"\n⚠️  Saldo insuficiente! Seu saldo é de R$ {saldo:.2f} e o valor solicitado foi de R$ {valor:.2f}!")
        return saldo, extrato
    elif limite_excedido:
        print(f"\n⚠️  O valor solicitado de R$ {valor:.2f} excede o valor máximo de R$ {limite_saque} para cada saque!")
        return saldo, extrato
    elif limite_saques_excedido:
        print(f"\n⚠️  Você já efetuou o número máximo de {limite_saques} saques permitidos!")
        return saldo, extrato
    else:
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return (saldo - valor), (extrato + f"\nEm {data_hora}, Saque de ......(R$ {valor:.2f})")

def exibir_extrato(saldo,/,*,extrato):
    print("\n" + " ".join("Extrato"))
    print(f"{extrato}")
    print(f"\nSaldo Atualizado = R$ {saldo:.2f}")

def validar_cpf(cpf,clientes):
    for cliente in clientes:
        if cliente.get("cpf") == cpf:
            return True
    else:
        return False

def obter_cliente(clientes):
    cpf = int(input("Informe o CPF : "))
    cpf_existe = validar_cpf(cpf,clientes)
    if cpf_existe:
        print("\n⚠️⚠️⚠️  Cliente já está cadastrado!")
    else:
        nome_cliente = str(input("\nInforme o nome : ")).title()
        data_nascimento_cliente = str(input("\nInforme a data de nascimento : "))
        endereco_logradouro = str(input("\nInforme o logradouro e número : ")).title()
        endereco_bairro = str(input("\nInforme o bairro : ")).title()
        endereco_cidade = str(input("\nInforme a cidade : ")).title()
        endereco_uf = str(input("\nInforme a UF : ")).upper()
        endereco_cliente = f"{endereco_logradouro} - {endereco_bairro} - {endereco_cidade}/{endereco_uf}"
        novo_cliente = {"cpf":cpf, "nome":nome_cliente, "data_nascimento": data_nascimento_cliente, "endereco":endereco_cliente}
        return novo_cliente

def listar_clientes(clientes):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lista_clientes = f"Relação de clientes cadastrados em {data_hora}".center(100,"#")
    for cliente in clientes:
        lista_clientes += f"\n\nCPF : {cliente.get('cpf')}\nNome : {cliente.get('nome')}\nData de nascimento : {cliente.get("data_nascimento")}\nEndereço : {cliente.get("endereco")}"
    lista_clientes += f"\n\nTotal de clientes cadastrados : {len(clientes)}"
    print(lista_clientes)
    return True

def listar_contas(contas,clientes):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lista_contas = f"Relação de contas bancárias cadastrados em {data_hora}".center(100,"#")
    for conta in contas:
        for cliente in clientes:
            if cliente.get("cpf") == conta.get("cliente"):
                nome_cliente = cliente.get("nome")
                break 
        else:
            nome_cliente = "Anonimo"
        lista_contas += f"\n\nCliente : {conta.get('cliente')} - {nome_cliente}    Agencia : {conta.get("agencia")}  Nro. da Conta : {conta.get("conta")}"
    lista_contas += f"\n\nTotal de contas bancárias cadastradas : {len(contas)}"
    print(lista_contas)
    return True

def main():

    saldo = 0.00
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUE = 500.00   #valor máximo para cada saque
    LIMITE_SAQUES = 3       #quantidade máxima de saques
    clientes = []           #lista de clientes cadastrados
    AGENCIA = "0001"        #Agência fixa dada
    contas = []             #lista de contas bancárias cadastradas

    while True:

        operacao = obter_operacao()

        if operacao == "d":
            valor_depositar = float(input("Informe o valor a depositar:").center(30))
            saldo, extrato = depositar(saldo, valor_depositar, extrato)
            print(f"\n✅✅✅ Depósito efetuado no valor de R$ {valor_depositar:.2f}!\n🚨 Seu saldo atualizado é de R$ {(saldo):.2f}!")
        elif operacao == "s":
            valor_sacar = float(input("Informe o valor a sacar:").center(30))
            saldo_anterior = saldo
            saldo, extrato = sacar(saldo=saldo, valor=valor_sacar, extrato=extrato, limite_saque=LIMITE_SAQUE,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
            if saldo_anterior > saldo:
                numero_saques += 1
                print(f"\n✅✅✅  Saque efetuado no valor de R$ {valor_sacar}!\n🚨Seu saldo atualizado é de R$ {(saldo):.2f}.\n🚨Você ainda poderá efetuar {(LIMITE_SAQUES - numero_saques)} saques.")
        elif operacao == "e":
            exibir_extrato(saldo,extrato=extrato)
        elif operacao == "u":
            novo_cliente = obter_cliente(clientes)
            if novo_cliente:
                clientes.append(novo_cliente)
                print("\n✅✅✅  Cliente cadastrado com sucesso!")
        elif operacao == "c":
            cpf = int(input("\nInforme o cpf do titular : "))
            cliente_cadastrado = validar_cpf(cpf,clientes)
            if cliente_cadastrado:
                nr_nova_conta = (int(contas[-1].get('conta')) + 1) if contas else 1
                nova_conta = {"cliente":cpf, "agencia":AGENCIA, "conta": '{:0>6}'.format(nr_nova_conta)}
                contas.append(nova_conta)
                print("\n✅✅✅  Conta cadastrada com sucesso!")
            else:
                print("\n⚠️⚠️⚠️  Cliente/Usuário não cadastrado!")
        elif operacao == 'lu':
            if clientes:
                listar_clientes(clientes)
            else:
                print("\n⚠️⚠️⚠️  Não há Clientes/Usuários cadastrados no momento!")
        elif operacao == 'lc':
            if contas:
                listar_contas(contas,clientes)
            else:
                print("\n⚠️⚠️⚠️  Não há Contas Bancárias cadastradas no momento!")  
        elif operacao == "q":
            break
        else:
            print("\n⚠️⚠️⚠️  Operação inválida, por favor selecione novamente a operação desejada.")

main()