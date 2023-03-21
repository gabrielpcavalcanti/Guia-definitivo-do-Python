"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo
abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""
num_fatorial = int(input("Fatorial de: ")) 
fatorial = num_fatorial
num_1 = 1

lista_num = []

for i in range(num_1 , num_fatorial, 1):
    if num_1 < num_fatorial:
        lista_num.append(i)
    
lista_num.reverse() 

for x in lista_num:
    fatorial = fatorial * x
    
for i in range(num_fatorial - 1):
    print(num_fatorial, end= ' . ')
    num_fatorial -= 1
    
print("1 = ", fatorial)
