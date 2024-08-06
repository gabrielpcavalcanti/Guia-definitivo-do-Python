import os

carros = {'Chevrolet Tracker': 120, 'Chevrolet Onix': 90, 'Chevrolet Spin': 150, 'Hyundai HB20': 85, 
          'Hyundai Tucson': 120, 'Fiat Uno': 60, 'Fiat Mobi': 70, 'fiat Pulse': 130}


def main():
    
    print("========")
    print("Bem-vindos a locadora de carros!")
    print("========")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")

    mostrar_portifolio()


def mostrar_portifolio():

    c = 0

    for i in carros:
        print(f'[{c}] {i} - R$ {carros[i]} /dia')
        c += 1
    
    print("\n\n========")
    print("0 - CONTINUAR | 1 - SAIR")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')


main()