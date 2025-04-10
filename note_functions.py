from classes_for_program import *
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from colorama import Fore

console = Console()

def add_note(book):
    """
    Add a new note to the notebook.
    Prompts for title, note content, and optional tags.
    If a note with the same title exists, prompts to replace it.
    """
    while True:
        title = input(f"{"✨"} Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return "Back to main menu."
        elif title:
            note = input(f"{"📜"} Enter a note:")
            tags = input(f"{"🏷️"} Enter a tags or (n):")
            if tags != "n":
                tags = tags.split(",")
                tags = [tag.strip() for tag in tags]
            else:
                tags = None

            record = book.find(title)
            if record is None:
                record = Note(title)
                record.add_note(note)
                if tags:
                    record.add_tags(tags)
                book.add_record(record)
                return "Note added."
            else:
                while True:
                    print("A note with this name already exists, do you want to replace it? (y/n)")
                    answer = input()
                    if answer == "y":
                        record.add_note(note)
                        if tags:
                            record.add_tags(note)
                        return "Note changed."
                    elif answer == "n":
                        return "Note not changed."
        print("Title cannot be empty. Please try again.")

def change_note(book):
    """
    Change the content of an existing note.
    Offers to edit the content of the note..
    If the note exists, updates its content and returns a success message.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input(f"{"✨"} Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return "Back to main menu."
        elif title:
            record = book.find(title)
            if record:
                note = input(f"{"📜"} Enter a new note:")
                record.add_note(note)
                return "Note changed."
            return "Note not found."
        print("Please enter a title.")

def show_note(book):
    """
    Display the content of a specific note.
    If the note exists, returns its content.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input(f"{"✨"} Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return "Back to main menu."
        elif title:
            record = book.find(title)
            return f"{"📜"} {record.note}" if record else "Note not found."
        print("Please enter a title.")

def show_all_notes(book):
    """
    Display all notes in the notebook.
    If the notebook is empty, returns a message indicating so.
    """
    return book if book else "NoteBook is empty"

def remove_note(book):
    """
    Remove a note from the notebook.
    If the note exists, deletes it and returns a success message.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input(f"{"✨"} Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return "Back to main menu."
        elif title:
            record = book.find(title)
            if record:
                book.delete(title)
                return "Note removed."
            return "Note not found."
        print("Please enter a title.")

def sorted_notes_by_tags(book):
    """
    Sort notes by tags.
    If the notebook is empty, returns a message indicating so.
    If the notebook is not empty, sort the notes by tags and returns them.
    """
    if book:
        sorted_note = book.sorted_notes_by_tags()
        panels = [
            Panel(
                Text(str(note), style="bold dark_blue", no_wrap=True),
                style="on light_green",
                border_style="dark_green",
                expand=False)  for note in sorted_note]
        print("--" * 40)
        console.print(Text("Notes sorted by tags", style="bold dark_blue"))
        for panel in panels:
            console.print(panel)
            print()
        print("--" * 40)
    else:
        print(f"{Fore.RED}NoteBook is empty{Fore.RESET}")