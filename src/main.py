from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

cnsl = Console()

def set_renderable(panel: Panel, new_value: str) -> Panel:
    panel.renderable = new_value
    return panel

def main():
    status_panel = Panel("random text", title="more random text")
    cnsl.print(status_panel)
    cnsl.print(set_renderable(status_panel, "more text"))

if __name__ == "__main__":
    main()