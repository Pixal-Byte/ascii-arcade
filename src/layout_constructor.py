from rich.panel import Panel
from rich.layout import Layout
from panels import header_construct, footer_construct


root_layout = Layout()
root_layout.split_column(
    Layout(name="Upper", ratio=16),
    Layout(name="Lower", renderable=footer_construct())
)
root_layout["Upper"].split_column(
    Layout(renderable=header_construct(),name="header"),
    Layout(name="main_window", ratio=15)
)