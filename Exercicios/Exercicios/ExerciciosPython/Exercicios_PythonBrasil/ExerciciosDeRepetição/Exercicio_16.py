"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
"""
fibo_primeiro = 1
fibo_segundo = 1

cout = 1

while cout <= 501:
    fibo_terceiro = fibo_primeiro + fibo_segundo
    fibo_primeiro = fibo_segundo 
    fibo_segundo = fibo_terceiro 
    print(fibo_terceiro)
    cout += 1