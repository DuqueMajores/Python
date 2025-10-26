"""
Crie um programa em Python que use várias funções para gerenciar um pequeno sistema de cadastro de pessoas.

🎯 Requisitos do exercício

1 - Função adicionar_pessoa(nome, idade)

# Deve receber o nome e a idade de uma pessoa.
# Deve retornar um dicionário com esses dados.
Exemplo de retorno:

{"nome": "Moises", "idade": 22}

                 ----

2 - Função mostrar_pessoas(*pessoas)

# Recebe várias pessoas (usando *args).
# Deve imprimir cada pessoa cadastrada.

                ----

3 - Função estatisticas(**dados)

# Recebe dados nomeados (**kwargs) com informações gerais, como total=, media_idade= etc.
# Mostra os dados formatados.

                ----

4 - Função principal main()

# Usa as funções anteriores:
    # Crie 3 pessoas diferentes.
    # Mostre todas as pessoas.
    # Calcule a média de idade e passe esse valor para estatisticas().

"""

# 1°

def adicionar_pessoa(nome, idade):
    pessoa = {"nome": nome, "idade": idade}
    return pessoa

pessoa = adicionar_pessoa("Moises", 28)
print(pessoa)

# 2°

def mostrar_pessoas(*pessoas):
    for pessoa in pessoas:
        print(f"{pessoa}\n")

pessoas = ("Moises", "Luana", "Carol")
mostrar_pessoas(pessoas)

# 3° ...
