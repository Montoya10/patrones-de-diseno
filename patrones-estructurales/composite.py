"""
Composite

Compone objetos en estructuras de árbol para representar jerarquías parte-todo.
Referencia: https://refactoring.guru/es/design-patterns/composite
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def operation(self) -> str: ...

    def add(self, component: "Component") -> None: pass
    def remove(self, component: "Component") -> None: pass
    def is_composite(self) -> bool: return False


class Leaf(Component):
    def operation(self) -> str:
        return "Hoja"


class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"Rama({'+'.join(results)})"


if __name__ == "__main__":
    tree = Composite()
    branch = Composite()
    branch.add(Leaf())
    branch.add(Leaf())
    tree.add(branch)
    tree.add(Leaf())
    print(tree.operation())
