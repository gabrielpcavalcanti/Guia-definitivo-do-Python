"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia 
da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e 
assim por diante.
"""

# switch não existe no python, mas podemos fazer de outra forma.

num_semana = int(input("Digite um número de 1 a 7: "))

if num_semana == 1:
    print("Domingo")

elif num_semana == 2:
    print("Segunda-feira")

elif num_semana == 3:
    print("Terça-feira")

elif num_semana == 4:
    print("Quarta-feira")

elif num_semana == 5:
    print("Quinta-feira")

elif num_semana == 6:
    print("Sexta-feira")

elif num_semana == 7:
    print("Sábado")

else:
    print("Número inválido")

