def menu():
    opcoes_menu = """

    Qual ação deseja realizar?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [e] Extrato
    [q] sair

    Informe a ação: """
    
    return input(opcoes_menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n*** Operação falhou! Você não tem saldo suficiente. ***")

    elif excedeu_limite:
        print("\n*** Operação falhou! O valor do saque excede o limite. ***")

    elif excedeu_saques:
        print("\n*** Operação falhou! Número máximo de saques excedido. ***")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n" +" Extrato ".center(30, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato, end="\n")
    print(f"Saldo atual: R$ {saldo:.2f}")  
    print("\n" + "=" * 100) 
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if cpf in usuarios:
        print("\n*** Já existe usuário com esse CPF! ***")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}

    print("=== Usuário criado com sucesso! ===")
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios:
        print("\n*** Usuário não encontrado, fluxo de criação de conta encerrado! ***")
        
        return None

    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios[cpf]}
    print("\n=== Conta criada com sucesso! ===")
    
    return conta  

def listar_contas(contas):
    print("\n" +" LISTA DE CONTAS ".center(30, "="))
    for i, conta in enumerate(contas, start=1):
        print(f"\nConta {i}:")
        print(f"Agência:\t{conta['agencia']}")
        print(f"Número:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{conta['usuario']['nome']}")
        print("\n" + "=" * 100)  
 

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = {}
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            print("Depósito")
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            print("Saque")
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            print("Novo usuário")
            criar_usuario(usuarios)

        elif opcao == "nc":
            print("Todas as contas")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            print("Listar contas")
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar os nossos serviços!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()