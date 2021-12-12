import os
import pickle

from AdressBook import AddressBook
from NoteBook import NoteBook


class Asisstant:
    def __init__(self) -> None:
        self.address_book = AddressBook()
        self.note_book = NoteBook()

    def load_data(self) -> None:
        """
            Load adress_book/note_book from file
        """
        if os.path.exists('data-adress.bin'):
            with open('data-adress.bin', 'rb') as file:
                self.address_book = pickle.load(file)
        if os.path.exists('data-note.bin'):
            with open('data-note.bin', 'rb') as file:
                self.note_book = pickle.load(file)

    def save_data(self) -> None:
        """
            Save data to file
        """
        with open('data-adress.bin', 'wb') as file:
            pickle.dump(self.address_book, file)
        with open('data-note.bin', 'wb') as file:
            pickle.dump(self.note_book, file)
