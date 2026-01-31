""" 
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira 
vez deve usar a estrutura de repetição for, a segunda while.
"""

for num in range(1, 101):
    print(num)

print()

count: int = 1

while count <= 100:

    print(count)
    count += 1
