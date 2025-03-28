"""b) Faça um programa que ler quatro notas de um aluno e mostre a média deles. Arredonde o resultado para duas casas decimais."""

grade_01: float = float(input("Digite a nota da primeira prova: "))
grade_02: float = float(input("Digite a nota da segunda prova: "))
grade_03: float = float(input("Digite a nota da terceira prova: "))
grade_04: float = float(input("Digite a nota da quarta prova: "))

average_grade: float = (grade_01 + grade_02 + grade_03 + grade_04) / 4

print(f'A média das notas foi: {average_grade:.2f}.')
