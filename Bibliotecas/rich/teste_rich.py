from time import sleep
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.progress import Progress
from rich.rule import Rule
from rich.markdown import Markdown

console = Console()

# Título
console.print(Panel("[bold cyan]Sistema de Médias Escolares[/bold cyan]", expand=False))

# Entrada de dados
nome = Prompt.ask("Nome do aluno")
qtd = int(Prompt.ask("Quantidade de notas", default="3"))

notas = []

# Barra de progresso
with Progress() as progress:
    tarefa = progress.add_task("[green]Lendo notas...", total=qtd)

    for i in range(qtd):
        nota = float(Prompt.ask(f"Nota {i+1}"))
        notas.append(nota)
        sleep(0.3)
        progress.update(tarefa, advance=1)

# Cálculo
with console.status("[yellow]Calculando média..."):
    sleep(1)
    media = sum(notas) / len(notas)

console.print(Rule())

# Tabela
tabela = Table(title="Boletim")

tabela.add_column("Aluno", style="cyan", justify="center")
tabela.add_column("Notas", justify="center")
tabela.add_column("Média", justify="center")

tabela.add_row(
    nome,
    ", ".join(f"{n:.1f}" for n in notas),
    f"{media:.2f}"
)

console.print(tabela)

# Resultado
if media >= 7:
    resultado = "[bold green]APROVADO ✅[/bold green]"
else:
    resultado = "[bold red]REPROVADO ❌[/bold red]"

console.print(Panel(resultado, title="Resultado Final", expand=False))

# Confirmação
salvar = Confirm.ask("Deseja salvar o resultado?")

if salvar:
    console.print("[green]Resultado salvo com sucesso![/green]")
else:
    console.print("[yellow]Resultado não salvo.[/yellow]")

console.print(Rule())

# Markdown
md = Markdown("""
## Observações
- Média mínima para aprovação: **7.0**
- Sistema desenvolvido em **Python**
- Interface feita com **Rich**
""")

console.print(md)
