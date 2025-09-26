"""
Interpreter

Dado un lenguaje, define una representación para su gramática junto con un intérprete que usa la representación para interpretar sentencias en el lenguaje.
Referencia: https://refactoring.guru/es/design-patterns/interpreter

Ejemplo: intérprete simple de expresiones booleanas con terminales y AND/OR/NOT.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict[str, bool]) -> bool: ...


class Variable(Expression):
    def __init__(self, name: str) -> None:
        self.name = name

    def interpret(self, context: dict[str, bool]) -> bool:
        return context.get(self.name, False)


class Constant(Expression):
    def __init__(self, value: bool) -> None:
        self.value = value

    def interpret(self, context: dict[str, bool]) -> bool:
        return self.value


class Not(Expression):
    def __init__(self, expr: Expression) -> None:
        self.expr = expr

    def interpret(self, context: dict[str, bool]) -> bool:
        return not self.expr.interpret(context)


class And(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: dict[str, bool]) -> bool:
        return self.left.interpret(context) and self.right.interpret(context)


class Or(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: dict[str, bool]) -> bool:
        return self.left.interpret(context) or self.right.interpret(context)


if __name__ == "__main__":
    # Expresión: (x AND y) OR NOT z
    expr = Or(And(Variable("x"), Variable("y")), Not(Variable("z")))
    ctx = {"x": True, "y": False, "z": False}
    print(expr.interpret(ctx))  # True (False OR True)
