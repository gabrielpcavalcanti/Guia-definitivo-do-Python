"""
a) A nota final de um estudante é calculada a partir de três notas (de 0 a 10), respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verticações necessárias.
"""

grade_work_lab: float = float(input("Digite a nota do trabalho no laboratório: "))
grade__semester_avaliation: float = float(input("Digite a nota da avaliação semestral: "))
grade_final_exam: float = float(input("Digite a nota da avaliação final: ")
                                )
mean_grade: float = (2 * grade_work_lab + 3 * grade__semester_avaliation + 5 * grade_final_exam) / 10

if 0 <= mean_grade <= 2.9:
    print()
    print("Você está reprovado.")

elif 3 <= mean_grade <= 4.9:
    print()
    print("Você está de recuperação.")

elif mean_grade >= 5:
    print()
    print("Aprovado.")

else:
    print("Erro.")
