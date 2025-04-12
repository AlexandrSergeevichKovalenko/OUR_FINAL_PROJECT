from classes_for_program import *
from rich.panel import Panel
from rich.text import Text
from rich.console import Console

console = Console()

def add_note(book):
    """
    Add a new note to the notebook.
    Prompts for title, note content, and optional tags.
    If a note with the same title exists, prompts to replace it.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ").strip().lower()
        if title == "back":
            return "Back to main menu"
        elif title:
            note = input("📜 Enter a note: ").strip().lower()
            tags = input("🏷️ Enter tags or (n): ").strip().lower()

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
                    answer = input().strip().lower()
                    if answer == "y":
                        record.add_note(note)
                        if tags:
                            record.add_tags(tags)
                        return "Note changed."
                    elif answer == "n":
                        return "Note not changed."
        print("Title cannot be empty. Please try again.")

def change_note(book):
    """
    Change the content of an existing note.
    Offers to edit the content of the note.
    If the note exists, updates its content and returns a success message.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ").strip().lower()
        if title == "back":
            return "Back to main menu."
        elif title:
            record = book.find(title)
            if record:
                note = input("📜 Enter a new note: ").strip().lower()
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
        title = input("✨ Enter a title or (back) to return to the main menu: ").strip().lower()
        if title == "back":
            return "Back to main menu."
        elif title:
            record = book.find(title)
            return f"📜 {record.note}" if record else "Note not found."
        print("Please enter a title.")

def show_all_notes(book):
    """
    Display all notes in the notebook.
    If the notebook is empty, returns a message indicating so.
    """
    return str(book) if book else "NoteBook is empty"

def remove_note(book, title=None):
    """
    Remove a note from the notebook.
    If 'title' is provided, it is used directly; otherwise, the user is prompted.
    """
    if title is None:
        title = input("✨ Enter a title to remove (or type 'cancel' to return to the main menu): ").strip().lower()
    if title == "cancel":
        return "Back to main menu."
    if not title:
        return "Title cannot be empty."
    record = book.find(title)
    if record:
        book.delete(title)
        return "Note removed."
    else:
        return "Note not found."

def search_note(command):
    """
    Sort notes by tags or search for a specific word in the notes by title, note, tags.
    If the notebook is empty, returns a message indicating so.
    If the notebook is not empty, sorts the notes by tags and displays them.
    """
    COMMANDS = {
        "search-notes" : lambda: input(f"🔍 Enter words to search for:")
        ,"search-by-tags-and-sort-by-title" : lambda: input(f"🏷️ Enter tags to sort by:").lower()
    }
    def inner(book):
        if book:
            input_text = COMMANDS[command]()
            if command == "search-by-tags-and-sort-by-title":
                input_text = [tag.strip().lower() for tag in input_text.split(',') if tag.strip()]
            else:
                input_text = input_text.strip().lower()
            STR = {
                "search-by-tags-and-sort-by-title": lambda : book.search_by_tags_and_sort_by_title(input_text)
                ,"search-notes": lambda : book.search_notes(input_text)
            }   

            sorted_note = STR[command]()
            if sorted_note:
                print("--" * 50)
                for note in sorted_note:
                    console.print(Panel.fit(str(note), border_style="#1E90FF"))  # note має повертати Rich Text або Text object
                print("--" * 50)
            else:
                console.print("No notes found.")
        else:
            console.print("NoteBook is empty.")
    return inner
