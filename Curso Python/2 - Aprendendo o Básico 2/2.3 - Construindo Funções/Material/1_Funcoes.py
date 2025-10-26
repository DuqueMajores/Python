"""
Uma função é um bloco de código reutilizável que executa uma tarefa específica. Em vez de repetir código, você cria uma função e a chama empre que precisar.

"""

def saudacao():
    print("Olá, bem-vindo!")

saudacao()

"""
Funções podem receber parâmetros - valores que você passa para personalizar seu comportamento.

"""

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Moises")
saudacao("Luana")

"""
Funções podem retornar valores com palavra-chave "return" - ele finaliza a execução da função e devolve um valor.

"""

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

"""
Você pode definir valores padrão para parâmetros - usados quando o argumento não é passado.

"""

def saudacao(nome="visitante"):
    print(f"Olá, {nome}!")

saudacao("Pedro")
saudacao()

"""
Parâmetros podem ser nomeados ou posicionais. Posicionais - a ordem importa; nomeados - você especifica o nome do parâmetro.

"""

def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos.")

apresentar("Karla", 35) # Posicional
apresentar(idade=30, nome="Raphael") # Nomeado

"""
Você também pode passar varias informações dentro dos parâmetros. É usado *args para vários argumentos posicionais, e **kwargs para vários argumentos nomeados.

"""

# *args - posicionais

def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(1, 2, 3, 4, 5))

# **kwargs - nomeados

def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Moises", idade=28, cidade="Rio de Janeiro")

"""
Existe uma função anônima chamada lambda - com o intuito de deixar as funções curtas e simples.

"""

dobro = lambda x: x * 2
print(dobro(5))

"""
Você também pode definir uma função dentro de outras funções.

"""

def saudacao(nome):
    def mensagem():
        return "Olá"
    print(mensagem(), nome)

saudacao("Moises")

"""
Funções de ordem superior recebem ou retornam outras funções.

"""

def aplicar(funcao, valor):
    return funcao(valor)

def quadrado(x):
    return x ** 2

print(aplicar(quadrado, 5))

"""
Já funções recursivas chamam a si mesmas.

"""

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))

"""
Uma boa prática em relação as funções, é escrever docstrings para explicar o que elas fazem.

"""

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b
