"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu 25% de aumento.
"""

salary = float(input("Digite o salário R$ "))

new_salary = salary + (salary * 0.25)

print("O novo salário é R$ {:.2f}".format(new_salary))
