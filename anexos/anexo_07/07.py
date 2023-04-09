"""
Nombre del Patrón: Facade / Facade

Definición - Facade: Peroporciona una interfaz simplificada a un conjunto de subsistemas que trabajan juntos. Define
una API de más alto nivel para simplificar el uso de un conjunto de objetos.

Problema: Modelado de una lavadora

Uso: simplificar el uso de sistemas complejos, manteniendo el acceso a los objetos individuales

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""


class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("Spinning...")


class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def start_washing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.start_washing()
