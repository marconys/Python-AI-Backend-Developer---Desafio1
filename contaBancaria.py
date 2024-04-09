menu = """

Qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

Informe a operação: """

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"DEPÓSITO: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            
        else: 
            print("O Valor do depóstivo deve ser positivo!")   
    
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Informe o valor do saque: "))
        
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido!")
            
        elif valor_saque > limite_valor_saque:
            print(f"O valor máximo por saque é de R$ {limite_valor_saque:.2f}!")
            
        elif valor_saque > saldo:
            print("Saldo insuficiente para saque!")   
             
        else:
            saldo -= valor_saque
            extrato += f"SAQUE: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!") 
    
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif opcao == "q":
        print("Obrigado por usar os nossos serviços!")          
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
