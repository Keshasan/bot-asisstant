import os
import pickle


class NoteBook:
    """
    Desrcibes object fo personal book with notes
    """

    def load_data(self) -> None:
        """
        Load adress_book/note_book from file
        """
        if os.path.exists("data-note.bin"):
            with open("data-note.bin", "rb") as file:
                self.note_book = pickle.load(file)

    def save_data(self) -> None:
        """
        Save data to file
        """
        with open("data-note.bin", "wb") as file:
            pickle.dump(self.note_book, file)
