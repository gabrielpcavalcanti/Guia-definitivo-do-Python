"""
Faça programas para calcular as seguintes sequéncias: 
1 + 2 + 3 + 4 + ... + n
1 - 2 + 3 - 4 + ... + (2n - 1) 
1 + 3 + 5 + 7 + ... + (2n - 1)
"""

# Sequência 1

num = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, num + 1):
    soma += i

print(soma)

# Sequência 2

num_1 = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, num_1 + 1):
    if i % 2 != 0:
        soma += i
        continue
    elif i % 2 == 0:
        soma -= i
        continue
    else:
        continue

print(soma)

# Sequência 3

num_2 = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, (2 * num_2 - 1) + 1):
    if i % 2 != 0:
        soma += i
        continue
    else:
        continue

print(soma)
