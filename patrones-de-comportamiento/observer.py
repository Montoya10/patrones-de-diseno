"""
Observer

Define un mecanismo de suscripción para notificar a múltiples objetos sobre eventos.
Referencia: https://refactoring.guru/es/design-patterns/observer
"""
from __future__ import annotations
from typing import List, Protocol


class Observer(Protocol):
    def update(self, state: int) -> None: ...


class ConcreteObserver:
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, state: int) -> None:
        print(f"{self.name} recibió estado -> {state}")


class Subject:
    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._state = 0

    def attach(self, obs: Observer) -> None:
        self._observers.append(obs)

    def detach(self, obs: Observer) -> None:
        self._observers.remove(obs)

    def set_state(self, state: int) -> None:
        self._state = state
        self._notify()

    def _notify(self) -> None:
        for obs in list(self._observers):
            obs.update(self._state)


if __name__ == "__main__":
    s = Subject()
    s.attach(ConcreteObserver("A"))
    s.attach(ConcreteObserver("B"))
    s.set_state(1)
