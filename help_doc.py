from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


def display_help():
    """
    Displays three tables (Contacts, Notes, General) stacked vertically,
    with adjusted title colors and extra spacing between tables.
    """
    # ========================= CONTACTS TABLE =========================
    contacts_table = Table(
        title="Contacts Commands",
        title_style="bold bright_blue",
        show_lines=True,
        border_style="bold white",
        expand=False,
        box=box.HEAVY
    )
    contacts_table.add_column(
        "Command",
        header_style="bold bright_green",
        style="white",
        width=20,
        no_wrap=True
    )
    contacts_table.add_column(
        "Description",
        header_style="bold bright_green",
        style="white",
        width=55,
        no_wrap=True
    )

    contacts_table.add_row(
        "add [name] [phone]",
        "Add a new contact or add a phone to an existing contact"
    )
    contacts_table.add_row(
        "change [name] [old] [new]",
        "Change a phone number"
    )
    contacts_table.add_row(
        "phone [name]",
        "Show phone numbers for a contact"
    )
    contacts_table.add_row(
        "all",
        "Show all contacts"
    )
    contacts_table.add_row(
        "add-birthday [name]",
        "Add birthday to a contact [DD.MM.YYYY]"
    )
    contacts_table.add_row(
        "show-birthday [name]",
        "Show birthday for a contact"
    )
    contacts_table.add_row(
        "birthdays [days]",
        "Show upcoming birthdays in the next [N] days"
    )
    contacts_table.add_row(
        "birthdays",
        "Show upcoming birthdays in the next 7 days"
    )
    contacts_table.add_row(
        "add-email [name] [email]",
        "Add or update email for a contact"
    )
    contacts_table.add_row(
        "change-email [name] [new_email]",
        "Change email for a contact"
    )
    contacts_table.add_row(
        "show-email [name]",
        "Show email for a contact"
    )
    contacts_table.add_row(
        "remove-email [name]",
        "Remove email from a contact"
    )
    contacts_table.add_row(
        "add-address [name] [address]",
        "Add or update address for a contact"
    )
    contacts_table.add_row(
        "change-address [name] [new_address]",
        "Change address for a contact"
    )
    contacts_table.add_row(
        "show-address [name]",
        "Show address for a contact"
    )
    contacts_table.add_row(
        "remove-address [name]",
        "Remove address from a contact"
    )

    # ========================= NOTES TABLE =========================
    notes_table = Table(
        title="Notes Commands",
        title_style="bold bright_blue",
        show_lines=True,
        border_style="bold white",
        expand=False,
        box=box.HEAVY
    )
    notes_table.add_column(
        "Command",
        header_style="bold bright_green",
        style="white",
        width=20,
        no_wrap=True
    )
    notes_table.add_column(
        "Description",
        header_style="bold bright_green",
        style="white",
        width=55,
        no_wrap=True
    )

    notes_table.add_row("add-note", "Add a new note")
    notes_table.add_row("change-note", "Change an existing note")
    notes_table.add_row("show-note", "Show a specific note")
    notes_table.add_row("show-all-notes", "Show all notes")
    notes_table.add_row(
        "sorted-notes-by-tags",
        "Display notes sorted by tags"
    )
    notes_table.add_row("remove-note", "Remove a note")
    notes_table.add_row("add-tags-to-note", "Add tags to a note")

    # ========================= GENERAL TABLE =========================
    general_table = Table(
        title="General Commands",
        title_style="bold bright_blue",
        show_lines=True,
        border_style="bold white",
        expand=False,
        box=box.HEAVY
    )
    general_table.add_column(
        "Command",
        header_style="bold bright_green",
        style="white",
        width=20,
        no_wrap=True
    )
    general_table.add_column(
        "Description",
        header_style="bold bright_green",
        style="white",
        width=55,
        no_wrap=True
    )

    general_table.add_row("hello", "Get a greeting from the bot")
    general_table.add_row("help", "Display help information")
    general_table.add_row("close / exit", "Exit the program")

    # ========================= DISPLAY TABLES =========================
    console.clear()
    console.print(contacts_table)
    console.print("\n")
    console.print(notes_table)
    console.print("\n")
    console.print(general_table)
    console.print("\n")


if __name__ == "__main__":
    display_help()
