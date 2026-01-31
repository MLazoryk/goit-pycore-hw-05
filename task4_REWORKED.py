# SIMPLE PHONE BOOK PROGRAM

#===========================
#ERROR HANDLER DECORATOR
#===========================

def input_error(func): 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError: # CATCH: if wrong number of arguments 
            return "Give me name and phone please."
        except KeyError: # CATCH: If contact doesn't exist 
            return "Contact not found"
        except IndexError: # CATCH: If missing argument 
            return "Enter the argument for the command."
    return inner # <-- FIXED: This line should be OUTSIDE the inner function!
    
#===========================
# DATA STORAGE
#===========================
contacts = {}

def parse_input(user_input): 
    # Split string into list of words by spaces
    # E.g. "add John 123" -> ["add", "John", "123"]
    parts = user_input.split()

    if not parts:
        return "", []
    
    # "ADD " -> "add"
    command = parts[0].lower()

    # "John", "123"
    args = parts[1:]

    return command, args


#===========================
#CONTACT FUNCTIONS
#===========================

@input_error
def add_contact(args, contacts):
    name, phone = args

    contacts[name] = phone
    return "Contact added."

# CHANGE contact: 
@input_error # Add error handler
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts: 
        raise KeyError
    
    contacts[name] = phone
    return "Contact updated."

# SHOW phone
@input_error
def show_phone(args, contacts):
    name = args[0]

    if name not in contacts:
        raise KeyError
    
    return contacts[name]

# SHOW ALL
def show_all(contacts):
    if not contacts: 
        return "No contacts saved."
    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
        # E.g. "John: 123\n" then "Marry: 456\n"

    return result.strip()

#===========================
#MAIN PROGRAM
#===========================

def main():
    print("Welcome to the phone book!")
    print("Type 'exit' to quit")
    print("Commands: add [name] [phone], change [name][phone], phone [name], all")

    while True:
        user_input = input("\nEnter command: ").strip()

        if not user_input: 
            continue

        command, args = parse_input(user_input)

        if command in ["exit", "close"]: # User can type either "exit" or "close"
            print("Goodbye!")
            break 

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) !=2:
                print("Give me name and phone please.")
            else:
                print(add_contact(args, contacts))

        elif command == "change":
            if len(args) != 2:
                print("Give me name and phone please.")
            else: 
                print(change_contact(args, contacts))

        elif command == "phone":
            if not args: 
                print("Enter the argument for the command.")
            else:
                print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))

        else: 
            print("Invalid command. Try: add, change, phone, all, or exit")

#===========================
#CALLING THE FUNCTION
#===========================

if __name__ == "__main__":
    main()