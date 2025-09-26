"""
Memento

Permite guardar y restaurar el estado previo de un objeto.
Referencia: https://refactoring.guru/es/design-patterns/memento
"""
from __future__ import annotations
from typing import List


class Memento:
    def __init__(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state


class Originator:
    def __init__(self) -> None:
        self._state = ""

    def set_state(self, state: str) -> None:
        self._state = state

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()

    def __str__(self) -> str:
        return f"Estado={self._state}"


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._history: List[Memento] = []

    def backup(self) -> None:
        self._history.append(self._originator.save())

    def undo(self) -> None:
        if self._history:
            self._originator.restore(self._history.pop())


if __name__ == "__main__":
    origin = Originator()
    caretaker = Caretaker(origin)
    origin.set_state("v1")
    caretaker.backup()
    origin.set_state("v2")
    caretaker.undo()
    print(origin)
