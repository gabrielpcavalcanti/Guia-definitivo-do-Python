def area(comprimento,largura):
    print(" Controle de Terrenos ")
    print('-' * 20)
    larg = float(input("LARGURA(m): "))
    comp = float(input("COMPRIMENTO (m): "))
    print(f'A área de um terreno {larg}x{comp} é de {larg * comp}m²')
    

area(1,2)