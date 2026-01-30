from rich.console import Console

console = Console()

def sum(num1: float, num2: float) -> float:
    return num1 + num2


def subtraction(num1: float, num2: float) -> float:
    return num1 - num2


def multiplication(num1: float, num2: float) -> float:
    return num1 * num2


def division(num1: float, num2: float) -> float:
    return num1 / num2


def main() -> None:
    res: str = console.input("Qual operação vc quer [yellow](soma, sub, mult ou div): [/]")
    num_01: float = float(console.input("Digite o [bold green]primeiro número:  [/]"))
    num_02: float = float(console.input("Digite o [bold green]segundo número:  [/]"))


    match res:

        case "soma":
            console.print(f'A soma de {num_01} e {num_02} é [white]{sum(num_01, num_02)}[/]' )
        
        case "sub":
            console.print(subtraction(num_01, num_02))
        
        case "mult":
            console.print(multiplication(num_01, num_02))
        
        case "div":
            console.print(division(num_01, num_02))
        
        case _:
            print("Valor inválido")
 
 
if __name__ == '__main__':
    main()