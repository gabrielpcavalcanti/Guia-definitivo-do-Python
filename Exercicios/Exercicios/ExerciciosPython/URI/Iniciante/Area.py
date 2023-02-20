"""
A = float(input())
B = float(input())
C = float(input())
pi = 3.14159

TRIANGULO = (A * C)/2
CIRCULO = pi * C**2
TRAPEZIO = ((A + B) * C)/2
QUADRADO = B**2
RETANGULO = A * B

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f"
      % (TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO))


"""
valor = input().split(" ")
a, b, c = valor
pi = 3.14159
triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)
print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))

