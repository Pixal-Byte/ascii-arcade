import time
from layout_constructor import root_layout
from rich.live import Live
from rich.console import Console

def main():
    cnsl = Console(color_system="256", force_terminal=True)
    with Live(root_layout, console=cnsl, screen=True, refresh_per_second=24) as live:
        loop_ctrl: bool = True
        while loop_ctrl:
            try:
                time.sleep(0.2)
            except KeyboardInterrupt:
                loop_ctrl = False

if __name__ == "__main__":
    main()


