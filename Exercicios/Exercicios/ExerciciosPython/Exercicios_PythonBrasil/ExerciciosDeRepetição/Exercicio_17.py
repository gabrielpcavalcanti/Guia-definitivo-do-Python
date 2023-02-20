"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

while True:

    num_fatorial = int(input("Digite o núemero que você queira saber o fatorial: "))
    num = num_fatorial

    if num_fatorial <=0:
        print("Erro. Digite um número maior do que zero.")
        print()
        continue
    
    fatorial = 1

    for i in range(num_fatorial + 1):
        fatorial = fatorial * num_fatorial
        num_fatorial -=1 
        
        if num_fatorial == 0:
            print(f"O fatorial de {num}! do número é: {fatorial}")
            print()
            
        
