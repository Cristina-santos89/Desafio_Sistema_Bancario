menu = """

[d] Deposito
[s] Saque
[q] Quantidade de saques
[e] Extrato
[o] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"

        else:
            print("Falha na operação. O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação. Saldo insuficiente")

        elif excedeu_limite:
            print("Falha na operação. O valor do saque excede o limite")

        elif excedeu_saques:
            print("Falha na operação. Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação. O valor informado é inválido.")

    elif opcao == "e":
        print("\n------------- EXTRATO -------------")
        print(f"\nQuantidade de saques realizados: {numero_saques}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------------")

    elif opcao == "q":
        print("\n------------- QUANTIDADE DE SAQUES -------------")
        print(f"\nQuantidade de saques realizados: {numero_saques}")
        print("--------------------------------------------------")        

    elif opcao == "o":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")