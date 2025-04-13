from prompt_toolkit import prompt
from rich.console import Console
from rich.panel import Panel
from classes_for_program import Note
from functions_block import (
    add_contact, add_phone, remove_contact, show_all, set_birthday,
    birthdays, add_email, change_email, add_address, change_address, save_data,
    search_records, rename_contact, remove_phone, remove_email, remove_address, 
    remove_birthday
)
from note_functions import (
    change_note, show_note, remove_note, search_note
)
import information_display as di
from animation import display_animals

console = Console()


def pause():
    console.print("[green]Press Enter to continue...[/green]")
    input()


# =========================== Menu Display ===========================
class InteractiveMenu:
    """
    Interactive menu for the contact and note assistant.
    Provides nested menus with numeric selection and Rich formatting.
    Users can cancel any action by entering 'back'.
    """

    def __init__(self):
        self.save_data = save_data

    def display(self, menu_text, title, bclear = True):
        panel = Panel.fit(menu_text, title=title, border_style="#1E90FF")
        if bclear: 
            console.clear()
        console.print(panel)
        return prompt("> ").strip()

    
    # =========================== Input Method ===========================
    def prompt_input(self, prompt_text):
        value = prompt(prompt_text).strip()
        if value.lower() == "back":
            return None
        return value


    # =========================== Contacts Handling ===========================
    def handle_add_contact(self, book):
        console.clear()
        console.print(Panel("Add Contact", style="bold green"))
        name = self.prompt_input("Enter contact name (or type 'back' to go back): ")
        if name:
            if book.find(name):
                console.print(f"Contact {name} already exist!")
                pause()                
                return
            else: 
                console.print(add_contact(name, book))
                pause()
        else:
            return
        while True:
            console.clear()
            console.print(f"[bold]Adding data to contact:[/] {name}")
            sub_choice = self.display(di.display_add_contact_menu, "Add Contact")
            if sub_choice == '5':
                break  # Back to Contacts Menu
            elif sub_choice == '1':
                phone = self.prompt_input("Enter phone number (10 digits) (or 'back'): ")
                if phone:
                    console.print(add_phone([name, phone], book))
            elif sub_choice == '2':
                email = self.prompt_input("Enter email (or 'back'): ")
                if email:
                    console.print(add_email([name, email], book))
            elif sub_choice == '3':
                address = self.prompt_input("Enter address (or 'back'): ")
                if address:
                    console.print(add_address([name, address], book))
            elif sub_choice == '4':
                birthday = self.prompt_input("Enter birthday (DD.MM.YYYY) (or 'back'): ")
                if birthday:
                    console.print(set_birthday([name, birthday], book))
            else:
                console.print("[bold red]Invalid option, please try again.[/bold red]")
            pause()


    def handle_change_contact(self, book):
        console.clear()
        console.print(Panel("Change Contact", style="bold green"))
        name = self.prompt_input("Enter the contact name to change (or 'back'): ")
        if name.lower() == 'back':
            return
        if not book.find(name):
             console.print(Panel(f"Contact {name} not found!", style="bold green"))
             pause()
             return
        while True:
            console.clear()
            console.print(Panel(f"{book.find(name)}", style="bold green"))            
            sub_choice = self.display(di.display_change_contact_menu, "Add Contact", False)

            if sub_choice == '0':
                break  # Back to Contacts Menu

            # Change name
            elif sub_choice == '1':
                new_name = self.prompt_input("Enter new Name (or 'back'): ")
                if new_name:
                    console.print(rename_contact([name, new_name], book))
                    name = new_name
                prompt("Press Enter to continue...")
            
            # Add Phone
            elif sub_choice == '2':
                phone = self.prompt_input("Enter phone number (or 'back'): ")
                if phone:
                    console.print(add_phone([name, phone], book))
                pause()                    

            # Change Email
            elif sub_choice == '3':
                new_email = self.prompt_input("Enter new email (or 'back'): ")
                if new_email:
                    console.print(change_email([name, new_email], book))
                pause()

            # Change Address
            elif sub_choice == '4':
                new_address = self.prompt_input("Enter new address (or 'back'): ")
                if new_address:
                    console.print(change_address([name, new_address], book))
                pause()

            # Change Birthday
            elif sub_choice == '5':
                new_birthday = self.prompt_input("Enter new birthday (DD.MM.YYYY) (or 'back'): ")
                if new_birthday:
                    console.print(set_birthday([name, new_birthday], book))
                pause()

            # Remove Phone
            elif sub_choice in '6':
                r_phone = self.prompt_input("Enter phone number to remove (or 'back'): ")
                if r_phone:
                    console.print(remove_phone([name, r_phone], book))
                pause()

            # Remove Email
            elif sub_choice == '7':
                console.print(remove_email([name], book))
                pause()

            # Remove Address
            elif sub_choice == '8':
                console.print(remove_address([name], book))
                pause()

            # Remove Birthday
            elif sub_choice == '9':
                console.print(remove_birthday([name, None], book))
                pause()


    def handle_view_contact(self, book):
        console.clear()
        console.print(Panel("Show Contact", style="bold green"))
        name = self.prompt_input("Enter contact name to view (or 'back'): ")
        if name:
            record = book.find(name)
            if record:
                console.print(Panel(str(record), title=f"Contact: {name}", border_style="#1E90FF"))
            else:
                console.print(f"[bold red]Contact '{name}' not found.[/bold red]")
        pause()


    def handle_delete_contact(self, book):
        console.clear()
        console.print(Panel("Remove Contact", style="bold green"))
        name = self.prompt_input("Enter contact name to delete (or 'back'): ")
        if not name:
            return
        answer = self.prompt_input("Are you sure you want to delete this contact? (y/n): ")
        if answer and answer.lower() == "y":
            console.print(remove_contact([name], book))
        else:
            console.print("Deletion cancelled.")
        pause()


    def handle_birthdays_week(self, book):
        console.clear()
        console.print(Panel("Birthdays in Next Week", style="bold green"))
        console.print(birthdays(book, ["7"]))
        pause()


    def handle_birthdays_x_days(self, book):
        console.clear()
        days = self.prompt_input("Enter the number of days to check birthdays (or 'back'): ")
        if days:
            console.print(Panel(f"Birthdays in next {days} days:", style="bold green"))
            console.print(birthdays(book, [days]))
        pause()


    def handle_contacts(self, book):
        while True:
            console.clear()
            choice = self.display(di.display_contacts_menu, "Manage Contacts")
            if choice == '8':  # Back to Main Menu
                break
            elif choice == '1':
                self.handle_add_contact(book)
            elif choice == '2':
                self.handle_change_contact(book)
            elif choice == '3':
                self.handle_view_contact(book)
            elif choice == '4':
                console.clear()
                console.print(Panel("Show All Contacts", style="bold green"))

                if not book.data:
                    console.print("[bold red]No contacts found.[/bold red]")
                else:
                    for record in book.data.values():
                        phones_str = ", ".join(p.value for p in record.phones) if record.phones else "—"
                        birthday_str = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "—"
                        email_str = record.email.value if record.email else "—"
                        address_str = record.address.value if record.address else "—"

                        content = (
                            f"[bold magenta]Name:[/] {record.name.value}\n"
                            f"[bold magenta]Phones:[/] {phones_str}\n"
                            f"[bold magenta]Birthday:[/] {birthday_str}\n"
                            f"[bold magenta]Email:[/] {email_str}\n"
                            f"[bold magenta]Address:[/] {address_str}"
                        )

                        panel = Panel.fit(content, border_style="bright_blue")
                        console.print(panel)

                pause()
            elif choice == '5':
                self.handle_delete_contact(book)
            elif choice == '6':
                self.handle_birthdays_week(book)
            elif choice == '7':
                self.handle_birthdays_x_days(book)
            else:
                console.print("[bold red]Invalid option in Contacts Menu.[/bold red]")
                pause()


    # =========================== Notes Handling ===========================
    def handle_notes(self, notebook):
        while True:
            console.clear()
            choice = self.display(di.display_notes_menu, "Manage Notes")
            if choice == '7':  # Back to Main Menu
                break
            elif choice == '1':
                console.clear()
                console.print(Panel("Add Note", style="bold green"))
                title = self.prompt_input("Enter note title (or 'back'): ")
                if not title:
                    pause()
                    continue
                note_text = self.prompt_input("Enter the note text (or 'back'): ")
                if note_text is None:
                    console.print("[bold red]Note creation cancelled.[/bold red]")
                    pause()
                    continue
                add_tags_answer = self.prompt_input("Would you like to add tags? (y/n or 'back'): ")
                if add_tags_answer and add_tags_answer.lower() == "y":
                    tags_input = self.prompt_input("Enter tags (comma-separated) (or just Enter for none): ")
                    if tags_input is None:
                        console.print("[bold red]Tag entry cancelled. No tags added.[/bold red]")
                        tags = []
                    elif not tags_input.strip():
                        tags = []
                    else:
                        tags = tags_input.split(",")
                else:
                    tags = []
                new_note = notebook.find(title)
                if not new_note:
                    new_note = Note(title)
                    notebook.add_record(new_note)
                new_note.add_note(note_text)
                new_note.add_tags(tags)
                console.print(f"[bold green]Note '{title}' added/updated successfully![/bold green]")
                pause()
            elif choice == '2':
                console.clear()
                console.print(Panel("Change Note", style="bold green"))
                console.print(change_note(notebook))
                pause()
            elif choice == '3':
                console.clear()
                console.print(Panel("Show Note", style="bold green"))
                console.print(show_note(notebook))
                pause()
            elif choice == '4':
                console.clear()
                console.print(Panel("Show All Notes", style="bold green"))
                console.print(str(notebook))
                pause()
            elif choice == '5':
                console.clear()
                console.print(Panel("Add Tags to Note", style="bold green"))
                title = self.prompt_input("Enter note title (or 'back'): ")
                if not title:
                    console.print("[bold red]Operation cancelled.[/bold red]")
                    pause()
                    continue
                record = notebook.find(title)
                if record is None:
                    console.print(f"[bold red]Note '{title}' not found.[/bold red]")
                    pause()
                    continue
                tags_input = self.prompt_input("Enter tags (comma-separated) (or 'back'): ")
                if tags_input is not None:
                    new_tags = tags_input.split(",")
                    record.add_tags(new_tags)
                    console.print("[bold green]Tags added successfully![/bold green]")
                else:
                    console.print("[bold red]Tag addition cancelled.[/bold red]")
                pause()
            elif choice == '6':
                console.clear()
                title = self.prompt_input("Enter note title to remove (or 'back'): ")
                console.print(remove_note(notebook, title))
                pause()
            else:
                console.print("[bold red]Invalid option in Notes Menu.[/bold red]")
                pause()


    # =========================== Search Handling ===========================
    def handle_search(self, book, notebook):
        def show_search_result(result: list):
            if result: 
                for i in result:
                    console.print(f'{i}')
                    console.print('\n')
            else:
                print('Not found!')

        while True:
            console.clear()
            choice = self.display(di.display_search_menu, "Search")
            if choice == '3':  # Back to Main Menu
                break
            elif choice == '1':
                query = self.prompt_input("Enter search query for contacts (or 'back'): ")
                console.print(Panel(f"Search contacts by string - {query}", style="bold green"))
                show_search_result(search_records([query], book))
                pause()                
            elif choice == '2':
                console.clear()
                s_choice = self.display(di.display_search_notes_menu, "Search Notes")
                if s_choice == '1':
                    search_notes = search_note("search-notes")
                    notes = search_notes(notebook)
                    display_animals()
                    console.clear()
                    if notes:
                        for note in notes:
                            console.print(Panel.fit(str(note), border_style="#1E90FF"))
                    else:
                        console.print("[bold red]No notes found.[/bold red]")
                    pause()
                elif s_choice == '2':
                    search_notes = search_note("search-by-tags-and-sort-by-title")
                    notes = search_notes(notebook)
                    display_animals()
                    console.clear()
                    if notes:
                        for note in notes:
                            console.print(Panel.fit(str(note), border_style="#1E90FF"))
                    else:
                        console.print("[bold red]No notes found.[/bold red]")
                    pause()
                elif s_choice == '3':
                    continue
                else:
                    query = self.prompt_input("Enter search query for notes (or 'back'): ")
                    if query:
                        console.print("Search Notes functionality (not implemented yet)")
                    pause()
            else:
                console.print("[bold red]Invalid option in Search Menu.[/bold red]")
                pause()


    # =========================== Main Menu Handling ===========================
    def run(self, book, notebook):
        while True:
            console.clear()
            choice = self.display(di.display_main_menu, "Main Menu")
            if choice == '1':
                self.handle_contacts(book)
            elif choice == '2':
                self.handle_notes(notebook)
            elif choice == '3':
                self.handle_search(book, notebook)
            elif choice == '4':
                console.clear()
                self.display(di.display_help, "Help Information")
            elif choice == '5':
                console.print(Panel("Goodbye!", style="bold #FF4500"))
                break
            else:
                console.print("[bold red]Invalid option in Main Menu.[/bold red]")
                pause()
