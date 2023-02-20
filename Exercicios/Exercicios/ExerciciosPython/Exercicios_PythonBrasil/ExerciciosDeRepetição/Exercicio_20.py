"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""

while True:

    num_fatorial = int(input("Digite o número que você queira saber o fatorial: "))
    num = num_fatorial
    print()
    
    if num_fatorial == 99:
        break

    if num_fatorial <=0 or num_fatorial >= 16:
        print("Erro. Digite um número maior do que zero e menor do que 17.")
        print()
        continue
    
    fatorial = 1

    for i in range(num_fatorial + 1):
        fatorial = fatorial * num_fatorial
        num_fatorial -=1 
        
        if num_fatorial == 0:
            print(f"O fatorial de {num}! do número é: {fatorial}")
            print()
            print("Para sair digite 99")
    