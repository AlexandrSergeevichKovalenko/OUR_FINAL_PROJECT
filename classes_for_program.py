from collections import UserDict
from datetime import datetime, date, timedelta
import re
from rich.panel import Panel


# ========================= BASE FIELD AND ITS SUBCLASSES ==========================


class Field:
    """Base class for contact fields."""
    def __init__(self, value):
      self.value = value

    def __str__(self):
      return str(self.value)


class Birthday(Field):
    """
    Represents a contact's birthday as a date object.
    Accepts date in DD.MM.YYYY format.
    """
    def __init__(self, value):
        pattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"
        if re.fullmatch(pattern, value):
            format = "%d.%m.%Y"
            self.value = datetime.strptime(value, format)
        else:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Name(Field):
    """Represents a contact's name."""
    pass


class Phone(Field):
    """
    Represents a contact's phone number.
    Validates 10-digit numeric format.
    """
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)


    #create a function to validate the phone number.
    @staticmethod
    def validate(number):
        return True if number.isdigit() and len(number) == 10 else False


class Email(Field):
    """
    Represents an email address with validation.

    Validation requirements:
    - The local part (before '@') can consist of lowercase letters, digits, and underscore.
    - The local part must include at least one lowercase letter.
    - The domain (after '@') must include only lowercase letters.
    - The extension (after '.') must consist only of lowercase letters.

    Example of valid email: user_123@example.com
    """


    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid email format. Please use a valid email address like user_123@example.com")
        super().__init__(value)


    @staticmethod
    def validate(email: str) -> bool:
        # The lookahead (?=[a-z0-9_]*[a-z]) ensures that the local part contains at least one letter
        pattern = r'^(?=[a-z0-9_]*[a-z])[a-z0-9_]+@[a-z]+\.[a-z]+$'
        return re.fullmatch(pattern, email) is not None


class Address(Field):
    """
    Represents an address field.
    The address can contain only letters, digits, commas, periods, and spaces.
    Example of valid address: "Example St, 123, Apt. 4B"
    """


    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid address format. Use only letters, digits, commas, periods, and spaces.")
        super().__init__(value)


    @staticmethod
    def validate(address: str) -> bool:
        # This regex allows uppercase and lowercase letters, digits, commas, periods, and spaces.
        pattern = r'^[A-Za-z0-9,\. ]+$'
        return re.fullmatch(pattern, address) is not None


# =========================== RECORD AND ADDRESSBOOK ===========================
 

class Record:
    """
    Stores contact information:
    - required name (Name)
    - optional birthday (Birthday)
    - multiple phones (Phone)
    - optional email (Email)
    - optional address (Address)
    """


    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None


    def set_birthday(self, data: str):
        """Set or update the contact's birthday."""
        self.birthday = Birthday(data)


    def remove_birthday(self):
        """Removes the contact's birthday."""
        self.birthday = None


    def add_phone(self, phone_number: str):
        """Add a new phone number to the contact."""
        phone = Phone(phone_number)
        self.phones.append(phone)


    def remove_phone(self, phone_number: str):
        """Remove an existing phone number from the contact."""
        if phone_number not in [phone.value for phone in self.phones]:
            return False
        else: 
            self.phones = [phone for phone in self.phones if phone.value !=phone_number]
            return True


    def edit_phone(self, old_number: str, new_number: str):
        """Replace old phone with a new phone number."""
        if not Phone.validate(new_number):
            raise ValueError("The new phone number is not valid. Please enter a valid 10-digit number.")


        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return
        raise ValueError("The phone number you entered does not exist")


    def find_phone(self, num_phone:str):
        """Find a phone object in the contact by its value."""
        for phone in self.phones:
            if phone.value == num_phone:
                return phone
        raise ValueError("The number was not found")


    def add_email(self, email_address: str):
        """Adds or updates the contact's email."""
        self.email = Email(email_address)


    def edit_email(self, new_email: str):
        """Replaces the existing email with a new email address."""
        self.email = Email(new_email)


    def remove_email(self):
        """Removes the contact's email."""
        self.email = None


    def add_address(self, address: str):
        """Adds or updates the contact's address."""
        self.address = Address(address)        


    def edit_address(self, new_address: str):
        """Replaces the existing address with a new address."""
        self.address = Address(new_address)


    def remove_address(self):
        """Removes the contact's address."""
        self.address = None


    def __str__(self):
        # Birthday
        birthday_str = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "—"
        # Email
        email_str = self.email.value if self.email else "—"
        # Address
        address_str = self.address.value if self.address else "—"
        # Phones
        phones_str = ", ".join(p.value for p in self.phones) if self.phones else "—"

        contact_info = (
                "[bold magenta]Name:[/] "
                f"{self.name.value}\n"
                "[bold magenta]Phones:[/] "
                f"{phones_str}\n"
                "[bold magenta]Birthday:[/] "
                f"{birthday_str}\n"
                "[bold magenta]Email:[/] "
                f"{email_str}\n"
                "[bold magenta]Address:[/] "
                f"{address_str}"
        )
        return contact_info


class AddressBook(UserDict):
    """
    A container for storing and managing multiple contact records.
    Supports:
    - add, find, delete contacts
    - upcoming birthday detection
    """


    def add_record(self, note: Record):
        """Add a Record instance to the address book."""
        self.data[note.name.value] = note


    def find(self, name: str) -> Record:
        """Find a contact by name. Returns the Record or None."""
        if name in self.data:
            return self.data[name]
        return None


    def delete(self, name:str) -> None:
        """Delete a contact by name, if it exists."""
        if name in self.data:
            del self.data[name]


    @staticmethod
    def date_to_string(date):
        return date.strftime("%d.%m.%Y")


    @staticmethod
    def find_next_weekday(start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)


    @staticmethod
    def adjust_for_weekend(birthday):
        if birthday.weekday() >= 5:
            return AddressBook.find_next_weekday(birthday, 0)
        return birthday


    def get_upcoming_birthdays(self, days = 7):
        """
        Return a list of upcoming birthdays within the next 7 days.
        If birthday falls on weekend, shift congratulations to Monday.
        """
        upcoming_birthdays = []
        today = date.today()

        for user, dict_record in self.data.items():
            #the first is to check if the dict_record object:Record has something in attribute birthday(it can happen,
            # that there is a name and a phone, but there is no birthday date entered by user)
            if dict_record.birthday:
                birthday_this_year = dict_record.birthday.value.replace(year=today.year).date()
                if birthday_this_year < today:
                    birthday_this_year = dict_record.birthday.value.replace(year=today.year + 1).date()

                if 0 <= (birthday_this_year - today).days <= int(days):
                    congratulation_date = AddressBook.adjust_for_weekend(birthday_this_year)
                    upcoming_birthdays.append({"name": user, "birthday": AddressBook.date_to_string(congratulation_date)})
        return upcoming_birthdays

    def __str__(self):
        if not self.data:
            return "No contacts found."
        return "\n".join(self.data.keys())


# =========================== Note AND NoteBook ===========================


class Note:
    """
    Represents a note with a title, optional note text, and tags.
    Supports adding notes and tags.
    """


    def __init__(self, title, note=None):
        self.title = title
        self.tags = []
        self.note = note


    def add_note(self, note):
        """Set or update the note text."""
        self.note = note


    def add_tags(self, tags):
        """Add tags to the note."""
        # Sort and add unique tags
        tags = [tag.strip() for tag in tags if tag.strip()]
        tags.sort()
        for tag in tags:
            if tag not in self.tags:
                self.tags.append(tag)


    def __str__(self):
        """
        Returns a string representing the note:
        Title, note text, and tags.
        """
        note_str = self.note if self.note else "-"
        tags_str = ", ".join(self.tags)
        return f""" ✨ [bold cyan]Title:[/] {self.title}
 📜 [bold yellow]Note:[/] {note_str}
 {f"🏷️  [bold magenta]Tags:[/] {tags_str}" if self.tags else "🏷️  [bold magenta]Tags:[/] -"}"""
        

class NoteBook(UserDict):
    """
    A container for storing and managing multiple notes.
    Supports:
    - 'add', 'find', 'delete notes', 'search notes' and 'search by tags and sort by title'
    """

    def get_titles(self):
        """Display the title of the note."""
        titles = []
        for note in self.data.values():
            titles.append(note.title)
        return titles


    def add_record(self, note: Note):
        """Add a Note instance to the notebook."""
        self.data[note.title] = note


    def find(self, title: str) -> Note:
        """Find a note by title. Returns the Note or None."""
        return self.data.get(title)


    def search_by_tags_and_sort_by_title(self, input_tags: str):
        """Search by tags and sort by title."""
        if not input_tags:
            return None
        input_tags = [tag.strip() for tag in input_tags.split(',') if tag.strip()]
        pattern = "|".join(re.escape(tag) for tag in input_tags)
        notes = [
            note for note in self.data.values() if re.search(pattern , ','.join(note.tags), re.IGNORECASE)
        ]
        if not notes:
            return None
        result = sorted(notes, key=lambda x: (x.tags, x.title))
        return result
    

    def search_notes(self, search_string: str):
        """Search notes by a word in the title, note text or tags."""
        if search_string:
            notes = [
                note for note in self.data.values() if re.search(search_string, note.title, re.IGNORECASE) 
                                                    or re.search(search_string, note.note, re.IGNORECASE)
                                                    or re.search(search_string, ','.join(note.tags), re.IGNORECASE)
            ]
            if not notes:
                return None
            result = sorted(notes, key=lambda x: x.title)
            return result


    def delete(self, title: str) -> None:
        """Delete a note by title, if it exists."""
        if title in self.data:
            del self.data[title]


    def __str__(self):
        """
        Returns a concatenation of all notes' string representations.
        If empty, returns a message.
        """
        if not self.data:
            return "[bold red]No notes found.[/bold red]"
        return "\n\n".join(str(note) for note in self.data.values())
