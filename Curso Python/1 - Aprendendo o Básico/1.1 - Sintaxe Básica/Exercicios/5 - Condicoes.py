"""
Peça a idade do usuário e mostre:

- "criança" se for menor de 12
- "Adolescente" se estiver entre 12 e 17
- "Adulto" se for 18 ou mais
- "Idoso" se for maior que 65

"""

idade = int(input("Digite sua idade: "))

if idade > 0 and idade <= 3:
    print("Bebê")
elif idade < 12:
    print("Criança")
elif idade >= 12 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 65:
    print("Adulto")
else:
    print("Idoso")