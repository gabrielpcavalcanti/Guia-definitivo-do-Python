"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo.
"""

def p_ou_n(n):
    if n > 0:
        return 'P'
    return 'N'


print(p_ou_n(5)) 
print(p_ou_n(0))
print(p_ou_n(-9)) 

