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

