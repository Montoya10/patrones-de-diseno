"""
Factory Method

Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar.
Referencia: https://refactoring.guru/es/design-patterns/factory-method
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:  # Contrato común para todos los productos
        raise NotImplementedError


class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Resultado del Producto A"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Resultado del Producto B"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:  # Delega la creación a las subclases
        raise NotImplementedError

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creador: trabajando con -> {product.operation()}"


class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


def client_code(creator: Creator) -> None:
    print(creator.some_operation())


if __name__ == "__main__":
    client_code(ConcreteCreatorA())
    client_code(ConcreteCreatorB())
