"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

salario_inicial = float(input("Digite o salário inicial do funcionário: "))
ano = int(input("Digite o ano inicial do aumento: "))
ano_atual = int(input("Digite o ano atual: "))
aumento_inicial = float(input("Digite o aumento salarial inicial em %: "))
salario = salario_inicial

aumento_inicial = aumento_inicial / 100

while ano != ano_atual + 1:

    aumento_inicial = 2 * aumento_inicial
    salario_atual = salario + (salario * aumento_inicial)
    ano += 1

print(f"O seu salário no ano {ano_atual} é de R$ {salario_atual}")



