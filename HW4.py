def parse_input(user_input):
    if not user_input.strip():
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, IndexError, ValueError) as e:
            if isinstance(e, ValueError) and str(e) == "not enough values to unpack (expected at least 2, got 0)":
                return "Empty input. Enter name and phone number."
            elif isinstance(e, KeyError):
                return "Enter name!"
            elif isinstance(e, IndexError):
                return "Enter name and phone number!"
            else:
                return str(e)
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone_number = args
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        for name, phone_number in contacts.items():
            print(f"{name} {phone_number}")
    else:
        print("No contacts.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command is None:
            print("Empty input. Please enter a command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
