menu = """"

========== Escolha uma Opção ==========
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Encerrar Sessão

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Valor de desposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
        else:
            print("Valor para Depósito invalido.")
        
    
    elif opcao == 2:
        valor = float(input("Valor de saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("Limite de R$500 por Saque.")
            
        elif excedeu_saques:
            print("Limete de 3 Saques diarios, tente novamente amanhã.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Valor de saque invalido.")

    elif opcao == 3:
            print("\n================== EXTRATO ==================")
            print("Sem movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=============================================")
            
    
    elif opcao == 4:
        print("Sessão Encerrada")
        break
    else:
        print("Opção Invalida")