"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

while True:

    quant_pessoas = int(input("Digite a quantidade de pessoas: "))

    pessoas_lista = []

    for i in range(quant_pessoas):
        idade = float(input("Digite a idade das pessoas: "))
        pessoas_lista.append(idade)

    media = sum(pessoas_lista) / quant_pessoas

    if 0 <= media <= 25:
        print("Turma jovem.")

    elif 26 <= media <= 60:
        print("Turma adulta.")

    elif media > 60:
        print("Turma idosa.")
    
    break