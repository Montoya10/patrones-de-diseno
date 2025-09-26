"""
Template Method

Define el esqueleto de un algoritmo en la superclase pero permite que las subclases sobrescriban pasos específicos.
Referencia: https://refactoring.guru/es/design-patterns/template-method
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None: print("Base 1")
    def base_operation2(self) -> None: print("Base 2")
    def base_operation3(self) -> None: print("Base 3")

    def hook1(self) -> None: pass
    def hook2(self) -> None: pass

    @abstractmethod
    def required_operations1(self) -> None: ...

    @abstractmethod
    def required_operations2(self) -> None: ...


class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None: print("Op requerida 1 - C1")
    def required_operations2(self) -> None: print("Op requerida 2 - C1")


class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None: print("Op requerida 1 - C2")
    def required_operations2(self) -> None: print("Op requerida 2 - C2")


if __name__ == "__main__":
    ConcreteClass1().template_method()
    ConcreteClass2().template_method()
