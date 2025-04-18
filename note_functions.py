from classes_for_program import Note
from rich.console import Console
from rich.panel import Panel
from animation import magic_animation


console = Console()


def add_note(book: Note):
    """
    Add a new note to the notebook.
    Prompts for title, note content, and optional tags.
    If a note with the same title exists, prompts to replace it.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ")
        if title == "back":
            return f"[bold red]Back to main menu.[/]"
        elif title:
            note = input("📜 Enter a note: ")
            tags = input("🏷️ Enter tags or (n): ")

            if tags != "n":
                tags = tags.split(",")
                tags = [tag.strip() for tag in tags]
            else:
                tags = None

            record = book.find(title)
            if record is None:
                magic_animation(reverse = True)
                console.clear()
                record = Note(title)
                record.add_note(note)
                if tags:
                    record.add_tags(tags)
                book.add_record(record)
                result = book.find(title)
                return Panel.fit(
                    f"{result}",
                    title=f"[bold green]Note added.[/]",
                    border_style="blue",
                )
            else:
                while True:
                    print("A note with this name already exists, do you want to replace it? (y/n)")
                    answer = input().strip().lower()
                    if answer == "y":
                        magic_animation(reverse = True)
                        console.clear()
                        record.add_note(note)
                        if tags:
                            record.add_tags(tags)
                        return f"[bold green]Note changed.[/]"
                    elif answer == "n":
                        return f"[bold red]Note not changed.[/]"
        print("Title cannot be empty. Please try again.")


def change_note(book: Note):
    """
    Change the content of an existing note.
    Offers to edit the content of the note.
    If the note exists, updates its content and returns a success message.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ")
        if title == "back":
            console.print(f"[bold red]Back to main menu.[/]")
            break
        elif title:
            record = book.find(title)
            if record:
                console.print(Panel.fit(f"{record}", title="Current note", border_style="blue"))
                note = input("📜 Enter a new note: ")
                record.add_note(note)
                magic_animation(reverse = True)
                console.clear()
                console.print(Panel.fit(f"{record}", title="Note changed", border_style="blue"))
                return
            console.print(f"[bold red]Note not found.[/]")
            return
        print("Please enter a title.")


def show_note(book: Note) -> str: 
    """
    Display the content of a specific note.
    If the note exists, returns its content.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ")
        if title == "back":
            return f"[bold red]Back to main menu.[/]"
        elif title:
            record = book.find(title)
            magic_animation(reverse = False)
            console.clear()
            if record:
                return Panel.fit(f"{record}", title=title, border_style="blue")
            else:
                return f"[bold red]Note not found.[/]"
        print("Please enter a title.")


def remove_note(book):
    """
    Remove a note from the notebook.
    If 'title' is provided, it is used directly; otherwise, the user is prompted.
    """
    while True:
        title = input("✨ Enter a title to remove or (back) to return to the main menu: ")
        if title:
            if title == "back":
                return f"[bold red]Back to main menu.[/]"
            record = book.find(title)
            if record:
                book.delete(title)
                magic_animation(reverse = True)
                console.clear()
                return f"[bold green]Note removed.[/]"
            else:
                return f"[bold red]Note not found.[/]"
        console.print("Title cannot be empty.", style="bold red")


def search_note(command: str) -> callable:
    """
    Sort notes by tags or search for a specific word in the notes by title, note, tags.
    If the notebook is empty, returns a message indicating so.
    If the notebook is not empty, sorts the notes by tags and displays them.
    """
    COMMANDS = {
        "search-notes" : lambda: input("🔍 Enter words to search for or (back):")
        ,"search-by-tags-and-sort-by-title" : lambda: input("🏷️ Enter tags to sort by or (back):")
    }


    def inner(book: Note) -> str:
        if book:
            while True:
                input_text = COMMANDS[command]()
                if input_text:
                    STR = {
                    "search-by-tags-and-sort-by-title": lambda : book.search_by_tags_and_sort_by_title(input_text)
                    ,"search-notes": lambda : book.search_notes(input_text)
                    }  
                    if input_text == "back":
                        return "back"
                    sorted_notes = STR[command]()
                    if sorted_notes:
                        return sorted_notes
                    else:
                        return None
                console.print(f"[bold yellow]Please enter a tag or word.[/]")
        else:
            return None
    return inner