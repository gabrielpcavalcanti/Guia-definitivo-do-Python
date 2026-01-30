"""
a) Calcule o salário de uma pessoa sabendo quantas horas ela trabalha por mês e quanto ela ganha por hora. Calcule o salário com 10%, 12% e 15%  de aumento.
"""

work_hour_month: int = int(input("Horas trabalhadas no mês: "))
money_hour: float = float(input("Quando ganha por hora: "))

salary_month: float = work_hour_month * money_hour

print(f'O salário é {salary_month:.2f}.')
print(f'O salário com 10% de aumento é {salary_month * 1.10:.2f}.')
print(f'O salário com 12% de aumento é {salary_month * 1.12:.2f}.')
print(f'O salário com 15% de aumento é {salary_month * 1.15:.2f}.')
