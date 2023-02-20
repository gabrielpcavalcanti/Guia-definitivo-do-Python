"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""

num = int(input("Digite um número inteiro: "))

for i in range(1, num + 1):
    if i % 11 == 0:
        print(f'múltiplo de 11: {i}')
        break
    else:
        continue
    
for i in range(1, num + 1):
    if i % 13 == 0:
        print(f'múltiplo de 13: {i}')
        break
    else:
        continue

for i in range(1, num + 1):
    if i % 17 == 0:
        print(f'múltiplo de 17: {i}')
        break
    else:
        continue
    