"""
d) Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
"""

salary: float = float(input("Digite seu salário: "))
provision_loan: float = float(input("Digite a prestação de um empréstimo: "))

if provision_loan > (0.2 * salary):
    print()
    print("Empréstimo não concedido.")

else:
    print()
    print("Empréstimo concedido.")
