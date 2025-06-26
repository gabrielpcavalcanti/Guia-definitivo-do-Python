"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n
linhas do chamado Triangulo de Pascal:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...
 
"""

num: int = int(input("Digite um número inteiro: "))

for linha in range(num):
    valor:int = 1

    for coluna in range(linha + 1):
        print(valor, end=' ')
        valor = valor * (linha - coluna) // (coluna + 1)

    print()  
    