from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from const import money, game_box

def header_construct() -> Table:
    #content
    formatted_money = Text(
        text=str(money),
        style="Bold White",
        justify="center"
    )
    formatted_title = Text(
        text="gametitle", 
        style="white", 
        justify="left"
    )

    #panels
    money_bar = Panel(
        renderable=formatted_money, 
        box=game_box, border_style="bold green", 
        title="Money", 
        style="white"
    )
    spacer = Panel(
        renderable="", 
        box=game_box, 
        border_style="dim white"
    )
    title_bar = Panel(
        renderable=formatted_title, 
        box=game_box, 
        border_style="bold"
    )

    #grid
    header_grid = Table.grid(expand=True)
    header_grid.add_column(ratio=1, justify="left")
    header_grid.add_column(ratio=1, justify="center")
    header_grid.add_column(ratio=1, justify="right")
    header_grid.add_row(money_bar, spacer, title_bar)
    return header_grid

def footer_construct() -> None:
    pass # To be implemented