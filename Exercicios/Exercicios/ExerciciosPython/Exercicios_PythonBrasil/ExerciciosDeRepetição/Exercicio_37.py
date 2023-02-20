"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes.
"""

while True:

    lista_altura = []
    lista_peso = []
    lista_codigo = []
    codigo = -55

    while codigo != 0:     
        codigo = int(input("Digite seu código: "))
        lista_codigo.append(codigo)
        if codigo != 0:
            altura = int(input("Digite sua altura em cm: "))
            peso = float(input("Digite seu peso em Kg: "))
            lista_altura.append(altura)
            lista_peso.append(peso)
        else:
            continue
    
    max_altura = max(lista_altura)
    max_altura_index = lista_altura.index(max_altura)

    min_altura = min(lista_altura)
    min_altura_index = lista_altura.index(min_altura)

    max_peso = max(lista_peso)
    max_peso_index = lista_altura.index(max_peso)
    
    min_peso = min(lista_peso)
    min_peso_index = lista_altura.index(min_peso)

    print(f"O cliente mais alto é {lista_codigo[max_altura_index]} com altura {max_altura}, o mais baixo é {lista_codigo[min_altura_index]} "
          f"com altura {min_altura}," 
          f"o mais gordo é o cliente {lista_codigo[max_peso_index]} com peso de {max_peso} kg e o mais magro é {lista_codigo[min_peso_index]} "
          f"com peso de {min_peso} kg")
