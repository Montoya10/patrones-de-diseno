"""
Chain of Responsibility

Pasa la solicitud a lo largo de una cadena de manejadores donde cada uno decide procesarla o pasarla al siguiente.
Referencia: https://refactoring.guru/es/design-patterns/chain-of-responsibility
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    _next: Optional["Handler"] = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler

    def handle(self, request: str) -> str:
        if self._next:
            return self._next.handle(request)
        return "Sin manejar"


class MonkeyHandler(Handler):
    def handle(self, request: str) -> str:
        if request == "banana":
            return "Mono: me como la banana"
        return super().handle(request)


class SquirrelHandler(Handler):
    def handle(self, request: str) -> str:
        if request == "nuez":
            return "Ardilla: me como la nuez"
        return super().handle(request)


class DogHandler(Handler):
    def handle(self, request: str) -> str:
        if request == "carne":
            return "Perro: me como la carne"
        return super().handle(request)


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)
    for food in ("nuez", "banana", "café"):
        print(monkey.handle(food))
