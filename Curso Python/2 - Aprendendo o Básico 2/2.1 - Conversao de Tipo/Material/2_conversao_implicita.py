"""
O Python faz conversão sozinho quando necessário.

"""

a = 5              # int
b = 2.0            # float
c = a + b          # int + float = float
print(c, type(c))  # 7.0


idade = input("Digite sua idade: ")
idade = int(idade)
print(idade * 2)
