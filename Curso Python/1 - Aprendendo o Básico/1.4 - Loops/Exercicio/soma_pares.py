"""
Peça ao usuário digitar um número inteiro positivo N. Calcule e mostre a soma de todos os números pares de 1 até N. Use um loop for ou while.

"""

soma = 0
n = int(input("Escolha um numero: "))
for i in range(0, n+1):
    if i % 2 == 0:
        print("+", i)
        soma += i
    else:
        continue

print("Soma total dos pares:", soma)
