"""
Proxy

Proporciona un sustituto o marcador de posición para controlar el acceso a un objeto.
Referencia: https://refactoring.guru/es/design-patterns/proxy
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self) -> str: ...


class RealSubject(Subject):
    def request(self) -> str:
        return "RealSubject: atendiendo la solicitud"


class Proxy(Subject):
    def __init__(self, real: RealSubject) -> None:
        self.real = real

    def request(self) -> str:
        # Ejemplo: control de acceso o cacheo
        return f"Proxy: verificando acceso -> {self.real.request()}"


if __name__ == "__main__":
    print(Proxy(RealSubject()).request())
