import os
import pickle

from partial.AdressBook import AdressBook
from partial.NoteBook import NoteBook


class Asisstant:
    def __init__(self) -> None:
        self.adress_book = AdressBook()
        self.note_book = NoteBook()

    def load_data(self) -> None:
        """
            Load adress_book/note_book from file
        """
        if os.path.exists('data-adress.bin'):
            with open('data-adress.bin', 'rb') as file:
                self.adress_book = pickle.load(file)
        if os.path.exists('data-note.bin'):
            with open('data-note.bin', 'rb') as file:
                self.note_book = pickle.load(file)

    def save_data(self) -> None:
        """
            Save data to file
        """
        with open('data-adress.bin', 'wb') as file:
            pickle.dump(self.adress_book, file)
        with open('data-note.bin', 'wb') as file:
            pickle.dump(self.note_book, file)
