"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação esco- 
lhida. Escreva uma mensagem de erro se a opção for inválida. 
Escolha a opção: 
1— Soma de 2 números,
2— Diferença entre 2 números (maior pelo menor), 
3— Produto entre 2 números,
4— Divisão entre 2 números (o denominador não pode ser zero). 
Opção 

"""

print("Escolha uma opção abaixo (digite o número): ")
print("1— Soma de 2 números, \n2— Diferença entre 2 números (maior pelo menor), \n3— Produto entre 2 números,") 
print("4— Divisão entre 2 números (o denominador não pode ser zero).")

opcao = input("->")

if opcao == "1":
    print()
    num_1 = float(input("digite um número: "))
    num_2 = float(input("digite outro número: "))
    print(f"soma: {num_1 + num_2}")

elif opcao == "2":
    num_1 = float(input("digite um número: "))
    num_2 = float(input("digite outro número: "))

    if num_1 > num_2:

        print(f"a diferença é: {num_1 - num_2}")
    else:
        print(f"a diferença é: {num_2 - num_1}")

elif opcao == "3":
    num_1 = float(input("digite um número: "))
    num_2 = float(input("digite outro número: "))
    print(f"o produto: {num_1 * num_2}")

elif opcao == "4":
    num_1 = float(input("digite um número: "))
    num_2 = float(input("digite outro número: "))
    print(f"o quociente: {num_1 / num_2}")

else:
    print("Opção inválida")

