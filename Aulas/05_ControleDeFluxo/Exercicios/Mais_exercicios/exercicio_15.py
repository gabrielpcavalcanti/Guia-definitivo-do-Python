"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a 
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito. 

nota             CONCEITO (ATE 20 FALTAS)         CONCEITO (MAIS DE 20 FALTAS) 
9.0 até 10.0               A                                  B
7.5 ate 8.9                B                                  C
5.0 até 7.4                C                                  D
4.0 ate 4.9                D                                  E
0.0 até 3.9                E                                  E
"""

grade = float(input("Digite a grade do aluno: "))
misses = int(input("Digite o número de faltas: "))

if grade >= 9 and grade < 10:

    if misses > 20:
        print("B")

    else:
        print("A")

if grade >= 7.5 and grade < 8.9:

    if misses > 20:
        print("C")

    else:
        print("B")

if grade >= 5 and grade < 7.4:
    
    if misses > 20:
        print("D")

    else:
        print("C")

if grade >= 4 and grade < 4.9:

    if misses > 20:
        print("E")

    else:
        print("D")

if grade >= 0 and grade < 3.9:
    
    if misses > 20:
        print("E")

    else:
        print("E")
        