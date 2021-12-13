import sys
from partial.Asisstant import Asisstant
from partial.Sorter import Sorter


def main():
    jarvis = Asisstant()
    commands_list = (
        "add contact",
        "find contact",
        "change contact",
        "del contact",
        "get birthdays",
        "show all",
        "sort folder",
    )
    user_commands = {
        "add contact": jarvis.add_contact,
        "find contact": jarvis.find_contact,
        "change contact": jarvis.change_contact,
        "del contact": jarvis.del_contact,
        "get birthdays": jarvis.get_birthdays,
        "show all": jarvis.address_book.show_all_records,
        "sort folder": Sorter().sort,
    
    }
    commands = sys.argv[1:]
    str_cmd = ' '.join(commands)
    if len(sys.argv) == 1:
        print(f'Hello my name is "Jarvis" i am your virtual assistant.\nI am support these commands: {commands_list}')
    else:
        if str_cmd in user_commands.keys():
            print(user_commands.get(str_cmd)())
        else:
            print(f"I do not support this command {str_cmd}")


if __name__ == "__main__":
    main()
