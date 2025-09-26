"""
Facade

Proporciona una interfaz unificada para un conjunto de interfaces en un subsistema.
Referencia: https://refactoring.guru/es/design-patterns/facade
"""

class SubsystemA:
    def operation_a(self) -> str:
        return "A"


class SubsystemB:
    def operation_b(self) -> str:
        return "B"


class Facade:
    def __init__(self, a: SubsystemA, b: SubsystemB) -> None:
        self.a = a
        self.b = b

    def operation(self) -> str:
        return f"Facade: {self.a.operation_a()} + {self.b.operation_b()}"


if __name__ == "__main__":
    print(Facade(SubsystemA(), SubsystemB()).operation())
