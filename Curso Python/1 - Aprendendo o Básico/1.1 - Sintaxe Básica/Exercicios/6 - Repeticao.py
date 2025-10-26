"""
Faça a tabuada com um For e depois com um While

"""

num1 = int(input("Digite um numero: "))
for i in range(11):
    print(i, "x", num1, "=", i * num1)

num2 = int(input("Digite outro numero: "))
num = 0
while num <= 10:
    print(num, "x", num2, "=", num * num2)
    num += 1
