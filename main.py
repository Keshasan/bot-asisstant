from partial.AdressBook import *
from partial import NoteBook
from partial.Sorter import *



def sort_folder(command: str) -> str:
    path = input("Write path which you want to sort: ")
    sort = Sorter()
    sort.sort_path(path)
    return f"Successfully sorted folder {path}"


def main():
    global address_book
    address_book = AddressBook()
    address_book.load_data("data.bin")
    commands_list = (
        "help",
        "hello",
        "add",
        "change",
        "phone",
        "show_all",
        "birthday",
        "add_phone",
        "set_birthday",
        "find",
        "del_phone",
        "good_bye",
        "close",
        "exit",
    )
    print('Hello my name is "Jarvis" i am your virtual assistant.')
    print(f"I am support these commands: {commands_list}")
    cmd = input("Write your command: ").capitalize()
    repl = cmd.replace("Jarvis", "").strip()
    user_commands = {
        "add_contact": add_contact,
        "find_contact": find_contact,
        "change_contact": change_contact,
        "del_contact": del_contact,
        "sort_folder": sort_folder,
    }
    if repl in user_commands.keys():
        print(user_commands.get(repl)())
    else:
        print(f"I do not support this command {repl}")


if __name__ == "__main__":
    main()
