from colorama import Fore

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "The requested contact does not exist in the phonebook."
        except IndexError:
            return "The command seems incomplete. Please provide all required arguments."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {Fore.GREEN}{name}{Fore.RESET} with phone {Fore.GREEN}{phone}{Fore.RESET} added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contact = contacts.get(name, "")
    if contact:
        contacts[name] = phone
        return f"Contact {Fore.GREEN}{name}{Fore.RESET} is changed."
    else:
        return f"{Fore.RED}Contact does not exist.{Fore.RESET}"
    
@input_error
def show_phone(args, contacts: dict):
    name, = args
    contact_phone = contacts.get(name, "")
    if contact_phone:
        return f"Phone: {Fore.GREEN}{contact_phone}{Fore.RESET}"
    else:
        return f"{Fore.RED}Contact not found{Fore.RESET}"
    
@input_error
def show_all(contacts):
    str_contacts = f"{Fore.CYAN}All contacts:{Fore.RESET} \n"
    if contacts:
        for i, (name, phone) in enumerate(contacts.items(), start=1):
            str_contacts += f"{i}: {Fore.GREEN}{name}{Fore.RESET} -> {Fore.GREEN}{phone}{Fore.RESET}\n"
        return str_contacts[:-1]
    else:
        return f"{Fore.RED}Contacts is empty{Fore.RESET}" 
    
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print(f"{Fore.GREEN}Welcome to the assistant bot!{Fore.RESET}")
    while True:
        user_input = input(f"Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print(f"{Fore.YELLOW} Good bye! {Fore.RESET}")
            break
        elif command == "hello":
            print(f"{Fore.YELLOW}How can I help you?{Fore.RESET}")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(f"{Fore.RED}Invalid command.{Fore.RESET}")

if __name__ == "__main__":
    main()