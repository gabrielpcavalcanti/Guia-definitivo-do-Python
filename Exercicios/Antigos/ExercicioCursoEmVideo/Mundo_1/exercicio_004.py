"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
"""

x = input("Digite algo na tela: ")

print("Tipo primitivo: ", type(x))
print("Tem espaços: ", x.isspace())
print("É um número: ", x.isnumeric())
print("É alfabético", x.isalpha())
print("É alfa numérico: ", x.isalnum())
print("Está em maiúsculas?: ", x.isupper())
print("Está em minsúscula?: ", x.islower())
print("Está capitalizado?: ", x.istitle())
