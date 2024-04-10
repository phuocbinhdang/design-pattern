from __future__ import annotations
from typing import List


class Document:
    _content: str

    def __init__(self, content: str):
        self._content = content

    def get_content(self) -> str:
        return self._content

    def write(self, text):
        self._content += text

    def create_memento(self) -> DocumentMemento:
        return DocumentMemento(self._content)

    def restore_from_memento(self, memento: DocumentMemento):
        self._content = memento.get_saved_content()


class DocumentMemento:
    _content: str

    def __init__(self, content: str):
        self._content = content

    def get_saved_content(self) -> str:
        return self._content


class History:
    _mementos: List[DocumentMemento]

    def __init__(self):
        self._mementos = []

    def add_memento(self, memento: DocumentMemento):
        self._mementos.append(memento)

    def get_memento(self, index: int) -> DocumentMemento:
        return self._mementos[index]


if __name__ == "__main__":
    document = Document("1")
    print(document.get_content())

    document.write(" 2")
    print(document.get_content())

    history = History()
    history.add_memento(document.create_memento())

    document.write(" 3")
    print(document.get_content())
    history.add_memento(document.create_memento())

    document.restore_from_memento(history.get_memento(0))
    print(document.get_content())
