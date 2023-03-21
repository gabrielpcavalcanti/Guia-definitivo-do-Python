"""
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

while True:

    quant_turmas = int(input("Digite a quantidade de turmas: "))

    lista_quant_alunos = []

    while len(lista_quant_alunos) < quant_turmas:

        quant_alunos = int(input("Digite um número: "))
        lista_quant_alunos.append(quant_alunos)

        if quant_alunos > 40:
            print("A turma não pode ter mais que 40 alunos.")
            lista_quant_alunos.pop()
            continue
        
    print(f"A média de alunos por turma é: {sum(lista_quant_alunos) / quant_turmas}")
