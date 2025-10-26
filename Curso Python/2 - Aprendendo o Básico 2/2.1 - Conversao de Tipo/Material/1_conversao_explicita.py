"""
Conversão de tipos é o processo de transformar um valor de um tipo para outro.

Existem dois tipo de conversão, a Explícita e a Inplícita. A implícita é feita com funções como int(), float(), str(), bool().

"""

print("\nTexto -> Numero")
num = int("10")
print(num, type(num))
num2 = float("3.14")
print(num2, type(num2))

# int() só funciona se o texto for numérico


print("\nNumero -> Texto")
texto = str(123)
print(texto, type(texto))


print("\nNumero -> Booleano")
print(bool(0))  # False
print(bool(1))  # True
print(bool(42)) # True

# 0 -> False
# Qualquer outro número é True

print("\nTexto -> Booleano")
print(bool(""))    # False (string vazia)
print(bool("abc")) # True (qualquer texto é True)

print("\nFloat -> Int")
x = int(3.9) # Corta a parte decimal -> 3
y = float(5) # Vira 5.0
