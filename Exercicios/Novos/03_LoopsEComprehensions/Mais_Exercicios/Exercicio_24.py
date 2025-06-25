"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
número do aluno e o segundo representando a sua altura em metros. Encontre o aluno
mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais alto, juntamente
com suas alturas.
"""

student_number: list[int] = []
hight: list[float] = []

print("Digite os valores dos números dos estudantes: \n")

for _ in range(5):
    value_01: int = int(input("Digite um valor inteiro: "))

    student_number.append(value_01)

print()
print("Digite os valores das alturas dos estudantes: \n")

for _ in range(5):
    value: float = float(input("Digite um valor inteiro: "))

    hight.append(value)

print()

print(f'O aluno mais baixo é o número {student_number[hight.index(min(hight))]} e com altura {min(hight)}')
print(f'O aluno mais alto é o número {student_number[hight.index(max(hight))]} e com altura {max(hight)}')
