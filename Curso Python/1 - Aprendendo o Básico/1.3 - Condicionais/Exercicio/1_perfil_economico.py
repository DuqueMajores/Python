"""
Crie um programa que receba:

a idade de uma pessoa, e a renda mensal (em R$). Com base nesses dados, classifique o perfil econômico e social dela de acordo com as regras abaixo:

Faixa de idade	Renda mensal (R$)	Classificação
Menor de 18	qualquer renda	“Menor de idade”
18 a 25	até 2.000	“Jovem de baixa renda”
18 a 25	até 5.000	“Jovem classe média”
18 a 25	acima de 5.000	“Jovem de alta renda”
26 a 60	até 3.000	“Adulto de baixa renda”
26 a 60	até 10.000	“Adulto classe média”
26 a 60	acima de 10.000	“Adulto de alta renda”
acima de 60	qualquer renda	“Idoso”

Implemente todas essas condições usando apenas if, elif, e else — nada de match.

"""

idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))

if idade >= 18 or idade <= 25:
    if renda <= 2.000:
        print("Jovem Liso")
    elif renda > 2.000 and renda<= 5.000:
        print("Jovem Sobrevivente")
    elif renda > 5.000:
        print("Jovem Com dindin")
elif idade >= 26 or idade <= 65:
    if renda <= 3.000:
        print("Adulto Liso")
    elif renda > 3.000 and renda <= 5.000:
        print("Adulto Sobrevivente")
    elif renda >= 10.000:
        print("Patrao")
elif idade < 18:
    print("Menor de idade")
elif idade > 65 and renda < 10.000:
    print("Veio da Praça")
elif idade > 65 and renda > 10.000:
    print("Veio da Lancha")
    
