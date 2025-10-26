"""
O comando de repetição For é usado quando você sabe quantas vezes quer repetir algo.

Em ambos vai existir o uso do break, para sair do loop, e continue, para continuar no loop.

"""
def dot():
    print("-----------------------")


for i in range(0, 6):
    print(i)
dot()

for i in range(6, 10):
    print(i)
dot()

for i in range(0, 20, 5):
    print(i)
dot()

nomes = ["Moises", "Luana", "Carol"]
for nome in nomes:
    print(nome)
dot()



