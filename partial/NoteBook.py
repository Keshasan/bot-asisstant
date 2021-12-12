from collections import UserDict, UserList


class Tag():
    
    def __init__(self, value:str) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value


class Note():
    
    def __init__(self, value:str) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value:str) -> None:
        self.__value = value


class NoteBook(UserDict):
    """
        Desrcibes object fo personal book with notes
    """
    def __init__(self, text:str, *tags:list[str]) -> None:
        self.text = Note(text)
        self.tags = []
        for tag in tags:
            self.tags.append(Tag(tag))

    def 