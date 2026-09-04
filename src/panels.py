from rich.panel import Panel
from rich.table import Table
from const import money, game_box

def header_construct() -> Table:
    money_bar = Panel(renderable=str(money), box=game_box, border_style="bold green", title="Money")
    spacer = Panel(renderable="", box=game_box, border_style="dim")
    title_bar = Panel(renderable="gametitle", box=game_box, border_style="bold")

    header_grid = Table.grid(expand=True)
    header_grid.add_column(ratio=1, justify="left")
    header_grid.add_column(ratio=1, justify="center")
    header_grid.add_column(ratio=1, justify="right")
    header_grid.add_row(money_bar, spacer, title_bar)
    return header_grid