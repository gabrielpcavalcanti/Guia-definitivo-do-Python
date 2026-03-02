"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo 
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguin- 
tes conceitos: 
• O comprimento de cada lado de um triângulo é menor do que a soma dos outros 
dois lados. 
• Chama-se equilátero o triângulo que tem três lados iguais. 
• Denominam-se isósceles o triângulo que tem comprimento de dois lados iguais. 
• Recebe o nome de escaleno o triângulo que tem os três lados diferentes. 
"""

lado_a = float(input("Digite o valor do lado A do triângulo: "))
lado_b = float(input("Digite o valor do lado B do triângulo: "))
lado_c = float(input("Digite o valor do lado C do triângulo: "))

soma_ab = lado_a + lado_b
soma_ac = lado_a + lado_c
soma_bc = lado_b + lado_c

if lado_a < soma_bc and lado_b < soma_ac and lado_c < soma_ab:

    if lado_a == lado_b == lado_c:
        print()
        print("É um triângulo equilátero")
    
    if (lado_a == lado_b != lado_c) or (lado_a == lado_c != lado_b) or (lado_b == lado_c != lado_a):
        print()
        print("É um triângulo isóceles")
    
    if lado_a != lado_b != lado_c and lado_b != lado_c != lado_a and lado_c != lado_b != lado_a:
        print()
        print("É um triângulo escaleno")

else:
    print()
    print("Não é um triângulo")

