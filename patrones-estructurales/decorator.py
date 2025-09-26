"""
Decorator

Adjunta responsabilidades adicionales a un objeto dinámicamente.
Referencia: https://refactoring.guru/es/design-patterns/decorator
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self) -> str: ...


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "Componente"


class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"DecoradorA({super().operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"DecoradorB({super().operation()})"


if __name__ == "__main__":
    simple = ConcreteComponent()
    decorated = ConcreteDecoratorB(ConcreteDecoratorA(simple))
    print(decorated.operation())
