import os
import pickle

from partial.AdressBook import AdressBook, Record
from partial.NoteBook import NoteBook


class JarvisCLI:
    def __init__(self) -> None:
        self.adress_book = AdressBook()
        self.note_book = NoteBook()
        self.adress_book.load_data()
        self.note_book.load_data()

    def add_record(self) -> None:
        """
        Define new Record + add record to book + save book
        """
        name = input("Type name : ")
        email = input("Type email : ")
        phones = input("Type phones : ").replace(" ", "").split(",")
        adress = input("Type adress : ")
        birthday = input("Type Birthday :")
        new_record = Record(
            name=name, email=email, phones=phones, adress=adress, birthday=birthday
        )
        self.adress_book.add_record(new_record)

        self.save_data()

    def save_data(self) -> None:
        """
        Update data
        """
        self.adress_book.save_data()
        self.note_book.save_data()
