from functions_block import *
from classes_for_program import *
from contextlib import contextmanager
from functions_block import load_data, save_data
from note_functions import *


def parse_input(user_input):
    """
    Parses a console line into a command and a data string.
    """
    parts = user_input.split(" ", 1)  # Split into at most 2 parts
    cmd = parts[0].strip().lower()
    data = parts[1] if len(parts) > 1 else ""
    return cmd, data

def print_help():
    """
    Displays a well-formatted list of available commands.
    """
    commands = {
        "add [name] [phone]": "Add a new contact or phone to existing contact",
        "change-name [old name] [new name]": "Change the contact name",
        "del [name]": "Delete the contact",
        "change-phone [name] [old] [new]": "Change a phone number",
        "search [pattern]": "Show records according search pattern",
        "all": "Show all contacts",
        "set-birthday [name] [DD.MM.YYYY]": "Set birthday to a contact",
        "show-birthday [name]": "Show birthday for a contact",
        "birthdays [days]": "Show upcoming birthdays in the next [N] days",
        "birthdays": "Show upcoming birthdays in the next 7 days",
        "add-email [name] [email]": "Add or update email for a contact",
        "change-email [name] [new_email]": "Change email for a contact",
        "show-email [name]": "Show email for a contact",
        "remove-email [name]": "Remove email from a contact",
        "add-address [name] [address]": "Add or update address for a contact",
        "change-address [name] [new_address]": "Change address for a contact",
        "show-address [name]": "Show address for a contact",
        "remove-address [name]": "Remove address from a contact",
        "hello": "Get a greeting from the bot",
        "close / exit": "Exit the program"
    }

    print("\nAvailable commands:")
    for cmd, desc in commands.items():
        print(f"  {cmd.ljust(35)} - {desc}")
    print()


@contextmanager
def record_manager(file):
    """
    use context manager to operate safely 
    """
    book = load_data(file)
    try:
        yield book
    finally:
        save_data(book, file)


def main():
    """
    Command-line assistant for managing contacts.
    Loads previous state from file, and saves data on exit.
    """
    with record_manager(FILENAME) as book, record_manager(NOTEFILENAME) as notebook:
        print("Welcome to the assistant bot!")
        print("Type 'help' to see available commands.")
        while True:
            user_input = input("Enter a command: ")
            command, data = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "help":
                from help_doc import display_help
                display_help()

            elif command == "add":
                print(add_contact(data.split(), book))

            elif command == "del":
                print(del_contact(data.split(), book))

            elif command == "change-name":
                print(change_contact(data.split(), book))

            elif command == "change-phone":
                print(change_phone(data.split(), book))

            elif command == "search":
                show_search_result(search_records(data.split(), book))

            elif command == "all":
                print(show_all(book))

            elif command == "set-birthday":
                print(set_birthday(data.split(), book))
            
            elif command == "show-birthday":
                print(show_birthday(data.split(), book))

            elif command == "birthdays":
                print(birthdays(book, data.split()))

            elif command == "add-email":
                print(add_email(data.split(), book))

            elif command == "change-email":
                print(change_email(data.split(), book))

            elif command == "show-email":
                print(show_email(data.split(), book))

            elif command == "remove-email":
                print(remove_email(data.split(), book))

            elif command == "add-note":
                print(add_note(notebook))

            elif command == "show-note":
                print(show_note(notebook))

            elif command == "show-all-notes":
                print(show_all_notes(notebook))

            elif command == "change-note":
                print(change_note(notebook))

            elif command in ["sorted-notes-by-tags", "search-notes"]:
                search_notes = search_note(command)
                search_notes(notebook)

            elif command == "remove-note":
                print(remove_note(notebook))

            elif command == "show-address":
                print(show_address(data.split(), book))

            elif command == "remove-address":
                print(remove_address(data.split(), book))

            elif command == "add-address":
                # 'data' now contains a single string, e.g.: "John Example St. 123, apt. 4B"
                # Split it into two parts: the first word (name) and the rest (address)
                parts = data.split(" ", 1)
                if len(parts) < 2:
                    print("Not enough arguments for add-address command.")
                else:
                    print(add_address(parts, book))

            elif command == "change-address":
                parts = data.split(" ", 1)
                if len(parts) < 2:
                    print("Not enough arguments for change-address command.")
                else:
                    print(change_address(parts, book))

            else:
                print("Invalid command.")

if __name__ == "__main__":
    main()
