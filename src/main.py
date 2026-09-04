import time
from layout_constructor import root_layout
from rich.live import Live
from rich.console import Console

def main():
    cnsl = Console(color_system="256", force_interactive=True)
    with Live(root_layout,console=cnsl, refresh_per_second=60, screen=True):
        for i in range(20):
            time.sleep(0.4)
            cnsl.print(root_layout)

if __name__ == "__main__":
    main()


