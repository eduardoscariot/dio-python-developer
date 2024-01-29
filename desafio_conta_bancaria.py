menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_VLR_SAQUE = 500
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Favor informar o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito efetuado de R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Favor informar o valor do saque: "))

        if valor > saldo:
            print("Atenção!!! Você não possui saldo suficiente para este saque.")
        elif valor > LIMITE_VLR_SAQUE:
            print(f"Atenção!!! Valor maior do que o limite de saque de R$ {LIMITE_VLR_SAQUE:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Atenção!!! Limite de saques excedidos. Seu limite de saques é {LIMITE_SAQUES}.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque efetuado no valor de R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n***** Entrato da sua conta *****")
        print("Não foram encontradas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("********************************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")