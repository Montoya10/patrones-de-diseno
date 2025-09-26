"""
Command

Convierte una solicitud en un objeto independiente que contiene toda la información de la solicitud.
Referencia: https://refactoring.guru/es/design-patterns/command
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...


class Receiver:
    def action(self) -> None:
        print("Receiver: realizando acción")


class ConcreteCommand(Command):
    def __init__(self, receiver: Receiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.action()


class Invoker:
    def __init__(self) -> None:
        self._on_start: Command | None = None

    def set_on_start(self, cmd: Command) -> None:
        self._on_start = cmd

    def do_something_important(self) -> None:
        if self._on_start:
            self._on_start.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(ConcreteCommand(Receiver()))
    invoker.do_something_important()
