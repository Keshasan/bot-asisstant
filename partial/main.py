import sys
from partial.Asisstant import Asisstant


def main():
    jarvis = Asisstant()

    commands = sys.argv[1:]
    if len(sys.argv) == 1:
        print("Hello, from Jarvis.")

    if "contact" in commands:

        if "add" in commands:
            jarvis.add_contact()
        elif "change" in commands:
            jarvis.change_contact()

        elif "show" in commands:
            jarvis.address_book.show_all_records()

        elif "find" in commands:
            if len(commands) != 3:
                print("Incorrect command usage.")
                return
            name = commands[-1]
            record = jarvis.address_book.find_record(name)
            print(record)

        elif "delete" in commands:
            if len(commands) != 3:
                print("Incorrect command usage.")
                return
            name = commands[-1]

    elif "note" in commands:
        if "add" in commands:
            jarvis.add_note()
        elif "show" in commands:
            jarvis.show_notes()


if __name__ == "__main__":
    main()
