"""
Função como o nome já diz, é uma estrutura criada para definir uma função desejada sempre que ele é chamada. 
Ela começa com def de definição, em seguida com o nome da função e um parâmetro de entrada.
Toda função deve estar indentada.

"""

def saudacao(nome):
    print("Seja bem vindo, ", nome)

nome = input("Digite o seu nome: ")
saudacao(nome)
