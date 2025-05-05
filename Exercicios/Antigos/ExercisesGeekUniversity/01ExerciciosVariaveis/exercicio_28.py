"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos. 
"""

num = float(input("Digite um número: "))
num_2 = float(input("Digite um número: "))
num_3 = float(input("Digite um número: "))

square_num = num ** 2
square_num_2 = num_2 ** 2
square_num_3 = num_3 ** 2

sum_squares = square_num + square_num_2 + square_num_3

print("A soma dos quadrados dos três valores lidos é {:.2f}".format(sum_squares))
