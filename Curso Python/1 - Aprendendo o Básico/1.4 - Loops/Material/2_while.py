"""
O while repete enquanto uma condição for verdadeira.

"""

def dot():
    print("--------------")

contador = 0
while contador <= 5:
    print("Contador:", contador)
    contador += 1
dot()

op = True
while op == True:
    print("Ligado")
    dot()
    escolha = int(input("1 - Ligar\n" \
    "2 - Desligar\n" \
    "---> "))
    dot()
    if escolha == 1:
        continue
    else:
        print("Desligado")
        op = False
        break


