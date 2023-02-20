"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

meses = ['1 - Janeiro', '2 - Fevereiro', '3 - Março', '4 - Abril', '5 - Maio', '6 - Junho', '7 - Julho', '8 - Agosto', '9 - Setembro', '10 - Outubro',
 '11 - Novembro', '12 - Dezembro']

lista_temperatura = []

for i in range(12):
    temperatura = int(input(f"Digite a temperatura média do mes de {meses[i]}: "))
    lista_temperatura.append(temperatura)

media_temperatura = sum(lista_temperatura) / len(lista_temperatura)

