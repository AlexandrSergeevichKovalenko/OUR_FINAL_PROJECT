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
        title = input(f"✨ Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return f"{Fore.YELLOW}Back to main menu.{Fore.YELLOW}"
        elif title:
            note = input(f"📜 Enter a note:")
            tags = input(f"🏷️ Enter a tags or (n):")
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
                return f"{Fore.GREEN}Note added.{Fore.RESET}"
            else:
                while True:
                    print(f"{Fore.YELLOW}A note with this name already exists, do you want to replace it? (y/n){Fore.RESET}")
                    answer = input().lover()
                    if answer == "y":
                        record.add_note(note)
                        if tags:
                            record.add_tags(tags)
                        return f"{Fore.GREEN}Note changed.{Fore.RESET}"
                    elif answer == "n":
                        return f"{Fore.YELLOW}Note not changed.{Fore.RESET}"
        print(f"{Fore.YELLOW}Title cannot be empty. Please try again.{Fore.RESET}")

def change_note(book):
    """
    Change the content of an existing note.
    Offers to edit the content of the note..
    If the note exists, updates its content and returns a success message.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input(f"✨ Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return f"{Fore.YELLOW}Back to main menu.{Fore.RESET}"
        elif title:
            record = book.find(title)
            if record:
                note = input(f"📜 Enter a new note:")
                record.add_note(note)
                return f"{Fore.GREEN}Note changed.{Fore.RESET}"
            return f"{Fore.YELLOW}Note not found.{Fore.RESET}"
        print(f"{Fore.YELLOW}Please enter a title.{Fore.RESET}")

def show_note(book):
    """
    Display the content of a specific note.
    If the note exists, returns its content.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input(f"✨ Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return f"{Fore.YELLOW}Back to main menu.{Fore.RESET}"
        elif title:
            record = book.find(title)
            return f"📜 {record.note}" if record else f"{Fore.YELLOW}Note not found.{Fore.RESET}"
        print(f"{Fore.YELLOW}Please enter a title.{Fore.RESET}")

def show_all_notes(book):
    """
    Display all notes in the notebook.
    If the notebook is empty, returns a message indicating so.
    """
    return book if book else f"{Fore.YELLOW}NoteBook is empty.{Fore.RESET}"

def remove_note(book):
    """
    Remove a note from the notebook.
    If the note exists, deletes it and returns a success message.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input(f"✨ Enter a title or (back) to return to the main menu:").lower()
        if title == "back":
            return f"{Fore.YELLOW}Back to main menu.{Fore.RESET}"
        elif title:
            record = book.find(title)
            if record:
                book.delete(title)
                return f"{Fore.GREEN}Note removed.{Fore.RESET}"
            return f"{Fore.YELLOW}Note not found.{Fore.RESET}"
        print("Please enter a title.")

def search_note(command):
    """
    Sort notes by tags or search for a specific word in the notes by title, note, tags.
    If the notebook is empty, returns a message indicating so.
    If the notebook is not empty, sort the notes by tags and returns them.
    """
    def inner(book):
        if book:
            if command == "search":
                word = input(f"🔍 Enter a word to search for:").lower()

            STR = {
                "sorted": lambda : book.sorted_notes_by_tags()
                ,"search": lambda : book.search_notes(word)
            }   

            sorted_note = STR[command]()
            if sorted_note:
                panels = [
                    Panel(
                        Text(str(note), style="bold dark_blue", no_wrap=True),
                        border_style="dark_green",
                        expand=False)  for note in sorted_note]
                print("--" * 50)
                for panel in panels:
                    console.print(panel)
                    print()
                print("--" * 50)
            else:
                print(f"{Fore.YELLOW}No notes found with that title, tag or note.{Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}NoteBook is empty{Fore.RESET}")
    return inner