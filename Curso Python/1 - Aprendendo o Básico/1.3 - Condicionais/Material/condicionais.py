"""
Condicionais servem para tomar decisões no código. Ou seja, executar um bloco de código se uma condição for verdadeira.

Em Python, usamos if, elif e else. 
E tambem usamos, em versões mais recentes, a instrução Match, parecida com o switch, servindo para substituir longas cadeias de if / elif / else de um jeito mais limpo e legível.

"""

animal = "gato"

if animal == "cachorro":
    print("Au au!")
elif animal == "gato":
    print("Miau!")
else:
    print("Outro animal")

print("------------")

match animal:
    case "cachorro":
        print("Au au!")
    case "gato":
        print("Miau!")
    case _:
        print("Outro animal")
