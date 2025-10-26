"""
Crie um programa que simule um menu de operações bancárias com base em um código digitado pelo usuário:

Código	Operação
1	Depositar
2	Sacar
3	Transferir
4	Consultar saldo
5	Encerrar conta

Cada caso deve imprimir uma mensagem diferente.
Mas o desafio é: para cada operação, o programa deve pedir um valor (quando fizer sentido) e validar valores negativos (usando um if dentro do match).

"""

saldo = 0
op = input("Abrir Menu [s / n]: ")
while op == "s":
    opmenu = int(input("" \
    "1 - Depositar\n" \
    "2 - Sacar\n" \
    "3 - Transferir\n" \
    "4 - Consultar Saldo\n" \
    "5 - Sair\n" \
    "--> "))

    match opmenu:
        case 1:
            dep = int(input("Digite o valor do deposito: "))
            saldo += dep
        case 2:
            saq = int(input("Digite o valor do saque: "))
            saldo -= saq
        case 3:
            cont = int(input("Digite o ID do destinatario: "))
            tran = int(input("Digite o valor a ser transferido: "))
            saldo -= tran
        case 4:
            print(saldo)
        case 5:
            op = input("Abrir Menu [s / n]: ")
        case _:
            print("Digite uma opçao valida!")
