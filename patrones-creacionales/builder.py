"""
Builder

Permite construir objetos complejos paso a paso.
Referencia: https://refactoring.guru/es/design-patterns/builder
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Product:
    def __init__(self) -> None:
        self.parts: List[str] = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def __str__(self) -> str:
        return f"Producto con partes: {', '.join(self.parts)}"


class Builder(ABC):
    @abstractmethod
    def reset(self) -> None: ...

    @abstractmethod
    def build_part_a(self) -> None: ...

    @abstractmethod
    def build_part_b(self) -> None: ...


class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    def build_part_a(self) -> None:
        self._product.add("ParteA")

    def build_part_b(self) -> None:
        self._product.add("ParteB")

    def get_product(self) -> Product:
        product = self._product
        self.reset()
        return product


class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def build_minimal(self) -> Product:
        self.builder.build_part_a()
        return self.builder.get_product()  # type: ignore[attr-defined]

    def build_full(self) -> Product:
        self.builder.build_part_a()
        self.builder.build_part_b()
        return self.builder.get_product()  # type: ignore[attr-defined]


if __name__ == "__main__":
    b = ConcreteBuilder()
    director = Director(b)
    print(director.build_minimal())
    print(director.build_full())
