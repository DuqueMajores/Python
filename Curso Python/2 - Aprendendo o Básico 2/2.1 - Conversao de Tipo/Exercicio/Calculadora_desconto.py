"""
Crie um programa que peça ao usuário, o nome do prouto (texto), o preço do produto (número decimal) e o percentual de desconto (número inteiro).

Converta os valores corretamente para fazer as operações matemáticas. Depois calcule o valor final do produto com desconto. E mostre na tela uma mensagem formatada:

Produto: Camisa
Preço original: R$ 100.00
Desconto: 15%
Preço com desconto: R$ 85.00

"""

def dot():
    print("--------------------")

op = True
while op == True:
    dot()
    print("CAIXA")
    dot()

    nome = input("Nome do produto: ")
    preco = input("Preco do produto: ")
    desc = input("Percentual de desconto: ")
    preco = float(preco)
    desc = int(desc)

    dot()
    print("Produto: ", nome)
    print("Preço original: R$", preco)
    print("Desconto: ", desc, "%")
    print("Preço com desconto: R$", (preco - (preco * desc) / 100))

    dot()
    opt = input("1 - Novo produto\n" \
    "2 - Sair\n" \
    "---> ")
    opt = int(opt)
    if opt == 1:
        continue
    else:
        op = False
        break

