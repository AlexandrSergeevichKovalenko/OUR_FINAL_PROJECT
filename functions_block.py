from decor import input_error
from classes_for_program import *
import pickle

"""
Here are functions whose names clearly matches their logic.
"""
@input_error(expected_arg_count=2)
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error(expected_arg_count=3)
def change_phone(args, book: AddressBook):
    name, old_number, new_number, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_number, new_number)
        return "Contact updated."
    else:
        return f"There is no person with {name} name"

# @input_error(expected_arg_count=2)
def change_contact(args, book: AddressBook):
    """
    Function for change name of contact'.
    change_contact(old_name: string, new_name: string) -> result message
    """
    old_name, new_name, *_ = args
    new_record = book.find(new_name)
    old_record = book.find(old_name)
    if new_record:
        return f"Contact with name: {new_name} already exist."
    else:
        if old_record:
            book.data[new_name] = book.data.pop(old_name)
            book.data[new_name].name.value = new_name
            return f"Contact name: {old_name} changed to {new_name}."
        else:
            return f"Contact with name: {new_name} not found"
        
@input_error(expected_arg_count=0)
def del_contact(args, book: AddressBook):
    """
    Function for delete contact from Address book'.
    del_contact(name: string) -> result message
    """
    name, *_ = args
    record = book.find(name)
    if record:
        if input('Are you shure ? (y/n)').lower() == 'y': 
            del book.data[name]
            return f"Contact {name} deleted."
    else:
        return f"There is no person with {name} name"

def show_all(book: AddressBook):
    if len(book.data) != 0:
        return str(book)
    else:
        return "There is no data to output."

@input_error(expected_arg_count=1)
def search_records(args, book: AddressBook):
    """
    Search string in all attributes of contact in addressbook.
    Usage: search [search_string] 
    """
    records = []
    search_string = str(args[0]).lower()
    for k, v in book.data.items():
        strN = v.name.value + '│'
        strB = v.birthday.value.strftime("%d.%m.%Y") if v.birthday else '│'
        strPhones = '│'.join(vp.value for vp in v.phones)
        strEmail = '│' + v.email.value if v.email else '│'
        strAddress = '│' + v.address.value if v.address else '│'
        target_string = strN + strB + strPhones + strEmail + strAddress
        if search_string in target_string.lower():
            records.append(v)          
    return records       
    
def show_search_result(result: list):
    if result: 
        for i in result:
            print(f'{i}')
    else:
        print('Not found!')

@input_error(expected_arg_count=2)
def set_birthday(args, book):
    name, birthday_day, *_ = args
    message = "Birthday is set."
    record = book.find(name)

    if record is None:
        return f"There is no person with {name} name"
    
    # to be sure that a user will not enter date, which is not exist, like 31.02.2020 (there is a check in __init__, but only for the correct format of an inputted data).
    try:
        record.set_birthday(birthday_day)
        return message
    except ValueError as e:
        return str(e)

@input_error(expected_arg_count=1)
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return f"There is no person with {name} name."
    else:
        if record.birthday is not None:
            return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}"
        else:
            return f"{name} does not have a birthday set."
        
@input_error(expected_arg_count=2)
def add_email(args, book: AddressBook):
    """
    Adds or updates the email for a contact.
    Usage: add-email [name] [email]
    """
    name, email_address, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_email(email_address)
    return "Email added/updated."


@input_error(expected_arg_count=2)
def change_email(args, book: AddressBook):
    """
    Changes the email for an existing contact.
    Usage: change-email [name] [new_email]
    """
    name, new_email, *_ = args
    record = book.find(name)
    if record is None or not record.email:
        return f"No existing email found for contact '{name}'. Use 'add-email' to add an email."
    record.edit_email(new_email)
    return "Email updated."


@input_error(expected_arg_count=1)
def show_email(args, book: AddressBook):
    """
    Shows the email for a contact.
    Usage: show-email [name]
    """
    name, *_ = args
    record = book.find(name)
    if record is None or not record.email:
        return f"No email found for contact '{name}'."
    return f"{name}'s email: {record.email.value}"

@input_error(expected_arg_count=1)
def remove_email(args, book: AddressBook):
    """
    Removes the email for a contact.
    Usage: remove-email [name]
    """
    name, *_ = args
    record = book.find(name)
    if record is None or record.email is None:
        return f"No email to remove for contact '{name}'."
    record.remove_email()
    return "Email removed."

@input_error(expected_arg_count=2)
def add_address(args, book: AddressBook):
    """
    Adds or updates the address for a contact.
    Usage: add-address [name] [address]
    """
    # The first element is the contact's name
    # All remaining elements are combined into one address string
    name = args[0]
    address = " ".join(args[1:])  # Join all remaining arguments with a space

    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_address(address)
    return "Address added/updated."

@input_error(expected_arg_count=2)
def change_address(args, book: AddressBook):
    """
    Changes the address for an existing contact.
    Usage: change-address [name] [new_address]
    """
    # The first element is the contact's name
    # All remaining elements are combined into one new address string
    name = args[0]
    new_address = " ".join(args[1:])

    record = book.find(name)
    if record is None or not record.address:
        return f"No existing address found for contact '{name}'. Use 'add-address' to add an address."
    record.edit_address(new_address)
    return "Address updated."

@input_error(expected_arg_count=1)
def show_address(args, book: AddressBook):
    """
    Shows the address for a contact.
    Usage: show-address [name]
    """
    name, *_ = args
    record = book.find(name)
    if record is None or not record.address:
        return f"No address found for contact '{name}'."
    return f"{name}'s address: {record.address.value}"

@input_error(expected_arg_count=1)
def remove_address(args, book: AddressBook):
    """
    Removes the address for a contact.
    Usage: remove-address [name]
    """
    name, *_ = args
    record = book.find(name)
    if record is None or not record.address:
        return f"No address to remove for contact '{name}'."
    record.remove_address()
    return "Address removed."

# forming a string of names of the persons, who should be congratulated and their respective birthday dates.
def birthdays(book, args):
    str = ""    
    if args:
        days = args[0]
    else:
        days = 7      
    if len(book.get_upcoming_birthdays(days)) != 0:
        for i in book.get_upcoming_birthdays(days):
            str += f"{i}\n"
        return str
    else:
        return f"The data base is empty."


#book instance serialization function using pickle module    
def save_data(book, filename = FILENAME):
    with open(filename, "wb") as record_file:
        pickle.dump(book, record_file)

#loading book from file or creating a new book instance if there is no file
def load_data():
    if FILENAME.is_file():
        try:
            with open(FILENAME, "rb") as record_file:
                return pickle.load(record_file)
        except (pickle.UnpicklingError, EOFError, FileNotFoundError):
            print("A mistake occurred trying to load the data")
    
    return AddressBook()
