"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base = int(input("Digite um número inteiro para ser a base do número: "))
expoente = int(input("Digite um número inteiro para ser o expoente do número: "))

cont_expoente = 1
potencia = 1

while cont_expoente <= expoente:
    potencia *= base
    cont_expoente +=1

print()
print(f"{base}^{expoente} = {potencia}")

