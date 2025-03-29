"""a) Calcule a área do quadrado, triângulo e trapézio e mostre os resultados na tela."""

# Área do quadrado
square_side: float = float(input("Digite o lado do quadrado: "))

square_area: float = square_side ** 2

print(f'A área do quadrado é {square_area:.2f}')


# Área do triângulo
triangle_side: float = float(input("Digite o lado do trinagulo: "))
triangle_hight: float = float(input("Digite a altura do trinagulo: "))

triangle_area: float = (triangle_side * triangle_hight) / 2

print(f'A área do triangulo é {triangle_area:.2f}')

# Área do trapézio
trapeze_bigger_base: float = float(input("Digite o lado da base maior do trapezio: "))
trapeze_smaller_base: float = float(input("Digite o lado da base menor do trapezio: "))
trapeze_hight: float = float(input("Digite a altura do trapézio: "))

trapeze_area: float = ((trapeze_bigger_base + trapeze_smaller_base) * trapeze_hight) / 2

print(f'A área do trapézio o é {trapeze_area:.2f}')
