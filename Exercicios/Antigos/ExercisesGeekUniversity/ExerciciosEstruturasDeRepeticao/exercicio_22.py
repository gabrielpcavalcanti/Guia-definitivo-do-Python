"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, 
uma sequéncia arbitråria de notas (vålidas no intervalo de 10 a 20) e que mostre na tela, 
como resultado, a correspondente média aritmética. O número de notas com que o aluno 
pretenda efetuar o cálculo não sera fornecido ao programa, o qual terminará quando for 
introduzido um valor que näo seja vålido como nota de aprovaqäo.
"""

c = 1
soma = 0
media = 0

while True:
    num = int(input("Digite um número: "))
    if num >=10 and num <= 20:
        soma += num
        media = soma / c
        c += 1
        continue
    else:
        break

print("A média das notas digitadas é {:.2f}".format(media))
