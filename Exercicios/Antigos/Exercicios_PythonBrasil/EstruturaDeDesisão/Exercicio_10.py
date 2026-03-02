"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

turn = str(input("Qual turno você estuda? \nDigite M para matutino, V para vespertino e N para noturno. \n").upper())

print()

if turn == 'M':
    print("Bom dia")
elif turn == 'V':
    print("Boa tarde")
elif turn == 'N':
    print("Boa noite")
else:
    print("Valor inválido")
