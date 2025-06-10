"""
Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os 
múltiplos de um número inteiro x num vetor e mostre-os na tela. 
"""

vector: list[int] = []

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector.append(value)

number: int = int(input("Digite um número: "))

multiples: list = list(filter(lambda x: x % number == 0, vector))
multiples.sort()

if multiples:
    print(f'Os multiplos do número {number} são {multiples}')
else:
    print(f'Não existem do número {number} na lista analisada.')
