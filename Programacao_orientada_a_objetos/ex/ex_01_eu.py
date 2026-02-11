from rich import print

class Funcionario:
    
    def __init__(self, nome:str, setor: str, cargo: str) -> None:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self) -> str:
        return f"Olá, sou [cyan]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo."
        
        
def main() -> None:
    
    c1 = Funcionario(nome = "Maria", setor = "Administração", cargo = "Diretora")
    print(c1.apresentacao())

    c2 = Funcionario(nome = "Pedro", setor = "TI", cargo = "Programador")
    print(c2.apresentacao())

if __name__ == "__main__":
    main()
