from functions_block import *
from classes_for_program import *
from contextlib import contextmanager
from functions_block import load_data, save_data
from note_functions import *


def parse_input(user_input):
    """
    parsing a console line 
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def print_help():
    """
    Displays a well-formatted list of available commands.
    """
    commands = {
        "add [name] [phone]": "Add a new contact or phone to existing contact",
        "change [name] [old] [new]": "Change a phone number",
        "phone [name]": "Show phone numbers for a contact",
        "all": "Show all contacts",
        "add-birthday [name] [DD.MM.YYYY]": "Add birthday to a contact",
        "show-birthday [name]": "Show birthday for a contact",
        "birthdays": "Show upcoming birthdays in the next 7 days",
        "hello": "Get a greeting from the bot",
        "close / exit": "Exit the program"
    }

    print("\nAvailable commands:")
    for cmd, desc in commands.items():
        print(f"  {cmd.ljust(35)} - {desc}")
    print()


@contextmanager
def record_manager():
    """
    use context manager to operate safely 
    """
    book = load_data()
    try:
        yield book
    finally:
        save_data(book)


def main():
    """
    Command-line assistant for managing contacts.
    Loads previous state from file, and saves data on exit.
    """
    with record_manager() as book:
        notebook = NoteBook()
        print("Welcome to the assistant bot!")
        print("Type 'help' to see available commands.")
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "help":
                print_help()

            elif command == "add":
                print(add_contact(args, book))

            elif command == "change":
                print(change_contact(args, book))
            
            elif command == "phone":
                print(show_phone(args, book))
            
            elif command == "all":
                print(show_all(book))

            elif command == "add-note":
                print(add_note(notebook))

            elif command == "show-note":
                print(show_note(notebook))

            elif command == "show-all-notes":
                print(show_all_notes(notebook))

            elif command == "change-note":
                print(change_note(notebook))

            elif command == "remove-note":
                print(remove_note(notebook))
            
            elif command == "add-birthday":
                print(add_birthday(args, book))

            elif command == "show-birthday":
                print(show_birthday(args, book))

            elif command == "birthdays":
                print(birthdays(book))
            
            else:
                print("Invalid command.")

if __name__ == "__main__":
    main()
