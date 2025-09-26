"""
Strategy

Define una familia de algoritmos, los hace intercambiables.
Referencia: https://refactoring.guru/es/design-patterns/strategy
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List[int]) -> List[int]: ...


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List[int]) -> List[int]:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List[int]) -> List[int]:
        return list(reversed(sorted(data)))


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def do_some_business_logic(self, data: List[int]) -> List[int]:
        return self.strategy.do_algorithm(data)


if __name__ == "__main__":
    ctx = Context(ConcreteStrategyA())
    print(ctx.do_some_business_logic([3, 1, 2]))
    ctx.strategy = ConcreteStrategyB()
    print(ctx.do_some_business_logic([3, 1, 2]))
