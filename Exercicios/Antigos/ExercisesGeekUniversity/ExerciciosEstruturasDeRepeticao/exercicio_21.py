"""
Faça um programa que receba dois números. Calcule e mostre: 
• a soma dos números pares desse intervalo de números, incluindo os números digi- 
tados; 
• a multiplicaçäo dos números impares desse intervalo, incluindo os digitados;
"""

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um número: "))
soma = 0
multi = 1

for i in range(num_1, num_2 + 1):
    if i % 2 == 0:
        soma += i
    else:
        multi *= i

print("A soma dos numeros pares do intervalo é {}".format(soma))
print("A multiplicação dos numeros ímpares do intervalo é {}".format(multi))

