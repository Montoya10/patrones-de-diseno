"""
Adapter

Permite la colaboración entre objetos con interfaces incompatibles.
Referencia: https://refactoring.guru/es/design-patterns/adapter
"""

class Target:
    def request(self) -> str:
        return "Target: comportamiento estándar"


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"  # mensaje al revés


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: {self.adaptee.specific_request()[::-1]}"


if __name__ == "__main__":
    target = Target()
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(target.request())
    print(adapter.request())
