    case "a":

            print()
            print(f'A média geométrica é: {geometric_mean(number_01, number_02, number_03):.2f}.')
        
        case "b":

            print()
            print(f'A média ponderada é: {weighted_mean(number_01, number_02, number_03):.2f}.')
        
        case "c":

            print()
            print(f'A média harmônica é: {harmonic_mean(number_01, number_02, number_03):.2f}.')
        
        case "d":

            print()
            print(f'A média aritimética é: {aritimetic_mean(number_01, number_02, number_03):.2f}.')

        case _:
            print()
            print("Erro.")