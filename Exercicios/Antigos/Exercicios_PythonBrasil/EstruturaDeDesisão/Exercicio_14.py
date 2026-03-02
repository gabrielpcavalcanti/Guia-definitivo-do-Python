"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2)/2

print()

if 9 < media <= 10:
    print("A")
    print("nota 1: {} \nnota 2: {}".format(nota1,nota2))
    print("Média: {}".format(media))
elif 7.5 < media <= 9:
    print("B")
    print("nota 1: {} \nnota 2: {}".format(nota1, nota2))
    print("Média: {}".format(media))
elif 6 < media <= 7.5:
    print("C")
    print("nota 1: {} \nnota 2: {}".format(nota1, nota2))
    print("Média: {}".format(media))
elif 4 < media <= 6:
    print("D")
    print("nota 1: {} \nnota 2: {}".format(nota1, nota2))
    print("Média: {}".format(media))
elif 0 < media <= 4:
    print("E")
    print("nota 1: {} \nnota 2: {}".format(nota1, nota2))
    print("Média: {}".format(media))
else:
    print("Erro")