"""
Você pode criar e lançar erros personalizados com raise, no sentido de construir.

Ou você pode usar raise para personalizar sua classe de exceção.

"""
def dot():
    print("------------------------")

def sacar(valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo")
    print(f"Saque de R${valor} realizado com sucesso!")


try:
    sacar(-100)

except Exception as erro:
    print("Erro ao sacar:", erro)

dot()
print("Excecao Personalizada\n")

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente!")
    return saldo - valor

try:
    novo_saldo = sacar(100, 150)
except SaldoInsuficienteError as erro:
    print("Erro:", erro)
