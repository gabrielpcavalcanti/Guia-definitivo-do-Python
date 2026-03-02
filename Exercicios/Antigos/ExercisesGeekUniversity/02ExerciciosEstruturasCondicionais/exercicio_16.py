"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima 0 mês 
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante. 
"""

# switch não existe no python, mas podemos fazer de outra forma.

num_mes = int(input("Digite um número de 1 a 12: "))

if num_mes == 1:
    print("Janeiro")

elif num_mes == 2:
    print("Fevereiro")

elif num_mes == 3:
    print("Março")

elif num_mes == 4:
    print("Abril")

elif num_mes == 5:
    print("Maio")

elif num_mes == 6:
    print("Junho")

elif num_mes == 7:
    print("Julho")

elif num_mes == 8:
    print("Agosto")

elif num_mes == 9:
    print("Setembro")

elif num_mes == 10:
    print("Outubro")

elif num_mes == 11:
    print("Novembro")

elif num_mes == 12:
    print("Dezembro")

else:
    print("Número inválido")

