import sys
from partial.Asisstant import Asisstant


def main():
    jarvis = Asisstant()

    commands = sys.argv[1:]
    if len(sys.argv) == 1:
        print("Hello, from Jarvis.")

    if "record" in commands:

        if "add" in commands:
            jarvis.add_contact()
        elif "change" in commands:
            jarvis.change_contact()

        elif "show" in commands:
            jarvis.address_book.show_all_records()

    elif "note" in commands:
        if "add" in commands:
            pass


if __name__ == "__main__":
    main()
