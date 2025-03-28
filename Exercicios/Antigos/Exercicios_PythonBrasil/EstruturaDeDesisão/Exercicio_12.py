"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
"""

valorHora = float(input("Digite o valor de hora trabalhada: "))
horas = float(input("Horas trabalhadas: "))

salarioBruto = valorHora * horas

print()

if 0 <= salarioBruto <=900:
    print("Salário Bruto: {}".format(salarioBruto))
    print("- IR: {}".format(salarioBruto*0))
    print("- INSS (10%): {}".format(salarioBruto*0.1))
    print("FGTS (11%): ".format(salarioBruto*0.11))
    print("Total de descontos: {}".format(salarioBruto + salarioBruto*0.1 + salarioBruto*0.11))
    print("Salário Líquido: {}".format(salarioBruto) - salarioBruto + salarioBruto*0.1 + salarioBruto*0.11)
elif 900 < salarioBruto <=1500:
    print("Salário Bruto: {}".format(salarioBruto))
    print("- IR (5%): {}".format(salarioBruto*0.05))
    print("- INSS (10%): {}".format(salarioBruto*0.1))
    print("FGTS (11%): ".format(salarioBruto)*0.11)
    print("Total de descontos: {}".format(salarioBruto*0.05 + salarioBruto*0.1 + salarioBruto*0.11))
    print("Salário Líquido: {}".format(salarioBruto) - salarioBruto*0.05 + salarioBruto*0.1 + salarioBruto*0.11)
elif 1500 < salarioBruto <=2500:
    print("Salário Bruto: {}".format(salarioBruto))
    print("- IR (10%): {}".format(salarioBruto*0.1))
    print("- INSS (10%): {}".format(salarioBruto*0.1))
    print("FGTS (11%): ".format(salarioBruto)*0.11)
    print("Total de descontos: {}".format(salarioBruto*0.1 + salarioBruto*0.1 + salarioBruto*0.11))
    print("Salário Líquido: {}".format(salarioBruto) - salarioBruto*0.1 + salarioBruto*0.1 + salarioBruto*0.11)
elif salarioBruto > 2500:
    print("Salário Bruto: {}".format(salarioBruto))
    print("- IR (20%): {}".format(salarioBruto*0.2))
    print("- INSS (10%): {}".format(salarioBruto*0.1))
    print("FGTS (11%): ".format(salarioBruto)*0.11)
    print("Total de descontos: {}".format(salarioBruto*0.2 + salarioBruto*0.1 + salarioBruto*0.11))
    print("Salário Líquido: {}".format(salarioBruto) - salarioBruto*0.2 + salarioBruto*0.1 + salarioBruto*0.11)
else:
    print("Erro")
