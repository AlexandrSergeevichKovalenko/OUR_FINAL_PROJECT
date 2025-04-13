from time import sleep
from rich.console import Console
from rich.live import Live
from random import choices


console = Console()
animals_emojis = ["🐎", "🦇", "🐇", "🐿️", "🦨", "🐦", "🐫", "🦣", "🐘", "🦒", "🐑", "🐖", "🐄", "🐐", "🧚"]


def display_animals(path_length: int = 40, animals_count: int = 10, animal_spacing: int = 4, speed: int = 40, emojis: list = animals_emojis):
    """
    Display a fixed set of animals moving right to left across the console.
    """
    console.print("Please wait while the magical creatures gather...", style="bold green")

    selected_animals = choices(emojis, k=animals_count)  # вибираємо 10 різних емодзі

    with Live(console=console, refresh_per_second=speed) as live:
        for i in range(path_length, 0, -1):
            line = [" "] * path_length

            for j in range(animals_count):
                pos = i - j * animal_spacing
                if 0 <= pos < path_length:
                    line[pos] = selected_animals[j]

            live.update("".join(line))
            sleep(0.1)