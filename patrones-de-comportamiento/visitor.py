"""
Visitor

Separa los algoritmos de los objetos sobre los que operan.
Referencia: https://refactoring.guru/es/design-patterns/visitor
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_a(self, element: "ConcreteElementA") -> None: ...

    @abstractmethod
    def visit_b(self, element: "ConcreteElementB") -> None: ...


class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None: ...


class ConcreteElementA(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_a(self)


class ConcreteElementB(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_b(self)


class ConcreteVisitor(Visitor):
    def visit_a(self, element: ConcreteElementA) -> None:
        print("Visitando A")

    def visit_b(self, element: ConcreteElementB) -> None:
        print("Visitando B")


if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]
    visitor = ConcreteVisitor()
    for el in elements:
        el.accept(visitor)
