"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e 
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno 
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou 
superior a 60 pontos.
"""

grade_01: float = float(input("Digite a primeira nota: "))
grade_02: float = float(input("Digite a segunda nota: "))
grade_03: float = float(input("Digite a terceira nota: "))

media_ponderada: float = (grade_01 + grade_02 + (grade_03 * 2)) / 4

print()

if media_ponderada >= 6:
    print("Você foi aprovado com média {}".format(media_ponderada))

else:
    print("Você foi reprovado com média {}".format(media_ponderada))
