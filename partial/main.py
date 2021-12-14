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
        "show all": jarvis.address_book.show_all_records,
       
        }
    user_commands_with_arguments = {
        "find contact": jarvis.find_contact,
        "change contact": jarvis.change_contact,
        "del contact": jarvis.del_contact,
        "get birthdays": jarvis.get_birthdays,
        "sort folder": Sorter().sort,
    }
    commands = sys.argv[1:]
    str_cmd = ' '.join(commands)
    if len(sys.argv) == 1:
        print(f'Hello my name is "Jarvis" i am your virtual assistant.\nI support these commands: {commands_list}')
    elif len(commands) == 2:
        if str_cmd in user_commands.keys():
            print(user_commands.get(str_cmd)())
        else:
            print(f"I do not support this command {str_cmd}")
    elif len(commands) == 3:
        
        str_cmd = ' '.join(commands[0:2])
        user_argument = commands[-1]
        
        if str_cmd in user_commands_with_arguments.keys():
            print(user_commands_with_arguments.get(str_cmd)(user_argument))
        else:
            print(f"I do not support this command {str_cmd}")
    else:
        print('Unknown command usage.')

if __name__ == "__main__":
    main()
