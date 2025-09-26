"""
Bridge

Separa una abstracción de su implementación para que ambas puedan variar independientemente.
Referencia: https://refactoring.guru/es/design-patterns/bridge
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def operation_impl(self) -> str: ...


class ConcreteImplementationA(Implementation):
    def operation_impl(self) -> str:
        return "Implementación A"


class ConcreteImplementationB(Implementation):
    def operation_impl(self) -> str:
        return "Implementación B"


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return f"Abstracción: {self.implementation.operation_impl()}"


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return f"Abstracción extendida: {self.implementation.operation_impl()}"


if __name__ == "__main__":
    print(Abstraction(ConcreteImplementationA()).operation())
    print(ExtendedAbstraction(ConcreteImplementationB()).operation())
