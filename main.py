from partial.AdressBook import *
from partial import NoteBook
from partial.Sorter import *

"""''
jarvis add_contact
add_contact()
Write your name: 
...
...
...
...
Successfully added contact {name} to contact book
""" ""


def add_contact() -> str:
    name = input("Name is key value, please write name: ")
    while len(name) == 0:
        name = input("Name is key value, please write name: ")
    new_contact = Record(name=name, phones=[], birthday=None, email=None, address=None)
    address_book.add_record(new_contact)
    phone = input("Phone is key value, please write phones: ")
    phones_list = phone.split(",") if phone is not None else []
    while address_book[name].get_phones() != phones_list:
        phones_list = phone.split(",") if phone is not None else []
        for item in phones_list:
            address_book[name].add_phone(item)
        address_book[name].delete_phone(
            []
        )  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if address_book[name].get_phones() != phones_list:
            address_book[name].phones.clear()
            phone = input("Phone is key value, please write phones: ")
    birthday = input(
        '"OPTIONAL" You can skip this info, just press enter\nWrite birthday: '
    )
    if len(birthday) == 0:
        address_book[name].birthday.value = None
    else:
        while str(address_book[name].birthday.value) != birthday:
            address_book[name].add_birthday(birthday)
            if str(address_book[name].birthday.value) != birthday:
                birthday = input(
                    '"OPTIONAL" You can skip this info, just press enter\nWrite birthday: '
                )
    email = input('"OPTIONAL" You can skip this info, just press enter\nWrite email: ')
    if len(email) == 0:
        address_book[name].email.value = None
    else:
        while str(address_book[name].email.value) != email:
            address_book[name].add_email(email)
            if str(address_book[name].email.value) != email:
                email = input(
                    '"OPTIONAL" You can skip this info, just press enter\nWrite email: '
                )
    address = input(
        '"OPTIONAL" You can skip this info, just press enter\nWrite address: '
    )
    if len(address) == 0:
        address_book[name].address.value = None
    else:
        while str(address_book[name].address.value) != address:
            address_book[name].add_address(address)
            if str(address_book[name].address.value) != address:
                address = input(
                    '"OPTIONAL" You can skip this info, just press enter\nWrite address: '
                )
    address_book.save_data("data.bin")
    return f"Successfully added contact {name} to contact book"


"""''
jarvis find_contact
find_contact()
Write contact name: 
Info for contact {result}
""" ""


def find_contact() -> str:
    name = input("Write contact name: ")
    result = address_book.find_record(name)
    return result


"""''
jarvis change_contact
change_contact()
Write contact name:
What you want to change? 
Write old phone: 
Write new phone: 
Successfully changed phone for contact {name}
""" ""


def change_contact() -> str:
    name = input("Write contact name: ")
    while name not in address_book.keys():
        print(f"I do not have {name} contact in my book")
        name = input("Write contact name: ")
    what_change = input("What you want to change?\n")
    if what_change == "phone":
        old_phone = input("Write old phone: ")
        while old_phone not in address_book[name].get_phones():
            old_phone = input(
                f'I do not have such phone: "{old_phone}", write old phone: '
            )
        address_book[name].delete_phone(old_phone)
        new_phone = input("Write new phone: ")
        address_book[name].add_phone(new_phone)
        while new_phone not in address_book[name].get_phones():
            new_phone = input("Write new phone: ")
            address_book[name].add_phone(new_phone)
            address_book[name].delete_phone([])
        address_book.save_data("data.bin")
        return f"Successfully changed {what_change} for contact {name}"
    elif what_change == "name":
        new_name = input("Write new name: ")
        address_book[name].name.value = new_name
        address_book.save_data("data.bin")
        return f"Successfully changed {what_change} for contact {name}"
    elif what_change == "birthday":
        new_birthday = input("Write new birthday: ")
        while str(address_book[name].birthday.value) != new_birthday:
            address_book[name].add_birthday(new_birthday)
            if str(address_book[name].birthday.value) != new_birthday:
                new_birthday = input("Write new birthday: ")
        address_book.save_data("data.bin")
        return f"Successfully changed {what_change} for contact {name}"
    elif what_change == "email":
        new_email = input("Write new email: ")
        while str(address_book[name].email.value) != new_email:
            address_book[name].add_email(new_email)
            if str(address_book[name].email.value) != new_email:
                new_email = input("Write new email: ")
        address_book.save_data("data.bin")
        return f"Successfully changed {what_change} for contact {name}"
    elif what_change == "address":
        new_address = input("Write new address: ")
        while str(address_book[name].address.value) != new_address:
            address_book[name].add_address(new_address)
            if str(address_book[name].address.value) != new_address:
                new_address = input("Write new address: ")
        address_book.save_data("data.bin")
        return f"Successfully changed {what_change} for contact {name}"


"""''
jarvis del_contact
del_contact()
Write contact name: 
Successfully deleted contact {name} from contact book
""" ""


def del_contact() -> str:
    name = input("Write contact name: ")
    while name not in address_book.keys():
        print(f"I do not have {name} contact in my book")
        name = input("Write contact name: ")
    address_book.delete_record(name)
    print(address_book)
    return f"Successfully deleted contact {name} from contact book"


"""''
jarvis sort_folder
sort_folder()
Write path which you want to sort: 
Successfully sorted folder {path}
""" ""


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
