from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console

cnsl = Console(color_system="256", force_interactive=True)
root_layout = Layout()
root_layout.split_column(
    Layout(name="Upper", ratio=15),
    Layout(name="Lower")
)
root_layout["Upper"].split_column(
    Layout(name="header"),
    Layout(name="main_window")
)

root_layout["Lower"].split_row(
    Layout(name="left"),
    Layout(name="right")
)

cnsl.print(root_layout)