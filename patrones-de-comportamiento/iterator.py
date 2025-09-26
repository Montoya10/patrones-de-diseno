"""
Iterator

Permite recorrer una colección sin exponer su representación interna.
Referencia: https://refactoring.guru/es/design-patterns/iterator
"""
from __future__ import annotations
from typing import Iterator as TypingIterator, Iterable, List


class WordsCollection(Iterable[str]):
    def __init__(self, items: List[str]) -> None:
        self._items = items

    def __iter__(self) -> TypingIterator[str]:
        return iter(self._items)

    def reversed(self) -> TypingIterator[str]:
        return reversed(self._items)


if __name__ == "__main__":
    words = WordsCollection(["uno", "dos", "tres"])
    for w in words:
        print(w)
    for w in words.reversed():
        print(w)
