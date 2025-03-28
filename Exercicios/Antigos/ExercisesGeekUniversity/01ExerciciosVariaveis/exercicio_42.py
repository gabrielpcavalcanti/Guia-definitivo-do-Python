"""
Receba o salário base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre
o salário base. Além disso, ele paga 7% de imposto sobre o salário base. 
"""

base_salary = float(input("Digite seu salário: "))

base_salary_5 = base_salary + (base_salary * 0.05)

base_salary_7 = base_salary_5 - (base_salary_5 * 0.07)

print("O salário final é de R$ {}".format(base_salary_7))
