"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
print("Responda com sim ou nao")

print("Telefonou para a vítima? ")
Q1 = str(input().upper())
print("Esteve no local do crime?")
Q2 = str(input().upper())
print("Mora perto da vítima?")
Q3 = str(input().upper())
print("Já trabalhou com a vítima?")
Q4 = str(input().upper())
print("Devia para a vítima?")
Q5 = srt(input().upper())

if Q1 == 'sim' and Q2 == 'sim'or Q1 == 'sim' and Q3 == 'sim' or Q1 == 'sim' and Q4 == 'sim' or Q1 == 'sim' and Q5 == 'sim' or Q2 == 'sim' and Q3 == 'sim'or Q2 == 'sim' and Q4 == 'sim' or Q2 == 'sim' and Q5 == 'sim'or Q3 == 'sim' and Q4 == 'sim'or Q3 == 'sim' and Q5 == 'sim' or Q4 == 'sim' and Q5 == 'sim':
    print("A pessoa é suspeita")


