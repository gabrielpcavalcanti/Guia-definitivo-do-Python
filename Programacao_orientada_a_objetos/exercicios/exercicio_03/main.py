from rich.console import Console
from rich.panel import Panel

console = Console()

class Churrasco:

    CONSUMO_PADRAO: int = 400
    PRECO_CARNE: float = 82.40

    def __init__(self, titulo: str, quant: int) -> None:
        self.titulo = titulo
        self.quant = quant


    def kg_por_pessoa(self) -> float:
        return self.CONSUMO_PADRAO / 1000


    def total_kg(self) -> float:
        return self.quant * self.kg_por_pessoa()


    def custo_total(self) -> float:
        return self.total_kg() * self.PRECO_CARNE


    def custo_por_pessoa(self) -> float:
        return self.custo_total() / self.quant if self.quant > 0 else 0


    def analisar(self) -> None:
        conteudo = f"""
            Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]

            Cada participante comerá {self.kg_por_pessoa:.3f} kg
            Cada kg custa R$ {self.PRECO_CARNE:.2f}

            Recomendo comprar [bold]{self.total_kg:.1f} kg[/] de carne
            O custo total será de [green]R$ {self.custo_total:.2f}[/]
            Cada pessoa pagará [yellow]R$ {self.custo_por_pessoa:.2f}[/] para participar.
            """.strip()

        painel = Panel(
            conteudo,
            title=self.titulo,
            expand=False,
        )

        console.print(painel)

        console.print(painel)


c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()
