"""
Singleton

Garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella.
Referencia: https://refactoring.guru/es/design-patterns/singleton
"""
from __future__ import annotations
from typing import Optional


class Singleton:
    _instance: Optional["Singleton"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: int = 0) -> None:
        if not hasattr(self, "initialized"):
            self.value = value
            self.initialized = True


if __name__ == "__main__":
    a = Singleton(10)
    b = Singleton(99)
    print(a is b)      # True
    print(a.value)     # 10 (no cambia con la segunda "instancia")
