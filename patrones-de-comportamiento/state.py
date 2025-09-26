"""
State

Permite que un objeto altere su comportamiento cuando su estado interno cambia.
Referencia: https://refactoring.guru/es/design-patterns/state
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    def __init__(self, state: "State") -> None:
        self.transition_to(state)

    def transition_to(self, state: "State") -> None:
        self.state = state
        self.state.context = self

    def request(self) -> None:
        self.state.handle()


class State(ABC):
    def __init__(self) -> None:
        self.context: Context | None = None

    @abstractmethod
    def handle(self) -> None: ...


class ConcreteStateA(State):
    def handle(self) -> None:
        print("Estado A -> hacer algo, cambiando a B")
        self.context and self.context.transition_to(ConcreteStateB())


class ConcreteStateB(State):
    def handle(self) -> None:
        print("Estado B -> hacer algo, cambiando a A")
        self.context and self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    ctx = Context(ConcreteStateA())
    ctx.request()
    ctx.request()
