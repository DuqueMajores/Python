"""
Crie um programa que simule operações bancárias:

✅ Regras
1. O programa deve ter um saldo inicial de R$ 1000,00.
2. O usuário poderá escolher entre 3 operações:

Depósito

Saque

Ver saldo

3. O programa deve tratar pelo menos os erros abaixo:
🔴 ValueError

Quando o usuário digitar valores inválidos (ex.: letras em vez de números).

🔴 Saque maior que o saldo

Nesse caso, crie uma exceção personalizada chamada:

class SaldoInsuficienteError(Exception):
    pass


E use raise quando o valor do saque for maior que o saldo.

4. Não permitir depósito ou saque com valor negativo ou zero.
5. O programa deve rodar em loop até o usuário digitar sair.
6. Use try, except, else e finally pelo menos uma vez.

"""

class ErroLetraError(Exception):
    pass
class OptInvalidoError(Exception):
    pass
class InvalidDepError(Exception):
    pass
class InvalidSaqError(Exception):
    pass
class InsufSaqError(Exception):
    pass
class InsufSaldError(Exception):
    pass

def optinvalidade(opt):
    if opt > 4 or opt < 1:
        raise OptInvalidoError("Escolha de 1 a 4 apenas!")
    return opt
def opcinvalidade(opc):
    if opc.lower() not in ["s", "n"]:
        raise ErroLetraError("Digite apenas s ou n !")
    else:
        return opc.lower()
def depinvalidade(dep):
    if dep < 0:
        raise InvalidDepError("Deposito invalido!")
def saqinvalidade(saq, saldo):
    if saq > saldo and saldo > 0:
        raise InsufSaqError("Voce não tem saldo necessario!")
    elif saldo == 0:
        raise InsufSaldError("Voce nao tem saldo!")
    elif saq < 0:
        raise InvalidSaqError("Saque invalido!")
def dot():
    print("--------------------------------")

saldo = 1000
op = bool("")

while op == False:
    while True:
        dot()
        print("MENU")
        dot()
        try:
            opt = int(input("1 - Deposito\n2 - Saque\n3 - Ver saldo\n4 - Sair ---> "))
            optinvalidade(opt)
            break
        except ValueError:
            print("Erro: digite um numero valido")
        except OptInvalidoError as erro:
            print(erro)

    match opt:
        case 1:
            dot()
            print("DEPOSITO")
            dot()
            while True:
                try:
                    dep = float(input("Digite o valor: "))
                    depinvalidade(dep)
                except InvalidDepError as erro:
                    print(erro)
                    dot()
                except ValueError:
                    print("Digite apenas numeros!")
                    dot()
                else:
                    saldo += dep
                    print("Deposito realizado com sucesso!")
                    dot()
                    print("Saldo atual: R$", saldo)
                    dot()
                    break
        case 2:
            dot()
            print("SAQUE")
            dot()
            while True:
                try:
                    saq = float(input("Digite um valor: "))
                    saqinvalidade(saq, saldo)
                except InvalidSaqError as erro:
                    print(erro)
                    dot()
                except InsufSaqError as erro:
                    print(erro)
                    dot()
                except InsufSaldError as erro:
                    print(erro)
                    dot()
                except ValueError:
                    print("Digite apenas numeros!")
                    dot()
                else:
                    saldo -= saq
                    print("Saque realizado com sucesso!")
                    dot()
                    print("Saldo atual: R$", saldo)
                    dot()
                    break
        case 3:
            dot()
            print("Saldo: R$", saldo)
            dot()
        case 4:
            print("Saindo")
            break
        case _:
            print("Opcao invalida")
    
    op2 = False
    while op2 == False:
        try:
            chuse = input("Deseja continuar? [s/n]: ")
            chuse = opcinvalidade(chuse)
        except ErroLetraError as erro:
            print(erro)
            continue
        else:
            if chuse == "n":
                op = True
            op2 = True
