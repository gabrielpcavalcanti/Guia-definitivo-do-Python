def main() -> None:
    minutes: int = int(input("Digite a quantidada de minutos: "))

    horas: int = int(minutes / 60)
    resto_horas: int = minutes % 60

    print(f'{horas} horas e {resto_horas} min')
    
 
if __name__ == '__main__':
    main()