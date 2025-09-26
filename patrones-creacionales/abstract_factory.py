"""
Abstract Factory

Proporciona una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas.
Referencia: https://refactoring.guru/es/design-patterns/abstract-factory
"""
from __future__ import annotations
from abc import ABC, abstractmethod


# Productos
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError


class Checkbox(ABC):
    @abstractmethod
    def toggle(self) -> str:
        raise NotImplementedError


class WinButton(Button):
    def render(self) -> str:
        return "Renderizando botón estilo Windows"


class MacButton(Button):
    def render(self) -> str:
        return "Renderizando botón estilo macOS"


class WinCheckbox(Checkbox):
    def toggle(self) -> str:
        return "Checkbox Windows -> cambiado"


class MacCheckbox(Checkbox):
    def toggle(self) -> str:
        return "Checkbox macOS -> cambiado"


# Fábricas
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        raise NotImplementedError


class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Cliente
class Application:
    def __init__(self, factory: GUIFactory) -> None:
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def draw(self) -> None:
        print(self.button.render())
        print(self.checkbox.toggle())


if __name__ == "__main__":
    print("-- Windows UI --")
    Application(WinFactory()).draw()
    print("-- macOS UI --")
    Application(MacFactory()).draw()
