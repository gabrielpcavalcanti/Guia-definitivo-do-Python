"""
b) Dado o salário de um funcionário, quanto que ele tem que pagar para o inss (8%), imposto de renda (11%) e seu salário líquido após essas reduções.
"""

salary_month: float = float(input("Digite seu salário: "))

inss: float = 0.08 * salary_month
imposto_de_renda: float = 0.11 * salary_month
salario_liquido: float = salary_month - inss - imposto_de_renda

print(f'O seu salário bruto é: {salary_month:.2f}.')
print(f'A parcela do inss: {inss:.2f}.')
print(f'A parcela do imposto de renda: {imposto_de_renda:.2f}.')
print(f'O seu salário líquido é: {salario_liquido:.2f}.')
