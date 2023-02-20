"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a 
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá ao valor 
8 (2 + 5 + 1). Se o número lido não for maior que zero, o programa terminará com a 
mensagem "Número inválido".
"""

# Esse exercicio não é possivel de ser feito com os conhecimentos abordados até agora (pelo menos eu não consegui). 
# No caso, variáveis e estruturas condicionais. mas caso queira ver a solução, está ai.

num = int(input("Digite um número inteiro: "))

lista_algarismos = list(str(num))

tamanho_num = len(lista_algarismos) - 1

soma = 0

for i in range(tamanho_num):
    operecao = num // (10 ** tamanho_num)
    soma += operecao
    num = num - (int(lista_algarismos[i])  *  (10 ** tamanho_num))
    tamanho_num -= 1
    
    if tamanho_num == 0:
        soma = soma + num

print(soma)
