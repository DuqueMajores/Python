"""
else executa somente se não ocorrer erro.

finally executa sempre, mesmo que haja erro.

"""

try:
    num = int(input("Digite um numero: "))

except ValueError:
    print("Erro: valor invalido")

else:
    print("Nenhum erro! Numero:", num)

finally:
    print("Fim da execucao")
