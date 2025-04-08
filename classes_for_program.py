from collections import UserDict
from datetime import datetime, date, timedelta
import re
from pathlib import Path

#global variable(name of the file) for storaging all programm progress 
FILENAME = Path("addressbook.pkl")

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

# =========================== RECORD AND ADDRESSBOOK ===========================

class Record:
    """
    Stores contact information:
    - required name (Name)
    - optional birthday (Birthday)
    - multiple phones (Phone)
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    

    def add_birthday(self, data: str):
        """Set or update the contact's birthday."""
        self.birthday = Birthday(data)


    def add_phone(self, phone_number: str):
        """Add a new phone number to the contact."""
        phone = Phone(phone_number)
        self.phones.append(phone)
    

    def remove_phone(self, phone_number: str):
        """Remove an existing phone number from the contact."""
        self.phones = [phone for phone in self.phones if phone.value !=phone_number]


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

    def __str__(self):
        birthday_str = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "N/A"
        phones_string = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_string}, birthday: {birthday_str}"


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
    
    #def string_to_date(date_string):
        #return datetime.strptime(date_string, "%Y.%m.%d").date()

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


    #str method is created to output the content in an understandable way
    def __str__(self):
        output = ["AddressBook: "]
        for key in self.data:
            contact_description_line = (f"name: {self.data[key].name.value}, phones: {'; '.join(phone.value for phone in self.data[key].phones)}")
            output.append(contact_description_line)
        total_info_line = "\n".join(output)
        return total_info_line

    
    