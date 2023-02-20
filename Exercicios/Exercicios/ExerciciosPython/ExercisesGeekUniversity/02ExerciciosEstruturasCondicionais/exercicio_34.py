"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a 
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito. 

NOTA              CONCEITO (ATE 20 FALTAS)         CONCEITO (MAIS DE 20 FALTAS) 
9.0 até 10.0               A                                  B
7.5 ate 8.9                B                                  C
5.0 até 7.4                C                                  D
4.0 ate 4.9                D                                  E
0.0 até 3.9                E                                  E
"""

nota = float(input("Digite a nota do aluno: "))
n_faltas = int(input("Digite o número de faltas: "))

if nota >= 9 and nota < 10:
    if n_faltas > 20:
        print("B")
    else:
        print("A")

if nota >= 7.5 and nota < 8.9:
    if n_faltas > 20:
        print("C")
    else:
        print("B")

if nota >= 5 and nota < 7.4:
    if n_faltas > 20:
        print("D")
    else:
        print("C")

if nota >= 4 and nota < 4.9:
    if n_faltas > 20:
        print("E")
    else:
        print("D")

if nota >= 0 and nota < 3.9:
    if n_faltas > 20:
        print("E")
    else:
        print("E")

