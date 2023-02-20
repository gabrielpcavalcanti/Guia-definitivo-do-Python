"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a 
prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso 
contrário imprima: Empréstimo concedido.
"""

salario = float(input("Digite o seu salário: R$ "))
prestacao = float(input("Digite o valor do empréstimo em %: "))

salario_20 = salario * 0.2

if prestacao > salario_20:
    print("Empréstimo não concedido")

else:
    print("Empréstimo Concedido")
 