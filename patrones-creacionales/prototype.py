"""
Prototype

Permite copiar objetos existentes sin que el código dependa de sus clases.
Referencia: https://refactoring.guru/es/design-patterns/prototype
"""
from __future__ import annotations
import copy
from dataclasses import dataclass


@dataclass
class Address:
    city: str
    street: str


class Person:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def clone(self) -> "Person":
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"Person(name={self.name}, city={self.address.city}, street={self.address.street})"


if __name__ == "__main__":
    original = Person("Ana", Address("Medellín", "Calle 123"))
    copia = original.clone()
    copia.name = "Ana (copia)"
    copia.address.street = "Calle 456"  # No afecta al original gracias a deepcopy
    print(original)
    print(copia)
