from note_class import *
import re

def add_note(book):
    while True:
        title = input(f"{"✨"} Enter a title:")
        if title:
            note = input(f"{"📜"} Enter a note:")
            tags = input(f"{"🏷️"} Enter a tags or (n):")
            if tags != "n":
                pattern = r"[ ,]"
                tags = re.split(pattern, tags)
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
    while True:
        title = input(f"{"✨"} Enter a title:")
        if title:
            note = input(f"{"📜"} Enter a new note:")
            record = book.find(title)
            if record:
                record.edit_note(note)
                return "Note changed."
            return "Note not found."
        print("Please enter a title.")

def show_note(book):
    while True:
        title = input(f"{"✨"} Enter a title:")
        if title:
            record = book.find(title)
            return f"{"📜"} {record.note}" if record else "Note not found."
        print("Please enter a title.")

def show_all_notes(book):
    return book if book else "NoteBook is empty"

def remove_note(book):
    while True:
        title = input(f"{"✨"} Enter a title:")
        if title:
            record = book.find(title)
            if record:
                book.delete(title)
                return "Note removed."
            return "Note not found."
        print("Please enter a title.")