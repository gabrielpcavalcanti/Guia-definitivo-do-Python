"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input("Digite o salário: "))

print()

if 0<= salario <=280:
    salariorea20 = salario + salario*0.2
    print(salario)
    print("20%")
    print(salario*0.2)
    print(salariorea20)
elif 280< salario <=700:
    salariorea15 = salario + salario*0.15
    print(salario)
    print("15%")
    print(salario*0.15)
    print(salariorea15)
elif 700< salario <=1500:
    salariorea10 = salario + salario*0.1
    print(salario)
    print("10%")
    print(salario*0.1)
    print(salariorea10)
elif salario > 1500:
    salariorea5 = salario + salario*0.05
    print(salario)
    print("5%")
    print(salario*0.05)
    print(salariorea5)
else:
    print("Erro")
