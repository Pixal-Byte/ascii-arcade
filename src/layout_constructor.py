from rich.panel import Panel
from rich.layout import Layout
from panels import header_construct


root_layout = Layout()
root_layout.split_column(
    Layout(name="Upper", ratio=15),
    Layout(name="Lower")
)
root_layout["Upper"].split_column(
    Layout(renderable=header_construct(),name="header"),
    Layout(name="main_window", ratio=10)
)

root_layout["Lower"].split_row(
    Layout(name="left"),
    Layout(name="right")
)