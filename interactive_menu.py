from prompt_toolkit import prompt
from rich.console import Console
from rich.panel import Panel
from classes_for_program import Note
from functions_block import (
    add_contact, change_phone, remove_contact, show_all, set_birthday,
    birthdays, add_email, change_email, add_address, change_address, save_data,
    search_records, rename_contact, remove_phone, remove_email, remove_address, 
    remove_birthday
)
from note_functions import (
    change_note, show_note, remove_note, search_note, add_note
)
import information_display as di
from animation import display_animals

console = Console()


# =========================== Menu Display ===========================
class InteractiveMenu:
    """
    Interactive menu for the contact and note assistant.
    Provides nested menus with numeric selection and Rich formatting.
    Users can cancel any action by entering 'cancel'.
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
        if value.lower() == "cancel":
            return None
        return value


    # =========================== Contacts Handling ===========================
    def handle_add_contact(self, book):
        console.clear()
        console.print(Panel("Add Contact", style="bold green"))
        name = self.prompt_input("Enter contact name (or type 'cancel' to go back): ")
        if not name:
            return
        while True:
            console.clear()
            console.print(f"[bold]Adding data to contact:[/] {name}")
            sub_choice = self.display(di.display_add_contact_menu, "Add Contact")
            if sub_choice == '5':
                break  # Back to Contacts Menu
            elif sub_choice == '1':
                phone = self.prompt_input("Enter phone number (10 digits) (or 'cancel'): ")
                if phone:
                    console.print(add_contact([name, phone], book))
            elif sub_choice == '2':
                email = self.prompt_input("Enter email (or 'cancel'): ")
                if email:
                    console.print(add_email([name, email], book))
            elif sub_choice == '3':
                address = self.prompt_input("Enter address (or 'cancel'): ")
                if address:
                    console.print(add_address([name, address], book))
            elif sub_choice == '4':
                birthday = self.prompt_input("Enter birthday (DD.MM.YYYY) (or 'cancel'): ")
                if birthday:
                    console.print(set_birthday([name, birthday], book))
            else:
                console.print("[bold red]Invalid option, please try again.[/bold red]")
            prompt("Press Enter to continue...")


    def handle_change_contact(self, book):
        console.clear()
        console.print(Panel("Change Contact", style="bold green"))
        name = self.prompt_input("Enter the contact name to change (or 'cancel'): ")
        if not book.find(name):
             console.print(Panel(f"Contact {name} not found!", style="bold green"))
             prompt("Press Enter to continue...")
             return
        while True:
            console.clear()
            console.print(Panel(f"{book.find(name)}", style="bold green"))            
            sub_choice = self.display(di.display_change_contact_menu, "Add Contact", False)

            if sub_choice == '0':
                break  # Back to Contacts Menu
            elif sub_choice == '1':
                new_name = self.prompt_input("Enter new Name (or 'cancel'): ")
                if new_name:
                    console.print(rename_contact([name, new_name], book))
                prompt("Press Enter to continue...")
            
            # Change Phone
            elif sub_choice == '2':
                
                old_phone = self.prompt_input("Enter phone number to change (or 'cancel'): ")
                new_phone = self.prompt_input("Enter new phone number (or 'cancel'): ")
                if new_phone:
                    console.print(change_phone([name, old_phone, new_phone], book))
                prompt("Press Enter to continue...")                    

            # Change Email
            elif sub_choice == '3':
                new_email = self.prompt_input("Enter new email (or 'cancel'): ")
                if new_email:
                    console.print(change_email([name, new_email], book))
                prompt("Press Enter to continue...")

            # Change Address
            elif sub_choice == '4':
                new_address = self.prompt_input("Enter new address (or 'cancel'): ")
                if new_address:
                    console.print(change_address([name, new_address], book))
                prompt("Press Enter to continue...")

            # Change Birthday
            elif sub_choice == '5':
                new_birthday = self.prompt_input("Enter new birthday (DD.MM.YYYY) (or 'cancel'): ")
                if new_birthday:
                    console.print(set_birthday([name, new_birthday], book))
                prompt("Press Enter to continue...")

            # Remove Phone
            elif sub_choice in '6':
                r_phone = self.prompt_input("Enter phone number to remove (or 'cancel'): ")
                if r_phone:
                    console.print(remove_phone([name, r_phone], book))
                prompt("Press Enter to continue...")

            # Remove Email
            elif sub_choice == '7':
                console.print(remove_email([name], book))
                prompt("Press Enter to continue...")

            # Remove Address
            elif sub_choice == '8':
                console.print(remove_address([name], book))
                prompt("Press Enter to continue...")

            # Remove Birthday
            elif sub_choice == '9':
                console.print(remove_birthday([name, None], book))
                prompt("Press Enter to continue...")


    def handle_view_contact(self, book):
        console.clear()
        console.print(Panel("Show Contact", style="bold green"))
        name = self.prompt_input("Enter contact name to view (or 'cancel'): ")
        if name:
            record = book.find(name)
            if record:
                console.print(Panel(str(record), title=f"Contact: {name}", border_style="#1E90FF"))
            else:
                console.print(f"[bold red]Contact '{name}' not found.[/bold red]")
        prompt("Press Enter to continue...")


    def handle_delete_contact(self, book):
        console.clear()
        console.print(Panel("Remove Contact", style="bold green"))
        name = self.prompt_input("Enter contact name to delete (or 'cancel'): ")
        if not name:
            return
        answer = self.prompt_input("Are you sure you want to delete this contact? (y/n): ")
        if answer and answer.lower() == "y":
            console.print(remove_contact([name], book))
        else:
            console.print("Deletion cancelled.")
        prompt("Press Enter to continue...")


    def handle_birthdays_week(self, book):
        console.clear()
        console.print(Panel("Birthdays in Next Week", style="bold green"))
        console.print(birthdays(book, ["7"]))
        prompt("Press Enter to continue...")


    def handle_birthdays_x_days(self, book):
        console.clear()
        days = self.prompt_input("Enter the number of days to check birthdays (or 'cancel'): ")
        if days:
            console.print(Panel(f"Birthdays in next {days} days:", style="bold green"))
            console.print(birthdays(book, [days]))
        prompt("Press Enter to continue...")


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
                console.print(str(show_all(book)))
                prompt("Press Enter to continue...")
            elif choice == '5':
                self.handle_delete_contact(book)
            elif choice == '6':
                self.handle_birthdays_week(book)
            elif choice == '7':
                self.handle_birthdays_x_days(book)
            else:
                console.print("[bold red]Invalid option in Contacts Menu.[/bold red]")
                prompt("Press Enter to continue...")


    # =========================== Notes Handling ===========================


    def print_note_titles(self, notebook):
        titles = notebook.get_titles()
        if titles:
            console.print(Panel.fit(f"{", ".join(titles)}", title="All titles", border_style="blue"))
        else:
            console.print("[bold red]No notes available.[/bold red]")



    def handle_notes(self, notebook):
        while True:
            choice = self.display(di.display_notes_menu, "Manage Notes")
            if choice == '7':  # Back to Main Menu
                break
            elif choice == '1':
                console.clear()
                console.print(Panel("Add Note", style="bold green"))
                self.print_note_titles(notebook)
                console.print(add_note(notebook))
                prompt("Press Enter to continue...")
            elif choice == '2':
                console.clear()
                console.print(Panel("Change Note", style="bold green"))
                self.print_note_titles(notebook)

                console.print(change_note(notebook))
                prompt("Press Enter to continue...")
            elif choice == '3':
                console.clear()
                console.print(Panel("Show Note", style="bold green"))
                self.print_note_titles(notebook)

                console.print(show_note(notebook))
                prompt("Press Enter to continue...")
            elif choice == '4':
                console.clear()
                console.print(Panel("Show All Notes", style="bold green"))
                console.print(str(notebook))
                prompt("Press Enter to continue...")
            elif choice == '5':
                console.clear()
                console.print(Panel("Add Tags to Note", style="bold green"))
                title = self.prompt_input("Enter note title (or 'cancel'): ")
                if not title:
                    console.print("[bold red]Operation cancelled.[/bold red]")
                    prompt("Press Enter to continue...")
                    continue
                record = notebook.find(title)
                if record is None:
                    console.print(f"[bold red]Note '{title}' not found.[/bold red]")
                    prompt("Press Enter to continue...")
                    continue
                tags_input = self.prompt_input("Enter tags (comma-separated) (or 'cancel'): ")
                if tags_input is not None:
                    new_tags = tags_input.split(",")
                    record.add_tags(new_tags)
                    console.print("[bold green]Tags added successfully![/bold green]")
                else:
                    console.print("[bold red]Tag addition cancelled.[/bold red]")
                prompt("Press Enter to continue...")
            elif choice == '6':
                console.clear()
                console.print(Panel("Remove Notes", style="bold green"))
                self.print_note_titles(notebook)
                
                title = self.prompt_input("Enter note title to remove (or 'cancel'): ")
                console.print(remove_note(notebook, title))
                prompt("Press Enter to continue...")
            else:
                console.print("[bold red]Invalid option in Notes Menu.[/bold red]")
                prompt("Press Enter to continue...")


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
                query = self.prompt_input("Enter search query for contacts (or 'cancel'): ")
                console.print(Panel(f"Search contacts by string - {query}", style="bold green"))
                show_search_result(search_records([query], book))
                prompt("Press Enter to continue...")                
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
                    prompt("Press Enter to continue...")
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
                    prompt("Press Enter to continue...")
                elif s_choice == '3':
                    continue
                else:
                    query = self.prompt_input("Enter search query for notes (or 'cancel'): ")
                    if query:
                        console.print("Search Notes functionality (not implemented yet)")
                    prompt("Press Enter to continue...")
            else:
                console.print("[bold red]Invalid option in Search Menu.[/bold red]")
                prompt("Press Enter to continue...")


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
                prompt("Press Enter to continue...")

