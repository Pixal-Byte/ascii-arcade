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

def footer_construct() -> Table:
    # Content
    formatted_action_prompts = Text()
    formatted_game_state = Text()
    formatted_message_log = Text()
    
    #panels
    prompt_bar = Panel(
        renderable=formatted_action_prompts,
        box=game_box, 
        style="white",
        subtitle="GAME CTRL",
        subtitle_align="right"
    )
    log_bar = Panel(
        formatted_message_log,
        box=game_box,
        style="bold cyan",
        subtitle="STATUS MSG",
        subtitle_align="center"
    )
    state_bar = Panel(
        renderable=formatted_game_state,
        box=game_box,
        style="bold blue",
        subtitle="STATUS",
        subtitle_align="left"
    )

    #grid
    footer_grid = Table.grid(expand=True)
    footer_grid.add_column(ratio=1, justify="left")
    footer_grid.add_column(ratio=2, justify="center")
    footer_grid.add_column(ratio=1, justify="right")
    footer_grid.add_row(prompt_bar, log_bar, state_bar)
    return footer_grid