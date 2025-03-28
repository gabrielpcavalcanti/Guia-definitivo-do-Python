"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

pais_a = 80000
pais_b = 200000
taxa_crescimento_a = 0.03
taxa_crescimento_b = 0.015
ano = 1

while pais_a < pais_b:
    pais_a = pais_a + pais_a * taxa_crescimento_a
    pais_b = pais_b + pais_b * taxa_crescimento_b
    ano += 1

    if pais_a < pais_b:
        continue
    else:
        print("A quantidade de anos necessárias para a população do país A ser igual ou ultrapassar a de B foi: {}"
              .format(ano))
        break
