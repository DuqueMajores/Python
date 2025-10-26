"""
Crie um programa em Python que peergunte nome, idade, altura e peso. Exiba todoas as informações assim:

--- DADOS CADASTRADOS ---
Nome: Moisés (tipo: <class 'str'>)
Idade: 30 (tipo: <class 'int'>)
Altura: 1.8 (tipo: <class 'float'>)
Peso: 75.0 (tipo: <class 'float'>)
Ano de nascimento: 1995 (tipo: <class 'int'>)
IMC: 23.15 (tipo: <class 'float'>)
Maior de idade: True (tipo: <class 'bool'>)

"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

print("Nome:", nome, "(tipo:", type(nome), ")")
print("Idade:", idade, "(tipo:", type(idade), ")")
print("Altura:", altura, "(tipo:", type(altura), ")")
print("Peso:", peso, "(tipo:", type(peso), ")")
print("Ano de nascimento:", 2025 - idade, "(tipo:", type(idade), ")")
print("IMC:", (peso * altura)/2, "(tipo:", type(altura), ")")
if idade > 18:
    print("Maior de idade: True (tipo: <class 'bool'>)")
else:
    print("Maior de idade: False (tipo: <class 'bool'>)")
