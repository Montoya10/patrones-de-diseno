"""
Flyweight

Minimiza el uso de memoria compartiendo tanto como sea posible con objetos similares.
Referencia: https://refactoring.guru/es/design-patterns/flyweight
"""
from __future__ import annotations
from typing import Dict, Tuple


class Flyweight:
    def __init__(self, shared_state: Tuple[str, str, str]) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> str:
        return f"Compartido={self._shared_state}, Único={unique_state}"


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    @classmethod
    def get_flyweight(cls, shared_state: Tuple[str, str, str]) -> Flyweight:
        key = "|".join(shared_state)
        if key not in cls._flyweights:
            cls._flyweights[key] = Flyweight(shared_state)
        return cls._flyweights[key]


if __name__ == "__main__":
    fw1 = FlyweightFactory.get_flyweight(("BMW", "M3", "negro"))
    fw2 = FlyweightFactory.get_flyweight(("BMW", "M3", "negro"))
    print(fw1 is fw2)  # True
    print(fw1.operation("ABC-123"))
