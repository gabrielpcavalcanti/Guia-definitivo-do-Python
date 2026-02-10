from rich import print
from rich import inspect

class Funcionario:
    
    empresa: str = "Curso em Vídeo"
    
    def __init__(self, nome:str, setor: str, cargo: str) -> None:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}."


def main() -> None:
    
    c1 = Funcionario(nome = "Maria", setor = "Administração", cargo = "Diretora")
    print(c1.apresentacao())

    c2 = Funcionario(nome = "Pedro", setor = "TI", cargo = "Programador")
    print(c2.apresentacao())

    #inspect(c1, methods=True)
    #inspect(c2, methods=True, dunder=True)
    
if __name__ == "__main__":
    main()
