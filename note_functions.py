from classes_for_program import Note
from rich.console import Console
from rich.panel import Panel


console = Console()


def add_note(book: Note):
    """
    Add a new note to the notebook.
    Prompts for title, note content, and optional tags.
    If a note with the same title exists, prompts to replace it.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ").strip()
        if title == "back":
            return "Back to main menu"
        elif title:
            note = input("📜 Enter a note: ").strip()
            tags = input("🏷️ Enter tags or (n): ").strip()

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
                result = book.find(title)
                return Panel.fit(
                    f"[blue]Current note:[/]\n {result}",
                    title=result.title,
                    border_style="blue",
                )
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


def change_note(book: Note):
    """
    Change the content of an existing note.
    Offers to edit the content of the note.
    If the note exists, updates its content and returns a success message.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ").strip()
        if title == "back":
            return "Back to main menu."
        elif title:
            record = book.find(title)
            if record:
                console.print(Panel.fit(f"[blue]Current note:[/]\n {record}", title=record.title, border_style="blue"))
                note = input("📜 Enter a new note: ").strip()
                record.add_note(note)
                return "Note changed."
            return "Note not found."
        print("Please enter a title.")


def show_note(book: Note) -> str: 
    """
    Display the content of a specific note.
    If the note exists, returns its content.
    If the note does not exist, returns a failure message.
    """
    while True:
        title = input("✨ Enter a title or (back) to return to the main menu: ").strip()
        if title == "back":
            return "Back to main menu."
        elif title:
            record = book.find(title)
            if record:
                return Panel.fit(f"[blue]Current note:[/]\n {record}", title=record.title, border_style="blue")
            else:
                return "Note not found."
        print("Please enter a title.")


def remove_note(book, title: str =None):
    """
    Remove a note from the notebook.
    If 'title' is provided, it is used directly; otherwise, the user is prompted.
    """
    if title is None:
        title = input("✨ Enter a title to remove or (back) to return to the main menu: ").strip()
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


def search_note(command: str) -> callable:
    """
    Sort notes by tags or search for a specific word in the notes by title, note, tags.
    If the notebook is empty, returns a message indicating so.
    If the notebook is not empty, sorts the notes by tags and displays them.
    """
    COMMANDS = {
        "search-notes" : lambda: input(f"🔍 Enter words to search for:")
        ,"search-by-tags-and-sort-by-title" : lambda: input(f"🏷️ Enter tags to sort by:")
    }


    def inner(book: Note) -> str:
        if book:
            input_text = COMMANDS[command]().strip()
            STR = {
                "search-by-tags-and-sort-by-title": lambda : book.search_by_tags_and_sort_by_title(input_text)
                ,"search-notes": lambda : book.search_notes(input_text)
            }   
            sorted_notes = STR[command]()
            if sorted_notes:
                return sorted_notes
            else:
                return None
        else:
            return None
    return inner