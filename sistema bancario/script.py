menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 2

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor: .2f}/n"
        else:
            print("Operação falhou! O valor informado e inválido. Tente novamente!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES
        if  excedeu_saldo:
            print("Operação falhou, Você não possui saldo suficiente")
        elif excedeu_limite:
            print("Operação falhou, número de saques foi limite")

        elif excedeu_saques:
            print("Operação falhou, o numero de saques foi excedido")

        elif valor >= 0:
            saldo -= valor
            extrato += f"Saque: R${valor: .2f}/n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido")

    elif opcao == "e":

        print("-------------EXTRATO------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"/n Saldo: R$ {saldo: .2f}")
        print("----------------------------")        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")    
