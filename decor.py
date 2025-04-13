# decorator function
def input_error(expected_arg_count=None):

    # dictionary with possible errors
    error_messages = {
        "ValueError": "Please provide a valid name and phone number.",
        "IncorrectDataInput": "Please provide correct information: command Name phone",
        "TypeError": "Invalid input type",
        "IndexError": "You did not provide arguments to proceed.",
        "NoNameError": "You did not provide name whose phone you want to see",
        "InvalidName": "Invalid format for name. Please use alphabetic characters only.",
        "InvalidPhone": "Invalid format for phone. Please use numeric characters only.",
        "InvalidEmail": "Invalid email format. Please use a valid email address like user_123@example.com.",
        "InvalidAddress": "Invalid address format. Please use only letters, digits, commas, periods, and spaces."
    }

    def decorator(func):
        def inner(*args, **kwargs):
            try:
                # Check if arguments are provided
                if not args:
                    raise IndexError(error_messages["IndexError"])

                # For functions like show_phone, ensure that the first argument is not empty
                if not args[0] and func.__name__ in ["show_phone"]:
                    raise ValueError(error_messages["NoNameError"])

                # Validate that the expected number of arguments is provided
                if expected_arg_count is not None and len(args[0]) < expected_arg_count:
                    if func.__name__ in ["add_contact", "change_contact"]:
                        raise ValueError(error_messages["IncorrectDataInput"])

                # For add_contact and change_contact, validate name and phone
                if func.__name__ in ["change_contact"]:
                    if not args[0][0].isalpha():
                        raise ValueError(error_messages["InvalidName"])
                    if not args[0][1].isdigit():
                        raise ValueError(error_messages["InvalidPhone"])

                # For add_email and change_email, validate email format
                if func.__name__ in ["add_email", "change_email"]:
                    if "@" not in args[0][1] or "." not in args[0][1]:
                        raise ValueError(error_messages["InvalidEmail"])

                # For add_address and change_address, validate address format using Address.validate
                if func.__name__ in ["add_address", "change_address"]:
                    from classes_for_program import \
                        Address  # Импорт внутри функции для избежания циклических зависимостей
                    if not Address.validate(args[0][1]):
                        raise ValueError(error_messages["InvalidAddress"])

                return func(*args, **kwargs)
            except Exception as e:
                return str(e)

        return inner

    return decorator
