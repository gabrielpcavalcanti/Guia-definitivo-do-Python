"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

nota_1 = float(input("Primeira nota do aluno: "))
nota_2 = float(input("Segunda nota do aluno: "))

print("A média entre {} e {} é igual a {:.1f}".format(nota_1, nota_2, ((nota_1 + nota_2) / 2)))
