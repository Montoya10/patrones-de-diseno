"""
Mediator

Reduce dependencias caóticas entre objetos al restringir la comunicación directa entre ellos.
Referencia: https://refactoring.guru/es/design-patterns/mediator
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None: ...


class ComponentBase:
    def __init__(self) -> None:
        self.mediator: Mediator | None = None

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator


class ComponentA(ComponentBase):
    def do_a(self) -> None:
        print("A: hace A")
        self.mediator and self.mediator.notify(self, "A")


class ComponentB(ComponentBase):
    def do_b(self) -> None:
        print("B: hace B")
        self.mediator and self.mediator.notify(self, "B")


class ConcreteMediator(Mediator):
    def __init__(self, a: ComponentA, b: ComponentB) -> None:
        self.a = a
        self.b = b
        self.a.set_mediator(self)
        self.b.set_mediator(self)

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            self.b.do_b()
        elif event == "B":
            self.a.do_a()


if __name__ == "__main__":
    a, b = ComponentA(), ComponentB()
    mediator = ConcreteMediator(a, b)
    a.do_a()
    b.do_b()
