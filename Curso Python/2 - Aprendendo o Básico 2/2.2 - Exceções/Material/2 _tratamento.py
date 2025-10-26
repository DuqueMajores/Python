"""
Você pode tratar as exceções de uma forma mais limpa. 

Use try no bloco onde o Python tenta executar.

Use o except para determinar o que fazer se um erro específico ocorrer.

Exception é a classe base de quase todos os erros.

"""

def dot():
    print("---------------------")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print(resultado)

except ZeroDivisionError:
    print("Erro: nao e possivel dividir por zero.")

except ValueError:
    print("Erro: voce precisa digitar um numero valido.")

dot()

print("Capturando qualquer erro\nCom Exception:\n\nx = 10 / 0")

try:
    x = 10 / 0

except Exception as erro:
    print("Ocorreu um erro:", erro)
