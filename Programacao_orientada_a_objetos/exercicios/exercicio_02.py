"""
Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.
"""

from rich.console import Console
from rich.panel import Panel

class Produto:

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    
    def etiqueta(self) -> None:

        console = Console()

        painel_01 = Panel(f'{self.nome} \n--------------------------\nR$ {self.preco:.^24}', title="Produto", title_align="center", expand=False)

        console.print(painel_01)

        
def main() -> None:
    
    p1 = Produto("iPhone 17 Pro Max", 25_000.85)
    p2 = Produto("Notebook Gamer", 8_000)

    p1.etiqueta()
    p2.etiqueta()
 
 
if __name__ == '__main__':
    main()