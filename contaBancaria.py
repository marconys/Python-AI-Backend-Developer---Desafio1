menu = """

Qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

"""

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
    
    elif opcao == "s":
        print("Saque")
    
    elif opcao == "e":
        print("Extrato")
    
    elif opcao == "q":
        print("Obrigado por usar os nossos serviços!")          
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
