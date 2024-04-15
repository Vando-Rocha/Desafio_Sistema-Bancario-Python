menu_inicio = '''
    Digite a letra correspondete a operação desejada. 
    [d] = Depósito
    [s] = Saque
    [e] = Extrato
    [q] = Sair
    
    =>
'''

saldo = 0
limite_saque = 500
NUM_SAQUES = 3
extrato = ""

while True:
    operacao = input(menu_inicio)
    
    if operacao == "d":
        deposito = float(input("Digite o valor de Déposito: "))
        if deposito > 0: 
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else: 
            print("Falha na operação! Valor informado é inválido.")
    elif operacao =="s":
        saque = float(input("Digite o valor do Saque: "))
        if saque > 0: 
            if saque <= limite_saque and NUM_SAQUES > 0:
                saldo -= saque
                NUM_SAQUES -= 1
                extrato += f"Saque: R$ {saque:.2f}\n"
            else:
                if saque > limite_saque and NUM_SAQUES > 0:
                    print("Falha na operação! Valor de Saque maior que limite permitido")
                elif NUM_SAQUES == 0:
                    print("Falha na operação! Limite de saques diário excedido.")           
        else: 
            print("Falha na operação! Valor informado é inválido.")
        print("Saque")
    elif operacao =="e":
        print("Extrato")
    elif operacao =="q":
        print("Finalizando operações")
        break
    else:
        print("Opção inválida! Retornando ao menu inicial.")
        