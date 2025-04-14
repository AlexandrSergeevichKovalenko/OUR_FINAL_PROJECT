from time import sleep
from rich.console import Console
from rich.live import Live


console = Console()


def magic_animation(name_emoji: str = "Fairy", path_length: int = 30, speed: int = 20, emoji_right = "🧚", emoji_left = "💻", emoji_moving = "🌟", reverse = False):
    """
    Display a fairy sending magic from right to left across the console.
    """
    if reverse:
         console.print(f"Please wait while the {name_emoji} sets the information...", style="bold green")
    else:
         console.print(f"Please wait while the {name_emoji} receives the information...", style="bold green")
         
    with Live(console=console, refresh_per_second=60) as live:
        for i in range(path_length):
            line = [" "] * path_length   
            line[0] = emoji_left
            line[-1] = emoji_right              
            if reverse:
                if 0 < path_length - i - 1 < path_length - 1:
                    line[path_length - i - 1] = emoji_moving 
            else:
                if 0 < i < path_length - 1:
                    line[i] = emoji_moving 

            live.update("".join(line))
            sleep(1/speed)