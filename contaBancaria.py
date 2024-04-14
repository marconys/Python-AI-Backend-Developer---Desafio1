def menu():
    opcoes_menu = """

    Qual ação deseja realizar?

    [d] Depositar
    [s] Sacar
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
    

 
