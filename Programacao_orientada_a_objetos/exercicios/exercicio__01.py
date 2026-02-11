"""
Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.
"""

from rich import print

class Funcionario:

    def __init__(self, nome: str = "", setor: str = "", cargo: str = "") -> None:
        self.nome: str = nome
        self.setor = setor
        self.cargo = cargo
    

    def apresentacao(self) -> str:

        return f' :open_hands: Olá, meu nome é [cyan]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo.'


def main() -> None:
    
    c1 = Funcionario("Maria", "Administração", "Diretora")
    print(c1.apresentacao())

    c2 = Funcionario("Pedro", "TI", "Programador")
    print(c2.apresentacao())
 

if __name__ == '__main__':
    main()